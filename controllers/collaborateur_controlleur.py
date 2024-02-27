from models.models import Collaborateur
from db_config import Session
from db_config import get_session
import hashlib
import secrets
import atexit
# TODO: créer permissions collaborateurs par rapport à leurs départements



# Fonction pour hacher le mot de passe
def hash_password(password):
    salt = secrets.token_hex(8)
    hashed_password = hashlib.sha3_256((password + salt).encode()).hexdigest()
    return hashed_password, salt

# Fonction pour créer un collaborateur
def create_collaborateur(nom_utilisateur, mot_de_passe, role):
    session = Session()
    hashed_password, salt = hash_password(mot_de_passe)
    collaborateur = Collaborateur(
        nom_utilisateur=nom_utilisateur,
        mot_de_passe=hashed_password,
        salt=salt,
        role=role,
    )
    session.add(collaborateur)
    session.commit()
    session.close()
    return collaborateur

def authenticate_collaborateur(nom_utilisateur, mot_de_passe):
    session = get_session()
    collaborateur = session.query(Collaborateur).filter_by(nom_utilisateur=nom_utilisateur).first()
    collaborateur_id = None
    if collaborateur:
        hashed_password_input = hashlib.sha3_256((mot_de_passe + collaborateur.salt).encode()).hexdigest()
        if hashed_password_input == collaborateur.mot_de_passe:
            collaborateur.is_connected = True
            session.commit()
            collaborateur_id = collaborateur.id
            print(collaborateur.role)
            print(collaborateur.id)
    else:
        print("User not found!")

    session.close()
    return collaborateur_id


def get_collaborateur_by_id(collaborateur_id):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    session.close()
    return collaborateur


def get_collaborateur_id_connected():
    session = get_session()
    collaborateur = session.query(Collaborateur).filter_by(is_connected=True).first()
    session.close()
    if collaborateur:
        print(collaborateur.role)
        print(collaborateur.id)
        return collaborateur.id, collaborateur.role
    else:
        print("aucun collaborateur connecté")
    return None, None


def update_collaborateur(collaborateur_id, new_values):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    if collaborateur:
        for attr in new_values:
            setattr(collaborateur, attr, new_values[attr])
        session.commit()
    session.close()


def delete_collaborateur(collaborateur_id):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    if collaborateur:
        session.delete(collaborateur)
        session.commit()
    session.close()





def get_all_collaborateurs(nom_utilisateur=None):
    session = Session()
    query = session.query(Collaborateur)
    if nom_utilisateur:
        query = query.filter(Collaborateur.nom_utilisateur == nom_utilisateur)
    query = query.order_by(Collaborateur.nom_utilisateur)
    collaborateurs = query.all()
    return collaborateurs


def get_collaborateurs_filtered(nom_utilisateur=None):
    session = Session()
    query = session.query(Collaborateur)

    if nom_utilisateur:
        query=query.filter(Collaborateur.nom_utilisateur== nom_utilisateur)
    query=query.order_by(Collaborateur.nom_utilisateur)
    collaborateur = query.all()
    return collaborateur


import atexit


def disconnection_collaborateur():
    session = get_session()
    collaborateur = session.query(Collaborateur).filter_by(is_connected=True).first()
    if collaborateur:
        collaborateur.is_connected = False  
        session.commit() 
        session.close()
        
atexit.register(disconnection_collaborateur)
