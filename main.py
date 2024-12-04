import os, sqlite3
import create, push


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
                create.input_to_sql()
            case 2:
                create.input_to_mcd()
            case 3:
                create.mcd_to_sql()
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
            push.sqlite_exec()
        case 2:
            push.exec_mcd()
        case 3:
            push.afficher()
        case 4:
            ...


interface()