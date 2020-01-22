#import repertoire_utils_dict as repertoire_utils
import repertoire_utils_text as repertoire_utils

repertoire = repertoire_utils.get_rep()

def ajouter_personne(repertoire, nom=None, telephone=None, mail=None):
    if not verif_presence(repertoire, telephone):
        personne = {"nom" : nom, "telephone" : telephone, "mail" : mail}
        repertoire_utils.append_rep(repertoire, personne)
    return repertoire

def verif_presence(repertoire, numero):
    for contact in repertoire:
        if contact["telephone"] == numero:
            return True
    return False

def supprimer_personne(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            repertoire_utils.del_rep(repertoire, contact)
    return repertoire

def chercher_personnes(repertoire, nom=None, telephone=None, mail=None):
    resultats = []
    for contact in repertoire:
        if contact["nom"] == nom:
            ajouter_personne(resultats, contact["nom"], contact["telephone"], contact["mail"])
    return resultats

def modification_contact(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            numero_a_modifier = input("Nouveau numéro : ")
            contact["numero"] = numero_a_modifier
            return True
    return False