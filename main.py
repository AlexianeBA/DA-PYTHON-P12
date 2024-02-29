import sys
import sentry_sdk
from controllers.client_controller import (
    create_client,
    get_client_by_id,
    update_client,
    delete_client,
    get_clients_filtered,
    
)

from controllers.contract_controller import (
    create_contract,
    get_contract_by_id,
    update_contract,
    delete_contract,
    get_contracts_filter_by_price
)
from controllers.collaborateur_controlleur import (
    create_collaborateur,
    authenticate_collaborateur,
    get_collaborateur_by_id,
    update_collaborateur,
    delete_collaborateur,
    get_collaborateurs_filtered,
    get_collaborateur_id_connected,
    disconnection_collaborateur
)
from controllers.event_controller import (
    create_event,
    get_event_by_id,
    update_event,
    delete_event,
    get_events_filter_by_date_passed
)
from view import (
    display_menu_start,
    get_username,
    get_password,
    display_welcome_message,
    display_menu,
    get_client_details,
    get_contract_details,
    display_success_message,
    display_error_message,
    get_role,
    get_event_details,
    update_client_view,
    update_contract_view,
    update_event_view,
    update_collaborateur_view,
    display_list_of_clients,
    display_list_of_collaborateurs,
    display_list_of_contracts,
    display_list_of_events,
    display_contracts_of_collaborateur_connected,
    display_events_of_collaborateur_connected,
    display_clients_of_collaborateur_connected,
    display_events_passed,
    display_events_future
)
sentry_sdk.init(
    dsn="https://10f5a086eadb50756921d93e4c02e773@o4506824189739008.ingest.sentry.io/4506824191377408",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


def main():
    try:
        choice = display_menu_start()
        if choice == "1":
            nom_utilisateur = get_username()
            mot_de_passe = get_password()
            role = get_role()
            collaborator = create_collaborateur(nom_utilisateur, mot_de_passe, role)
            if collaborator:
                display_success_message("Création de compte réussie !")
                while True:
                    action = input(
                        "Tapez 'menu' pour afficher le menu ou 'exit' pour quitter: "
                    )
                    if action == "menu":
                        display_welcome_message(nom_utilisateur)
                        display_menu()

                    elif action == "exit":
                        print("Au revoir !")
                        sys.exit()
                    else:
                        display_error_message("Option non valide. Veuillez réessayer.")
        elif choice == "2":
            nom_utilisateur = get_username()
            password = get_password()
            user = authenticate_collaborateur(nom_utilisateur, password)
            if user:
                display_welcome_message(nom_utilisateur)
                while True:
                    action = display_menu() 
                    if action == "1":
                        collaborateur_id = input(
                            "Entrez votre identifiant d'utilisateur : "
                        )
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
                        collaborateur_id = input(
                            "Entrez l'ID du collaborateur que vous souhaitez supprimer : "
                        )
                        confirm = input(
                            "Êtes-vous sûr de vouloir supprimer ce collaborateur ? (oui/non) : "
                        )
                        if confirm.lower() == "oui":
                            try:
                                delete_collaborateur(collaborateur_id)
                                display_success_message(
                                    "Collaborateur supprimé avec succès !"
                                )
                            except:
                                display_error_message(
                                    "Erreur lors de la suppression du collaborateur."
                                )
                        else:
                            display_error_message("Suppression annulée.")
                    elif action == "3":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        try:
                            if collaborateur_id and collaborateur_role == 'commercial':
                                client_details = get_client_details()
                                create_client(*client_details, collaborateur_id=collaborateur_id)
                                display_success_message("Client ajouté avec succès !")
                            else:
                                print("Vous n'avez pas les droits pour créer une fiche client.")
                        except:
                            display_error_message(f"Erreur lors de l'ajout du client.")
                    elif action == "4":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "commercial":
                            display_clients_of_collaborateur_connected()
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
                            display_error_message("Vous devez être un commercial pour modifier un client.")
                    elif action == "5":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "commercial":
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
                            display_error_message("Vous devez être un commercial pour supprimer un client.")
                    elif action == "6":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "gestion":
                            contract_details = get_contract_details()
                            try:
                                create_contract(*contract_details)
                                display_success_message("Contrat créé avec succès !")
                            except Exception as e:
                                display_error_message(
                                    f"Erreur lors de l'ajout du contrat : {e}"
                                )
                        else:
                            display_error_message("Vous devez être un gestionnaire pour créer un contrat.")
                    elif action == "7":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
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
                                display_error_message(
                                    f"Erreur lors de la modification du contrat."
                                )
                        else:
                            display_error_message("Vous devez être un gestionnaire ou un commercial pour modifier un contrat.")
                    elif action == "8":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "gestion":
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
                            display_error_message("Vous devez être un gestionnaire pour supprimer un contrat.")
                    elif action == "9":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "commercial":
                            event_details = get_event_details()
                            print(event_details)
                            try:
                                create_event(*event_details)
                                display_success_message("Evenement créer avec succès!")
                            except Exception as e:
                                display_error_message(
                                    f"Erreur lors de l'ajout de l'évenement: {e}"
                                )
                        else:
                            display_error_message("Vous devez être un commercial pour créer un évenement.")
                    elif action == "10":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "support":
                            display_events_of_collaborateur_connected()
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
                            display_error_message("Vous devez être un membre du département support pour modifier un évenement.")
                    elif action == "11":
                        collaborateur_id, collaborateur_role = get_collaborateur_id_connected()
                        if collaborateur_role == "support":
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
                        events = get_events_filter_by_date_passed()
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
            else:
                display_error_message("Adresse e-mail ou mot de passe incorrect.")
        elif choice == "3":
            sys.exit()
        else:
            display_error_message("Option non valide. Veuillez réessayer.")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print("Une erreur s'est produite. Veuillez contacter le support.")
        sys.exit(1)


if __name__ == "__main__":
    main()



