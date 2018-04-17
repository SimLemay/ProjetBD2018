USE ProjetBD;

CREATE INDEX indexUtilisateur ON Utilisateur(id) USING HASH;

CREATE INDEX indexMotdepasse ON Mot_de_passe(id, mot_de_passe) USING HASH;

CREATE INDEX indexMicrobrasserie ON Microbrasserie(id) USING HASH;

CREATE INDEX indexAcheteur ON Acheteur(id) USING HASH;

CREATE INDEX indexAchete ON Achete(id_biere, date_achat, quantite) USING BTREE;

CREATE INDEX indexVendre ON Vendre(id_microbrasserie, id_biere, quantite) USING BTREE;

CREATE INDEX indexBiere ON Biere(id_sorte, prix, ibu) USING BTREE;

CREATE INDEX indexSorte ON Sorte(id, nom) USING HASH;

CREATE INDEX indexTypede ON Type_de(id_sorte_parent) USING BTREE;

delimiter //
CREATE TRIGGER update_quantite BEFORE INSERT ON Achete
  FOR EACH ROW
  BEGIN
    DECLARE stock INT;
    SET stock := (SELECT MIN(Vendre.quantite) FROM Vendre WHERE Vendre.id_biere = NEW.id_biere);
    IF stock - NEW.quantite < 0
    THEN SET NEW.id_acheteur = NULL;
    ELSE
      UPDATE Vendre V SET V.quantite = V.quantite - NEW.quantite WHERE V.id_biere = NEW.id_biere;
    END IF;
  END;//
delimiter ;
