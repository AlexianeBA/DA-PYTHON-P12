import sys
from controllers.client_controller import (
    create_client,
    get_client_by_id,
    update_client,
    delete_client,
)

from controllers.contract_controller import (
    create_contract,
    get_contract_by_id,
    update_contract,
    delete_contract,
)
from controllers.collaborateur_controlleur import (
    create_collaborateur,
    authenticate_collaborateur,
    get_collaborateur_by_id,
    update_collaborateur,
    delete_collaborateur,
)
from controllers.event_controller import (
    create_event,
    get_event_by_id,
    update_event,
    delete_event,
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
)


def main():
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
                    display_welcome_message()
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
            display_welcome_message()
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
                    client_details = get_client_details()
                    try:
                        create_client(*client_details)
                        display_success_message("Client ajouté avec succès !")
                    except Exception as e:
                        display_error_message(f"Erreur lors de l'ajout du client : {e}")
                elif action == "4":
                    client_id = input(
                        "Entrez l'ID du client que vous souhaitez mettre à jour : "
                    )

                    current_client = get_client_by_id(client_id)
                    if current_client:
                        new_values = update_client_view(client_id, current_client)
                        try:
                            update_client(client_id, new_values)
                            display_success_message("Client modifié avec succès !")
                        except:
                            display_error_message(
                                f"Erreur lors de la modification du client."
                            )
                    else:
                        display_error_message("Client non trouvé.")
                elif action == "5":
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
                elif action == "6":
                    contract_details = get_contract_details()
                    try:
                        create_contract(*contract_details)
                        display_success_message("Contrat créé avec succès !")
                    except Exception as e:
                        display_error_message(
                            f"Erreur lors de l'ajout du contrat : {e}"
                        )
                elif action == "7":
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
                elif action == "8":
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
                elif action == "9":
                    event_details = get_event_details()
                    try:
                        create_event(*event_details)
                        display_success_message("Evenement créer avec succès!")
                    except Exception as e:
                        display_error_message(
                            f"Erreur lors de l'ajout de l'évenement: {e}"
                        )
                elif action == "10":
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
                elif action == "11":
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
                elif action == "exit":
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


if __name__ == "__main__":
    main()
