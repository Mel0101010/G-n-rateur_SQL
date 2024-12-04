import create, push, os


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
                os.system("rm "+filename+"_geo.json")
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
        print("Que voulez vous faire : ")
        print("1: Exec SQL\n2: Exec MCD\n3: Print Table\n4: None")
        IN = int(input("votre réponse : "))
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
            ...


"""
files=input("Nom du fichier : ")
        if files == "":
            files = "main"
"""
# À mettre dans les case


interface()