import create, push, os

os.system('clear')
def interface():
    while True:
        IN = -1
        while not (0 < IN < 7):
            print("\nQue voulez vous faire : ")
            print(
                "+---+-------------------+\n"
                "| # | Option            |\n"
                "+---+-------------------+\n"
                "| 1 | TEXT TO SQL       |\n"
                "+---+-------------------+\n"
                "| 2 | TEXT TO MCD       |\n"
                "+---+-------------------+\n"
                "| 3 | MCD TO SQL        |\n"
                "+---+-------------------+\n"
                "| 4 | CSV TO SQL        |\n"
                "+---+-------------------+\n"
                "| 5 | RUN FILES         |\n"
                "+---+-------------------+\n"
                "| 6 | STOP              |\n"
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
                os.system("mocodo -i ./filescreated/"+filename+" -t arrange")
                os.remove('./filescreated/'+filename+'_geo.json')
                os.remove('./filescreated/'+filename+'.svg')
            case 3:
                filename=input("\nNom du fichier : ")
                if filename == "":
                    filename = "main"
                choice = create.textinput(filename)
                choice.mcd_to_sql()
                os.remove('./filescreated/'+filename+'_geo.json')
                os.remove('./filescreated/'+filename+'.svg')
            case 4:
                filename=input("\nNom du fichier : ")
                if filename == "":
                    filename = "main"
                choice = create.textinput(filename)
                choice.csv_to_sql()
            case 5:
                execution()
            case _:
                return


def execution():
    IN = -1
    while not (0 < IN < 5):
        print("\nQue voulez vous faire : ")
        print(
            "+---+---------------+\n"
            "| # | Option        |\n"
            "+---+---------------+\n"
            "| 1 | RUN SQL       |\n"
            "+---+---------------+\n"
            "| 2 | RUN MCD       |\n"
            "+---+---------------+\n"
            "| 3 | VIEW TABLE    |\n"
            "+---+---------------+\n"
            "| 4 | LOOK BACK     |\n"
            "+---+---------------+")
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
            os.remove('./filescreated/'+filename+'_geo.json')
        case 3:
            filename=input("\nNom du fichier : ")
            if filename == "":
                filename = "main"
            choice = push.exect(filename)
            choice.afficher()
        case 4:
            pass


interface()
