from database.db_config import Session
from models.collaborateur import Collaborateur
from models.client import Client

def create_client(
    nom_complet,
    email,
    telephone,
    nom_entreprise,
    date_de_creation,
    derniere_maj_contact,
    collaborateur_id,
):
    print("Creating client...")
    try:
        session = Session()
        collaborateur = session.query(Collaborateur).filter_by(id=collaborateur_id).first()
        if collaborateur:
            if collaborateur.role == 'commercial':
                client = Client(
                    nom_complet=nom_complet,
                    email=email,
                    telephone=telephone,
                    nom_entreprise=nom_entreprise,
                    date_de_creation=date_de_creation,
                    derniere_maj_contact=derniere_maj_contact,
                    collaborateur_id=collaborateur_id
                )
                session.add(client)
                session.commit()
                session.close()
                print("Client created successfully!")
                return client
            else:
                raise ValueError("Seuls les collaborateurs avec le rôle 'commercial' sont autorisés à créer un client.")
        else:
            raise ValueError("Collaborateur not found.")
    except Exception as e:
        session.rollback()
        print("Error creating client:", e)
        raise

def get_client_by_id(client_id: int) -> Client:
    """
    Récupère un client à partir de son identifiant.

    Args:
        client_id (int): L'identifiant du client à récupérer.

    Returns:
        Client: Le client correspondant à l'identifiant donné.
    """
    session=Session()
    client = session.query(Client).filter_by(id=client_id).first()
    session.close()
    return client


def update_client(client_id: int, new_values: dict) -> None:

    """
    Met à jour les informations d'un client donné avec de nouvelles valeurs.

    Args:
        client_id (int): L'identifiant du client à mettre à jour.
        new_values (dict): Un dictionnaire contenant les nouvelles valeurs à attribuer
                           aux attributs du client.

    Returns:
        None
    """
    session=Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        for attr in new_values:
            setattr(client, attr, new_values[attr])
        session.commit()
    session.close()


def delete_client(client_id: int) -> None:
    """
    Supprime un client de la base de données.

    Args:
        client_id (int): L'identifiant du client à supprimer.

    Returns:
        None
    """
    session=Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        session.delete(client)
        session.commit()
    session.close()


def get_clients_filtered(nom_complet=None):
    """
    Récupère une liste de clients filtrés par nom complet.

    Args:
        nom_complet (str, optional): Le nom complet du client à filtrer. Si spécifié,
                                      seuls les clients dont le nom complet correspond
                                      à cette valeur seront retournés. Par défaut, None.

    Returns:
        list: Une liste de clients filtrés par nom complet.
    """
    session=Session()
    query = session.query(Client)

    if nom_complet:
        query = query.filter(Client.nom_complet == nom_complet)
    query = query.order_by(Client.nom_complet)
    client = query.all()
    return client

def get_clients_filter_by_collaborateur(collaborateur_id):
    """
    Récupère tous les clients associés à un collaborateur donné.

    Args:
        collaborateur_id (int): L'identifiant du collaborateur.

    Returns:
        list: Une liste des clients associés au collaborateur.
    """
    session=Session()
    client = session.query(Client).filter_by(collaborateur_id=collaborateur_id).all()
    return client

def get_clients():
    """
    Récupère la liste complète des clients depuis la base de données.

    Returns:
        list: Liste des clients.
    """
    session = Session()
    clients = session.query(Client).all()
    session.close()
    return clients