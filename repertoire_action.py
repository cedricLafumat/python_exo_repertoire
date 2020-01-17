def ajout_contact(repertoire, nom, numero, mail):
    if verif_presence(repertoire, nom):
        return False
    else:
        repertoire.append({"nom" : nom, "numero" : numero, "mail" : mail})
        return True

def verif_presence(repertoire, nom):
    presence_contact = False
    for contact in repertoire:
        if contact["nom"] == nom:
            presence_contact = True
            break
    return presence_contact

def suppression_contact(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            repertoire.remove(contact)
            return True
    return False

def recherche_contact(repertoire, nom):
    resultats = []
    for contact in repertoire:
        if contact["nom"] == nom:
            ajout_contact(resultats, contact["nom"], contact["numero"], contact["mail"])
    return resultats

def modification_contact(repertoire, nom):
    for contact in repertoire:
        if contact["nom"] == nom:
            numero_a_modifier = input("Nouveau numéro : ")
            contact["numero"] = numero_a_modifier
            return True
    return  False