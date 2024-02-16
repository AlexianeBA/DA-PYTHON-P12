-- Active: 1708009053742@@127.0.0.1@3306

CREATE TABLE client (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, nom_complet VARCHAR(256) NOT NULL, email VARCHAR(256) NOT NULL, telephone VARCHAR(16), nom_entreprise VARCHAR(256), date_de_creation DATE, dernière_maj_contact DATE NOT NULL, contact_commercial_chez_epic_events VARCHAR(256) NOT NULL
);

SHOW COLUMNS FROM client;

CREATE TABLE contract (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, client_id INTEGER NOT NULL, FOREIGN KEY (client_id) REFERENCES client (id), contact_commercial VARCHAR(256) NOT NULL, montant_total INTEGER, montant_restant_a_payer INTEGER, statut_contrat BOOLEAN NOT NULL
);

SHOW COLUMNS FROM contract;


CREATE TABLE events(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, contract_id INTEGER NOT NULL, FOREIGN KEY (contract_id) REFERENCES contract (id), client_name VARCHAR(256) NOT NULL, FOREIGN KEY (client_name) REFERENCES client (nom_complet), date_debut DATE NOT NULL, date_fin DATE NOT NULL, contact_support VARCHAR(256), lieu VARCHAR(1024), participants INTEGER, notes VARCHAR(2048) 
);

INSERT INTO `client` (`nom_complet`,`email`, `telephone`, `nom_entreprise`, `date_de_creation`,`derniere_maj_contact`,`contact_commercial_chez_epic_events`)
VALUES ('Kevin Casez', 'kevin@startup.io', '+678 123 456 78', 'Cool Startup LLC', '18-04-2021', '29-03-2023', 'Bill Boquet')


INSERT INTO `events` (``,``,``,``,``,``)

CREATE USER 'Bill Boquet'@'localhost' IDENTIFIED BY 'billboquet123';
