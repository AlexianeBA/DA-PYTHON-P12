from models.models import Client
from db_config import Session


def create_client(
    nom_complet,
    email,
    telephone,
    nom_entreprise,
    date_de_creation,
    dernière_maj_contact,
    contact_commercial_chez_epic_events,
):
    session = Session()
    client = Client(
        nom_complet=nom_complet,
        email=email,
        telephone=telephone,
        nom_entreprise=nom_entreprise,
        date_de_creation=date_de_creation,
        dernière_maj_contact=dernière_maj_contact,
        contact_commercial_chez_epic_events=contact_commercial_chez_epic_events,
    )
    session.add(client)
    session.commit()
    session.close()
    return client


def get_client_by_id(client_id):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    session.close()
    return client


def update_client(client_id, new_values):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        for attr, value in new_values.items():
            setattr(client, attr, value)
        session.commit()
    session.close()


def delete_client(client_id):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        session.delete(client)
        session.commit()
    session.close()
