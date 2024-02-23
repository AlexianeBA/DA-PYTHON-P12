from models.models import Events
from db_config import Session

# TODO: filtrer l'affichage


def create_event(
    contract_id,
    client_name,
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


def get_all_events():
    session = Session()
    events = session.query(Events).all()
    return events
