# import datetime
# import pytest
# from unittest.mock import MagicMock
# from controllers.contract_controller import create_contract, Contract
# from models.models import Client  # Importez le modèle Client

# @pytest.fixture
# def mock_session():
#     return MagicMock()

# def test_create_contract(mock_session):
#     # Créez un objet Client réel
#     client = Client(
#         id=10,
#         nom_complet='Fabien',
#         email='fabien@fabien.fr',
#         telephone='12345678',
#         nom_entreprise='FabandCo',
#         date_de_creation=datetime.datetime(2024, 2, 29),
#         derniere_maj_contact=datetime.datetime(2024, 2, 29),
#         contact_commercial_chez_epic_events='Test',
#         collaborateur_id =20
#     )

#     # Test parameters
#     client_id = 10
#     contact_commercial = "Test"
#     collaborateur_id = 20
#     montant_total = 1000.0
#     montant_restant_a_payer = 500.0
#     statut_contrat = "en cours"

#     # Call the function under test with real client object and mock session
#     created_contract = create_contract(
#         client_id,
#         client,  # Utilisez l'objet client réel
#         contact_commercial,
#         collaborateur_id,
#         montant_total,
#         montant_restant_a_payer,
#         statut_contrat,
#         session=mock_session
#     )

#     # Assert that add method is called with the correct client
#     mock_session.add.assert_called_once_with(created_contract.client)

#     # Assert that commit method is called once (if necessary for your test)
#     mock_session.commit.assert_called_once()

#     # Assert specific attributes of the created contract
#     assert created_contract.client_id == client_id
#     assert created_contract.client == client
#     assert created_contract.contact_commercial == contact_commercial
#     assert created_contract.collaborateur_id == collaborateur_id
#     assert created_contract.montant_total == montant_total
#     assert created_contract.montant_restant_a_payer == montant_restant_a_payer
#     assert created_contract.statut_contrat == statut_contrat
