from models.models import Contract
from db_config import Session
from controllers.client_controller import get_client_by_id

# TODO: filtrer l'affichage


def create_contract(
    client_id,
    client,
    contact_commercial,
    collaborateur_id,
    montant_total,
    montant_restant_a_payer,
    statut_contrat,
):
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
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    session.close()
    return contract


def update_contract(contract_id, new_values):
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    if contract:
        for attr in new_values:
            setattr(contract, attr, new_values[attr])
        session.commit()
    session.close()


def delete_contract(contract_id):
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    if contract:
        session.delete(contract)
        session.commit()
    session.close()


def get_contracts_filter_by_statut(statut):
    session = Session()
    contracts = session.query(Contract).filter(Contract.statut_contrat == statut)
    session.close()
    return contracts


def get_contracts_filter_by_collaborateur(collaborateur_id):
    session = Session()
    contracts = session.query(Contract).filter_by(collaborateur_id=collaborateur_id).all()
    session.close()
    return contracts


def get_all_contracts():
    session = Session()
    contracts = session.query(Contract).all()
    return contracts
