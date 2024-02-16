from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    telephone = Column(String(16))
    nom_entreprise = Column(String(256))
    date_de_creation = Column(Date)
    dernière_maj_contact = Column(Date, nullable=False)
    contact_commercial_chez_epic_events = Column(String(256), nullable=False)

class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    client = relationship("Client")
    contact_commercial = Column(String(256), nullable=False)
    montant_total = Column(Integer)
    montant_restant_a_payer = Column(Integer)
    statut_contrat = Column(Boolean, nullable=False)

class Collaborateur(Base):
    __tablename__ = 'collaborateurs'

    id = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(256), unique=True, nullable=False)
    mot_de_passe = Column(String(32), nullable=False)
    role = Column(String(50), nullable=False)