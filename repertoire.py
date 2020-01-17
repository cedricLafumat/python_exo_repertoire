repertoire = [{
    "nom" : "toto",
    "numero" : "0605040302",
    "mail" : "toto@campus"
    },{
    "nom" : "tata",
    "numero" : "0102030405",
    "mail" : "tata@campus"
    }
]

print(repertoire[0], repertoire[1])


def saisie_menu():
    saisie_utilisateur = input(
        "\nQuel est votre choix?\n"
        "L pour Lister le répertoire\n"
        "A pour Ajouter un contact\n"
        "S pour Supprimer un contact\n"
        "R pour Rechercher un contact\n"
        "M pour Modifier le numéro d'un contact\nChoix : "
        ).upper()
    return saisie_utilisateur

def listing(repertoire):
    for contact in repertoire:
        print("Nom : {}\nNuméro de téléphone : {}\n@ : {}\n".format(contact["nom"], contact["numero"], contact["mail"]))

def ajout_contact(repertoire, nom, numero, mail):
    presence_contact = verif_presence(repertoire, nom)
    if presence_contact == True:
        print("\n{} est déjà présent dans le répertoire".format(nom))
    else:
        repertoire.append({"nom" : nom, "numero" : numero, "mail" : mail})

def suppression_contact(repertoire, nom):
    presence_contact = verif_presence(repertoire, nom)
    if presence_contact == True:
        del repertoire[nom]
        print("\nContact supprimé")
    else:
        print("\n{} n'est pas présent dans le répertoire".format(nom))

def recherche_contact(repertoire, nom):
    rech_contact = {}
    for nom_rech, telephone in repertoire.items():
        if nom_rech == nom:
            ajout_contact(rech_contact, nom_rech, telephone)
    return rech_contact

def modification_contact(repertoire, nom):
    presence_contact = verif_presence(repertoire, nom)
    if presence_contact == True:
        numero_a_modifier = input("Nouveau numéro : ")
        repertoire[nom] = numero_a_modifier
    else:
        print("\n{} n'est pas présent dans le répertoire".format(nom))

def verif_presence(repertoire, nom):
    presence_contact = False
    for contact in repertoire:
        if contact["nom"] == nom:
            presence_contact = True
            break
    return presence_contact

while True:
    saisie_utilisateur = saisie_menu()
    if saisie_utilisateur == "L":
        print("Vous avez choisi de lister le répertoire\n")
        listing(repertoire)
    elif saisie_utilisateur == "A":
        print("Vous avez choisi d'ajouter un contact\n")
        nom_a_ajouter = input("Ecrivez le nom du contact à ajouter : ").lower()
        numero_a_ajouter = input("Ecrivez le numéro du contact : ")
        mail_a_ajouter = input("Ecrivez l'adresse mail du contact : ")
        ajout_contact(repertoire, nom_a_ajouter, numero_a_ajouter, mail_a_ajouter)
    elif saisie_utilisateur == "S":
        print("Vous avez choisi de supprimer un contact\n")
        nom_a_supprimer = input("Quel contact voulez-vous supprimer ? ").lower()
        suppression_contact(repertoire, nom_a_supprimer)
    elif saisie_utilisateur == "R":
        print("Vous avez choisi de faire une recherche\n")
        nom_a_rechercher = input("Quel contact recherchez-vous ? ").lower()
        resultat_recherche = recherche_contact(repertoire, nom_a_rechercher)
        listing(resultat_recherche)
    elif saisie_utilisateur == "M":
        print("Vous avez choisi de modifier le numéro d'un contact\n")
        nom_a_modifier = input("Quel contact voulez-vous modifier? ").lower()
        modification_contact(repertoire, nom_a_modifier)
