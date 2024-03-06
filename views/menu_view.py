from views.main_view import console
from rich.prompt import Prompt
import sys
import sentry_sdk
from controllers.client_controller import (
    create_client,
    get_client_by_id,
    update_client,
    delete_client,
    get_clients_filtered,
    get_clients,
)

from controllers.contract_controller import (
    create_contract,
    get_contract_by_id,
    update_contract,
    delete_contract,
    get_contracts_filter_by_price,
    get_all_contracts,
)
from controllers.collaborateur_controlleur import (
    create_collaborateur,
    authenticate_collaborateur,
    get_collaborateur_by_id,
    update_collaborateur,
    delete_collaborateur,
    get_collaborateurs_filtered,
    get_collaborateur_id_connected,
    disconnection_collaborateur,
)
from controllers.event_controller import (
    create_event,
    get_event_by_id,
    get_events_filter_by_date,
    update_event,
    delete_event,
    get_events_filter_by_date_passed,
    get_all_events,
)

from views.client_view import (
    display_clients_of_collaborateur_connected,
    display_list_of_clients,
    get_client_details,
    update_client_view,
)
from views.collaborateur_view import (
    get_username,
    get_role,
    get_password,
    display_list_of_collaborateurs,
    update_collaborateur_view,
)
from views.contract_view import (
    get_contract_details,
    update_contract_view,
    display_list_of_contracts,
    display_contracts_of_collaborateur_connected,
)
from views.event_view import (
    get_event_details,
    update_event_view,
    display_list_of_events,
    display_events_passed,
    display_events_future,
    display_events_of_collaborateur_connected,
)
from views.main_view import (
    display_success_message,
    display_error_message,
    display_welcome_message,
)


def display_menu_start() -> str:
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


def display_menu() -> str:
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
    console.print(
        "12. Afficher la liste de tous les clients classés par ordre alphabétique"
    )
    console.print(
        "13. Afficher la liste de tous les collaborateurs classés par ordre alphabétique"
    )
    console.print("14. Afficher la liste de tous les contrats classés par statut")
    console.print("15. Afficher la liste de tous les événements classés par date")
    console.print("16. Afficher la liste de tous les événements passés")
    console.print("17. Afficher la liste de tous les événements à venir")
    console.print("[red]exit. Quitter")
    console.rule(style="bright_yellow")
    return Prompt.ask("Entrez votre choix ")


def handle_menu_options(nom_utilisateur):
    while True:
        action = display_menu()
        if action == "1":
            collaborateur_id = input("Entrez votre identifiant d'utilisateur : ")
            current_collaborateur = get_collaborateur_by_id(collaborateur_id)
            if current_collaborateur:
                new_values = update_collaborateur_view(
                    collaborateur_id, current_collaborateur
                )
                try:
                    update_collaborateur(collaborateur_id, new_values)
                    display_success_message(
                        "Identifiant utilisateur modifié avec succès !"
                    )
                except:
                    display_error_message(
                        "Erreur lors de la modification de l'identifiant utilisateur."
                    )
            else:
                display_error_message("Utilisateur non trouvé.")
        elif action == "2":
            get_collaborateur_id_connected(nom_utilisateur)
            print(nom_utilisateur)

            confirm = input(
                "Êtes-vous sûr de vouloir supprimer votre compte utilisateur? (oui/non) : "
            )
            if confirm.lower() == "oui":
                try:
                    delete_collaborateur(nom_utilisateur)
                    display_success_message("Collaborateur supprimé avec succès !")
                except:
                    display_error_message(
                        "Erreur lors de la suppression du collaborateur."
                    )
            else:
                display_error_message("Suppression annulée.")
        elif action == "3":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            try:
                if (
                    collaborateur_id and collaborateur_role == "commercial"
                ):  # Vérifiez si le collaborateur a un rôle commercial
                    client_details = get_client_details()
                    create_client(
                        *client_details[:-1],
                        collaborateur_id=collaborateur_id,
                    )  # Passez collaborateur_id explicitement
                    display_success_message("Client ajouté avec succès !")
                else:
                    print(
                        "Vous n'avez pas les droits pour créer une fiche client ou votre rôle n'est pas 'commercial'."
                    )
            except Exception as e:
                display_error_message(f"Erreur lors de l'ajout du client : {str(e)}")
        elif action == "4":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "commercial":
                display_clients_of_collaborateur_connected(nom_utilisateur)
                client_id = input(
                    "Entrez l'ID du client que vous souhaitez mettre à jour : "
                )

                current_client = get_client_by_id(client_id)
                if current_client:
                    new_values = update_client_view(client_id, current_client)
                    try:
                        update_client(client_id, new_values)
                        display_success_message("Client modifié avec succès !")
                    except Exception as e:
                        sentry_sdk.capture_exception(e)
                        display_error_message(
                            f"Erreur lors de la modification du client: {str(e)}"
                        )
                else:
                    display_error_message("Client non trouvé.")
            else:
                display_error_message(
                    "Vous devez être un commercial pour modifier un client."
                )
        elif action == "5":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "commercial":
                display_clients_of_collaborateur_connected(nom_utilisateur)
                client_id = input(
                    "Entrez l'ID du client que vous souhaitez supprimer : "
                )
                confirm = input(
                    "Êtes-vous sûr de vouloir supprimer ce client? (oui/non) : "
                )
                if confirm.lower() == "oui":
                    try:
                        delete_client(client_id)
                        display_success_message("Client supprimé avec succès !")
                    except:
                        display_error_message(
                            "Erreur lors de la suppression du client."
                        )
                else:
                    display_error_message("Suppression annulée.")
            else:
                display_error_message(
                    "Vous devez être un commercial pour supprimer un client."
                )
        elif action == "6":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "gestion":
                clients = get_clients()
                display_list_of_clients(clients)
                client_id = input("Entrez l'identifiant du client : ")
                try:
                    contract_details = get_contract_details(client_id)
                    create_contract(*contract_details)
                    display_success_message("Contrat créé avec succès !")
                except Exception as e:
                    display_error_message(f"Erreur lors de l'ajout du contrat : {e}")
            else:
                display_error_message(
                    "Vous devez être un gestionnaire pour créer un contrat."
                )
        elif action == "7":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "gestion" or "commercial":
                display_contracts_of_collaborateur_connected()
                contract_id = input(
                    "Entrez l'ID du contrat que vous souhaitez mettre à jour :"
                )
                current_contract = get_contract_by_id(contract_id)
                if current_contract:
                    new_values_contract = update_contract_view(
                        contract_id, current_contract
                    )
                try:
                    update_contract(contract_id, new_values_contract)
                    display_success_message("Contrat modifié avec succès !")
                except:
                    display_error_message(f"Erreur lors de la modification du contrat.")
            else:
                display_error_message(
                    "Vous devez être un gestionnaire ou un commercial pour modifier un contrat."
                )
        elif action == "8":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "gestion":
                display_contracts_of_collaborateur_connected()
                contract_id = input(
                    "Entrez l'ID du contrat que vous souhaitez supprimer : "
                )
                confirm = input(
                    "Êtes-vous sûr de vouloir supprimer ce contrat ? (oui/non) : "
                )
                if confirm.lower() == "oui":
                    try:
                        delete_contract(contract_id)
                        display_success_message("Contrat supprimé avec succès !")
                    except:
                        display_error_message(
                            "Erreur lors de la suppression du contrat."
                        )
                else:
                    display_error_message("Suppression annulée.")
            else:
                display_error_message(
                    "Vous devez être un gestionnaire pour supprimer un contrat."
                )
        elif action == "9":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "commercial":
                contracts = get_all_contracts()
                display_list_of_contracts(contracts)
                event_details = get_event_details()
                print(event_details)
                try:
                    create_event(*event_details)
                    display_success_message("Evenement créer avec succès!")
                except Exception as e:
                    display_error_message(f"Erreur lors de l'ajout de l'évenement: {e}")
            else:
                display_error_message(
                    "Vous devez être un commercial pour créer un évenement."
                )
        elif action == "10":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "support":
                events = get_all_events()
                display_list_of_events(events)
                event_id = input(
                    "Entrez l'ID de l'évenement que vous souhaitez mettre à jour :"
                )
                current_event = get_event_by_id(event_id)
                if current_event:
                    new_values_event = update_event_view(event_id, current_event)
                try:
                    update_event(event_id, new_values_event)
                    display_success_message("Evenement modifié avec succès !")
                except:
                    display_error_message(
                        f"Erreur lors de la modification de l'evenement."
                    )
            else:
                display_error_message(
                    "Vous devez être un membre du département support pour modifier un évenement."
                )
        elif action == "11":
            collaborateur_id, collaborateur_role = get_collaborateur_id_connected(
                nom_utilisateur
            )
            if collaborateur_role == "support":
                events = get_all_events()
                display_list_of_events(events)
                event_id = input(
                    "Entrez l'ID de l'évenement que vous souhaitez supprimer : "
                )
                confirm = input(
                    "Êtes-vous sûr de vouloir supprimer cet évenement ? (oui/non) : "
                )
                if confirm.lower() == "oui":
                    try:
                        delete_event(event_id)
                        display_success_message("Evenement supprimé avec succès !")
                    except:
                        display_error_message(
                            "Erreur lors de la suppression de l'évenement."
                        )
                else:
                    display_error_message("Suppression annulée.")
        elif action == "12":
            clients = get_clients_filtered()
            display_list_of_clients(clients)
        elif action == "13":
            collaborateurs = get_collaborateurs_filtered()
            display_list_of_collaborateurs(collaborateurs)
        elif action == "14":
            contracts = get_contracts_filter_by_price()
            display_list_of_contracts(contracts)
        elif action == "15":
            events = get_events_filter_by_date()
            display_list_of_events(events)
        elif action == "16":
            display_events_passed()
        elif action == "17":
            display_events_future()
        elif action == "exit":
            print("Déconnexion en cours...")
            disconnection_collaborateur()
            print("Au revoir !")
            sys.exit()
        else:
            display_error_message("Option non valide. Veuillez réessayer.")
