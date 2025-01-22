DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS statut;
DROP TABLE IF EXISTS cheval;
DROP TABLE IF EXISTS cheval_pre;
DROP TABLE IF EXISTS pre;
DROP TABLE IF EXISTS membre;
DROP TABLE IF EXISTS role;


CREATE TABLE genre (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT UNIQUE NOT NULL
);


CREATE TABLE statut (
    statut_id INTEGER PRIMARY KEY AUTOINCREMENT,
    etat TEXT UNIQUE NOT NULL
);


CREATE TABLE cheval (
    cheval_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    genre_id INTEGER NOT NULL,
    statut_id INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (statut_id) REFERENCES statut(statut_id)
);



CREATE TABLE pre (
    pre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    capacite INTEGER NOT NULL CHECK (capacite > 0 )
);

CREATE TABLE cheval_pre (
    cheval_id INTEGER NOT NULL,
    pre_id INTEGER NOT NULL,
    PRIMARY KEY (cheval_id, pre_id),
    FOREIGN KEY (cheval_id) REFERENCES cheval(cheval_id),
    FOREIGN KEY (pre_id) REFERENCES pre(pre_id)
);

CREATE TABLE role (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_role TEXT UNIQUE NOT NULL
);

CREATE TABLE membre (
    membre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identifiant TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(role_id)
);

INSERT INTO role (nom_role) VALUES ('Adhérent'), ('Propriétaire'), ('Gestionnaire');









