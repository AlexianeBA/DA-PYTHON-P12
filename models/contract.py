from models.base import Base
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship


class Contract(Base):
    """
    Représente un contrat dans la base de données.

    Attributes:
        id (int): Identifiant unique du contrat.
        client_id (int): Identifiant du client associé au contrat.
        contact_commercial (str): Contact commercial pour le contrat.
        collaborateur_id (int): Identifiant du collaborateur associé au contrat.
        montant_total (int): Montant total du contrat.
        montant_restant_a_payer (int): Montant restant à payer pour le contrat.
        statut_contrat (str): Statut du contrat.
        events (relationship): Relation avec la table Events.
        client (relationship): Relation avec la table Client.
        collaborateur (relationship): Relation avec la table Collaborateur.
    """
    __tablename__ = "contract"

    #ajouter foreignfey pour contact_commercial
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    contact_commercial = Column(String(256),  nullable=False)
    collaborateur_id = Column(Integer, ForeignKey("collaborateurs.id"))
    montant_total = Column(Integer)
    montant_restant_a_payer = Column(Integer)
    statut_contrat = Column(String(50), nullable=False)

    events = relationship("Events", back_populates="contract")
    client = relationship("Client", back_populates="contracts")
    collaborateur = relationship("Collaborateur", back_populates="contracts")