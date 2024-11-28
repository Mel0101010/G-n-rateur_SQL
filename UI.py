import tkinter as tk
from tkinter import ttk
import main

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple d'interface Tkinter")
root.geometry("1080x720")

#root.config(bg="lightblue")  # Couleur de fond de la fenêtre principale

# Fonction pour récupérer les valeurs
def afficher_valeurs():
    input_text = entry.get()  # Récupère le texte de l'input
    selected_option = combo.get()  # Récupère l'option sélectionnée dans le menu déroulant
    label_resultat.config(text=f"Name: {input_text}\nConvert: {selected_option}")

# Champ de saisie (input)
entry_label = tk.Label(root, text="Entrez quelque chose:")
entry_label.pack(pady=10)

entry = tk.Entry(root, bg="gray")  # Couleur de fond du champ de saisie
entry.pack(pady=5)

# Menu déroulant (Combobox)
combo_label = tk.Label(root, text="Choisissez une convertion:")
combo_label.pack(pady=10)

options = ["Info -> SQL", "Info -> MCD", "MCD -> SQL"]


if options == 'Info -> SQL':
    action = main.input_to_sql()

elif options == 'Info -> MCD':
    action = main.input_to_mcd()

elif options == 'MCD -> SQL':
    action = main.mcd_to_sql()


combo = ttk.Combobox(root, values=options, state="readonly")
combo.pack(pady=5)

# Bouton pour afficher les valeurs
button = tk.Button(root, text="Afficher", command=action)
button.pack(pady=20)

# Label pour afficher les résultats
label_resultat = tk.Label(root, text="Résultat affiché ici")
label_resultat.pack(pady=10)

# Lancement de l'application
root.mainloop()
