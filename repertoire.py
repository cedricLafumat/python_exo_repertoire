repertoire = {
    "toto" : "0601020304",
    "tata" : "0706050403"
}

def saisie_menu():
    saisie_utilisateur = input(
        "\nQuel est votre choix?\nL pour Lister le répertoire\nA pour Ajouter un contact\nS pour Supprimer un contact\nR pour Rechercher un contact\nChoix : ")
    return saisie_utilisateur

def listing(repertoire):
    for nom, telephone in repertoire.items():
        print("Nom : {}\nNuméro de téléphone : {}".format(nom, telephone))

def ajout_contact(repertoire, nom, numero):
    repertoire[nom] = numero

def suppression_contact(repertoire, nom):
    del repertoire[nom]

def recherche_contact(repertoire, nom):
    rech_contact = {}
    for nom_rech, telephone in repertoire.items():
        if nom_rech == nom:
            ajout_contact(rech_contact, nom_rech, telephone)
    return rech_contact

while True:
    saisie_utilisateur = saisie_menu()
    if saisie_utilisateur == "L":
        print("Vous avez choisi de lister le répertoire\n")
        listing(repertoire)
    elif saisie_utilisateur == "A":
        print("Vous avez choisi d'ajouter un contact\n")
        nom_a_ajouter = input("Ecrivez le nom du contact à ajouter : ")
        numero_a_ajouter = input("Ecrivez le numéro du contact : ")
        ajout_contact(repertoire, nom_a_ajouter, numero_a_ajouter)
    elif saisie_utilisateur == "S":
        print("Vous avez choisi de supprimer un contact\n")
        nom_a_supprimer = input("Quel contact voulez-vous supprimer ? ")
        suppression_contact(repertoire, nom_a_supprimer)
    elif saisie_utilisateur == "R":
        print("Vous avez choisi de faire une recherche\n")
        nom_a_rechercher = input("Quel contact recherchez-vous ? ")
        resultat_recherche = recherche_contact(repertoire, nom_a_rechercher)
        listing(resultat_recherche)
