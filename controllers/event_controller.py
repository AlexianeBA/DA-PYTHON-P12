from models import Event
from db_config import Session


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
    event = Event(
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


def update_event(event_id, new_values):
    session = Session()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        for attr, value in new_values.items():
            setattr(event, attr, value)
        session.commit()
    session.close()


def delete_event(event_id):
    session = Session()
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        session.delete(event)
        session.commit()
    session.close()
