-- SQLBook: Code
-- Active: 1708009053742@@127.0.0.1@3306

CREATE TABLE client (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, nom_complet VARCHAR(256) NOT NULL, email VARCHAR(256) NOT NULL, telephone VARCHAR(16), nom_entreprise VARCHAR(256), date_de_creation DATE, dernière_maj_contact DATE NOT NULL, contact_commercial_chez_epic_events VARCHAR(256) NOT NULL
);
DELETE FROM client WHERE nom_complet="Alexiane Barbe";
SHOW COLUMNS FROM client;
INSERT INTO `client` (`nom_complet`,`email`, `telephone`, `nom_entreprise`, `date_de_creation`,`dernière_maj_contact`,`contact_commercial_chez_epic_events`)
VALUES ('Kevin Casez', 'kevin@startup.io', '+678 123 456 78', 'Cool Startup LLC', '2021-04-18', '2023-03-29', 'Bill Boquet')

CREATE TABLE contract (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, client_id INTEGER NOT NULL, FOREIGN KEY (client_id) REFERENCES client (id), contact_commercial VARCHAR(256) NOT NULL, montant_total INTEGER, montant_restant_a_payer INTEGER, statut_contrat BOOLEAN NOT NULL
);

SHOW COLUMNS FROM contract;
INSERT INTO `contract` (`client_id`,`contact_commercial`,`montant_total`,`montant_restant_a_payer`,`statut_contrat`)
VALUES(1, 'Bill Boquet', 1230, 1230, FALSE)

SELECT * FROM contract;

CREATE INDEX idx_client_name ON client (nom_complet);
CREATE TABLE events(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    contract_id INTEGER NOT NULL, 
    FOREIGN KEY (contract_id) REFERENCES contract (id), 
    client_name VARCHAR(256) NOT NULL, 
    FOREIGN KEY (client_name) REFERENCES client (nom_complet), 
    date_debut DATE NOT NULL, 
    date_fin DATE NOT NULL, 
    contact_support VARCHAR(256), 
    lieu VARCHAR(1024), 
    participants INTEGER, 
    notes VARCHAR(2048) 
);

SHOW COLUMNS FROM events;

INSERT INTO events (`contract_id`, `client_name`, `date_debut`, `date_fin`, `contact_support`, `lieu`, `participants`, `notes`)
VALUES (1, 'Kevin Casez', '2023-06-04', '2026-06-05', 'Kate Hastroff', '53 Rue du Château, 41120 Candé-sur-Beuvron, France', '75', 'Weeding starts at 3PM, by the river. Catering is organized, reception starts at 5PM. Kate needs to organize the DJ for after party.');
SELECT * FROM events;
SHOW COLUMNS FROM client;
SELECT * FROM client;




CREATE TABLE collaborateurs(id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, nom_utilisateur VARCHAR(256) NOT NULL UNIQUE, mot_de_passe VARCHAR(32) NOT NULL, role VARCHAR(50) NOT NULL CHECK (role IN ('commercial', 'support', 'gestion')));

SHOW COLUMNS FROM collaborateurs;

INSERT INTO `collaborateurs` (`nom_utilisateur`, `mot_de_passe`, `role`)
VALUES('Bill Boquet', 'Billboquet123.', 'commercial');
SELECT * FROM collaborateurs;