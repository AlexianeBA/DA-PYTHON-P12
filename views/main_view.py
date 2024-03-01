from rich.console import Console
from rich import print
from rich.table import Table


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


console = Console()

def display_welcome_message(nom_utilisateur):
    """
    Affiche un message de bienvenue personnalisé.

    Args:
        nom_utilisateur (str): Le nom d'utilisateur connecté.
    """
    console.print(f"Bienvenue,[bold green]{nom_utilisateur}[/bold green]")