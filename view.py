import datetime
from rich.console import Console
from rich import print


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
    return input("Rôle: commercial, gestion ou admin")


def display_welcome_message():
    print("Connexion réussie! Bienvenue,")


def display_menu():
    console = Console()
    console.print("Que souhaitez-vous faire ?", style="bold green")
    console.print("1. Créer un client")
    console.print("2. Modifier la fiche d'un client")
    console.print("3. Créer un contrat")
    console.print("4. Modifier un contrat")
    console.print("5. Créer un évenement")
    console.print("2. Modifier un évenement")
    console.print("[red]exit[/red]. Quitter")
    return input("Entrez votre choix : ")


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


def update_client(client_id, current_values):
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
    montant_total = input("Entrez le montant total en €: ")
    montant_restant_a_payer = input("Montant restant à payer en €: ")
    statut_contrat = input("Renseigner le statut du contrat (en cours ou terminé): ")

    return (
        client_id,
        client,
        contact_commercial,
        montant_total,
        montant_restant_a_payer,
        statut_contrat,
    )


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


def display_success_message(message):
    print(message)


def display_error_message(message):
    print(f"Erreur : {message}")
