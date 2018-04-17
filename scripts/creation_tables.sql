CREATE TABLE Sorte (
  id  INTEGER PRIMARY KEY,
  nom VARCHAR(100) NOT NULL
);

CREATE TABLE Utilisateur (
  id        INTEGER AUTO_INCREMENT PRIMARY KEY,
  ville     VARCHAR(100) NOT NULL,
  nom       VARCHAR(100) NOT NULL,
  age       INTEGER      NOT NULL,
  adresse   VARCHAR(200) NOT NULL,
  telephone CHAR(11)     NOT NULL,
  courriel  VARCHAR(100) NOT NULL UNIQUE,
  prenom    VARCHAR(100) NOT NULL
);

CREATE TABLE Mot_de_passe (
  id           INTEGER PRIMARY KEY,
  mot_de_passe BINARY(64) NOT NULL,
  FOREIGN KEY (id)
  REFERENCES Utilisateur (id)
);

CREATE TABLE Acheteur (
  id INTEGER PRIMARY KEY,
  FOREIGN KEY (id)
  REFERENCES Utilisateur (id)
);

CREATE TABLE Microbrasserie (
  id                 INTEGER PRIMARY KEY,
  nom                VARCHAR(100) NOT NULL UNIQUE,
  emplacement        VARCHAR(200) NOT NULL,
  annee_inauguration INTEGER      NOT NULL,
  FOREIGN KEY (id)
  REFERENCES Utilisateur (id)
);

CREATE TABLE Biere (
  id                 INTEGER AUTO_INCREMENT PRIMARY KEY,
  image_url          VARCHAR(500) NOT NULL,
  prix               FLOAT(2)     NOT NULL,
  nom                VARCHAR(100) NOT NULL,
  pourcentage_alcool FLOAT(1)     NOT NULL,
  ibu                INTEGER      NOT NULL,
  annee_production   INTEGER      NOT NULL,
  description        VARCHAR(200) NOT NULL,
  date_ajout         DATE         NOT NULL,
  id_sorte           INTEGER      NOT NULL,
  FOREIGN KEY (id_sorte)
  REFERENCES Sorte (id)
);

CREATE TABLE Vendre (
  id_microbrasserie INTEGER,
  id_biere          INTEGER,
  quantite          INTEGER NOT NULL,
  PRIMARY KEY (id_microbrasserie, id_biere),
  FOREIGN KEY (id_microbrasserie)
  REFERENCES Microbrasserie (id),
  FOREIGN KEY (id_biere)
  REFERENCES Biere (id)
);

CREATE TABLE Achete (
  id_acheteur INTEGER,
  id_biere    INTEGER,
  quantite    INTEGER NOT NULL,
  date_achat  TIMESTAMP,
  PRIMARY KEY (id_acheteur, id_biere, date_achat),
  FOREIGN KEY (id_acheteur)
  REFERENCES Acheteur (id),
  FOREIGN KEY (id_biere)
  REFERENCES Biere (id)
);

CREATE TABLE Type_de (
  id_sorte_parent INTEGER NOT NULL,
  id_sorte_enfant INTEGER PRIMARY KEY,
  FOREIGN KEY (id_sorte_enfant)
  REFERENCES Sorte (id),
  FOREIGN KEY (id_sorte_parent)
  REFERENCES Sorte (id)
);

delimiter //
CREATE TRIGGER update_quantite BEFORE INSERT ON Achete
  FOR EACH ROW
  BEGIN
    DECLARE stock INT;
    SET stock = (SELECT MIN(Vendre.quantite) FROM Vendre WHERE Vendre.id_biere = NEW.id_biere);
    IF stock - NEW.quantite < 0
    THEN SET NEW.id_acheteur = NULL;
    ELSE
      UPDATE Vendre V SET V.quantite = V.quantite - NEW.quantite WHERE V.id_biere = NEW.id_biere;
    END IF;
  END;//
delimiter ;
