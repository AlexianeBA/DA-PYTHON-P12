import datetime
from rich.console import Console
from rich import print
from rich.table import Table
from controllers.collaborateur_controlleur import get_collaborateur_id_connected
from controllers.contract_controller import get_contracts_filter_by_collaborateur


def display_menu_start():
    print("Bienvenue!")
    print("Voulez-vous créer un compte ou vous connecter ?")
    print("1. Créer un compte")
    print("2. Se connecter")
    print("3. Quitter")
    choice = input("Entrez votre choix: ")
    return choice


def get_username():
    return input("Nom d'utilisateur : ")


def get_password():
    return input("Mot de passe : ")


def get_role():
    return input("Rôle: commercial, gestion ou support")


def display_welcome_message():
    print("Connexion réussie! Bienvenue,")


def display_menu():
    console = Console()
    console.print("Que souhaitez-vous faire ?", style="bold green")
    console.print("1. Modifier identifiant ou mot de passe")
    console.print("2. Supprimer mon compte collaborateur")
    console.print("3. Créer un client")
    console.print("4. Modifier la fiche d'un client")
    console.print("5. Supprimer la fiche d'un client")
    console.print("6. Créer un contrat")
    console.print("7. Modifier un contrat")
    console.print("8. Supprimer un contrat")
    console.print("9. Créer un évenement")
    console.print("10. Modifier un évenement")
    console.print("11. Supprimer un évenement")
    console.print(
        "12. Afficher la liste de tous les clients classés par ordre alphabétique"
    )
    console.print("13. Afficher la liste de tous les collaborateurs")
    console.print("14. Afficher la liste de tous les contrats")
    console.print("15. Afficher la liste de tous les évenements")
    console.print("[red]exit[/red]. Quitter")
    return input("Entrez votre choix : ")


def update_collaborateur_view(collaborateur_id, current_values):
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
    nom_complet = input("Entrez le nom complet du client : ")
    email = input("Entrez l'email du client : ")
    telephone = input("Entrez le numéro de téléphone du client : ")
    nom_entreprise = input("Entrez le nom de l'entreprise du client : ")
    date_de_creation = datetime.date.today()
    dernière_maj_contact = datetime.date.today()
    contact_commercial_chez_epic_events = input(
        "Entrez le nom du contact commercial chez Epic Events : "
    )

    return (
        nom_complet,
        email,
        telephone,
        nom_entreprise,
        date_de_creation,
        dernière_maj_contact,
        contact_commercial_chez_epic_events,
    )


def update_client_view(client_id, current_values):
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
    client_id = input("Entrez le numéro de l'identifiant du client: ")
    client = input("Entrez le nom complet du client: ")
    contact_commercial = input("Entrez votre identifiant: ")
    collaborateur_id = input("Entrez votre ID/ ")
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
    contract_id = input("Entrez l'identifiant contrat: ")
    client_name = input("Entrez le nom du client: ")
    date_debut = input("Entrez la date du début de l'évènement: ")
    date_fin = input("Entrez la date de fin de l'évènement: ")
    contact_support = input("Entrez le nom du contact support: ")
    lieu = input("Entrez le lieu de l'évenement ")
    participants = input("Renseignez le nombre de participants ")
    notes = input("Informations supplémentaires: ")

    return (
        contract_id,
        client_name,
        date_debut,
        date_fin,
        contact_support,
        lieu,
        participants,
        notes,
    )


def update_event_view(event_id, current_values):
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
    print(message)


def display_error_message(message):
    print(f"Erreur : {message}")


def display_list_of_clients(clients):
    console = Console()
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
            str(client.dernière_maj_contact),
            client.contact_commercial_chez_epic_events,
        )
    print("Voici la liste des clients chez Epicevents: ")
    console.print(table)


def display_list_of_collaborateurs(collaborateurs):
    console = Console()
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
    console = Console()
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
    print("Voici la liste des contrats chez Epicevents: ")
    console.print(table)


def display_list_of_events(events):
    console = Console()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du contrat")
    table.add_column("Nom du client concerné")
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
            event.date_debut.strftime("%Y-%m-%d"),
            event.date_fin.strftime("%Y-%m-%d"),
            event.contact_support,
            event.lieu,
            str(event.participants),
            event.notes,
        )
        table.add_row()
    print("Voici la liste des évenement: ")
    console.print(table)


def display_contracts_of_collaborateur_connected():
    collaborateur_id = get_collaborateur_id_connected()
    contracts = get_contracts_filter_by_collaborateur(collaborateur_id)
    print(collaborateur_id)
    console = Console()
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
