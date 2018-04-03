INSERT INTO Microbrasserie(id_utilisateur, nom) VALUES(1, 'Boreale');
INSERT INTO Ingredient(id, nom) VALUES(1, 'Houblon');
INSERT INTO Liste_ingredients(id, id_ingredient) VALUES(1, 1);
INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients) VALUES(1, 'IPA du Nord-Est', 1, 1);
INSERT INTO Biere(id, nom, id_microbrasserie, id_liste_ingredients) VALUES(2, 'Boreale IPA', 1, 1);

insert into Utilisateur(id, courriel, nom, prenom) values(1, 'simon@test.ca', 'Lemay-Lauziere', 'Simon');
insert into Utilisateur(id, courriel, nom, prenom) values(2, 'keven@ulaval.ca', 'Lamontagne', 'Keven');
-- Simon : test
insert into Mot_de_passe(id_utilisateur, mot_de_passe) values(1, X'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff');
-- Keven : ulaval
insert into Mot_de_passe(id_utilisateur, mot_de_passe) values(2, X'5c75dc48fdb6b2b3a8349899fd7963b9c043e7dffe720368ff2ef16dbd45afcb50869585671fa9d270ea411ee83b86dd8701f7a9eb986095e5f9a4305c8e2015');
