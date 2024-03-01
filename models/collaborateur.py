from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from models.base import Base
from models.client import Client 





class Collaborateur(Base):
    """
    Représente un collaborateur dans la base de données.

    Attributes:
        id (int): Identifiant unique du collaborateur.
        nom_utilisateur (str): Nom d'utilisateur du collaborateur.
        mot_de_passe (str): Mot de passe du collaborateur.
        salt (str): Sel utilisé pour hasher le mot de passe.
        role (str): Rôle du collaborateur.
        is_connected (bool): Indique si le collaborateur est connecté ou non.
        contracts (relationship): Relation avec la table Contract.
        events (relationship): Relation avec la table Events.
        client (relationship): Relation avec la table Client.
    """
    __tablename__ = "collaborateurs"

    id = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(256), unique=True, nullable=False)
    mot_de_passe = Column(String(64), nullable=False)
    salt = Column(String(16), nullable=False)
    role = Column(String(50), nullable=False)
    is_connected = Column(Boolean, default=False)

    contracts = relationship("Contract", back_populates="collaborateur")
    events = relationship("Events", back_populates="collaborateur")
    client = relationship("Client", back_populates="collaborateur")




