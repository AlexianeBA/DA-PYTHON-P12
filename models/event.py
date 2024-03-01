from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from models.base import Base



class Events(Base):
    """
    Représente un événement dans la base de données.

    Attributes:
        id (int): Identifiant unique de l'événement.
        contract_id (int): Identifiant du contrat associé à l'événement.
        client_name (str): Nom du client associé à l'événement.
        collaborateur_id (int): Identifiant du collaborateur associé à l'événement.
        date_debut (Date): Date de début de l'événement.
        date_fin (Date): Date de fin de l'événement.
        contact_support (str): Contact de support pour l'événement.
        lieu (str): Lieu de l'événement.
        participants (int): Nombre de participants à l'événement.
        notes (str): Notes de l'événement.
        contract (relationship): Relation avec la table Contract.
        client (relationship): Relation avec la table Client.
        collaborateur (relationship): Relation avec la table Collaborateur.
    """
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("contract.id"), nullable=False)
    client_name = Column(Integer, ForeignKey("client.nom_complet"), nullable=False)
    collaborateur_id = Column(Integer, ForeignKey("collaborateurs.id"))
    date_debut = Column(Date)
    date_fin = Column(Date)
    contact_support = Column(String(256))
    lieu = Column(String(1024))
    participants = Column(Integer)
    notes = Column(String(2048))

    contract = relationship("Contract", back_populates="events")
    client = relationship("Client", back_populates="events")
    collaborateur = relationship("Collaborateur", back_populates="events")
