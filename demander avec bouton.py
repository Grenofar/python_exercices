import tkinter as tk
from tkinter import messagebox

# Fonction appelée quand on clique sur "Valider"
def valider():
    nom = entree_nom.get()
    age = entree_age.get()

    if age.isdigit():  # Vérifie que c’est un nombre
        age = int(age)
        if age < 10:
            messagebox.showwarning("Trop jeune", f"Tu es trop jeune, désolé 😅")
        else:
            messagebox.showinfo("Bienvenue", f"Bonjour {nom}, tu as {age} ans ! 😎")
    else:
        messagebox.showerror("Erreur", "L'âge doit être un nombre !")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Formulaire simple")
fenetre.geometry("300x200")

# Label et champ pour le prénom
tk.Label(fenetre, text="Prénom :").pack()
entree_nom = tk.Entry(fenetre)
entree_nom.pack()

# Label et champ pour l’âge
tk.Label(fenetre, text="Âge :").pack()
entree_age = tk.Entry(fenetre)
entree_age.pack()

# Bouton pour valider
btn_valider = tk.Button(fenetre, text="Valider", command=valider)
btn_valider.pack(pady=10)

# Lancer l'application
fenetre.mainloop()
     
