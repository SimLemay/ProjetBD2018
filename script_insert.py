import datetime
import hashlib

from util import util_bd as bd
from random import randint, random

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam malesuada tristique ipsum, ac mollis " \
              "felis viverra sit amet. Suspendisse consectetur sit amet massa vitae fringilla. Duis a purus a nis"
VILLES = ['La Baie', 'Saguenay', 'Chicoutimi', 'Jonquière', 'Shipshaw', 'Falardeau', 'Kenogami', 'Arvida', 'Alma',
          'Chambord', 'St-Félicien', 'Dolbeau', 'Hébertville']
PRENOM = ['Simon', 'Keven', 'Alexis', 'Antoine', 'Guillaume', 'Laurent', 'Félix', 'Jérôme', 'Isaac', 'Charles',
          'Julien', 'Miguel', 'Elie', 'Jordan']
ADRESSE = ['324 rue ADAWDA', '4234 rue Fdsfkh', '2342 rue Feffs', '343 rue Hjffo', '456 rue Kfhesf', '765 rue Tfosef',
           '099 rue Fekshf', '4324 rue Gfjse', '345 rue Ffesf', '532 rue Ygrg', '7657 avenue Tygf']
NOM = ['Tremblay', 'Lemay', 'Bilodeau', 'Lessard', 'Boivin', 'Bélanger', 'Auger', 'Morel', 'Desbiens', 'Corneau',
       'Lavoie', 'Sévigny', 'Doe']
NOM_MICRO = ['Brasserie La Baie', 'Brasserie Saguenay', 'Brasserie Chicoutimi', 'Brasserie Jonquière',
             'Brasserie Shipshaw', 'Brasserie Falardeau', 'Brasserie Kenogami', 'Brasserie Arvida', 'Brasserie Alma',
             'Brasserie Chambord', 'Brasserie Dolbeau', 'Brasserie Hébertville']
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

courriels_set = set()
while len(courriels_set) < 100:
    courriels_set.add(''.join(ALPHABET[randint(0, 25)] for _ in range(20)) + '@ulaval.ca')
courriels = [*courriels_set]

requete_utilisateur = 'INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES (%s, %s, %s, %s, %s, %s, %s);'
requete_mot_de_passe = 'INSERT INTO Mot_de_passe VALUES (%s, %s)'
requete_micro = 'INSERT INTO Microbrasserie VALUES (%s, %s, %s, %s);'
requete_acheteur = 'INSERT INTO Acheteur VALUES (%s)'
requete_biere = 'INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
requete_vendre = 'INSERT INTO Vendre VALUES (%s, %s, %s);'
requete_achete = 'INSERT INTO Achete(id_acheteur, id_biere, quantite) VALUES(%s, %s, %s);'

conn, cursor = bd.open_connection_and_cursor()

try:
    # Insertion des utilisateurs
    j = 0
    for i in range(100):
        nom = NOM[randint(0, len(NOM) - 1)]
        cursor.execute(requete_utilisateur,
                       (VILLES[randint(0, len(VILLES) - 1)], nom, randint(18, 100),
                        LOREM_IPSUM[randint(0, 75):-randint(1, 75)], randint(11111111111, 99999999999),
                        courriels[i], PRENOM[randint(0, len(PRENOM) - 1)]))
        cursor.execute('SELECT LAST_INSERT_ID();')
        id_utilisateur = cursor.fetchone()
        cursor.execute(requete_mot_de_passe, (id_utilisateur, hashlib.sha512(nom.encode('utf-8')).digest()))
        if i % 10 == 0:
            cursor.execute(requete_micro, (id_utilisateur, NOM_MICRO[j] + str(i),
                                           LOREM_IPSUM[randint(0, 75):-randint(1, 75)], randint(1960, 2018)))
            j += 1

        else:
            cursor.execute(requete_acheteur, id_utilisateur)
        conn.commit()

    # Insertion des Bieres pour les 10 micros
    for i in range(100):
        cursor.execute(requete_biere, ('./images/' + str(randint(1, 5)) + '.jpg',
                                       randint(5, 25), LOREM_IPSUM[0:randint(10, 20)],
                                       randint(0, 11), randint(0, 120), randint(1980, 2018),
                                       LOREM_IPSUM[randint(0, 75):-randint(1, 75)],
                                       datetime.datetime.now().strftime('%Y-%m-%d'), randint(17, 84)))
        cursor.execute('SELECT LAST_INSERT_ID();')
        id_biere = cursor.fetchone()
        cursor.execute(requete_vendre, (((i % 10) + 1) * 10 - 2, id_biere, randint(6, 100)))
        conn.commit()

    # Creation de quelques achats
    for i in range(25):
        id_utilisateur = randint(2, 99)
        try:
            cursor.execute(requete_achete, (id_utilisateur if id_utilisateur % 10 != 0 else id_utilisateur - 1,
                                            randint(1, 99), randint(1, 3)))
            conn.commit()
        except Exception:
            pass

except Exception as e:
    print(e)
bd.close_connection_and_cursor(conn, cursor)
