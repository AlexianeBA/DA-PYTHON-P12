from typing import Any, Dict, List, Tuple
from controllers.client_controller import get_client_by_id
from controllers.collaborateur_controlleur import get_collaborateur_id_connected, get_support_name
from controllers.contract_controller import get_contracts_filter_by_collaborateur
import datetime
from rich.table import Table
from models.contract import Contract
from views.main_view import console
from views.collaborateur_view import display_list_of_commercial
def get_contract_details(client_id: int) -> Tuple[int, int, int, str, str, str]:
    """
    Récupère automatiquement les détails du contrat en fonction de l'ID du client et du collaborateur connecté.

    Args:
        client_id (int): L'identifiant du client associé au contrat.

    Returns:
        tuple: Les détails du contrat.
    """
    collaborateur_id, _ = get_collaborateur_id_connected()
    client = get_client_by_id(client_id)

    if client and collaborateur_id:
        display_list_of_commercial()
        contact_commercial = input("Entrez l'id du commercial auquel sera rattacher le contrat")
        montant_total = input("Entrez le montant total en € : ")
        montant_restant_a_payer = input("Montant restant à payer en € : ")
        statut_contrat = input("Renseigner le statut du contrat (en cours ou terminé) : ")

        return (
            client_id,
            contact_commercial,
            collaborateur_id,
            montant_total,
            montant_restant_a_payer,
            statut_contrat,
        )
    else:
        raise ValueError("Impossible de récupérer les détails du contrat. Veuillez vous assurer que le client existe et qu'un collaborateur est connecté.")


def update_contract_view(contract_id: int,current_values: Any) -> Dict[str, str]:
    """
    Affiche la vue de mise à jour du contrat.

    Args:
        contract_id (int): L'identifiant du contrat à mettre à jour.
        current_values (Contract): Les valeurs actuelles du contrat.

    Returns:
        dict: Les nouvelles valeurs saisies pour le contrat.
    """
    new_values = {}

    print(
        "Entrez les nouvelles valeurs pour le contrat (laissez vide pour conserver les valeurs actuelles) :"
    )

    new_values["client_id"] = (
        input(f"Nouvel identifiant du client ({current_values.client_id}): ")
        or current_values.client_id
    )
    new_values["contact_commercial"] = (
        input(f"Nouveau contact commercial ({current_values.contact_commercial}): ")
        or current_values.contact_commercial
    )
    new_values["montant_total"] = (
        input(f"Nouveau montant ({current_values.montant_total}): ")
        or current_values.montant_total
    )
    new_values["montant_restant_a_payer"] = (
        input(
            f"Nouveau montant restant à payer ({current_values.montant_restant_a_payer}): "
        )
        or current_values.montant_restant_a_payer
    )
    new_values["statut_contrat"] = (
        input(f"Nouveau statut du contrat ({current_values.statut_contrat}):")
        or current_values.statut_contrat
    )
    return new_values


def display_list_of_contracts(contracts: List[Contract]) -> None:
    """
    Affiche la liste des contrats.

    Args:
        contrats (list): La liste des contrats à afficher.
    """
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du client concerné")
    table.add_column("Nom du contact commercial")
    table.add_column("Nom du support")
    table.add_column("ID du contrat")
    table.add_column("Montant total à payer en €")
    table.add_column("Montant restant à payer en €")
    table.add_column("Statut du contrat")

    for contract in contracts:
        
        support_name = get_support_name(contract.collaborateur_id)

        table.add_row(
            str(contract.client_id),
            contract.contact_commercial,
            support_name, 
            str(contract.id),
            f"{str(contract.montant_total)} €",
            f"{str(contract.montant_restant_a_payer)} €",
            contract.statut_contrat
        )
    print("Voici la liste des contrats classés par prix croissant chez Epicevents: ")
    console.print(table)

def display_contracts_of_collaborateur_connected()-> List[Contract]:
    """
    Affiche les contrats du collaborateur connecté.
    """
    collaborateur_id = get_collaborateur_id_connected()
    contracts = get_contracts_filter_by_collaborateur(collaborateur_id)
    print(collaborateur_id)
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID du contrat")
    table.add_column("ID du client")
    table.add_column("Contact commercial")
    table.add_column("ID du commercial")
    table.add_column("Montant total")
    table.add_column("Montant restant à payer")
    table.add_column("Statut du contrat")
    for contract in contracts:
        table.add_row(
            str(contract.id),
            str(contract.client_id),
            contract.contact_commercial,
            str(contract.collaborateur_id),
            f"{str(contract.montant_total)} €",
            f"{str(contract.montant_restant_a_payer)} €",
            contract.statut_contrat,
        )
    print("Liste de vos contrats: ")
    console.print(table)
   