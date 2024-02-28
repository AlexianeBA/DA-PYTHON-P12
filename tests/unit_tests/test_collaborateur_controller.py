import pytest
from unittest.mock import MagicMock
from controllers.collaborateur_controlleur import create_collaborateur, Collaborateur

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