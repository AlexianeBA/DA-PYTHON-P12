from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from models.base import Base




class Client(Base):
    """
    Représente un client dans la base de données.

    Attributes:
        id (int): Identifiant unique du client.
        nom_complet (str): Nom complet du client.
        email (str): Adresse e-mail du client.
        telephone (str): Numéro de téléphone du client.
        nom_entreprise (str): Nom de l'entreprise du client.
        date_de_creation (Date): Date de création du client.
        derniere_maj_contact (Date, optional): Dernière mise à jour du contact avec le client.
        contact_commercial_chez_epic_events (str): Contact commercial chez Epic Events.
        collaborateur_id (int): Identifiant du collaborateur associé au client.
        events (relationship): Relation avec la table Events.
        contracts (relationship): Relation avec la table Contract.
        collaborateur (relationship): Relation avec la table Collaborateur.
    """
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    telephone = Column(String(16))
    nom_entreprise = Column(String(256))
    date_de_creation = Column(DateTime, default=datetime.now)
    derniere_maj_contact = Column(DateTime, nullable=True)
    contact_commercial_chez_epic_events = Column(String(256), nullable=False)
    collaborateur_id = Column(Integer, ForeignKey("collaborateurs.id"))

    events = relationship("Events", back_populates="client")
    contracts = relationship("Contract", back_populates="client")
    collaborateur = relationship("Collaborateur", back_populates="client")

    def __repr__(self) -> str:
        return (
            f"Client(id={self.id!r}, "
            f"name={self.nom_complet!r}, "
            f"email={self.email!r}, "
            f"téléphone={self.telephone!r}, "
            f"nom de l'entreprise={self.nom_entreprise!r}, "
            f"date de création={self.date_de_creation!r}, "
            f"dernière mise à jour du contact={self.derniere_maj_contact!r}, "
            f"contact commercial chez épic events={self.contact_commercial_chez_epic_events!r}"
            f"id du commercial={self.collaborateur_id!r})"
        )
