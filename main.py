import datetime
import sys
from controllers.client_controller import create_client
from controllers.user_controller import authenticate_user
from controllers.contract_controller import create_contract
from db_config import Session


def main():
    print("Veuillez vous connecter:")
    nom_utilisateur = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    user = authenticate_user(nom_utilisateur, password)
    if user:
        print("Connexion réussie! Bienvenue,")
        action = input(
            "Que souhaitez-vous faire ? Tapez 1 pour créer un client ou 2 pour créer un contrat: ",
        )
        if action == "1":
            nom_complet = input("Entrez le nom complet du client : ")
            email = input("Entrez l'email du client : ")
            telephone = input("Entrez le numéro de téléphone du client : ")
            nom_entreprise = input("Entrez le nom de l'entreprise du client : ")
            date_de_creation = datetime.date.today()
            dernière_maj_contact = datetime.date.today()
            contact_commercial_chez_epic_events = input(
                "Entrez le nom du contact commercial chez Epic Events : "
            )

            nouveau_client = create_client(
                nom_complet=nom_complet,
                email=email,
                telephone=telephone,
                nom_entreprise=nom_entreprise,
                date_de_creation=date_de_creation,
                dernière_maj_contact=dernière_maj_contact,
                contact_commercial_chez_epic_events=contact_commercial_chez_epic_events,
            )

            with Session() as session:
                try:
                    session.add(nouveau_client)
                    session.commit()
                    print("Client ajouté avec succès !")
                except Exception as e:
                    session.rollback()
                    print(f"Erreur lors de l'ajout du client : {e}")
        elif action == "2":
            client_id = input("Entrez le numéro de l'identifiant du client: ")
            client = input("Entrez le nom complet du client: ")
            contact_commercial = input("Entrez votre identifiant: ")
            montant_total = input("Entrez le montant total en €: ")
            montant_restant_a_payer = input("Montant restant à payer en €: ")
            statut_contrat = input(
                "Renseigner le statut du contrat (en cours ou terminé): "
            )

            nouveau_contrat = create_contract(
                client_id=client_id,
                client=client,
                contact_commercial=contact_commercial,
                montant_total=montant_total,
                montant_restant_a_payer=montant_restant_a_payer,
                statut_contrat=statut_contrat,
            )

            with Session() as session:
                try:
                    session.add(nouveau_contrat)
                    session.commit()
                    print("Contrat créé avec succès !")
                except Exception as e:
                    session.rollback()
                    print(f"Erreur lors de l'ajout du contrat : {e}")
        elif action == "exit":
            print("au revoir")
            sys.exit()
        else:
            print("Option non valide. Veuillez réessayer.")
    else:
        print("Adresse e-mail ou mot de passe incorrect.")


if __name__ == "__main__":
    main()
