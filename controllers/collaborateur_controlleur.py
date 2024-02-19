from models import Collaborateur
from db_config import Session


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


def update_collaborateur(collaborateur_id, new_values):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    if collaborateur:
        for attr, value in new_values.items():
            setattr(collaborateur, attr, value)
        session.commit()
    session.close()


def delete_collaborateur(collaborateur_id):
    session = Session()
    collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
    if collaborateur:
        session.delete(collaborateur)
        session.commit()
    session.close()
