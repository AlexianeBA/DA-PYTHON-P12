from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
