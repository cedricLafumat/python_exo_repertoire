import repertoire_action as action

def saisie_menu():
    saisie_utilisateur = input(
        "\nQuel est votre choix?\n"
        "L pour Lister le répertoire\n"
        "A pour Ajouter un contact\n"
        "S pour Supprimer un contact\n"
        "R pour Rechercher un contact\n"
        "M pour Modifier le numéro d'un contact\n"
        "Q pour Quitter le programme\n"
        "Choix : "
        ).upper()
    return saisie_utilisateur

def afficher_repertoire(repertoire):
    liste_contact = action.lister_tous_les_contacts(repertoire)
    afficher_contact(liste_contact)

def afficher_contact(liste_contact):
    for contact in liste_contact:
        print("Nom : '{}'\nNuméro de téléphone : '{}'\nMail : '{}'\n".format(contact["nom"], contact["telephone"], contact["mail"]))

def saisie_ajout_contact():
    nom_a_ajouter = input("Ecrivez le nom du contact à ajouter : ").lower()
    numero_a_ajouter = input("Ecrivez le numéro du contact : ")
    mail_a_ajouter = input("Ecrivez l'adresse mail du contact : ")
    action.ajouter_personne(repertoire, nom_a_ajouter, numero_a_ajouter, mail_a_ajouter)

def saisie_supprimer_contact():
    nom_a_supprimer = input("Quel contact voulez-vous supprimer ? ").lower()
    contacts = action.chercher_personnes(repertoire, nom_a_supprimer)
    if len(contacts) == 1:
        action.supprimer_personne(repertoire, nom_a_supprimer)
        print("\nContact supprimé")
    elif len(contacts) > 1:
        afficher_contact(contacts)
        liste_suppression = []
        telephone_contact = input("Saisissez le numéro du contact à supprimer : ")
        for contact in contacts:
            if contact["telephone"] == telephone_contact:
                liste_suppression.append(contact)
                action.supprimer_personne(repertoire, nom_a_supprimer)
                print("\nContact supprimé")
    else:
        print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_supprimer))

def saisie_rechercher_contact():
    nom_a_rechercher = input("Quel contact recherchez-vous ? ").lower()
    resultats = action.chercher_personnes(repertoire, nom_a_rechercher)
    if resultats:
        print("\nContact trouvé\n")
        afficher_contact(resultats)
    else:
        print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_rechercher))

def saisie_modifier_contact():
    nom_a_modifier = input("Quel contact voulez-vous modifier? ").lower()
    numero_a_modifier = input("Nouveau numéro : ")
    modification = action.modification_contact(repertoire, nom_a_modifier, numero_a_modifier)
    if modification:
        print("\nModification effectué")
    else:
        print("\n'{}' n'est pas présent dans le répertoire".format(nom_a_modifier))

while True:
    repertoire = action.repertoire_utils.get_rep()
    saisie_utilisateur = saisie_menu()
    if saisie_utilisateur == "L":
        print("Vous avez choisi de lister le répertoire\n")
        afficher_repertoire(repertoire)

    elif saisie_utilisateur == "A":
        print("Vous avez choisi d'ajouter un contact\n")
        saisie_ajout_contact()

    elif saisie_utilisateur == "S":
        print("Vous avez choisi de supprimer un contact\n")
        saisie_supprimer_contact()

    elif saisie_utilisateur == "R":
        print("Vous avez choisi de faire une recherche\n")
        saisie_rechercher_contact()

    elif saisie_utilisateur == "M":
        print("Vous avez choisi de modifier le numéro d'un contact\n")
        saisie_modifier_contact()

    elif saisie_utilisateur == "Q":
        print("Vous avez choisi de quitter le programme")
        exit()
