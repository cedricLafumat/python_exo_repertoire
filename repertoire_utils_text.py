import json

def get_rep():
    repertoire = open("repertoire.json", "r")
    retour = json.loads(repertoire.read())
    repertoire.close()
    return retour

def append_rep(repertoire, personne):
    repertoire.append(personne)
    fichier = open("repertoire.json", "w")
    fichier.write(json.dumps(repertoire))
    fichier.close()
    return repertoire

def del_rep(repertoire, personne):
    repertoire.remove(personne)
    fichier = open("repertoire.json", "w")
    fichier.write(json.dumps(repertoire))
    fichier.close()
    return repertoire

def lister_tous_les_contacts(repertoire):
    liste_contacts = []
    for contact in repertoire:
        liste_contacts.append(contact)
    return liste_contacts