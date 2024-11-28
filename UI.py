import tkinter as tk
from tkinter import messagebox
import main

def execute_option(selection):
    """
    Exécute la fonction correspondant à l'option sélectionnée.
    """
    if selection == "Input to SQL":
        result = main.input_to_sql()
    elif selection == "Input to MCD":
        result = main.input_to_mcd()
    elif selection == "MCD to SQL":
        result = main.mcd_to_sql()
    else:
        result = "Aucune option valide sélectionnée."
    
    messagebox.showinfo("Résultat", result)

# Configuration de l'interface principale
def main_interface():
    root = tk.Tk()
    root.title("Interface Menu Python")

    # Taille de la fenêtre
    root.geometry("400x200")

    # Titre principal
    title = tk.Label(root, text="Menu Principal", font=("Arial", 18, "bold"))
    title.pack(pady=20)

    # Options disponibles
    options = ["Input to SQL", "Input to MCD", "MCD to SQL"]
    
    # Variable pour le menu déroulant
    selected_option = tk.StringVar()
    selected_option.set("Sélectionnez une option")

    # Menu déroulant
    dropdown_menu = tk.OptionMenu(root, selected_option, *options)
    dropdown_menu.config(font=("Arial", 14), width=20)
    dropdown_menu.pack(pady=10)

    # Bouton pour exécuter l'option sélectionnée
    execute_btn = tk.Button(root, text="Exécuter", font=("Arial", 14), 
                            command=lambda: execute_option(selected_option.get()))
    execute_btn.pack(pady=10)

    # Bouton pour quitter
    quit_btn = tk.Button(root, text="Quitter", font=("Arial", 14), command=root.quit, bg="red", fg="white")
    quit_btn.pack(pady=20)

    root.loop()

main_interface()
