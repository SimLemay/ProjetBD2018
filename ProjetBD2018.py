import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import RequestEntityTooLarge
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


@app.route('/')
def accueil():
    requete = 'SELECT id, nom From Biere'
    bieres = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
    _handle_erreur_connexion()
    return render_template('accueil.html', bieres=bieres, model=model)


@app.route('/nous-contacter', methods=['GET'])
def nous_contacter():
    _handle_erreur_connexion()
    return render_template('nous-contacter.html', model=model)


@app.route('/nous-contacter', methods=['POST'])
def nous_contacter_post():
    return render_template('nous-contacter.html', model=model)


@app.route('/ajout-biere', methods=['GET'])
def ajout_biere():
    if 'est_une_microbrasserie' not in model['utilisateur_courant'].keys() or not model['utilisateur_courant']['est_une_microbrasserie']:
        return redirect('/')

    now = datetime.datetime.now()
    model['current_year'] = now.year

    requete = 'SELECT id, nom FROM Sorte WHERE id NOT IN (SELECT id_sorte_parent FROM Type_de) '
    model['sous_sortes'] = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    _handle_erreur_connexion()
    return render_template('ajout-biere.html', model=model)


@app.route('/ajout-biere', methods=['POST'])
def ajout_biere_post():

    prix = request.form.get('prix')
    nom = request.form.get('nom')
    pourcentage_alcool = request.form.get('alcool')
    ibu = request.form.get('ibu')
    annee_production = request.form.get('annee')
    description = request.form.get('description')
    id_sorte = request.form.get('id_sous_sorte')
    image = request.form.get('image')

    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename != '' and _allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            file_length = os.stat(path).st_size
            if file_length > 5000000:  # 5 MB
                os.remove(path)
                model['message_erreur_upload'] = "La taille de l'image doit etre de 5 Mo maximum"
                return render_template('ajout-biere.html', model=model)
            else:
                pass

    # 'image_url'
    # 'id_microbrasserie'
    # 'date_ajout'

    model['message_erreur_upload'] = "L'image n'a pas pu etre importe"
    return render_template('ajout-biere.html', model=model)


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


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
            requete = 'SELECT B.id AS id, B.nom AS bnom, S.nom AS snom, B.prix AS prix, B.ibu AS ibu, B.pourcentage_alcool AS pa FROM Biere B, Sorte S WHERE B.id_sorte IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s) AND B.id_sorte = S.id;'
            biere_dispo = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

        except (ValueError, TypeError):
            id_sorte = None
            sous_sortes = []
            requete = 'SELECT B.id AS id, B.nom AS bnom, S.nom AS snom, B.prix AS prix, B.ibu AS ibu, B.pourcentage_alcool AS pa FROM Biere B, Sorte S WHERE B.id_sorte = S.id;'
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
        requete = 'SELECT id_utilisateur, mot_de_passe FROM Mot_de_passe WHERE id_utilisateur IN (SELECT id FROM Utilisateur WHERE courriel=%s);'
        row = bd.execute_requete_lecture(requete, courriel)
        if row is not None:
            id_, hash_bd = row
            if hash_bd is not None and hash_bd == hashlib.sha512(mot_de_passe.encode('utf-8')).digest():
                requete = 'SELECT nom, prenom FROM Utilisateur WHERE id=%s;'
                model['utilisateur_courant'] = bd.execute_requete_lecture(requete, id_, obtenir_dict=True)
                model['utilisateur_courant']['panier'] = dict()
                model['utilisateur_courant']['nombre_bieres'] = 0
                requete = 'SELECT id_utilisateur FROM Microbrasserie WHERE id_utilisateur=%s'
                model['utilisateur_courant']['est_une_microbrasserie'] = bd.execute_requete_lecture(requete, id_) is not None
                return redirect(_redirect_to_page_courante(page_courante))

    erreur_connexion = True
    return redirect(_redirect_to_page_courante(page_courante))


@app.route('/inscription', methods=['GET'])
def afficher_signup():
    _handle_erreur_connexion()
    return render_template('inscription.html', model=model)


@app.route('/inscription', methods=['POST'])
def signup():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    courriel = request.form.get('courriel')
    mot_de_passe = request.form.get('motdepasse')
    confirmation = request.form.get('confirmation')

    if courriel is not None and len(courriel) <= 100 and re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel):
        requete = 'SELECT id FROM Utilisateur WHERE courriel = %s;'
        courrielexiste = bd.execute_requete_lecture(requete, courriel)
    else:
        return render_template('inscription.html', message_erreur="L'adresse courriel est invalide")

    if not courrielexiste:
        if mot_de_passe == confirmation and re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel) and re.match(r'[a-zA-Z\s\-]+$', prenom) and re.match(r'[a-zA-Z\s\-]+$', nom):
            hash_bd = hashlib.sha512(mot_de_passe.encode('utf-8')).digest()
            ajout = 'INSERT INTO Utilisateur (courriel, nom, prenom) VALUES (%s, %s, %s);'
            bd.execute_requete_ecriture(ajout, courriel, nom, prenom)
            ajout_mdp = 'INSERT INTO Mot_de_passe (mot_de_passe) VALUES (%s);'
            bd.execute_requete_ecriture(ajout_mdp, hash_bd)
            return redirect('/')

    return render_template('inscription.html', message_erreur= 'Le courriel est déjà utilisé ou les mots de passes ne concordent pas')


@app.route('/panier')
def panier():
    bierepanier = list()
    for idbiere in model['utilisateur_courant'].keys():
        requete = 'SELECT B.nom as bnom, B.prix as prix, M.nom as mnom, S.nom as snom FROM Biere B, Microbrasserie M, Sorte S WHERE B.id_sorte = S.id AND B.id_microbrasserie = M.id_utilisateur AND B.id = %s;'
        info = bd.execute_requete_lecture(requete, idbiere, fetchall=True, obtenir_dict=True)
        bierepanier.append(info)
    _handle_erreur_connexion()
    return render_template('panier.html', model=model, bierepanier=bierepanier)


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
        if 'panier' not in model['utilisateur_courant'].keys() or 'nombre_bieres' not in model['utilisateur_courant'].keys():
            model['utilisateur_courant']['panier'] = dict()
            model['utilisateur_courant']['nombre_bieres'] = 0
        model['utilisateur_courant']['panier'][id_biere] = model['utilisateur_courant']['panier'].get(id_biere, 0) + quantite
        model['utilisateur_courant']['nombre_bieres'] += quantite
    except ValueError:
        pass
    return redirect(_redirect_to_page_courante(request.form.get('redirect_url')))


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
