import sys
import sentry_sdk
from controllers.collaborateur_controlleur import (
    create_collaborateur,
    authenticate_collaborateur,
)

from views.menu_view import display_menu, display_menu_start, handle_menu_options

from views.collaborateur_view import (
    get_username,
    get_role,
    get_password,
)
from views.main_view import (
    display_success_message,
    display_error_message,
    display_welcome_message,
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


def main() -> None:
    try:
        choice = display_menu_start()
        if choice == "1":
            nom_utilisateur = get_username()
            mot_de_passe = get_password()
            role = get_role()
            create_collaborateur(nom_utilisateur, mot_de_passe, role)
            user = authenticate_collaborateur(nom_utilisateur, mot_de_passe)
            if user:
                display_success_message("Création de compte réussie !")
                display_welcome_message(nom_utilisateur)
                handle_menu_options()
            else:
                display_error_message("Erreur lors de la création du compte.")
        elif choice == "2":
            nom_utilisateur = get_username()
            password = get_password()
            user = authenticate_collaborateur(nom_utilisateur, password)
            if user:
                display_welcome_message(nom_utilisateur)
                handle_menu_options()
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
