from views.main_view import console
from rich.prompt import Prompt

def display_menu_start()-> str:
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

def display_menu()-> str:
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
    console.print("12. Afficher la liste de tous les clients classés par ordre alphabétique")
    console.print("13. Afficher la liste de tous les collaborateurs classés par ordre alphabétique")
    console.print("14. Afficher la liste de tous les contrats classés par statut")
    console.print("15. Afficher la liste de tous les événements classés par date")
    console.print("16. Afficher la liste de tous les événements passés")
    console.print("17. Afficher la liste de tous les événements à venir")
    console.print("[red]exit. Quitter")
    console.rule(style="bright_yellow")
    return Prompt.ask("Entrez votre choix ")

