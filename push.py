import os, sqlite3


class exect():
    def __init__(self, filename):
        self.filename=filename

    def afficher(self):
        nom, extension=os.path.splitext(self.filename)

        if extension.lower()==".sql":
            pass
        else:
            self.filename=self.filename+".sql"
        # Nom de la base de données temporaire
        db_temp = "temp_database.db"

        try:
            # Étape 1 : Créer une base de données SQLite temporaire
            connexion = sqlite3.connect(db_temp)
            curseur = connexion.cursor()

            # Lire le contenu du fichier SQL et filtrer les SELECT
            instructions = []
            with open(self.filename, "r", encoding="utf-8") as f:
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
            print(f"Erreur : Le fichier '{self.filename}' est introuvable.")
        except sqlite3.Error as e:
            print(f"Erreur SQLite : {e}")
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            # Supprimer la base temporaire
            if os.path.exists(db_temp):
                os.remove(db_temp)




    def sqlite_exec(self):
        nom, extension=os.path.splitext(self.filename)

        if extension.lower()==".sql":
            pass
        else:
            self.filename=self.filename+".sql"
        
        # Vérifier si le fichier existe
        if not os.path.exists(self.filename):
            print(f"Erreur : le fichier {self.filename} n'existe pas.")
            return

        # Connexion à une base de données SQLite en mémoire
        conn = sqlite3.connect(':memory:')  # Utilisation de la RAM uniquement
        cursor = conn.cursor()

        # Lire le contenu du fichier SQL
        try:
            with open(self.filename, 'r') as file:
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



    def exec_mcd(self):
        os.system("mocodo --input "+self.filename+" -t arrange --output_dir ./filescreated")
