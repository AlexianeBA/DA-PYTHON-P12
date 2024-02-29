from models.models import Contract
from database.db_config import Session
from controllers.client_controller import get_client_by_id



def create_contract(
    client_id,
    client,
    contact_commercial,
    collaborateur_id,
    montant_total,
    montant_restant_a_payer,
    statut_contrat,
):
    """
    Crée un nouveau contrat dans la base de données.

    Args:
        client_id (int): L'identifiant du client associé au contrat.
        client (Client): Le client associé au contrat.
        contact_commercial (str): Le contact commercial pour le contrat.
        collaborateur_id (int): L'identifiant du collaborateur associé au contrat.
        montant_total (float): Le montant total du contrat.
        montant_restant_a_payer (float): Le montant restant à payer pour le contrat.
        statut_contrat (str): Le statut du contrat.

    Returns:
        Contract: Le contrat créé.
    """
    client = get_client_by_id(client_id)
    session = Session()
    contract = Contract(
        client_id=client_id,
        client=client,
        contact_commercial=contact_commercial,
        collaborateur_id=collaborateur_id,
        montant_total=montant_total,
        montant_restant_a_payer=montant_restant_a_payer,
        statut_contrat=statut_contrat,
    )
    session.add(contract)
    session.commit()
    session.close()
    return contract


def get_contract_by_id(contract_id):
    """
    Récupère un contrat à partir de son identifiant.

    Args:
        contract_id (int): L'identifiant du contrat à récupérer.

    Returns:
        Contract: Le contrat correspondant à l'identifiant donné.
    """
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    session.close()
    return contract


def update_contract(contract_id, new_values):
    """
    Met à jour les informations d'un contrat.

    Args:
        contract_id (int): L'identifiant du contrat à mettre à jour.
        new_values (dict): Un dictionnaire contenant les nouvelles valeurs à attribuer
                           aux attributs du contrat.

    Returns:
        None
    """
    session = Session()
    try:
        contract = session.query(Contract).filter_by(id=contract_id).first()
        if contract:
            for attr, value in new_values.items():
                setattr(contract, attr, value)
            session.commit()
            print("Le contrat a été mis à jour avec succès.")
        else:
            print("Contrat introuvable.")
    except Exception as e:
        session.rollback()
        print(f"Erreur lors de la mise à jour du contrat : {str(e)}")
    finally:
        session.close()


def delete_contract(contract_id):
    """
    Supprime un contrat de la base de données.

    Args:
        contract_id (int): L'identifiant du contrat à supprimer.

    Returns:
        None
    """
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    if contract:
        session.delete(contract)
        session.commit()
    session.close()


def get_contracts_filter_by_price():
    """
    Récupère tous les contrats filtrés par prix.

    Returns:
        list: Une liste des contrats triés par montant total décroissant.
    """
    session = Session()
    contracts = session.query(Contract).order_by(Contract.montant_total.desc()).all()
    session.close()
    return contracts


def get_contracts_filter_by_collaborateur(collaborateur_id):
    """
    Récupère tous les contrats associés à un collaborateur donné.

    Args:
        collaborateur_id (int): L'identifiant du collaborateur.

    Returns:
        list: Une liste des contrats associés au collaborateur.
    """
    session = Session()
    contracts = session.query(Contract).filter_by(collaborateur_id=collaborateur_id[0]).all()
    session.close()
    return contracts


def get_all_contracts():
    """
    Récupère tous les contrats de la base de données.

    Returns:
        list: Une liste de tous les contrats.
    """
    session = Session()
    contracts = session.query(Contract).all()
    return contracts
