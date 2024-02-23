from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
