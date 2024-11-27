class Table:
    def __init__(self, nom, attributs):
        self.nb_attributs = attributs
        self.nom = nom
        self.attributs = []
        for i in range(attributs):
            elt = input(f"Nom de l'attribut n°{i+1}")
            self.attributs.append(elt)
        self.nb_entree = 0
        self.entities = [self.attributs]


    def ajouter(self, attribut): # ajoute un attribut à la fin de la table
        self.entities.append(attribut) # faut typer ses attributs
        self.nb_entree+=1
    
    def retirer(self): # retirer le dernier attribut ajouté
        self.entities.pop()
        self.nb_entree-=1

    def afficher(self): # affiche une table non nulle || faire cette fonction la prochaine fois
        longueur_max = taille_ligne(self.entities) + 1 + self.nb_attributs
        print("-"*longueur_max)
        print('|' + self.nom + '|')
        print("-"*longueur_max)
        
        for i in range(len(self.entities)):
            line = "|"
            for j in range(len(self.entities[i])):
                line = line + str(self.entities[i][j]) + '|'
            print(line)
            print("-" * longueur_max)
            

class List_Tables:
    def __init__(self):
        self.taille = 0
        self.liste = []
    
    def ajouter_table(self, table):
        self.taille +=1
        self.liste.append(table)

    def retirer_table(self, table):
        self.taille-=1
        self.liste.pop()

def Input_to_SQL(tableau):
    nom = input("Nom du tableau : ")
    taille = int(input("nombres d'attributs : "))
    table = Table(nom, taille)
    entity = []
    for i in range(taille): # permet d'ajouter une ligne
        attribut = input(f"ligne 1 : attribut n° {i+1} : ")
        entity.append(attribut)
    table.ajouter(entity)
    table.afficher()


def Input_to_mcd():
    # Demande du nombre de tables et de liens
    nb_tab = int(input("Nombre de tables : "))
    nb_emt = int(input("Nombre de liens par table (en moyenne) : "))

    # Initialisation du dictionnaire
    dico = {}

    # Saisie des noms de tables et initialisation des liens
    for j in range(nb_tab):
        key = input(f"Nom de la table {j + 1} : ")  # Demande du nom de la table
        dico[key] = []  # Chaque table est associée à une liste de liens

    # Ajout des liens pour chaque table
    for table in dico:
        print(f"Ajoutez des éléments pour la table '{table}' :")
        for _ in range(nb_emt):
            emt = input(f"Éléments {_ + 1} : ")
            dico[table].append(emt)  # Ajout du lien à la liste de la table

    # Affichage du dictionnaire final
    print("\nDictionnaire des tables et leurs éléments :")
    for table, emts in dico.items():
        print(f"{table} : {emts}")



def taille_ligne(tab): 
    """
    prend en entree un tableau 2D et renvoie la taille de la ligne la plus grande. -- utile dans Table.afficher
    """
    res = 0
    for ligne in tab:
        len_line = 0
        for inp in ligne:
            len_line+=len(inp)
        res = max(res, len_line)
    return res

def interface():
    liste_tables = List_Tables()
    IN = -1
    while not (0 < IN < 5):
        print("Que voulez vous faire :")
        print("1: info -> SQL\n2: info -> mcd...\n")
        IN = int(input("votre réponse : "))
    match IN:
        case 1:
            Input_to_SQL(liste_tables)
        case 2:
            Input_to_mcd()
        case _:
            pass

"""

    to do list :
    - Fix table.ajouter et table.retirer
    - faire Input_to_SQL
    - faire Interface
    - faire dico des liens
"""

interface()
