import os, sqlite3


def afficher():
    files = input("Quel fichier : ")
    # Nom de la base de données temporaire
    db_temp = "temp_database.db"

    try:
        # Étape 1 : Créer une base de données SQLite temporaire
        connexion = sqlite3.connect(db_temp)
        curseur = connexion.cursor()

        # Lire le contenu du fichier SQL et filtrer les SELECT
        instructions = []
        with open(files, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne_str = ligne.strip()
                # Ignorer les lignes SELECT
                if ligne_str.upper().startswith("SELECT"):
                    continue
                instructions.append(ligne_str)

        # Joindre et exécuter les instructions filtrées
        script_filtre = "\n".join(instructions)
        curseur.executescript(script_filtre)
        connexion.commit()

        # Étape 2 : Récupérer toutes les tables
        curseur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = curseur.fetchall()

        if not tables:
            print("Aucune table trouvée dans le fichier SQL.")
        else:
            print("Tables et leur contenu :")
            # Étape 3 : Afficher le contenu de chaque table
            for table_name, in tables:
                print(f"\nTable : {table_name}")
                curseur.execute(f"SELECT * FROM {table_name};")
                rows = curseur.fetchall()

                # Récupérer les colonnes de la table
                colonnes = [desc[0] for desc in curseur.description]
                print(f"Colonnes : {', '.join(colonnes)}")

                # Afficher les données
                for row in rows:
                    print(row)

        # Fermer la connexion
        connexion.close()

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{files}' est introuvable.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        # Supprimer la base temporaire
        if os.path.exists(db_temp):
            os.remove(db_temp)


def input_to_sql():
    # Demande du nombre de tables
    files=input("Nom du fichier : ")
    if files == "":
        files = "main"

    
    nb_tab = int(input("Nombre de tables : "))

    # Initialisation du dictionnaire pour les tables
    tables = {}

    # Création des tables
    for t in range(nb_tab):
        table_name = input(f"Nom de la table {t + 1} : ")
        nb_col = int(input(f"Nombre de colonnes pour la table '{table_name}' : "))

        # Saisie des colonnes
        print(f"\nAjoutez les colonnes pour la table '{table_name}' :")
        columns = []
        for i in range(nb_col):
            col_name = input(f"Nom de la colonne {i + 1} : ")
            col_type = input(f"Type SQL de la colonne '{col_name}' (ex : INT, VARCHAR(255)) : ")
            columns.append((col_name, col_type))  # Stocker le nom et le type de la colonne

        # Saisie des lignes
        nb_line = int(input(f"Combien de lignes pour la table '{table_name}' ? "))
        rows = []
        for l in range(nb_line):
            print(f"\nAjoutez les données pour la ligne {l + 1} :")
            row = {}
            for col_name, _ in columns:
                value = input(f"Valeur pour la colonne '{col_name}' : ")
                # Ajout de guillemets pour les types texte
                if isinstance(value, str) and not value.isdigit():
                    value = f"'{value}'"
                row[col_name] = value
            rows.append(row)

        # Ajout de la table au dictionnaire
        tables[table_name] = {"columns": columns, "rows": rows}

    # Affichage du contenu des tables en SQL
    print("\n=== Instructions SQL ===")
    for table_name, table_data in tables.items():
        # Génération de la commande CREATE TABLE
        columns_sql = ", ".join([f"{col_name} {col_type}" for col_name, col_type in table_data["columns"]])
        print(f"CREATE TABLE {table_name} ({columns_sql});")
        f = open(files+".sql", "a")
        f.write(f"CREATE TABLE {table_name} ({columns_sql});\n")
        f.close

        # Génération des commandes INSERT INTO
        for row in table_data["rows"]:
            values_sql = ", ".join([str(row[col_name]) for col_name, _ in table_data["columns"]])
            print(f"INSERT INTO {table_name} VALUES ({values_sql});")
            f = open(files+".sql", "a")
            f.write(f"INSERT INTO {table_name} VALUES ({values_sql});\n")
            f.close


def input_to_mcd():
    # Demande du nombre de tables et de éléments
    files=input("Nom du fichier (sans extension) : ")
    if files == "":
        files = "main"
    
    nb_tab = int(input("Nombre de tables : "))
    nb_emt = int(input("Nombre de éléments par table (en moyenne) : "))


    # Initialisation du dictionnaire
    dico_table = {}

    # Saisie des noms de tables et initialisation des éléments
    for j in range(nb_tab):
        key = input(f"Nom de la table {j + 1} : ")  # Demande du nom de la table
        dico_table[key] = []  # Chaque table est associée à une liste de éléments

    # Ajout des éléments pour chaque table
    for table in dico_table:
        print(f"Ajoutez des éléments pour la table '{table}' :")
        for _ in range(nb_emt):
            emt = input(f"Éléments {_ + 1} : ")
            dico_table[table].append(emt)  # Ajout emt à la liste de la table

    # Création des liens entre les tables
    print("\nCréation des liens :")
    nb_link = int(input("Combien de liens voulez-vous créer ? "))
    dico_link = {}

    # Saisie des liens et des tables associées
    for h in range(nb_link):
        link_name = input(f"Nom du lien {h + 1} : ")
        dico_link[link_name] = []  # Chaque lien sera une liste de tables

    for link in dico_link:
        print(f"\nAjoutez des tables au lien '{link}' :")
        nb_related_tables = int(input(f"Combien de tables pour le lien '{link}' ? "))
        for _ in range(nb_related_tables):
            related_table = input("Nom de la table à ajouter : ")
            dico_link[link].append(related_table)  # Ajout de la table à la liste associée au lien

    # Affichage des liens et des tables associées
    print("\nDictionnaire des liens :")
    for link, tables in dico_link.items():
        liens_str = ", ".join(tables)  # Convertit la liste en une chaîne séparée par des virgules
        print(f"Lien {link}, {liens_str}")
        f = open(files+".mcd", "a")
        f.write(f"{link}, {liens_str}\n")
        f.close
    
    #Affichage des Tables et des éléments associés
    for tables, emt in dico_table.items():
        table_str=", ".join(emt)
        print(f"Tables {tables}: {table_str}")
        f = open(files+".mcd", "a")
        f.write(f"{tables}: {table_str}\n")
        f.close


def mcd_to_sql():
    files=input("Nom du fichier à exporter : ")
    base_name = os.path.splitext(files)[0]
    os.system('mocodo -i '+files+' -t sqlite\n') # Créer un fichier avec ddl dans le nom



def sqlite_exec():
    # Chemin du fichier SQL
    files=input("Quel est votre fichier : ")
    nom, extension=os.path.splitext(files)

    if extension.lower()==".sql":
        pass
    else:
        files=files+".sql"
    
    # Vérifier si le fichier existe
    if not os.path.exists(files):
        print(f"Erreur : le fichier {files} n'existe pas.")
        return

    # Connexion à une base de données SQLite en mémoire
    conn = sqlite3.connect(':memory:')  # Utilisation de la RAM uniquement
    cursor = conn.cursor()

    # Lire le contenu du fichier SQL
    try:
        with open(files, 'r') as file:
            sql_script = file.read()

        # Exécuter les commandes SQL du fichier
        try:
            cursor.executescript(sql_script)
            print("Script SQL exécuté avec succès.")
            
            # Afficher les résultats des requêtes SELECT du script
            print("\nRésultats des requêtes SELECT :")
            for statement in sql_script.split(';'):
                statement = statement.strip()
                if statement.upper().startswith("SELECT"):
                    try:
                        cursor.execute(statement)
                        rows = cursor.fetchall()
                        if rows:
                            print(f"\nRequête : {statement}")
                            for row in rows:
                                print(row)
                        else:
                            print(f"\nRequête : {statement} (Aucun résultat trouvé)")
                    except sqlite3.Error as e:
                        print(f"Erreur lors de l'exécution de la requête '{statement}' : {e}")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution du script SQL : {e}")
    except Exception as ex:
        print(f"Erreur lors de la lecture du fichier SQL : {ex}")
    finally:
        conn.close()
    
    print("\n")



def exec_mcd():
    files=input("Quel est votre fichier : ")
    os.system("mocodo --input "+files)


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
    stop = True
    while stop:
        IN = -1
        while not (0 < IN < 6):
            print("Que voulez vous faire : ")
            print("1: TEXT -> SQL\n2: TEXT -> MCD\n3: MCD -> SQL\n4: Exec\n5: Stop")
            IN = int(input("votre réponse : "))
        match IN:
            case 1:
                input_to_sql()
            case 2:
                input_to_mcd()
            case 3:
                mcd_to_sql()
            case 4:
                execution()
            case 5:
                stop=False


def execution():
    IN = -1
    while not (0 < IN < 5):
        print("Que voulez vous faire : ")
        print("1: Exec SQL\n2: Exec MCD\n3: None\n4: None")
        IN = int(input("votre réponse : "))
    match IN:
        case 1:
            sqlite_exec()
        case 2:
            exec_mcd()
        case 3:
            ...
        case 4:
            ...


afficher()