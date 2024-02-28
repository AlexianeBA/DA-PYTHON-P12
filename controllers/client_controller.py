from database.db_config import Session
from models.models import Collaborateur, Client

session=Session()
def create_client(
    nom_complet,
    email,
    telephone,
    nom_entreprise,
    date_de_creation,
    derniere_maj_contact,
    contact_commercial_chez_epic_events,
    collaborateur_id,
):
    """
    Créer un nouveau client dans la base de données.

    Args:
        nom_complet (str): Le nom complet du client.
        email (str): L'adresse e-mail du client.
        telephone (str): Le numéro de téléphone du client.
        nom_entreprise (str): Le nom de l'entreprise du client.
        date_de_creation (date): La date de création du client.
        derniere_maj_contact (date): La dernière date de mise à jour du contact client.
        contact_commercial_chez_epic_events (str): Le contact commercial chez Epic Events.
        collaborateur_id (int): L'identifiant du collaborateur créant le client.

    Returns:
        Client: Le client créé.
    Raises:
        ValueError: Si le collaborateur n'a pas le rôle 'commercial'.
    """
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
                contact_commercial_chez_epic_events=contact_commercial_chez_epic_events,
                collaborateur_id=collaborateur_id
            )
            session.add(client)
            session.commit()
            session.close()
            return client
    else:
        raise ValueError("Seuls les collaborateurs avec le rôle 'commercial' "
                         "sont autorisés à créer un client.")



def get_client_by_id(client_id: int) -> Client:
    """
    Récupère un client à partir de son identifiant.

    Args:
        client_id (int): L'identifiant du client à récupérer.

    Returns:
        Client: Le client correspondant à l'identifiant donné.
    """
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
    
    client = session.query(Client)\
                    .filter_by(collaborateur_id=collaborateur_id)\
                    .all()
    return client