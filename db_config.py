import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
password = os.getenv("PASSWORD")

engine = create_engine(f"mysql://root:{password}@localhost/epicevents")
Session = sessionmaker(bind=engine)


def get_session():
    return Session()
