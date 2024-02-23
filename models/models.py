from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO : découper les models
# TODO: associer par défaut le commercial lors de la création d'une fiche client


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    telephone = Column(String(16))
    nom_entreprise = Column(String(256))
    date_de_creation = Column(Date)
    dernière_maj_contact = Column(Date, nullable=True)
    contact_commercial_chez_epic_events = Column(String(256), nullable=False)

    events = relationship("Events", back_populates="client")
    contract = relationship("Contract", back_populates="client")
    # contact_commercial_chez_epic_events = relationship(
    #     "Collaborateur", back_populates="client"
    # )

    def __repr__(self) -> str:
        return (
            f"Client(id={self.id!r}, "
            f"name={self.nom_complet!r}, "
            f"email={self.email!r}, "
            f"téléphone={self.telephone!r}, "
            f"nom de l'entreprise={self.nom_entreprise!r}, "
            f"date de création={self.date_de_creation!r}, "
            f"dernière mise à jour du contact={self.dernière_maj_contact!r}, "
            f"contact commercial chez épic events={self.contact_commercial_chez_epic_events!r})"
        )


class Contract(Base):
    __tablename__ = "contract"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    client = relationship("Client", back_populates="contract")
    contact_commercial = Column(String(256), nullable=False)
    montant_total = Column(Integer)
    montant_restant_a_payer = Column(Integer)
    statut_contrat = Column(String(50), nullable=False)

    events = relationship("Events", back_populates="contract")


class Collaborateur(Base):
    __tablename__ = "collaborateurs"

    id = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(256), unique=True, nullable=False)
    mot_de_passe = Column(String(32), nullable=False)
    role = Column(String(50), nullable=False)


# TODO : établir relation avec collaborateur (contact support)
class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("contract.id"), nullable=False)
    client_name = Column(Integer, ForeignKey("client.nom_complet"), nullable=False)
    date_debut = Column(Date)
    date_fin = Column(Date)
    contact_support = Column(String(256))
    lieu = Column(String(1024))
    participants = Column(Integer)
    notes = Column(String(2048))

    contract = relationship("Contract", back_populates="events")
    client = relationship("Client", back_populates="events")
