from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base


Base = declarative_base()


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
    date_de_creation = Column(Date)
    derniere_maj_contact = Column(Date, nullable=True)
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

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    contact_commercial = Column(String(256), nullable=False)
    collaborateur_id = Column(Integer, ForeignKey("collaborateurs.id"))
    montant_total = Column(Integer)
    montant_restant_a_payer = Column(Integer)
    statut_contrat = Column(String(50), nullable=False)

    events = relationship("Events", back_populates="contract")
    client = relationship("Client", back_populates="contracts")
    collaborateur = relationship("Collaborateur", back_populates="contracts")


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
