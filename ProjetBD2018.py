from flask import Flask, render_template, request, redirect
import hashlib
import re
from util import util_bd as bd

app = Flask(__name__)
utilisateur_courant = {}


@app.route('/')
def accueil():
    requete = 'SELECT id, nom FROM Biere'
    bieres = bd.execute_requete_lecture(requete, fetchall=True)
    return render_template('accueil.html', bieres=bieres, utilisateur_courant=utilisateur_courant)


@app.route('/connexion', methods=['GET'])
def afficher_connexion():
    return render_template('login.html')


@app.route('/connexion', methods=['POST'])
def connexion():
    global utilisateur_courant
    courriel = request.form.get('courriel')
    mot_de_passe = request.form['mot_de_passe']
    if courriel is not None and mot_de_passe is not None and len(courriel) <= 100 and re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", courriel):
        requete = 'SELECT id_utilisateur, mot_de_passe FROM Mot_de_passe WHERE id_utilisateur IN (SELECT id FROM Utilisateur WHERE courriel=' + '"' + courriel + '"' + ');'
        row = bd.execute_requete_lecture(requete)
        if row is not None:
            id_, hash_bd = row
            if hash_bd is not None and hash_bd == hashlib.sha512(mot_de_passe.encode('utf-8')).digest():
                requete = 'SELECT nom, prenom FROM Utilisateur WHERE id=' + str(id_) + ';'
                row = bd.execute_requete_lecture(requete)
                if row is not None:
                    nom, prenom = row
                    utilisateur_courant['nom'] = nom
                    utilisateur_courant['prenom'] = prenom
                    return redirect('/')
    return render_template('login.html', message_erreur="L'adresse courriel ou le mot de passe n'est pas valide")


@app.route('/deconnexion')
def deconnexion():
    global utilisateur_courant
    utilisateur_courant = {}
    return redirect('/')

@app.route('/recherche')
def recherche():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
