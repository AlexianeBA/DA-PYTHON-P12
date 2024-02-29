import pytest
from unittest.mock import MagicMock
from controllers.contract_controller import create_contract, Contract

@pytest.fixture
def mock_session():
    return MagicMock()

def test_create_contract(mock_session):
    # Test parameters
    client_id = 10
    client = MagicMock()
    contact_commercial = "Test"
    collaborateur_id = 20
    montant_total = 1000.0
    montant_restant_a_payer = 500.0
    statut_contrat = "en cours"

    # Create a mock contract object
    mock_contract = Contract(
        client_id=client_id,
        client=client,
        contact_commercial=contact_commercial,
        collaborateur_id=collaborateur_id,
        montant_total=montant_total,
        montant_restant_a_payer=montant_restant_a_payer,
        statut_contrat=statut_contrat,
    )

    # Mock the add method to return the mock contract
    mock_session.add.return_value = mock_contract

    # Call the function under test
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

    # Assert that add method is called with the mock contract
    mock_session.add.assert_called_once_with(mock_contract)

    # Assert that commit method is called once (if necessary for your test)
    mock_session.commit.assert_called_once()

    # Assert specific attributes of the created contract
    assert created_contract.client_id == client_id
    assert created_contract.client == client
    assert created_contract.contact_commercial == contact_commercial
    assert created_contract.collaborateur_id == collaborateur_id
    assert created_contract.montant_total == montant_total
    assert created_contract.montant_restant_a_payer == montant_restant_a_payer
    assert created_contract.statut_contrat == statut_contrat
