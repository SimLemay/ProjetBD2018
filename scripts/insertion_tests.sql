INSERT INTO Microbrasserie(id_utilisateur, nom) VALUES(1, 'Boreale');
INSERT INTO Ingredient(id, nom) VALUES(1, 'Houblon');
INSERT INTO Liste_ingredients(id, id_ingredient) VALUES(1, 1);
INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients) VALUES(1, 'IPA du Nord-Est', 1, 1);
INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients) VALUES(2, 'Boreale IPA', 1, 1);