import os
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import hashlib
import re
import argparse
import datetime
from util import util_bd as bd

parser = argparse.ArgumentParser()
parser.add_argument('--reset', action='store_true')
args = parser.parse_args()

app = Flask(__name__)

model = {'utilisateur_courant': {}}
erreur_connexion = False

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Le serveur de developpement va reset la connection si la taille est depassee
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB


@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/')
def accueil():
    global model
    _handle_erreur_connexion()
    model['message_reussite'] = ""
    return render_template('accueil.html', model=model)


@app.route('/mot-de-passe-oublie')
def mot_de_passe_oublie():
    global model
    model['message_reussite'] = 'Un courriel vous a été envoyé avec un lien pour récupérer votre compte.'
    return render_template('accueil.html', model=model)


@app.route('/nous-contacter', methods=['GET'])
def nous_contacter():
    _handle_erreur_connexion()
    return render_template('nous-contacter.html', model=model)


@app.route('/nous-contacter', methods=['POST'])
def nous_contacter_post():
    return render_template('nous-contacter.html', model=model)


@app.route('/ajout-biere', methods=['GET'])
def ajout_biere():
    global model
    model['message_erreur'] = ""
    model['message_reussite'] = ""

    if 'est_une_microbrasserie' not in model['utilisateur_courant'].keys() or not model['utilisateur_courant'][
        'est_une_microbrasserie']:
        return redirect('/')

    now = datetime.datetime.now()
    model['current_year'] = now.year

    requete = 'SELECT id, nom FROM Sorte WHERE id NOT IN (SELECT id_sorte_parent FROM Type_de) '
    model['sous_sortes'] = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    _handle_erreur_connexion()
    return render_template('ajout-biere.html', model=model)


@app.route('/ajout-biere', methods=['POST'])
def ajout_biere_post():
    model['message_erreur'] = ""
    prix_ = request.form.get('prix')
    alcool_ = request.form.get('alcool')
    ibu_ = request.form.get('ibu')
    annee_ = request.form.get('annee')
    id_sorte_ = request.form.get('id_sous_sorte')
    quantite_ = request.form.get('quantite')
    try:
        if prix_ and alcool_ and ibu_ and annee_ and id_sorte_:
            prix = float(prix_)
            pourcentage_alcool = float(alcool_)
            ibu = int(ibu_)
            annee_production = int(annee_)
            id_sorte = int(id_sorte_)
            quantite = int(quantite_)
        else:
            raise ValueError
    except ValueError:
        model['message_erreur'] = "Veuillez entrer des nombres valides"
        return render_template('ajout-biere.html', model=model)

    nom = request.form.get('nom')
    description = request.form.get('description')
    if not nom or len(nom) == 0:
        model['message_erreur'] = "Vous devez saisir un nom"
        return render_template('ajout-biere.html', model=model)
    if not re.match(r"[1-9a-zA-Z\s\-]+$", nom):
        model['message_erreur'] = "Vous devez saisir un nom valide"
        return render_template('ajout-biere.html', model=model)
    requete = 'SELECT nom FROM Biere WHERE nom=%s'
    nom_existe = bd.execute_requete_lecture(requete, nom)
    if nom_existe:
        model['message_erreur'] = "Une bière portant ce nom existe déjà dans le système"
        return render_template('ajout-biere.html', model=model)

    if not description or len(description) == 0:
        model['message_erreur'] = "Vous devez saisir une description"
        return render_template('ajout-biere.html', model=model)
    if not re.match(r"[1-9a-zA-Z\s\-]+$", description):
        model['message_erreur'] = "Veuillez saisir une description valide"
        return render_template('ajout-biere.html', model=model)

    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename != '' and _allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], str(datetime.datetime.now()).replace(' ', '') + filename)
            file.save(path)
            file_length = os.stat(path).st_size
            if file_length > 5000000:  # 5 MB
                os.remove(path)
                model['message_erreur'] = "La taille de l'image doit etre de 5 Mo maximum"
                return render_template('ajout-biere.html', model=model)
            else:  # Tout est valide
                id_microbrasserie = model['utilisateur_courant']['id']
                date_ajout = datetime.datetime.now().strftime('%Y-%m-%d')

                conn, cursor = bd.open_connection_and_cursor()
                try:
                    requete = 'INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
                    cursor.execute(requete, (path, prix, nom, pourcentage_alcool, ibu, annee_production,
                                                description, date_ajout, id_sorte))
                    cursor.execute('SELECT LAST_INSERT_ID();')
                    id_biere = cursor.fetchone()
                    requete = 'INSERT INTO Vendre VALUES (%s, %s, %s)'
                    cursor.execute(requete, (id_microbrasserie, id_biere, quantite))
                    conn.commit()
                except Exception as e:
                    print(e)
                    model['message_erreur'] = "Une erreur est survenue lors de l'ajout de la bière"
                    return render_template('ajout-biere.html', model=model)
                bd.close_connection_and_cursor(conn, cursor)

                # La biere a été ajoutée avec succès
                model['message_reussite'] = "La bière a été importé avec succès"
                return render_template('ajout-biere.html', model=model)

    model['message_erreur'] = "L'image n'a pas pu etre importe"
    return render_template('ajout-biere.html', model=model)


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


@app.route('/consulter-biere')
def consulter_biere():
    try:
        id_biere = int(request.args.get("id_biere"))
    except (ValueError, TypeError):
        return redirect('/bieres')

    requete = 'SELECT B.image_url, B.id AS id, B.nom AS bnom, S.nom AS snom, B.prix AS prix, B.ibu AS ibu, B.pourcentage_alcool AS pa FROM Biere B, Sorte S WHERE B.id_sorte = S.id AND B.id = %s;'
    biere = bd.execute_requete_lecture(requete, id_biere, obtenir_dict=True)
    _handle_erreur_connexion()
    return render_template('une-biere.html', biere=biere, model=model)


@app.route('/bieres', methods=['GET'])
def bieres():
    requete = 'SELECT id, nom FROM Sorte WHERE id NOT IN (SELECT id_sorte_enfant FROM Type_de);'
    sortes = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    try:
        id_sorte = int(request.args.get("id_sorte"))
        id_sous_sorte = int(request.args.get("id_sous_sorte"))
        requete = 'SELECT * FROM Biere WHERE id_sorte = %s;'
        biere_dispo = bd.execute_requete_lecture(requete, id_sous_sorte, fetchall=True, obtenir_dict=True)

        # Sous-sortes
        requete = 'SELECT id, nom FROM Sorte WHERE id IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s);'
        sous_sortes = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

    except (ValueError, TypeError):
        id_sous_sorte = None
        try:
            id_sorte = int(request.args.get("id_sorte"))

            # Sous-sortes
            requete = 'SELECT id, nom FROM Sorte WHERE id IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s);'
            sous_sortes = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

            # Bieres dispos
            requete = 'SELECT B.image_url, B.id AS id, B.nom AS bnom, S.nom AS snom, B.prix AS prix, B.ibu AS ibu, B.pourcentage_alcool AS pa FROM Biere B, Sorte S WHERE B.id_sorte IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s) AND B.id_sorte = S.id;'
            biere_dispo = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

        except (ValueError, TypeError):
            id_sorte = None
            sous_sortes = []
            requete = 'SELECT B.image_url, B.id AS id, B.nom AS bnom, S.nom AS snom, B.prix AS prix, B.ibu AS ibu, B.pourcentage_alcool AS pa FROM Biere B, Sorte S WHERE B.id_sorte = S.id;'
            biere_dispo = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    _handle_erreur_connexion()
    return render_template('bieres.html', sortes=sortes, id_sorte=id_sorte, sous_sortes=sous_sortes,
                           id_sous_sorte=id_sous_sorte, bieresdispo=biere_dispo,
                           model=model)


@app.route('/Microbrasserie', methods=['GET'])
def microbrasserie():
    requete = 'SELECT * FROM Microbrasserie'
    micro = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
    _handle_erreur_connexion()
    return render_template("microbrasserie.html", micro=micro, model=model)


@app.route('/connexion', methods=['POST'])
def connexion():
    global model, erreur_connexion
    courriel = request.form.get('courriel')
    mot_de_passe = request.form.get('mot_de_passe')
    page_courante = request.form.get('page_courante')
    if courriel is not None and mot_de_passe is not None and len(courriel) <= 100 and re.match(
            r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel):
        requete = 'SELECT id, mot_de_passe FROM Mot_de_passe WHERE id IN (SELECT id FROM Utilisateur WHERE courriel=%s);'
        row = bd.execute_requete_lecture(requete, courriel)
        if row is not None:
            id_, hash_bd = row
            if hash_bd is not None and hash_bd == hashlib.sha512(mot_de_passe.encode('utf-8')).digest():
                requete = 'SELECT nom, prenom, id FROM Utilisateur WHERE id=%s;'
                model['utilisateur_courant'].update(bd.execute_requete_lecture(requete, id_, obtenir_dict=True))
                if 'panier' not in model['utilisateur_courant'].keys() or 'nombre_bieres' not in model[
                    'utilisateur_courant'].keys():
                    model['utilisateur_courant']['panier'] = dict()
                    model['utilisateur_courant']['nombre_bieres'] = 0
                requete = 'SELECT id FROM Microbrasserie WHERE id=%s'
                model['utilisateur_courant']['est_une_microbrasserie'] = bd.execute_requete_lecture(requete,
                                                                                                    id_) is not None
                requete = 'SELECT id FROM Acheteur WHERE id=%s'
                model['utilisateur_courant']['est_un_acheteur'] = bd.execute_requete_lecture(requete,
                                                                                                    id_) is not None
                return redirect(_redirect_to_page_courante(page_courante))

    erreur_connexion = True
    return redirect(_redirect_to_page_courante(page_courante))


@app.route('/inscription', methods=['GET'])
def afficher_signup():
    _handle_erreur_connexion()
    model['current_year'] = datetime.datetime.now().year
    return render_template('inscription.html', model=model)


@app.route('/inscription', methods=['POST'])
def signup():
    model['current_year'] = datetime.datetime.now().year

    # On recupere les informations du form
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    courriel = request.form.get('courriel')
    ville = request.form.get('ville')
    age_ = request.form.get('age')
    telephone = request.form.get('telephone')
    adresse = request.form.get('adresse')
    mot_de_passe = request.form.get('motdepasse')
    confirmation = request.form.get('confirmation')
    nom_micro = request.form.get('nommicro')
    emplacement = request.form.get('emplacement')
    annee_ = request.form.get('annee')

    # On verifie les entrees numeriques
    try:
        annee = int(annee_)
        age = int(age_)
    except ValueError:
        return render_template('inscription.html', message_erreur="Veuillez entrer des nombres valides", model=model)

    # Si le couriel est valide
    if courriel is not None and len(courriel) <= 100 and re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel):

        # On vérifie si le courriel est déjà présent dans le système
        requete = 'SELECT id FROM Utilisateur WHERE courriel = %s;'
        courrielexiste = bd.execute_requete_lecture(requete, courriel)
        if not courrielexiste:

            # On valide que les mots de passes concordent
            if mot_de_passe == confirmation:
                if re.match(r'[a-zA-Z\s\-]+$', prenom) and re.match(r'[a-zA-Z\s\-]+$', nom) and re.match(r'[a-zA-Z\s\-]+$', ville) and \
                   re.match(r'[a-zA-Z0-9\s\-]+$', adresse) and re.match(r'[0-9\-]+$', telephone):

                    # Si c'est une microbrasserie qui s'inscrit:
                    if nom_micro:
                        if emplacement and annee:
                            requete = 'SELECT nom FROM Utilisateur WHERE nom=%s;'
                            micro_existe = bd.execute_requete_lecture(requete, nom_micro)
                            if micro_existe is not None:
                                return render_template('inscription.html',
                                                       message_erreur="Une microbrasserie portant ce nom existe deja",
                                                       model=model)
                        else:
                            return render_template('inscription.html',
                                                   message_erreur="Veuillez entrer un emplacement et une annee d'inauguration",
                                                   model=model)

                    # On insert l'utilisateur et le mot de passe
                    conn, cursor = bd.open_connection_and_cursor()
                    try:
                        hash_bd = hashlib.sha512(mot_de_passe.encode('utf-8')).digest()
                        ajout = 'INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES (%s, %s, %s, %s, %s, %s, %s);'
                        cursor.execute(ajout, (ville, nom, age, adresse, telephone, courriel, prenom))
                        cursor.execute('SELECT LAST_INSERT_ID();')
                        id_utilisateur = cursor.fetchone()
                        ajout_mdp = 'INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (%s, %s);'
                        cursor.execute(ajout_mdp, (id_utilisateur, hash_bd))

                        # On ajoute le bon type d'utilisateur
                        if nom_micro:
                            ajout = 'INSERT INTO Microbrasserie (id, nom, emplacement, annee_inauguration) VALUES (%s, %s, %s, %s);'
                            cursor.execute(ajout, (id_utilisateur, nom_micro, emplacement, annee))
                        else:
                            ajout = 'INSERT INTO Acheteur VALUES (%s)'
                            cursor.execute(ajout, id_utilisateur)
                        # On commit les inserts si tout c'est bien passé
                        conn.commit()
                    except Exception as e:
                        return render_template('inscription.html',
                                               message_erreur="Une erreur est survenue lors de l'ajout de votre utilisateur",
                                               model=model)
                    bd.close_connection_and_cursor(conn, cursor)
                    if nom_micro:
                        return render_template('inscription.html',
                                               message_reussite='Votre compte de microbrasserie a été correctement créé. Félicitation!',
                                               model=model)
                    else:
                        return render_template('inscription.html',
                                               message_reussite='Votre compte a été correctement créé. Félicitation!',
                                               model=model)
                else:
                    return render_template('inscription.html',
                                           message_erreur='Des caractères invalides sont présents dans les champs de saisie',
                                           model=model)
    else:
        return render_template('inscription.html', message_erreur="L'adresse courriel est invalide", model=model)

    return render_template('inscription.html',
                           message_erreur='Le courriel est déjà utilisé ou les mots de passes ne concordent pas',
                           model=model)


@app.route('/panier')
def panier():
    global model
    _handle_erreur_connexion()
    if 'id' in model['utilisateur_courant']:
        model['message_erreur'] = ""
    if 'panier' in model['utilisateur_courant']:
        id_bieres = str([id_ for id_ in model['utilisateur_courant']['panier'].keys()])[1:-1]
        requete = 'SELECT B.id, B.image_url, B.nom AS bnom, B.prix AS prix, M.nom AS mnom, S.nom AS snom FROM Biere B, Microbrasserie M, Sorte S WHERE B.id_sorte = S.id AND M.id IN (SELECT id_microbrasserie FROM Vendre WHERE id_biere = B.id) AND B.id IN (' + id_bieres + ');'
        print(requete)
        bieres = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
        panier_biere = {}
        for biere in bieres:
            id_ = biere.pop('id')
            panier_biere[id_] = biere

        total_panier = 0
        for id_ in model['utilisateur_courant']['panier'].keys():
            model['utilisateur_courant']['panier'][id_].update(panier_biere[id_])
            total_panier += model['utilisateur_courant']['panier'][id_]['prix'] * \
                            model['utilisateur_courant']['panier'][id_]['quantite']
        model['total_panier'] = total_panier
        return render_template('panier.html', model=model)
    return redirect('/bieres')


@app.route('/update-panier')
def update_panier():
    global model
    quantite_ = request.args.get('quantite')
    id_biere_ = request.args.get('id_biere')
    try:
        quantite = int(quantite_)
        id_biere = int(id_biere_)
        if quantite == 0:
            del model['utilisateur_courant']['panier'][id_biere]
            if len(model['utilisateur_courant']['panier']) == 0:
                return redirect('/bieres')
        else:
            model['utilisateur_courant']['panier'][id_biere]['quantite'] = quantite
    except ValueError:
        pass
    return redirect('/panier')


@app.route('/deconnexion', methods=['POST'])
def deconnexion():
    global model
    model['utilisateur_courant'] = {}
    return redirect(_redirect_to_page_courante(request.form.get('page_courante')))


@app.route('/ajouter-au-panier', methods=['POST'])
def ajout_panier():
    global model
    try:
        id_biere = int(request.form.get('id_biere'))
        quantite = int(request.form.get('quantite'))
        if 'panier' not in model['utilisateur_courant'].keys() or 'nombre_bieres' not in model[
            'utilisateur_courant'].keys():
            model['utilisateur_courant']['panier'] = dict()
            model['utilisateur_courant']['nombre_bieres'] = 0
        if id_biere not in model['utilisateur_courant']['panier']:
            model['utilisateur_courant']['panier'][id_biere] = {'quantite': quantite}
        else:
            model['utilisateur_courant']['panier'][id_biere]['quantite'] += quantite
        model['utilisateur_courant']['nombre_bieres'] += quantite
    except ValueError:
        pass
    return redirect(_redirect_to_page_courante(request.form.get('redirect_url')))


@app.route('/checkout-panier')
def checkout_panier():
    if 'panier' not in model['utilisateur_courant']:
        return redirect('/bieres')
    if 'id' in model['utilisateur_courant']:
        if not model['utilisateur_courant']['est_un_acheteur']:
            model['message_erreur'] = "Vous devez etre un acheteur pour passer une commande"
            return redirect('/panier')
        id_acheteur = model['utilisateur_courant']['id']
        date_achat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn, cursor = bd.open_connection_and_cursor()
        for id_biere, info in model['utilisateur_courant']['panier'].items():
            quantite = info['quantite']
            try:
                requete = 'INSERT INTO Achete(id_acheteur, id_biere, quantite, date_achat) VALUES (%s, %s, %s, %s)'
                cursor.execute(requete, (id_acheteur, id_biere, quantite, date_achat))
            except Exception as e:  # Il ne reste plus de biere :(
                print(e)
                model['message_erreur'] = "Il ne reste plus assez de bieres pour passer votre commande!"
                conn.rollback()
                bd.close_connection_and_cursor(conn, cursor)
                return render_template('panier.html', model=model)
        conn.commit()
        bd.close_connection_and_cursor(conn, cursor)
        model['message_reussite'] = "Votre commande a bien été passée. Vous recevrez vos bières sous peu"
        model['utilisateur_courant']['panier'] = dict()
        model['utilisateur_courant']['nombre_bieres'] = 0
        return render_template('accueil.html', model=model)
    else:
        model['message_erreur'] = "Vous devez vous connecter avant de passer une commande"
        return redirect('/panier')


def _allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def _handle_erreur_connexion():
    global erreur_connexion, model
    if erreur_connexion:
        model['message_erreur_connexion'] = "L'adresse courriel ou le mot de passe n'est pas valide"
        erreur_connexion = False
    else:
        model['message_erreur_connexion'] = ""


def _redirect_to_page_courante(page_courante):
    return page_courante if page_courante is not None and len(page_courante) > 0 else '/'


if args.reset:
    bd.execute_script_creation('scripts/reset_bd.sql')
    bd.execute_script_creation('scripts/creation_tables.sql')
    bd.execute_script_insertion('scripts/insertion_tests.sql')
    print("La BD et les tables ont ete correctement generees")
elif __name__ == '__main__':
    app.run(debug=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))  # host='0.0.0.0'
