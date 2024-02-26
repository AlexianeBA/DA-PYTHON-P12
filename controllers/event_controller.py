from models.models import Events
from db_config import Session



def create_event(
    contract_id,
    client_name,
    collaborateur_id,
    date_debut,
    date_fin,
    contact_support,
    lieu,
    participants,
    notes,
):
    session = Session()
    event = Events(
        contract_id=contract_id,
        client_name=client_name,
        collaborateur_id=collaborateur_id,
        date_debut=date_debut,
        date_fin=date_fin,
        contact_support=contact_support,
        lieu=lieu,
        participants=participants,
        notes=notes,
    )
    session.add(event)
    session.commit()
    session.close()
    return event


def get_event_by_id(event_id):
    session = Session()
    event = session.query(Events).filter_by(id=event_id).first()
    session.close()
    return event


def update_event(event_id, new_values):
    session = Session()
    event = session.query(Events).filter_by(id=event_id).first()
    if event:
        for attr in new_values:
            setattr(event, attr, new_values[attr])
        session.commit()
    session.close()


def delete_event(event_id):
    session = Session()
    event = session.query(Events).filter_by(id=event_id).first()
    if event:
        session.delete(event)
        session.commit()
    session.close()

def get_events_filter_by_collaborateur(collaborateur_id):
    session = Session()
    events = session.query(Events).filter_by(collaborateur_id=collaborateur_id).all()
    return events


def get_all_events():
    session = Session()
    events = session.query(Events).all()
    return events

def get_events_filter_by_date(date_debut=None):
    session = Session()
    query = session.query(Events)

    if date_debut:
        query= query.filter(Events.date_debut==date_debut)
    query = query.order_by(Events.date_debut)
    event = query.all()
    return event