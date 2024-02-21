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
    console.print("2. Créer un contrat")
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


def display_success_message(message):
    print(message)


def display_error_message(message):
    print(f"Erreur : {message}")
