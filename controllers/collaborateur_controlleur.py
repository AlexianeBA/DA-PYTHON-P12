from models.models import Collaborateur
from db_config import Session
from db_config import get_session


def create_collaborateur(nom_utilisateur, mot_de_passe, role):
    session = Session()
    collaborateur = Collaborateur(
        nom_utilisateur=nom_utilisateur,
        mot_de_passe=mot_de_passe,
        role=role,
    )
    session.add(collaborateur)
    session.commit()
    session.close()
    return collaborateur


def authenticate_collaborateur(nom_utilisateur, mot_de_passe):
    session = get_session()
    user = (
        session.query(Collaborateur)
        .filter_by(nom_utilisateur=nom_utilisateur, mot_de_passe=mot_de_passe)
        .first()
    )
    session.close()

    return user


def get_collaborateur_by_id(collaborateur_id):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    session.close()
    return collaborateur


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
