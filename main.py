import sys
from controllers.client_controller import create_client
from controllers.contract_controller import create_contract
from controllers.user_controller import authenticate_user
from controllers.collaborateur_controlleur import create_collaborateur
from controllers.event_controller import create_event
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
        user = authenticate_user(nom_utilisateur, password)
        if user:
            display_welcome_message()
            while True:
                action = display_menu()
                if action == "1":
                    client_details = get_client_details()
                    try:
                        create_client(*client_details)
                        display_success_message("Client ajouté avec succès !")
                    except Exception as e:
                        display_error_message(f"Erreur lors de l'ajout du client : {e}")
                elif action == "2":
                    contract_details = get_contract_details()
                    try:
                        create_contract(*contract_details)
                        display_success_message("Contrat créé avec succès !")
                    except Exception as e:
                        display_error_message(
                            f"Erreur lors de l'ajout du contrat : {e}"
                        )
                elif action == "3":
                    event_details = get_event_details()
                    try:
                        create_event(*event_details)
                        display_success_message("Evenement créer avec succès!")
                    except Exception as e:
                        display_error_message(
                            f"Erreur lors de l'ajout de l'évenement: {e}"
                        )
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
