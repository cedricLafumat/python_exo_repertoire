#import repertoire_utils_dict as repertoire_utils
import repertoire_utils_text as repertoire_utils

#repertoire = repertoire_utils.get_rep()

def lister_tous_les_contacts(repertoire):
    return repertoire_utils.lister_tous_les_contacts(repertoire)

def ajouter_personne(repertoire, nom=None, telephone=None, mail=None):
    if not verif_presence(repertoire, telephone):
        personne = {"nom" : nom, "telephone" : telephone, "mail" : mail}
        repertoire_utils.append_rep(repertoire, personne)
    return repertoire

def verif_presence(repertoire, numero):
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if contact["telephone"] == numero:
            return True
    return False

def supprimer_personne(repertoire, nom):
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if contact["nom"] == nom:
            repertoire_utils.del_rep(repertoire, contact)
    return repertoire

def chercher_personnes(repertoire, nom=None, telephone=None, mail=None):
    resultats = []
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if contact["nom"] == nom:
            resultats.append(contact)
    return resultats

def modification_contact(repertoire, nom, numero):
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if contact["nom"] == nom:
            contact["numero"] = numero
            return True
    return False