from typing import Any, Dict, List, Tuple
from controllers.collaborateur_controlleur import get_collaborateur_id_connected
from controllers.event_controller import get_events_filter_by_collaborateur, get_events_filter_by_date_passed, get_events_filter_by_date_future
import datetime
from rich.table import Table
from models.event import Events
from views.main_view import console
def get_event_details()-> Tuple[str, str, str, str, str, str, str, str, str]:
    """
    Demande et renvoie les détails de l'événement saisis par l'utilisateur.

    Returns:
        tuple: Les détails de l'événement saisis par l'utilisateur.
    """
    contract_id = input("Entrez l'identifiant contrat: ")
    client_name = input("Entrez le nom du client: ")
    collaborateur_id=input("Entrez votre id")
    date_debut = input("Entrez la date du début de l'évènement: ")
    date_fin = input("Entrez la date de fin de l'évènement: ")
    contact_support = input("Entrez le nom du contact support: ")
    lieu = input("Entrez le lieu de l'évenement ")
    participants = input("Renseignez le nombre de participants ")
    notes = input("Informations supplémentaires: ")

    return (
        contract_id,
        client_name,
        collaborateur_id,
        date_debut,
        date_fin,
        contact_support,
        lieu,
        participants,
        notes,
    )


def update_event_view(event_id: int, current_values: Dict[str, Any]) -> Dict[str, Any]:
    """
    Affiche la vue de mise à jour de l'événement.

    Args:
        event_id (int): L'identifiant de l'événement à mettre à jour.
        current_values (Events): Les valeurs actuelles de l'événement.

    Returns:
        dict: Les nouvelles valeurs saisies pour l'événement.
    """
    new_values = {}

    print(
        "Entrez les nouvelles valeurs pour l'évenement (laissez vide pour conserver les valeurs actuelles) :"
    )

    new_values["contract_id"] = (
        input(f"Nouvel identifiant du contra ({current_values.contract_id}): ")
        or current_values.contract_id
    )
    new_values["client_name"] = (
        input(f"Nouveau nom du client ({current_values.client_name}): ")
        or current_values.client_name
    )
    new_values["date_debut"] = (
        input(f"Nouvelle date de début ({current_values.date_debut}): ")
        or current_values.date_debut
    )
    new_values["date_fin"] = (
        input(f"Nouvelle date de fin ({current_values.date_fin}): ")
        or current_values.date_fin
    )
    new_values["contact_support"] = (
        input(f"Nouveau contact support ({current_values.contact_support}):")
        or current_values.contact_support
    )
    new_values["lieu"] = (
        input(f"Nouveau lieu ({current_values.lieu}):") or current_values.lieu
    )
    new_values["participants"] = (
        input(f"Nouveau nombre de participants ({current_values.participants}):")
        or current_values.participants
    )
    new_values["notes"] = (
        input(f"Nouvelles notes ({current_values.notes}):") or current_values.notes
    )
    return new_values

def display_list_of_events(events: List[Dict[str, Any]]) -> List[Events]:
    """
    Affiche la liste des événements.

    Args:
        events (list): La liste des événements à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du contrat")
    table.add_column("Nom du client concerné")
    table.add_column("ID du support")
    table.add_column("Date de début de l'évenement")
    table.add_column("Date de fin de l'évenement")
    table.add_column("Contact support chez Epicevents")
    table.add_column("Lieu de l'évenement")
    table.add_column("Nombre de participants à l'évenement")
    table.add_column("Notes")
    for event in events:
        table.add_row(
            str(event.contract_id),
            event.client_name,
            str(event.collaborateur_id),
            event.date_debut.strftime("%Y-%m-%d"),
            event.date_fin.strftime("%Y-%m-%d"),
            event.contact_support,
            event.lieu,
            str(event.participants),
            str(event.notes),
        )
        table.add_row()
    print("Voici la liste des évenement: ")
    console.print(table)

def display_events_of_collaborateur_connected()-> List[Events]:
    """
    Affiche les événements du collaborateur connecté.
    """
    collaborateur_id = get_collaborateur_id_connected()
    events = get_events_filter_by_collaborateur(collaborateur_id)
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID de l'évenement")
    table.add_column("Nom complet du client")
    table.add_column("ID du support")
    table.add_column("Date de début de l'évenement")
    table.add_column("Date de fin de l'évenement")
    table.add_column("Nom du contact commercial")
    table.add_column("Lieu de l'évenement")
    table.add_column("Nombre de participants")
    table.add_column("Notes")
    for event in events:
        table.add_row(
            str(event.id),
            str(event.contract_id),
            str(event.collaborateur_id),
            event.date_debut.strftime('%Y-%m-%d %H:%M:%S'),
            event.date_fin.strftime('%Y-%m-%d %H:%M:%S'),
            event.contact_support,
            event.lieu,
            str(event.participants),
            str(event.notes),
        )
    print("Liste de vos évenements: ")
    console.print(table)



def display_events_passed()-> List[Events]:
    """
    Affiche les événements passés.
    """
    past_events = get_events_filter_by_date_passed()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID de l'événement")
    table.add_column("Nom complet du client")
    table.add_column("ID du support")
    table.add_column("Date de début de l'événement")
    table.add_column("Date de fin de l'événement")
    table.add_column("Nom du contact commercial")
    table.add_column("Lieu de l'événement")
    table.add_column("Nombre de participants")
    table.add_column("Notes")
    for event in past_events:
        table.add_row(
            str(event.id),
            str(event.contract_id),
            str(event.collaborateur_id),
            event.date_debut.strftime('%Y-%m-%d %H:%M:%S'),  
            event.date_fin.strftime('%Y-%m-%d %H:%M:%S'),   
            event.contact_support,
            event.lieu,
            str(event.participants),
            str(event.notes)
        )
    print("Liste de vos événements passés: ")
    console.print(table)


def display_events_future():
    """
    Affiche les événements à venir.
    """
    past_events = get_events_filter_by_date_future()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID de l'événement")
    table.add_column("Nom complet du client")
    table.add_column("ID du support")
    table.add_column("Date de début de l'événement")
    table.add_column("Date de fin de l'événement")
    table.add_column("Nom du contact commercial")
    table.add_column("Lieu de l'événement")
    table.add_column("Nombre de participants")
    table.add_column("Notes")
    for event in past_events:
        table.add_row(
            str(event.id),
            str(event.client_name),
            str(event.collaborateur_id),
            event.date_debut.strftime('%Y-%m-%d %H:%M:%S'),  
            event.date_fin.strftime('%Y-%m-%d %H:%M:%S'),   
            event.contact_support,
            event.lieu,
            str(event.participants),
            str(event.notes)
        )
    print("Liste de vos événements à venir: ")
    console.print(table)
