INSERT INTO Microbrasserie(id_utilisateur, nom) VALUES(1, 'Boreale');
INSERT INTO Ingredient(id, nom) VALUES(1, 'Houblon');
INSERT INTO Liste_ingredients(id, id_ingredient) VALUES(1, 1);
INSERT INTO Sorte(id, aromes, nom) VALUES(1, 'Houblon houblonné', 'IPA');

INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients, id_sorte) VALUES(1, 'IPA du Nord-Est', 1, 1, 1);
INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients, id_sorte) VALUES(2, 'Boreale IPA', 1, 1, 1);

insert into Utilisateur(id, courriel, nom, prenom) values(1, 'simon@test.ca', 'Lemay-Lauziere', 'Simon');
insert into Utilisateur(id, courriel, nom, prenom) values(2, 'keven@ulaval.ca', 'Lamontagne', 'Keven');
-- Simon : test
insert into Mot_de_passe(id_utilisateur, mot_de_passe) values(1, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
-- Keven : ulaval
insert into Mot_de_passe(id_utilisateur, mot_de_passe) values(2, X'5c75dc48fdb6b2b3a8349899fd7963b9c043e7dffe720368ff2ef16dbd45afcb50869585671fa9d270ea411ee83b86dd8701f7a9eb986095e5f9a4305c8e2015');



# Création des représentants des microbrasseries
INSERT INTO Utilisateur VALUES(1, 'Représentant Microbrasserie Dunham', 'Dunham', 'Tremblay', 30, '1111 rue de la Bière', '418-332-4323', 'Dunham@bière.ca', 'Jean');
INSERT INTO Utilisateur VALUES(2, 'Representant Microbrasserie PitCaribou', 'Percé', 'Boivin', 32, '2222 rue de la Bière', '418-322-3534', 'PitCaribou@bière.ca', 'Marc');
INSERT INTO Utilisateur VALUES(3, 'Representant Microbrasserie Vox Populi', 'Boucherville', 'Turcotte', 35, '3333 rue de la Bière', '418-434-5453', 'VoxPopuli@bière.ca', 'Étienne');
INSERT INTO Utilisateur VALUES(4, 'Representant Microbrasserie Trou du Diable', 'Shawinigan', 'Chrétien', 40, '4444 rue de la Bière', '418-433-4324', 'TrouDuDiable@bière.ca', 'Jean');
INSERT INTO Utilisateur VALUES(5, 'Representant Microbrasserie Auval', 'Gaspé', 'Lessard', 28, '5555 rue de la Bière', '418-433-4343', 'Auval@bière.ca', 'Guy');

#Création des microbrasseries
INSERT INTO Microbrasserie VALUES(1, 'Brasserie Dunham', 'Dunham', 2011, 0);
INSERT INTO Microbrasserie VALUES(2, 'Pit Caribou', 'Anse-à-Beaufils', 2007, 0);
INSERT INTO Microbrasserie VALUES(3, 'Microbrasserie Vox Populi', 'Boucherville', 2016, 0);
INSERT INTO Microbrasserie VALUES(4, 'Trou du Diable', 'Shawinigan', 2006, 0);
INSERT INTO Microbrasserie VALUES(5, 'Brasserie Auval', 'Val d\'Espoir', 2016, 0);

#Ajout de bieres

INSERT INTO Biere VALUES(1, '', 20.00,'Cyclope Kappa IPA', 5.7, 60, 2018, '', 1, 2018-04-06, 0);
INSERT INTO Biere VALUES(2, '', 15.00, 'Supermoine Numéro 4', 4.5, NULL, 2018, '', 1, 2018-04-06, 0);
INSERT INTO Biere VALUES(3, '', 15.00, 'Saison du Pinacle', 6.5, 52, 2018, '', 1, 2018-04-06, 0);
INSERT INTO Biere VALUES(4, '', 15.00, 'Berliner Melon Weisse', 3.9, 8, 2018, 1, 2018-04-06, 0);
INSERT INTO Biere VALUES(5, '', 15.00, 'LaBatt Porter Robuste', 6.0, 51, 2018, 1, 2018-04-06, 0);

INSERT INTO Biere VALUES(6, '', 10.00, 'IPA Américaine des Appalaches', 7.0, 77, 2018, '', 2, 2018-04-06, 0);
INSERT INTO Biere VALUES(7, '', 10.00, 'La Blonde de l\'Anse', 5.0, 17, 2018, '', 2, 2018-04-06, 0);
INSERT INTO Biere VALUES(8, '', 10.00, 'Brown Ale Américaine', 7.0, 90, 2018, '', 2, 2018-04-06, 0);
INSERT INTO Biere VALUES(9, '', 10.00, 'La Bonne Aventure', 5.0, 25, 2018, '', 2, 2018-04-06, 0);
INSERT INTO Biere VALUES(10, '', 10.00, 'Gose IPA du Barachois', 3.8, 30, 2018, '', 2, 2018-04-06, 0);

INSERT INTO Biere VALUES(11, '', 8.00, 'Double Fruit Punch IPA', 8.0, 100, 2018, '', 3, 2018-04-06, 0);
INSERT INTO Biere VALUES(12, '', 8.00, 'Anna', 10.0, 75, 2018, '', 3, 2018-04-06, 0);
INSERT INTO Biere VALUES(13, '', 8.00, 'Vox Stout(MilkShake)', 5.5, 25, 2018, '', 3, 2018-04-06, 0);
INSERT INTO Biere VALUES(14, '', 8.00, 'Kettle Sour', 3.0, 3, 2018, '', 3, 2018-04-06, 0);
INSERT INTO Biere VALUES(15, '', 8.00, 'Vox Pop IPA', 6.5, 45, 2018, '', 3, 2018-04-06, 0);

INSERT INTO Biere VALUES(16, '', 5.00, 'La Saison du Tracteur', 6.0, 35, 2018, '', 4, 2018-04-06, 0);
INSERT INTO Biere VALUES(17, '', 5.00, 'Les Quatres Surfeurs de L\'Apocalypso', 6.5, 60, 2018, '', 4, 2018-04-06, 0);
INSERT INTO Biere VALUES(18, '', 5.00, 'La Buteuse', 10.0, 60, 2018, '', 4, 2018-04-06, 0);
INSERT INTO Biere VALUES(19, '', 5.00, 'Le Sang d\'Encre', 5.5, 45, 2018, '', 4, 2018-04-06, 0);
INSERT INTO Biere VALUES(20, '', 5.00, 'La Morsure', 6.5, 77, 2018, '', 4, 2018-04-06, 0);

INSERT INTO Biere VALUES(21, '', 12.00, 'Super A', 8.0, 60, 2018, '', 5, 2018-04-06, 0);
INSERT INTO Biere VALUES(22, '', 12.00, 'Saison Espinay', 6.5, 30, 2018, '', 5, 2018-04-06, 0);
INSERT INTO Biere VALUES(23, '', 12.00, 'Arrière-Pays Grisette', 4.5, NULL, 2018, '', 5, 2018-04-06, 0);
INSERT INTO Biere VALUES(24, '', 12.00, 'Arcane 17 IPA', 5.2, 60, 2018, '', 5, 2018-04-06, 0);
INSERT INTO Biere VALUES(25, '', 12.00, 'Guerilla SSS', 7.8, 40, 2016, '', 5, 2018-04-06, 0);

#Création des sortes de bières selon CraftBeer.com

#Sortes parents

INSERT INTO Sorte VALUES(1, '', 'Pales Ales');
INSERT INTO Sorte VALUES(2, '', 'Dark Lagers');
INSERT INTO Sorte VALUES(3, '', 'Brown Ales');
INSERT INTO Sorte VALUES(4, '', 'India Pale Ales');
INSERT INTO Sorte VALUES(5, '', 'Wheat Beers');
INSERT INTO Sorte VALUES(6, '', 'Strong Ales');
INSERT INTO Sorte VALUES(7, '', 'Belgian Styles');
INSERT INTO Sorte VALUES(8, '', 'Hybrid Beers');
INSERT INTO Sorte VALUES(9, '', 'Porters');
INSERT INTO Sorte VALUES(10, '','Stouts');
INSERT INTO Sorte VALUES(11, '', 'Bocks');
INSERT INTO Sorte VALUES(12, '', 'Scottish-Style Ales');
INSERT INTO Sorte VALUES(13, '', 'Wild/Sour Beers');
INSERT INTO Sorte VALUES(14,'', 'Pilsners and Pale Lagers');
INSERT INTO Sorte VALUES(15, '', 'Specialty Beers');
INSERT INTO Sorte VALUES(16,'', 'Session');

