import pytest
from datetime import date
from unittest.mock import MagicMock
from controllers.client_controller import create_client, Client, Collaborateur

@pytest.fixture
def mock_session():
    return MagicMock()

def test_create_client_with_valid_collaborator_role(mock_session):
    collaborateur_id = 1
    nom_complet = "John Doe"
    email = "john.doe@example.com"
    telephone = "1234567890"
    nom_entreprise = "ABC Company"
    date_de_creation = date.today()
    derniere_maj_contact = date.today()
    contact_commercial_chez_epic_events = "Test"
    
    
    commercial_collaborateur = Collaborateur(id=collaborateur_id, role='commercial')
    mock_session.query.return_value.filter_by.return_value.first.return_value = commercial_collaborateur
    

    created_client = create_client(
        nom_complet, email, telephone, nom_entreprise, date_de_creation,
        derniere_maj_contact, contact_commercial_chez_epic_events, collaborateur_id, session=mock_session)
    

    mock_session.query.assert_called_once_with(Collaborateur)
    mock_session.query.return_value.filter_by.assert_called_once_with(id=collaborateur_id)
    mock_session.add.assert_called_once_with(created_client)
    mock_session.commit.assert_called_once()
    mock_session.close.assert_called_once()
    

    assert isinstance(created_client, Client)


def test_create_client_with_invalid_collaborator_role(mock_session):
    
    collaborateur_id = 2
    non_commercial_collaborateur = Collaborateur(id=collaborateur_id, role='gestion')
    mock_session.query.return_value.filter_by.return_value.first.return_value = non_commercial_collaborateur
    
    
    nom_complet = "John Doe"
    email = "john.doe@example.com"
    telephone = "1234567890"
    nom_entreprise = "ABC Company"
    date_de_creation = date.today()
    derniere_maj_contact = date.today()
    contact_commercial_chez_epic_events = "Joe"
    

    with pytest.raises(ValueError, match="Seuls les collaborateurs avec le rôle 'commercial'"):
        create_client(
            nom_complet, email, telephone, nom_entreprise, date_de_creation,
            derniere_maj_contact, contact_commercial_chez_epic_events, collaborateur_id, session=mock_session
        )
    

    mock_session.query.assert_called_once_with(Collaborateur)
    mock_session.query.return_value.filter_by.assert_called_once_with(id=collaborateur_id)
    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()
    mock_session.close.assert_not_called()