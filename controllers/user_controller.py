from db_config import get_session
from models.models import Collaborateur
import hashlib


def authenticate_user(nom_utilisateur, mot_de_passe):

    session = get_session()
    user = (
        session.query(Collaborateur)
        .filter_by(nom_utilisateur=nom_utilisateur, mot_de_passe=mot_de_passe)
        .first()
    )
    session.close()

    return user
