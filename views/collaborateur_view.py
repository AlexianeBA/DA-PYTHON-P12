import getpass
import datetime
from typing import Any, Dict, List
from rich.table import Table
from models.collaborateur import Collaborateur
from views.main_view import console
from controllers.collaborateur_controlleur import get_all_commercial


def get_username() -> str:
    """
    Demande et renvoie le nom d'utilisateur entré par l'utilisateur.

    Returns:
        str: Le nom d'utilisateur saisi.
    """
    return input("Nom d'utilisateur : ")


def get_password() -> str:
    """
    Demande et renvoie le mot de passe entré par l'utilisateur (avec masquage).

    Returns:
        str: Le mot de passe saisi.
    """
    return getpass.getpass("Mot de passe : ")


def get_role() -> str:
    """
    Demande et renvoie le rôle défini par l'utilisateur.

    Returns:
        str: Le rôle choisi par l'utilisateur.
    """
    return input("Définissez votre rôle: commercial, gestion ou support: ")


def update_collaborateur_view(
    collaborateur_id: int, current_values: Any
) -> Dict[str, str]:
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


def display_list_of_collaborateurs(collaborateurs: List[Collaborateur]) -> None:
    """
    Affiche la liste des collaborateurs.

    Args:
        collaborateurs (list): La liste des collaborateurs à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID utilisateur")
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


def display_list_of_commercial() -> None:
    """
    Affiche la liste de tous les commerciaux disponibles.
    """
    commercials = get_all_commercial()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID commercial")
    table.add_column("Nom d'utilisateur du commercial")

    for commercial in commercials:
        table.add_row(
            str(commercial.id),
            commercial.nom_utilisateur,
        )

    print("Voici la liste des commerciaux chez Epicevents :")
    console.print(table)
