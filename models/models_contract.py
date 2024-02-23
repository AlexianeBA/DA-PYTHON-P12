from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO : découper les models
# TODO: associer par défaut le commercial lors de la création d'une fiche client


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
