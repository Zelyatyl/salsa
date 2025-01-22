
INSERT INTO genre (genre) VALUES ('Hongre'), ('Jument');
INSERT INTO statut (etat) VALUES ('Actif'), ('En retraite');


INSERT INTO cheval (nom, genre_id, statut_id) VALUES
('Écuyer d''Or', 1, 1),
('Tempête du Vent', 1, 1),
('Loup des Champs', 1, 1),
('Ciel d''Argent', 1, 2),
('Prince du Soleil', 1, 1),
('Mystère Noir', 1, 1),
('Roi de l''Étoile', 1, 1),
('Élan de Feu', 1, 1),
('Baron des Bois', 1, 2),
('Titan des Prairies', 1, 1),
('Perle du Lac', 2, 1),
('Reine de l''Aube', 2, 1),
('Étoile Filante', 2, 1),
('Fleur de Lune', 2, 1),
('Belle de Nuit', 2, 1),
('Lumière d''Or', 2, 1),
('Vénus des Cieux', 2, 1),
('Douce Mélodie', 2, 1);

INSERT INTO pre (nom, capacite) VALUES
('Pré des Étoiles', 5),
('Prairie du Soleil', 10),
('Clairière des Bois', 7);

INSERT OR IGNORE INTO role (role_id, nom_role) VALUES
(1, 'Adhérent'),
(2, 'Propriétaire'),
(3, 'Gestionnaire');

INSERT INTO membre (identifiant, mot_de_passe, role_id) VALUES
('adherent1', 'password', 1),
('adherent2', 'password2', 1),
('proprietaire1', 'password3', 2),
('proprietaire2', 'password4', 2),
('gestionnaire1', 'password5', 3),
('gestionnaire2', 'password6', 3);
