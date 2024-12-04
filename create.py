import os


class textinput():
    def __init__(self, filename):
        self.filename=filename

    def input_to_sql(self):
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
        f = open(self.filename+".sql", "a")
        print("\n=== Instructions SQL ===")
        for table_name, table_data in tables.items():
            # Génération de la commande CREATE TABLE
            columns_sql = ", ".join([f"{col_name} {col_type}" for col_name, col_type in table_data["columns"]])
            print(f"CREATE TABLE {table_name} ({columns_sql});")
            f.write(f"CREATE TABLE {table_name} ({columns_sql});\n")

            # Génération des commandes INSERT INTO
            for row in table_data["rows"]:
                values_sql = ", ".join([str(row[col_name]) for col_name, _ in table_data["columns"]])
                print(f"INSERT INTO {table_name} VALUES ({values_sql});")
                f.write(f"INSERT INTO {table_name} VALUES ({values_sql});\n")
        f.close


    def input_to_mcd(self):
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

        print("\nDictionnaire des liens :")
        f = open(self.filename+".mcd", "a")
        #Affichage des Tables et des éléments associés
        for tables, emt in dico_table.items():
            table_str=", ".join(emt)
            print(f"Tables {tables}: {table_str}")
            f.write(f"{tables}: {table_str}\n")

        # Affichage des liens et des tables associées
        for link, tables in dico_link.items():
            liens_str = ", ".join(tables)  # Convertit la liste en une chaîne séparée par des virgules
            print(f"Lien {link}, {liens_str}")
            f.write(f"{link}, {liens_str}\n")
        f.close

    def mcd_to_sql(self):
        os.system('mocodo -i '+self.filename+' -t sqlite\n') # Créer un fichier avec ddl dans le nom

