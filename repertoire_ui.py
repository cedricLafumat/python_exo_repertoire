from repertoire_action import *

def saisie_menu():
    saisie_utilisateur = input(
        "\nQuel est votre choix?\n"
        "L pour Lister le répertoire\n"
        "A pour Ajouter un contact\n"
        "S pour Supprimer un contact\n"
        "R pour Rechercher un contact\n"
        "M pour Modifier le numéro d'un contact\n"
        "T pour Sortir du programme\n"
        "Choix : "
        ).upper()
    return saisie_utilisateur

def listing(repertoire):
    for contact in repertoire:
        print("Nom : '{}'\nNuméro de téléphone : '{}'\nMail : '{}'\n".format(contact["nom"], contact["numero"], contact["mail"]))

print(repertoire)

while True:
    repertoire = get_rep()
    saisie_utilisateur = saisie_menu()
    if saisie_utilisateur == "L":
        print("Vous avez choisi de lister le répertoire\n")
        listing(repertoire)

    elif saisie_utilisateur == "A":
        print("Vous avez choisi d'ajouter un contact\n")
        nom_a_ajouter = input("Ecrivez le nom du contact à ajouter : ").lower()
        numero_a_ajouter = input("Ecrivez le numéro du contact : ")
        mail_a_ajouter = input("Ecrivez l'adresse mail du contact : ")
        ajout = ajouter_personne(repertoire, nom_a_ajouter, numero_a_ajouter, mail_a_ajouter)

    elif saisie_utilisateur == "S":
        print("Vous avez choisi de supprimer un contact\n")
        nom_a_supprimer = input("Quel contact voulez-vous supprimer ? ").lower()
        suppression = supprimer_personne(repertoire, nom_a_supprimer)
        if suppression:
            print("\nContact supprimé")
        else:
            print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_supprimer))

    elif saisie_utilisateur == "R":
        print("Vous avez choisi de faire une recherche\n")
        nom_a_rechercher = input("Quel contact recherchez-vous ? ").lower()
        resultats = chercher_personnes(repertoire, nom_a_rechercher)
        if resultats:
            print("\nContact trouvé\n")
            listing(resultats)
        else:
            print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_rechercher))

    elif saisie_utilisateur == "M":
        print("Vous avez choisi de modifier le numéro d'un contact\n")
        nom_a_modifier = input("Quel contact voulez-vous modifier? ").lower()
        modification = modification_contact(repertoire, nom_a_modifier)
        if modification:
            print("\nModification effectué")
        else:
            print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_modifier))

    elif saisie_utilisateur == "T":
        exit()
