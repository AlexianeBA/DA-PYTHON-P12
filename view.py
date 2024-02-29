import datetime
import getpass
from rich.console import Console
from rich import print
from rich.table import Table
from rich.prompt import Prompt
from controllers.collaborateur_controlleur import get_collaborateur_id_connected
from controllers.contract_controller import get_contracts_filter_by_collaborateur
from controllers.event_controller import get_events_filter_by_collaborateur, get_events_filter_by_date_passed, get_events_filter_by_date_future
from controllers.client_controller import get_clients_filter_by_collaborateur


console = Console()
def display_menu_start():
    """
    Affiche le menu principal pour créer un compte, se connecter ou quitter.
    
    Returns:
        str: Le choix de l'utilisateur.
    """
    console.print("Bienvenue!", style="bold green")
    console.print("Voulez-vous créer un compte ou vous connecter ?")
    console.print("1. Créer un compte")
    console.print("2. Se connecter")
    console.print("3. Quitter")
    choice = Prompt.ask("Entrez votre choix: ")
    return choice



def get_username():
    """
    Demande et renvoie le nom d'utilisateur entré par l'utilisateur.

    Returns:
        str: Le nom d'utilisateur saisi.
    """
    return input("Nom d'utilisateur : ")


def get_password():
    """
    Demande et renvoie le mot de passe entré par l'utilisateur (avec masquage).

    Returns:
        str: Le mot de passe saisi.
    """
    return getpass.getpass("Mot de passe : ")


def get_role():
    """
    Demande et renvoie le rôle défini par l'utilisateur.

    Returns:
        str: Le rôle choisi par l'utilisateur.
    """
    return input("Définissez votre rôle: commercial, gestion ou support: ")


def display_welcome_message(nom_utilisateur):
    """
    Affiche un message de bienvenue personnalisé.

    Args:
        nom_utilisateur (str): Le nom d'utilisateur connecté.
    """
    console.print(f"Bienvenue,[bold green]{nom_utilisateur}[/bold green]")


def display_menu():
    """
    Affiche le menu principal pour les actions disponibles pour l'utilisateur connecté.
    
    Returns:
        str: Le choix de l'utilisateur.
    """
    console.print("Que souhaitez-vous faire ?", style="bold magenta")
    console.rule(style="bright_yellow")
    console.print("1. Modifier identifiant ou mot de passe")
    console.print("2. Supprimer mon compte collaborateur")
    console.print("3. Créer un client")
    console.print("4. Modifier la fiche d'un client")
    console.print("5. Supprimer la fiche d'un client")
    console.print("6. Créer un contrat")
    console.print("7. Modifier un contrat")
    console.print("8. Supprimer un contrat")
    console.print("9. Créer un événement")
    console.print("10. Modifier un événement")
    console.print("11. Supprimer un événement")
    console.print("12. Afficher la liste de tous les clients classés par ordre alphabétique")
    console.print("13. Afficher la liste de tous les collaborateurs classés par ordre alphabétique")
    console.print("14. Afficher la liste de tous les contrats classés par statut")
    console.print("15. Afficher la liste de tous les événements classés par date")
    console.print("16. Afficher la liste de tous les événements passés")
    console.print("16. Afficher la liste de tous les événements à venir")
    console.print("[red]exit. Quitter")
    console.rule(style="bright_yellow")
    return Prompt.ask("Entrez votre choix ")


def update_collaborateur_view(collaborateur_id, current_values):
    """
    Affiche la vue de mise à jour du collaborateur.

    Args:
        collaborateur_id (int): L'identifiant du collaborateur à mettre à jour.
        current_values (Collaborateur): Les valeurs actuelles du collaborateur.

    Returns:
        dict: Les nouvelles valeurs saisies pour le collaborateur.
    """
    new_values = {}

    print(
        "Entrez les nouveaux paramètres de connexion (laissez vide pour conserver les valeurs actuelles) :"
    )
    new_values["nom_utilisateur"] = (
        input(f"Nouveau nom d'utilisateur ({current_values.nom_utilisateur}): ")
        or current_values.nom_utilisateur
    )
    new_values["mot_de_passe"] = (
        input(f"Nouveau mot de passe ({current_values.mot_de_passe}): ")
        or current_values.mot_de_passe
    )
    new_values["role"] = (
        input(f"Nouveau rôle ({current_values.role}): ") or current_values.role
    )
    return new_values


def get_client_details():
    """
    Demande et renvoie les détails du client saisis par l'utilisateur.

    Returns:
        tuple: Les détails du client saisis par l'utilisateur.
    """
    nom_complet = input("Entrez le nom complet du client : ")
    email = input("Entrez l'email du client : ")
    telephone = input("Entrez le numéro de téléphone du client : ")
    nom_entreprise = input("Entrez le nom de l'entreprise du client : ")
    date_de_creation = datetime.date.today()
    derniere_maj_contact = datetime.date.today()
    contact_commercial_chez_epic_events = input(
        "Entrez le nom du contact commercial chez Epic Events : "
    )

    return (
        nom_complet,
        email,
        telephone,
        nom_entreprise,
        date_de_creation,
        derniere_maj_contact,
        contact_commercial_chez_epic_events,
    )


def update_client_view(client_id, current_values):
    """
    Affiche la vue de mise à jour du client.

    Args:
        client_id (int): L'identifiant du client à mettre à jour.
        current_values (Client): Les valeurs actuelles du client.

    Returns:
        dict: Les nouvelles valeurs saisies pour le client.
    """
    new_values = {}

    print(
        "Entrez les nouvelles valeurs pour le client (laissez vide pour conserver les valeurs actuelles) :"
    )

    new_values["nom_complet"] = (
        input(f"Nouveau nom complet du client ({current_values.nom_complet}): ")
        or current_values.nom_complet
    )
    new_values["email"] = (
        input(f"Nouvel email du client ({current_values.email}): ")
        or current_values.email
    )
    new_values["telephone"] = (
        input(f"Nouveau numéro de téléphone du client ({current_values.telephone}): ")
        or current_values.telephone
    )
    new_values["nom_entreprise"] = (
        input(
            f"Nouveau nom de l'entreprise du client ({current_values.nom_entreprise}): "
        )
        or current_values.nom_entreprise
    )
    new_values["contact_commercial_chez_epic_events"] = (
        input(
            f"Nouveau contact commercial Epic Events ({current_values.contact_commercial_chez_epic_events}):"
        )
        or current_values.contact_commercial_chez_epic_events
    )
    return new_values


def get_contract_details():
    """
    Demande et renvoie les détails du contrat saisis par l'utilisateur.

    Returns:
        tuple: Les détails du contrat saisis par l'utilisateur.
    """
    client_id = input("Entrez le numéro de l'identifiant du client: ")
    client = input("Entrez le nom complet du client: ")
    contact_commercial = input("Entrez votre identifiant: ")
    collaborateur_id = input("Entrez votre ID: ")
    montant_total = input("Entrez le montant total en €: ")
    montant_restant_a_payer = input("Montant restant à payer en €: ")
    statut_contrat = input("Renseigner le statut du contrat (en cours ou terminé): ")

    return (
        client_id,
        client,
        contact_commercial,
        collaborateur_id,
        montant_total,
        montant_restant_a_payer,
        statut_contrat,
    )


def update_contract_view(contract_id, current_values):
    """
    Affiche la vue de mise à jour du contrat.

    Args:
        contract_id (int): L'identifiant du contrat à mettre à jour.
        current_values (Contract): Les valeurs actuelles du contrat.

    Returns:
        dict: Les nouvelles valeurs saisies pour le contrat.
    """
    new_values = {}

    print(
        "Entrez les nouvelles valeurs pour le contrat (laissez vide pour conserver les valeurs actuelles) :"
    )

    new_values["client_id"] = (
        input(f"Nouvel identifiant du client ({current_values.client_id}): ")
        or current_values.client_id
    )
    new_values["contact_commercial"] = (
        input(f"Nouveau contact commercial ({current_values.contact_commercial}): ")
        or current_values.contact_commercial
    )
    new_values["montant_total"] = (
        input(f"Nouveau montant ({current_values.montant_total}): ")
        or current_values.montant_total
    )
    new_values["montant_restant_a_payer"] = (
        input(
            f"Nouveau montant restant à payer ({current_values.montant_restant_a_payer}): "
        )
        or current_values.montant_restant_a_payer
    )
    new_values["statut_contrat"] = (
        input(f"Nouveau statut du contrat ({current_values.statut_contrat}):")
        or current_values.statut_contrat
    )
    return new_values


def get_event_details():
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


def update_event_view(event_id, current_values):
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


def display_success_message(message):
    """
    Affiche un message de succès.

    Args:
        message (str): Le message de succès à afficher.
    """
    print(message)


def display_error_message(message):
    """
    Affiche un message d'erreur.

    Args:
        message (str): Le message d'erreur à afficher.
    """
    print(f"{message}")


def display_list_of_clients(clients):
    """
    Affiche la liste des clients.

    Args:
        clients (list): La liste des clients à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID")
    table.add_column("Nom complet")
    table.add_column("Email")
    table.add_column("Téléphone")
    table.add_column("Nom de l'entreprise")
    table.add_column("Date de création")
    table.add_column("Dernière mise à jour du contact")
    table.add_column("Contact commercial chez Epic Events")

    for client in clients:
        table.add_row(
            str(client.id),
            client.nom_complet,
            client.email,
            client.telephone,
            client.nom_entreprise,
            str(client.date_de_creation),
            str(client.derniere_maj_contact),
            client.contact_commercial_chez_epic_events,
        )
    print("Voici la liste des clients chez Epicevents: ")
    console.print(table)


def display_list_of_collaborateurs(collaborateurs):
    """
    Affiche la liste des collaborateurs.

    Args:
        collaborateurs (list): La liste des collaborateurs à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Nom d'utilisateur")
    table.add_column("Rôle")

    for collaborateur in collaborateurs:
        table.add_row(
            str(collaborateur.id),
            collaborateur.nom_utilisateur,
            collaborateur.role,
        )
    print("Voici la liste des collaborateurs chez Epicevents: ")
    console.print(table)


def display_list_of_contracts(contracts):
    """
    Affiche la liste des contrats.

    Args:
        contrats (list): La liste des contrats à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du client concerné")
    table.add_column("Nom du contact commercial")
    table.add_column("Montant total à payer en €")
    table.add_column("Montant restant à payer en €")
    table.add_column("Statut du contrat")

    for contract in contracts:
        table.add_row(
            str(contract.client_id),
            contract.contact_commercial,
            f"{str(contract.montant_total)} €",
            f"{str(contract.montant_restant_a_payer)} €",
            contract.statut_contrat,
        )
    print("Voici la liste des contrats classés par prix croissant chez Epicevents: ")
    console.print(table)


def display_list_of_events(events):
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


def display_contracts_of_collaborateur_connected():
    """
    Affiche les contrats du collaborateur connecté.
    """
    collaborateur_id = get_collaborateur_id_connected()
    contracts = get_contracts_filter_by_collaborateur(collaborateur_id)
    print(collaborateur_id)
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du contrat")
    table.add_column("ID du client")
    table.add_column("Contact commercial")
    table.add_column("ID du commercial")
    table.add_column("Montant total")
    table.add_column("Montant restant à payer")
    table.add_column("Statut du contrat")
    for contract in contracts:
        table.add_row(
            str(contract.id),
            str(contract.client_id),
            contract.contact_commercial,
            str(contract.collaborateur_id),
            f"{str(contract.montant_total)} €",
            f"{str(contract.montant_restant_a_payer)} €",
            contract.statut_contrat,
        )
    print("Liste de vos contrats: ")
    console.print(table)


def display_events_of_collaborateur_connected():
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

def display_clients_of_collaborateur_connected():
    """
    Affiche les clients du collaborateur connecté.
    """
    collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
    if collaborateur_id:
        clients = get_clients_filter_by_collaborateur(collaborateur_id)
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Nom complet du client")
        table.add_column("Adresse email du client")
        table.add_column("Numéro de téléphone du client")
        table.add_column("Nom de l'entreprise du client")
        table.add_column("Date de création de la fiche client")
        table.add_column("Dernière mise à jour de la fiche client")
        table.add_column("Nom du contact commercial chez Epicevents")
        table.add_column("ID du commercial")
        for client in clients:
            table.add_row(
                str(client.id),
                client.nom_complet,
                client.email,
                str(client.telephone),
                client.nom_complet,
                client.date_de_creation.strftime("%Y-%m-%d"), 
                client.derniere_maj_contact.strftime("%Y-%m-%d"),
                client.contact_commercial_chez_epic_events,
            )
        print("Liste de vos clients: ")
        console.print(table)
    else:
        print("aucun collaborateur connecté")


def display_events_passed():
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
