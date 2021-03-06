-- Création des représentants des microbrasseries
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES
  ('Dunham', 'Tremblay', 30, '1111 rue de la Bière', '4183324323',
   'Dunham@bière.ca', 'Jean');
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES
  ('Percé', 'Boivin', 32, '2222 rue de la Bière', '4183223534',
   'PitCaribou@bière.ca', 'Marc');
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES
  ('Boucherville', 'Turcotte', 35, '3333 rue de la Bière', '4184345453',
   'VoxPopuli@bière.ca', 'Étienne');
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES
  ('Shawinigan', 'Chrétien', 40, '4444 rue de la Bière', '4184334324',
   'TrouDuDiable@bière.ca', 'Jean');
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES
  ('Gaspé', 'Lessard', 28, '5555 rue de la Bière', '4184334343', 'Auval@bière.ca',
   'Guy');

-- Création des microbrasseries
INSERT INTO Microbrasserie VALUES (1, 'Brasserie Dunham', 'Dunham', 2011);
INSERT INTO Microbrasserie VALUES (2, 'Pit Caribou', 'Anse-à-Beaufils', 2007);
INSERT INTO Microbrasserie VALUES (3, 'Microbrasserie Vox Populi', 'Boucherville', 2016);
INSERT INTO Microbrasserie VALUES (4, 'Trou du Diable', 'Shawinigan', 2006);
INSERT INTO Microbrasserie VALUES (5, 'Brasserie Auval', 'Val d\'Espoir', 2016);

-- Creation des utilisateurs de tests
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES ('Quebec', 'Lemay-Lauziere', 22, 'ipsum lorem', '41893215789', 'simon@test.ca', 'Simon');
INSERT INTO Utilisateur (ville, nom, age, adresse, telephone, courriel, prenom) VALUES ('Saguenay', 'Lamontagne', 20, 'bla bla bla', '58178351237', 'keven@ulaval.ca', 'Keven');
INSERT INTO Acheteur VALUES (6);
INSERT INTO Acheteur VALUES (7);


INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (1, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (2, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (3, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (4, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (5, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');




-- Simon : test
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (6, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
-- Keven : ulaval
INSERT INTO Mot_de_passe (id, mot_de_passe) VALUES (7, X'5c75dc48fdb6b2b3a8349899fd7963b9c043e7dffe720368ff2ef16dbd45afcb50869585671fa9d270ea411ee83b86dd8701f7a9eb986095e5f9a4305c8e2015');

-- Création des sortes de bières selon CraftBeer.com

-- Sortes parents
INSERT INTO Sorte VALUES (1, 'Pales Ales');
INSERT INTO Sorte VALUES (2, 'Dark Lagers');
INSERT INTO Sorte VALUES (3, 'Brown Ales');
INSERT INTO Sorte VALUES (4, 'India Pale Ales');
INSERT INTO Sorte VALUES (5, 'Wheat Beers');
INSERT INTO Sorte VALUES (6, 'Strong Ales');
INSERT INTO Sorte VALUES (7, 'Belgian Styles');
INSERT INTO Sorte VALUES (8, 'Hybrid Beers');
INSERT INTO Sorte VALUES (9, 'Porters');
INSERT INTO Sorte VALUES (10, 'Stouts');
INSERT INTO Sorte VALUES (11, 'Bocks');
INSERT INTO Sorte VALUES (12, 'Scottish-Style Ales');
INSERT INTO Sorte VALUES (13, 'Wild/Sour Beers');
INSERT INTO Sorte VALUES (14, 'Pilsners and Pale Lagers');
INSERT INTO Sorte VALUES (15, 'Specialty Beers');
INSERT INTO Sorte VALUES (16, 'Session');
INSERT INTO Sorte VALUES (85, 'Barrel-Aged Beer');

-- Sortes enfants suivi des relations type de

INSERT INTO Sorte VALUES (17, 'American Amber Ale');
INSERT INTO Sorte VALUES (18, 'American Pale Ale');
INSERT INTO Sorte VALUES (19, 'Blonde Ale');
INSERT INTO Sorte VALUES (20, 'English-style Bitter');
INSERT INTO Sorte VALUES (21, 'English-style Pale Ale');

INSERT INTO Type_de VALUES (1, 17);
INSERT INTO Type_de VALUES (1, 18);
INSERT INTO Type_de VALUES (1, 19);
INSERT INTO Type_de VALUES (1, 20);
INSERT INTO Type_de VALUES (1, 21);

INSERT INTO Sorte VALUES (22, 'American Amber Lager');
INSERT INTO Sorte VALUES (23, 'German-style Dunken');
INSERT INTO Sorte VALUES (24, 'German-style Marzen');
INSERT INTO Sorte VALUES (25, 'German-style Schwarzbier');
INSERT INTO Sorte VALUES (26, 'Vienna-style Lager');

INSERT INTO Type_de VALUES (2, 22);
INSERT INTO Type_de VALUES (2, 23);
INSERT INTO Type_de VALUES (2, 24);
INSERT INTO Type_de VALUES (2, 25);
INSERT INTO Type_de VALUES (2, 26);

INSERT INTO Sorte VALUES (27, 'American Brown Ale');
INSERT INTO Sorte VALUES (28, 'English-style Brown Ale');
INSERT INTO Sorte VALUES (29, 'English-style Mild');

INSERT INTO Type_de VALUES (3, 27);
INSERT INTO Type_de VALUES (3, 28);
INSERT INTO Type_de VALUES (3, 29);

INSERT INTO Sorte VALUES (30, 'American IPA');
INSERT INTO Sorte VALUES (31, 'English-style IPA');
INSERT INTO Sorte VALUES (32, 'Imperial IPA');
INSERT INTO Sorte VALUES (33, 'New England IPA');

INSERT INTO Type_de VALUES (4, 30);
INSERT INTO Type_de VALUES (4, 31);
INSERT INTO Type_de VALUES (4, 32);
INSERT INTO Type_de VALUES (4, 33);

INSERT INTO Sorte VALUES (34, 'American-style Wheat Wine Ale');
INSERT INTO Sorte VALUES (35, 'American Wheat');
INSERT INTO Sorte VALUES (36, 'Belgian-style Witbier');
INSERT INTO Sorte VALUES (37, 'Berline-style Weisse');
INSERT INTO Sorte VALUES (38, 'German-style Dunkelweizen');
INSERT INTO Sorte VALUES (39, 'German-style Hefeweizen');

INSERT INTO Type_de VALUES (5, 34);
INSERT INTO Type_de VALUES (5, 35);
INSERT INTO Type_de VALUES (5, 36);
INSERT INTO Type_de VALUES (5, 37);
INSERT INTO Type_de VALUES (5, 38);
INSERT INTO Type_de VALUES (5, 39);

INSERT INTO Sorte VALUES (40, 'American Barley Wine');
INSERT INTO Sorte VALUES (41, 'American Imperial Red Wine');
INSERT INTO Sorte VALUES (42, 'British-style Barley Wine Ale');
INSERT INTO Sorte VALUES (43, 'English-style Old Ale');

INSERT INTO Type_de VALUES (6, 40);
INSERT INTO Type_de VALUES (6, 41);
INSERT INTO Type_de VALUES (6, 42);
INSERT INTO Type_de VALUES (6, 43);

INSERT INTO Sorte VALUES (44, 'Belgian-style Blonde Ale');
INSERT INTO Sorte VALUES (45, 'Belgian-style Dubbel');
INSERT INTO Sorte VALUES (46, 'Belgian-style Golden Blonde Ale');
INSERT INTO Sorte VALUES (47, 'Belgian-style Pale Ale');
INSERT INTO Sorte VALUES (48, 'Belgian-style Quadrupel');
INSERT INTO Sorte VALUES (49, 'Belgian-style Saison');
INSERT INTO Sorte VALUES (50, 'Belgian-style Tripel');

INSERT INTO Type_de VALUES (7, 44);
INSERT INTO Type_de VALUES (7, 45);
INSERT INTO Type_de VALUES (7, 46);
INSERT INTO Type_de VALUES (7, 47);
INSERT INTO Type_de VALUES (7, 48);
INSERT INTO Type_de VALUES (7, 49);
INSERT INTO Type_de VALUES (7, 50);

INSERT INTO Sorte VALUES (51, 'American Cream Ale');
INSERT INTO Sorte VALUES (52, 'French-style Biere de Garde');
INSERT INTO Sorte VALUES (53, 'California Common');
INSERT INTO Sorte VALUES (54, 'German-style Altbier');
INSERT INTO Sorte VALUES (55, 'German-style Kolsch');
INSERT INTO Sorte VALUES (56, 'Irish-style Red');

INSERT INTO Type_de VALUES (8, 51);
INSERT INTO Type_de VALUES (8, 52);
INSERT INTO Type_de VALUES (8, 53);
INSERT INTO Type_de VALUES (8, 54);
INSERT INTO Type_de VALUES (8, 55);
INSERT INTO Type_de VALUES (8, 56);

INSERT INTO Sorte VALUES (57, 'American Imperial Porter');
INSERT INTO Sorte VALUES (58, 'Baltic-style Porter');
INSERT INTO Sorte VALUES (59, 'English-style Brown Porter');
INSERT INTO Sorte VALUES (60, 'Robust Porter');
INSERT INTO Sorte VALUES (61, 'Smoke Porter');

INSERT INTO Type_de VALUES (9, 57);
INSERT INTO Type_de VALUES (9, 58);
INSERT INTO Type_de VALUES (9, 59);
INSERT INTO Type_de VALUES (9, 60);
INSERT INTO Type_de VALUES (9, 61);

INSERT INTO Sorte VALUES (62, 'American Imperial Stout');
INSERT INTO Sorte VALUES (63, 'American Stout');
INSERT INTO Sorte VALUES (64, 'English-style Oatmeal Stout');
INSERT INTO Sorte VALUES (65, 'English-style Sweet Stout');
INSERT INTO Sorte VALUES (66, 'Irish-style Dry Stout');

INSERT INTO Type_de VALUES (10, 62);
INSERT INTO Type_de VALUES (10, 63);
INSERT INTO Type_de VALUES (10, 64);
INSERT INTO Type_de VALUES (10, 65);
INSERT INTO Type_de VALUES (10, 66);

INSERT INTO Sorte VALUES (67, 'German-style Bock');
INSERT INTO Sorte VALUES (68, 'German-style Doppelbock');
INSERT INTO Sorte VALUES (69, 'German-style Maibock');
INSERT INTO Sorte VALUES (70, 'German-style Weizenbock');

INSERT INTO Type_de VALUES (11, 67);
INSERT INTO Type_de VALUES (11, 68);
INSERT INTO Type_de VALUES (11, 69);
INSERT INTO Type_de VALUES (11, 70);

INSERT INTO Sorte VALUES (71, 'Scotch Ale/Wee Heavy');
INSERT INTO Sorte VALUES (72, 'Scottish-style Ale');

INSERT INTO Type_de VALUES (12, 71);
INSERT INTO Type_de VALUES (12, 72);

INSERT INTO Sorte VALUES (73, 'American Brett');
INSERT INTO Sorte VALUES (74, 'American Sour');
INSERT INTO Sorte VALUES (75, 'Belgian-style Flanders');
INSERT INTO Sorte VALUES (76, 'Belgian-style Fruit Lambic');
INSERT INTO Sorte VALUES (77, 'Belgian-style Lambic/Gueuze');
INSERT INTO Sorte VALUES (78, 'Contemporary Gose');

INSERT INTO Type_de VALUES (13, 73);
INSERT INTO Type_de VALUES (13, 74);
INSERT INTO Type_de VALUES (13, 75);
INSERT INTO Type_de VALUES (13, 76);
INSERT INTO Type_de VALUES (13, 77);
INSERT INTO Type_de VALUES (13, 78);

INSERT INTO Sorte VALUES (79, 'American Lager');
INSERT INTO Sorte VALUES (80, 'Bohemian-style Pilsner');
INSERT INTO Sorte VALUES (81, 'European-style Export');
INSERT INTO Sorte VALUES (82, 'German-style Helles');
INSERT INTO Sorte VALUES (83, 'German-style Pilsner');

INSERT INTO Type_de VALUES (14, 79);
INSERT INTO Type_de VALUES (14, 80);
INSERT INTO Type_de VALUES (14, 81);
INSERT INTO Type_de VALUES (14, 82);
INSERT INTO Type_de VALUES (14, 83);

INSERT INTO Sorte VALUES (84, 'American Black Ale');
INSERT INTO Sorte VALUES (86, 'Chocolate Beer');
INSERT INTO Sorte VALUES (87, 'Coffee Beer');
INSERT INTO Sorte VALUES (88, 'Fruit and field Beer');
INSERT INTO Sorte VALUES (89, 'Gluten Free');
INSERT INTO Sorte VALUES (90, 'Herb and Spice Beer');
INSERT INTO Sorte VALUES (91, 'Honey Beer');
INSERT INTO Sorte VALUES (92, 'Pumpkin Beer');
INSERT INTO Sorte VALUES (93, 'Rye Beer');
INSERT INTO Sorte VALUES (94, 'Smoke Beer');
INSERT INTO Sorte VALUES (95, 'Specialty Beer');
INSERT INTO Sorte VALUES (96, 'Grisette');

INSERT INTO Type_de VALUES (15, 84);
INSERT INTO Type_de VALUES (15, 86);
INSERT INTO Type_de VALUES (15, 87);
INSERT INTO Type_de VALUES (15, 88);
INSERT INTO Type_de VALUES (15, 89);
INSERT INTO Type_de VALUES (15, 90);
INSERT INTO Type_de VALUES (15, 91);
INSERT INTO Type_de VALUES (15, 92);
INSERT INTO Type_de VALUES (15, 93);
INSERT INTO Type_de VALUES (15, 94);
INSERT INTO Type_de VALUES (15, 95);
INSERT INTO Type_de VALUES (15, 96);

-- Ajout de Bieres
INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/1.jpg', 20.00, 'Leo\'s Early Breakfast IPA', 6.2, 54, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (1, 1, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/2.jpg', 15.00, 'Supermoine Numéro 4', 4.5, 0, 2018, 'Une description pas tres descriptive', '2018-04-06', 46);
INSERT INTO Vendre VALUES (1, 2, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/3.jpg', 15.00, 'Saison du Pinacle', 6.5, 52, 2018, 'Une description pas tres descriptive', '2018-04-06', 16);
INSERT INTO Vendre VALUES (1, 3, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/4.jpg', 15.00, 'Berliner Melon Weisse', 3.9, 8, 2018, 'Une description pas tres descriptive', '2018-04-06', 37);
INSERT INTO Vendre VALUES (1, 4, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/5.jpg', 15.00, 'LaBatt Porter Robuste', 6.0, 51, 2018, 'Une description pas tres descriptive', '2018-04-06', 60);
INSERT INTO Vendre VALUES (3, 5, 5);


INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/3.jpg', 10.00, 'IPA Américaine des Appalaches', 7.0, 77, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (3, 6, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/1.jpg', 10.00, 'La Blonde de l\'Anse', 5.0, 17, 2018, 'Une description pas tres descriptive', '2018-04-06', 46);
INSERT INTO Vendre VALUES (3, 7, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/4.jpg', 10.00, 'Brown Ale Américaine', 7.0, 90, 2018, 'Une description pas tres descriptive', '2018-04-06', 27);
INSERT INTO Vendre VALUES (3, 8, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/2.jpg', 10.00, 'La Bonne Aventure', 5.0, 25, 2018, 'Une description pas tres descriptive', '2018-04-06', 75);
INSERT INTO Vendre VALUES (3, 9, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/3.jpg', 10.00, 'Gose IPA du Barachois', 3.8, 30, 2018, 'Une description pas tres descriptive', '2018-04-06', 78);
INSERT INTO Vendre VALUES (3, 10, 5);


INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/5.jpg', 8.00, 'Double Fruit Punch IPA', 8.0, 100, 2018, 'Une description pas tres descriptive', '2018-04-06', 32);
INSERT INTO Vendre VALUES (2, 11, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/1.jpg', 8.00, 'Anna', 10.0, 75, 2018, 'Une description pas tres descriptive', '2018-04-06', 50);
INSERT INTO Vendre VALUES (2, 12, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/5.jpg', 8.00, 'Vox Stout(MilkShake)', 5.5, 25, 2018, 'Une description pas tres descriptive', '2018-04-06', 65);
INSERT INTO Vendre VALUES (2, 13, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/2.jpg', 8.00, 'Kettle Sour', 3.0, 3, 2018, 'Une description pas tres descriptive', '2018-04-06', 37);
INSERT INTO Vendre VALUES (2, 14, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/4.jpg', 8.00, 'Vox Pop IPA', 6.5, 45, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (2, 15, 5);


INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/4.jpg', 5.00, 'La Saison du Tracteur', 6.0, 35, 2018, 'Une description pas tres descriptive', '2018-04-06', 16);
INSERT INTO Vendre VALUES (5, 16, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/1.jpg', 5.00, 'Les Quatres Surfeurs de L\'Apocalypso', 6.5, 60, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (5, 17, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/2.jpg', 5.00, 'La Buteuse', 10.0, 60, 2018, 'Une description pas tres descriptive', '2018-04-06', 50);
INSERT INTO Vendre VALUES (5, 18, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/3.jpg', 5.00, 'Le Sang d\'Encre', 5.5, 45, 2018, 'Une description pas tres descriptive', '2018-04-06', 66);
INSERT INTO Vendre VALUES (5, 19, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/5.jpg', 5.00, 'La Morsure', 6.5, 77, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (5, 20, 5);


INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/4.jpg', 12.00, 'Super A', 8.0, 60, 2018, 'Une description pas tres descriptive', '2018-04-06', 32);
INSERT INTO Vendre VALUES (4, 21, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/1.jpg', 12.00, 'Saison Espinay', 6.5, 30, 2018, 'Une description pas tres descriptive', '2018-04-06', 16);
INSERT INTO Vendre VALUES (4, 22, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/3.jpg', 12.00, 'Arrière-Pays Grisette', 4.5, 0, 2018, 'Une description pas tres descriptive', '2018-04-06', 96);
INSERT INTO Vendre VALUES (4, 23, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/2.jpg', 12.00, 'Arcane 17 IPA', 5.2, 60, 2018, 'Une description pas tres descriptive', '2018-04-06', 30);
INSERT INTO Vendre VALUES (4, 24, 5);

INSERT INTO Biere (image_url, prix, nom, pourcentage_alcool, ibu, annee_production, description, date_ajout, id_sorte)
VALUES ('./images/5.jpg', 12.00, 'Guerilla SSS', 7.8, 40, 2016, 'Une description pas tres descriptive', '2018-04-06', 62);
INSERT INTO Vendre VALUES (4, 25, 5);
