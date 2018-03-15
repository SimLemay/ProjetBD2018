CREATE TABLE Sorte (
    id INTEGER PRIMARY KEY,
    aromes VARCHAR(500),
    nom VARCHAR(100)
);

CREATE TABLE Ingredient (
    id INTEGER PRIMARY KEY,
    nom VARCHAR(100),
    categorie VARCHAR(100)
);

CREATE TABLE Utilisateur (
    id INTEGER PRIMARY KEY,
    role VARCHAR(50),
    ville VARCHAR(100),
    nom VARCHAR(100),
    age INTEGER,
    adresse VARCHAR(200),
    telephone CHAR(11),
    mot_de_passe BINARY(64),
    nom_utilisateur VARCHAR(100)
);

CREATE TABLE Acheteur (
    id_utilisateur INTEGER NOT NULL REFERENCES Utilisateur (id),
    PRIMARY KEY (id_utilisateur)
);

CREATE TABLE Microbrasserie (
    id_utilisateur INTEGER NOT NULL REFERENCES Utilisateur (id),
    nom VARCHAR(100),
    emplacement VARCHAR(200),
    annee_inauguration INTEGER,
    cote INTEGER,
    PRIMARY KEY (id_utilisateur)
);

CREATE TABLE Liste_ingredients (
    id INTEGER PRIMARY KEY,
    id_ingredient INTEGER NOT NULL,
    FOREIGN KEY (id)
        REFERENCES Ingredient (id)
);

CREATE TABLE Biere (
    id INTEGER PRIMARY KEY,
    image_url VARCHAR(500),
    prix FLOAT(2),
    nom VARCHAR(100),
    pourcentage_alcool FLOAT(1),
    ibu FLOAT(1),
    annee_production INTEGER,
    mention VARCHAR(200),
    id_microbrasserie INTEGER NOT NULL,
    date_ajout DATE,
    id_liste_ingredients INTEGER NOT NULL,
    FOREIGN KEY (id_microbrasserie)
        REFERENCES Microbrasserie (id_utilisateur),
    FOREIGN KEY (id_liste_ingredients)
        REFERENCES Liste_ingredients (id)
);

CREATE TABLE Achete (
    id_acheteur INTEGER NOT NULL REFERENCES Acheteur (id_utilisateur),
    id_biere INTEGER NOT NULL REFERENCES Biere (id),
    quantite INTEGER NOT NULL,
    date_achat TIMESTAMP,
    PRIMARY KEY (id_acheteur , id_biere)
);

CREATE TABLE Type_de (
    id_sorte_parent INTEGER NOT NULL,
    id_sorte_enfant INTEGER NOT NULL PRIMARY KEY REFERENCES Sorte (id),
    FOREIGN KEY (id_sorte_parent)
        REFERENCES Sorte (id)
);

CREATE TABLE Contient (
    id_biere INTEGER,
    id_ingredient INTEGER,
    FOREIGN KEY (id_biere)
        REFERENCES Biere (id),
    FOREIGN KEY (id_ingredient)
        REFERENCES Ingredient (id)
);