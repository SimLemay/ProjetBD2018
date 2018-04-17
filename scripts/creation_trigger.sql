USE ProjetBD;

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
