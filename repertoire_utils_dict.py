# repertoire = [{
#     "nom" : "toto",
#     "telephone" : "0605040302",
#     "mail" : "toto@campus"
#     },{
#     "nom" : "tata",
#     "telephone" : "0102030405",
#     "mail" : "tata@campus"
#     }
]

# def get_rep():
#     return repertoire

# def append_rep(repertoire, personne):
#     repertoire.append({"nom" : personne.get("nom"), "telephone" : personne.get("telephone"),
#                        "mail" : personne.get("mail")})

def del_rep(repertoire, personne):
    repertoire.remove(personne)