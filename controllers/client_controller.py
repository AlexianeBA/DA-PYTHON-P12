from models.models import Client
from db_config import Session

# TODO: filtrer l'affichage
#


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


def get_client_by_id(client_id: int) -> Client:
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    session.close()
    return client


def update_client(client_id: int, new_values: dict) -> None:
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        for attr in new_values:
            setattr(client, attr, new_values[attr])
        session.commit()
    session.close()


def delete_client(client_id: int) -> None:
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        session.delete(client)
        session.commit()
    session.close()


def get_clients_filtered(nom_complet=None):
    session = Session()
    query = session.query(Client)

    if nom_complet:
        query = query.filter(Client.nom_complet == nom_complet)

    client = query.all()
    return client


def get_all_clients():
    session = Session()
    clients = session.query(Client).all()
    return clients
