# DA-Python-P12

Développez une architecture back-end sécurisée avec Python et SQL



## Epic Events :

Epic Events est mon douxième projet en Python dans le cadre de ma formation de Développeur d'Application Python via la plateforme de formation OpenClassrooms.
EpicEvents CRM Software est un logiciel à exécuter localement. Il s'agit d'un outil permettant de collecter et de traiter les données des clients et de leurs événements, tout en facilitant la communication entre les différents pôles de l'entreprise EpicEvents. Cette application est implémentée sous la forme d'un CLI (Command-Line Interface). Elle permet la lecture, la création, la mise à jour et la supression de collaborateurs, clients, contrats et évènements.

## Pré-requis :

Ce logiciel a été développé en utilisant MySQL et en Python, leur installation est donc obligatoire.

## Pré-requis :

L'application peut être installée en suivant ces étapes :
1. Cloner le repository : ``` git clone https://github.com/AlexianeBA/DA-Python-P12 ```
2. Créer votre environnement virtuel à l'aide de : ``` python3 -m venv venv ``` puis entrer dans ce dernier : ``` source venv/bin/activate ```
3. Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```
4. Créer une variable d'environnement afin de stocker les informations confidentielles telles que le mot de passe de la base de données par exemple : 
    ```import os
    # Définir une variable d'environnement
    os.environ["NOM_VARIABLE"] = "valeur"
    # Accéder à la variable d'environnement
    print(os.environ["NOM_VARIABLE"])```

## Démarrage

Lancer le script dans votre terminal : ``` python3 main.py ```