from util import util_bd as bd
from random import randint

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam malesuada tristique ipsum, ac mollis " \
              "felis viverra sit amet. Suspendisse consectetur sit amet massa vitae fringilla. Duis a purus a nisl " \
              "rutrum finibus non vitae sem. Curabitur nisl dui, ultricies id bibendum quis, mattis sit amet posuere. "

VILLES = ['La Baie', 'Saguenay', 'Chicoutimi', 'Jonquière', 'Shipshaw', 'Falardeau', 'Kenogami', 'Arvida', 'Alma', 'Chambord', 'St-Félicien', 'Dolbeau', 'Hébertville']
PRENOM = ['Simon', 'Keven', 'Alexis', 'Antoine', 'Guillaume', 'Laurent', 'Félix', 'Jérôme', 'Isaac', 'Charles', 'Julien', 'Miguel', 'Elie', 'Jordan']
ADRESSE = ['324 rue ADAWDA', '4234 rue Fdsfkh', '2342 rue Feffs', '343 rue Hjffo', '456 rue Kfhesf', '765 rue Tfosef', '099 rue Fekshf', '4324 rue Gfjse', '345 rue Ffesf', '532 rue Ygrg', '7657 avenue Tygf']
NOM = ['Tremblay', 'Lemay', 'Bilodeau', 'Lessard', 'Boivin', 'Bélanger', 'Auger', 'Morel', 'Desbiens', 'Corneau', 'Lavoie', 'Sévigny', 'Doe']
# Utilisateur
requete = 'INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES (%s, %s, %s, %s, %s, %s, %s);'
for i in range(200):
    print(i)

# acheteur
conn, cursor = bd.open_connection_and_cursor()
try:
    cursor.execute('INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES (%s, %s, %s, %s, %s, %s, %s);', (VILLES, ))
    conn.commit()
except Exception as e:
    print(e)
bd.close_connection_and_cursor(conn, cursor)


# Microbrasserie

NOM_MICRO = ['Brasserie La Baie', 'Brasserie Saguenay', 'Brasserie Chicoutimi', 'Brasserie Jonquière', 'Brasserie Shipshaw', 'Brasserie Falardeau', 'Brasserie Kenogami', 'Brasserie Arvida', 'Brasserie Alma', 'Brasserie Chambord', 'Brasserie Dolbeau', 'Brasserie Hébertville']
requete3 = 'INSERT INTO Microbrasserie VALUES (%s, %s, %s, %s);'
# Mot de passe


# Biere
requete1 = 'INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, id_microbrasserie, date_ajout, id_sorte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

# Vendre

requete2 = 'INSERT INTO Vendre VALUES (%s, %s, %s);'

# Achete

requete2 = 'INSERT INTO Achete VALUES(%s, %s, %s, %s);'

