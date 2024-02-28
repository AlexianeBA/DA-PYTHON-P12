import pytest
from unittest.mock import MagicMock
from controllers.collaborateur_controlleur import create_collaborateur, Collaborateur, authenticate_collaborateur

@pytest.fixture
def mock_session():
    return MagicMock()

def test_create_collaborateur(mock_session):
    nom_utilisateur = "damien"
    mot_de_passe = "password123"
    role = "commercial"
  
    created_collaborateur = create_collaborateur(
        nom_utilisateur, mot_de_passe, role, mock_session) 
    
    
    assert isinstance(created_collaborateur, Collaborateur)
    assert created_collaborateur.nom_utilisateur == nom_utilisateur
    assert created_collaborateur.role == role


def test_authenticate_collaborateur(mock_session):
    mock_collaborateur = Collaborateur(nom_utilisateur="damien", mot_de_passe="f1eceb1794a04e5ca2f512037b97c960763fba3d3052c974e6c5e5414add05f8", salt="f1eceb1794a04e5ca2f512037b97c960763fba3d3052c974e6c5e5414add05f8")
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_collaborateur
    collaborateur_id = authenticate_collaborateur("damien", "f1eceb1794a04e5ca2f512037b97c960763fba3d3052c974e6c5e5414add05f8", mock_session)
    assert collaborateur_id == mock_collaborateur.id

def test_authenticate_collaborateur_not_found(mock_session):
    mock_session.query.return_value.filter_by.return_value.first.return_value = None
    collaborateur_id = authenticate_collaborateur("olivier", "473d0984075c832eda9c18f27c6fe54f012b2ec7a3236183b3b9d40a4867df6c", mock_session)
    assert collaborateur_id is None

def test_authenticate_collaborateur_invalid_password(mock_session):
    
    mock_collaborateur = Collaborateur(nom_utilisateur="john", mot_de_passe="hashed_password", salt="salt")
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_collaborateur
    collaborateur_id = authenticate_collaborateur("john", "wrong_password", mock_session)
    assert collaborateur_id is None