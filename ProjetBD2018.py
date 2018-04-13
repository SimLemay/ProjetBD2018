

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
    requete = 'SELECT id, nom FROM Biere;'
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
            requete = 'SELECT * FROM Biere WHERE id_sorte IN (SELECT id_sorte_enfant FROM Type_de WHERE id_sorte_parent = %s);'
            biere_dispo = bd.execute_requete_lecture(requete, id_sorte, fetchall=True, obtenir_dict=True)

        except (ValueError, TypeError):
            id_sorte = None
            sous_sortes = []
            requete = 'SELECT * FROM Biere;'
            biere_dispo = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)

    return render_template('bieres.html', sortes=sortes, id_sorte=id_sorte, sous_sortes=sous_sortes, id_sous_sorte=id_sous_sorte, bieresdispo=biere_dispo)


@app.route('/Microbrasserie', methods=['GET'])
def microbrasserie():
    requete = 'SELECT * FROM Microbrasserie'
    micro = bd.execute_requete_lecture(requete, fetchall=True, obtenir_dict=True)
    return render_template("microbrasserie.html", micro=micro)

@app.route('/connexion', methods=['GET'])
def afficher_connexion():
    return render_template('login.html')


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
                if utilisateur_courant:
                    return redirect('/')
    return render_template('login.html', message_erreur="L'adresse courriel ou le mot de passe n'est pas valide")


@app.route('/deconnexion')
def deconnexion():
    global utilisateur_courant
    utilisateur_courant = {}
    return redirect('/')


if args.reset:
    bd.execute_script_creation('scripts/reset_bd.sql')
    bd.execute_script_creation('scripts/creation_tables.sql')
    bd.execute_script_insertion('scripts/insertion_tests.sql')
    print("La BD et les tables ont ete correctement generees")
elif __name__ == '__main__':
    app.run(debug=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
