from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Collaborateur(Base):
    __tablename__ = "collaborateurs"

    id = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(256), unique=True, nullable=False)
    mot_de_passe = Column(String(32), nullable=False)
    role = Column(String(50), nullable=False)
