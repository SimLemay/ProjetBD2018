

from flask import Flask, render_template, request, redirect
import hashlib
import re
import argparse
from util import util_bd as bd

parser = argparse.ArgumentParser()
parser.add_argument('--reset', action='store_true')
args = parser.parse_args()

app = Flask(__name__)
utilisateur_courant = {}


@app.route('/')
def accueil():
    requete = 'SELECT B.id as id, B.nom as bnom, S.nom as snom, B.prix as prix, B.ibu as ibu, B.pourcentage_alcool as pa FROM Biere B, Sorte S WHERE B.id_sorte = S.id;'
    bieres = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
    return render_template('accueil.html', bieres=bieres, utilisateur_courant=utilisateur_courant)

@app.route('/nousContacter', methods=['GET'])
def nousContacter():
    return render_template('nousContacter.html')

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

            #Bieres dispos
            requete = 'SELECT B.id as id, B.nom as bnom, S.nom as snom, B.prix as prix, B.ibu as ibu, B.pourcentage_alcool as pa FROM Biere B, Sorte S WHERE B.id_sorte IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s) AND B.id_sorte = S.id;'
            biere_dispo = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

        except (ValueError, TypeError):
            id_sorte = None
            sous_sortes = []
            requete = 'SELECT B.id as id, B.nom as bnom, S.nom as snom, B.prix as prix, B.ibu as ibu, B.pourcentage_alcool as pa FROM Biere B, Sorte S WHERE B.id_sorte = S.id;'
            biere_dispo = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    return render_template('bieres.html', sortes=sortes, id_sorte=id_sorte, sous_sortes=sous_sortes, id_sous_sorte=id_sous_sorte, bieresdispo=biere_dispo, utilisateur_courant=utilisateur_courant)


@app.route('/Microbrasserie', methods=['GET'])
def microbrasserie():
    requete = 'SELECT * FROM Microbrasserie'
    micro = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
    return render_template("microbrasserie.html", micro=micro, utilisateur_courant=utilisateur_courant)


@app.route('/connexion', methods=['GET'])
def afficher_connexion():
    return render_template('login.html', utilisateur_courant=utilisateur_courant)


@app.route('/connexion', methods=['POST'])
def connexion():
    global utilisateur_courant
    courriel = request.form.get('courriel')
    mot_de_passe = request.form['mot_de_passe']
    if courriel is not None and mot_de_passe is not None and len(courriel) <= 100 and re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel):
        requete = 'SELECT id_utilisateur, mot_de_passe FROM Mot_de_passe WHERE id_utilisateur IN (SELECT id FROM Utilisateur WHERE courriel=%s);'
        row = bd.execute_requete_lecture(requete, courriel)
        if row is not None:
            id_, hash_bd = row
            if hash_bd is not None and hash_bd == hashlib.sha512(mot_de_passe.encode('utf-8')).digest():
                requete = 'SELECT nom, prenom FROM Utilisateur WHERE id=%s;'
                utilisateur_courant = bd.execute_requete_lecture(requete, id_, obtenir_dict=True)
                utilisateur_courant['panier'] = list()
                utilisateur_courant['nombre_bieres'] = 0
                return redirect('/')
    return render_template('login.html', message_erreur="L'adresse courriel ou le mot de passe n'est pas valide", utilisateur_courant=utilisateur_courant)


@app.route('/deconnexion', methods=['POST'])
def deconnexion():
    global utilisateur_courant
    utilisateur_courant = {}
    return redirect('/')


@app.route('/ajouter-au-panier', methods=['POST'])
def ajout_panier():
    global utilisateur_courant
    try:
        id_biere = int(request.form.get('id_biere'))
        quantite = int(request.form.get('quantite'))
        if ('panier', 'nombre_bieres') not in utilisateur_courant.keys():
            utilisateur_courant['panier'] = list()
            utilisateur_courant['nombre_bieres'] = 0
        utilisateur_courant['panier'].append((id_biere, quantite))
        utilisateur_courant['nombre_bieres'] += quantite
    except ValueError:
        pass
    redirect_url = request.form.get('redirect_url')
    return redirect(redirect_url)


if args.reset:
    bd.execute_script_creation('scripts/reset_bd.sql')
    bd.execute_script_creation('scripts/creation_tables.sql')
    bd.execute_script_insertion('scripts/insertion_tests.sql')
    print("La BD et les tables ont ete correctement generees")
elif __name__ == '__main__':
    app.run(debug=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
