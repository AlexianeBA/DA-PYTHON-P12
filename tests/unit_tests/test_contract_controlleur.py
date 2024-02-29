import pytest
from unittest.mock import MagicMock
from controllers.contract_controller import create_contract, Contract

@pytest.fixture
def mock_session():
    return MagicMock()

def test_create_contract(mock_session):
    # Paramètres de test
    client_id = 1
    client = MagicMock()
    contact_commercial = "John Doe"
    collaborateur_id = 2
    montant_total = 1000.0
    montant_restant_a_payer = 500.0
    statut_contrat = "En cours"

    # Créer un mock de contrat
    mock_contract = Contract(
        client_id=client_id,
        client=client,
        contact_commercial=contact_commercial,
        collaborateur_id=collaborateur_id,
        montant_total=montant_total,
        montant_restant_a_payer=montant_restant_a_payer,
        statut_contrat=statut_contrat,
    )

    # Configurer le comportement du mock de session pour retourner le mock de contrat
    mock_session.add.return_value = mock_contract

    # Appeler la fonction pour créer le contrat
    created_contract = create_contract(
        client_id,
        client,
        contact_commercial,
        collaborateur_id,
        montant_total,
        montant_restant_a_payer,
        statut_contrat,
        session=mock_session
    )

    # Assurez-vous que les objets Contract sont liés à la session
    mock_session.add.assert_called_once_with(mock_contract)
    mock_session.commit.assert_called_once()
    # Accéder aux attributs de created_contract après l'appel de la fonction pour éviter les DetachedInstanceError
    assert created_contract.client_id == client_id
    assert created_contract.client == client
    assert created_contract.contact_commercial == contact_commercial
    assert created_contract.collaborateur_id == collaborateur_id
    assert created_contract.montant_total == montant_total
    assert created_contract.montant_restant_a_payer == montant_restant_a_payer
    assert created_contract.statut_contrat == statut_contrat
