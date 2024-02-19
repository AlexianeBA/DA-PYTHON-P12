from models import Contract
from db_config import Session


def create_contract(
    client_id,
    client,
    contact_commercial,
    montant_total,
    montant_restant_a_payer,
    statut_contrat,
):
    session = Session()
    contract = Contract(
        client_id=client_id,
        client=client,
        contact_commercial=contact_commercial,
        montant_total=montant_total,
        montant_restant_a_payer=montant_restant_a_payer,
        statut_contrat=statut_contrat,
    )
    session.add(contract)
    session.commit()
    session.close()
    return contract


def update_contract(contract_id, new_values):
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    if contract:
        for attr, value in new_values.items():
            setattr(contract, attr, value)
        session.commit()
    session.close()


def delete_contract(contract_id):
    session = Session()
    contract = session.query(Contract).filter_by(id=contract_id).first()
    if contract:
        session.delete(contract)
        session.commit()
    session.close()
