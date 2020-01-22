repertoire = [{
    "nom" : "toto",
    "numero" : "0605040302",
    "mail" : "toto@campus"
    },{
    "nom" : "toto",
    "numero" : "0102030405",
    "mail" : "tata@campus"
    }
]

def ajouter_personne(repertoire, nom=None, telephone=None, mail=None):
    if not verif_presence(repertoire, telephone):
        repertoire.append({"nom" : nom, "numero" : telephone, "mail" : mail})
    return repertoire

def verif_presence(repertoire, numero):
    for contact in repertoire:
        if contact["numero"] == numero:
            return True
    return False

def supprimer_personne(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            repertoire.remove(contact)
    return repertoire

def chercher_personnes(repertoire, nom=None, telephone=None, mail=None):
    resultats = []
    for contact in repertoire:
        if contact["nom"] == nom:
            ajouter_personne(resultats, contact["nom"], contact["numero"], contact["mail"])
    return resultats

def modification_contact(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            numero_a_modifier = input("Nouveau numéro : ")
            contact["numero"] = numero_a_modifier
            return True
    return False

def get_rep():
    return repertoire