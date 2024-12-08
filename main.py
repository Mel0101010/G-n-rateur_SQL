import create, push, os


def interface():
    stop = True
    while stop:
        IN = -1
        while not (0 < IN < 6):
            print("\nQue voulez vous faire : ")
            print(
                "+---+-------------------+\n"
                "| # | Option            |\n"
                "+---+-------------------+\n"
                "| 1 | TEXT TO SQL       |\n"
                "| 2 | TEXT TO MCD       |\n"
                "| 3 | MCD TO SQL Table  |\n"
                "| 4 | EXEC              |\n"
                "| 5 | STOP              |\n"
                "+---+-------------------+")
            IN = int(input("votre réponse : "))
            os.system('clear')
        match IN:
            case 1:
                filename=input("\nNom du fichier : ")
                if filename == "":
                    filename = "main"
                choice = create.textinput(filename)
                choice.input_to_sql()
            case 2:
                filename=input("\nNom du fichier : ")
                if filename == "":
                    filename = "main"
                choice = create.textinput(filename)
                choice.input_to_mcd()
                os.system("mocodo -i "+filename+" -t arrange")
                os.system("rm "+filename+"_geo.json") #rajouter -f en cas de fichier toujours présent dans la corbeille
                print("\nUn fichier MCD et SVG viennent d'être créés")
            case 3:
                filename=input("\nNom du fichier : ")
                if filename == "":
                    filename = "main"
                choice = create.textinput(filename)
                choice.mcd_to_sql()
            case 4:
                execution()
            case 5:
                stop=False


def execution():
    IN = -1
    while not (0 < IN < 5):
        print("\nQue voulez vous faire : ")
        print(
            "+---+----------------+\n"
            "| # | Option         |\n"
            "+---+----------------+\n"
            "| 1 | Exec SQL       |\n"
            "| 2 | Exec MCD       |\n"
            "| 3 | Print Table    |\n"
            "| 4 | BACK           |\n"
            "+---+----------------+")
        IN = int(input("votre réponse : "))
        os.system('clear')
    match IN:
        case 1:
            filename=input("\nNom du fichier : ")
            if filename == "":
                filename = "main"
            choice = push.exect(filename)
            choice.sqlite_exec()
        case 2:
            filename=input("\nNom du fichier : ")
            if filename == "":
                filename = "main"
            choice = push.exect(filename)
            choice.exec_mcd()
        case 3:
            filename=input("\nNom du fichier : ")
            if filename == "":
                filename = "main"
            choice = push.exect(filename)
            choice.afficher()
        case 4:
            pass


interface()