import tkinter as tk
import random

def afficher_page2():
    frame_page1.pack_forget()
    frame_page2.pack(fill="both", expand=True)

def afficher_page3():
    frame_page2.pack_forget()
    frame_page3.pack(fill="both", expand=True)

def afficher_page4():
    frame_page2.pack_forget()
    frame_page4.pack(fill="both", expand=True)

def afficher_page_devine():
    frame_page4.pack_forget()
    frame_devine.pack(fill="both", expand=True)
    nouvelle_partie()

def afficher_page5():
    frame_page2.pack_forget()
    frame_page5.pack(fill="both", expand=True)

def afficher_addition():
    frame_page5.pack_forget()
    frame_addition.pack(fill="both", expand=True)

def retour_page2():
    frame_page3.pack_forget()
    frame_page4.pack_forget()
    frame_devine.pack_forget()
    frame_page5.pack_forget()
    frame_addition.pack_forget()
    frame_page2.pack(fill="both", expand=True)

def nouvelle_partie():
    global nombre_secret, essais, limite_essais
    nombre_secret = random.randint(1, 100)
    essais = 0
    limite_essais = 15
    label_resultat.config(text="Devine un nombre entre 1 et 100.")
    entree_nombre.delete(0, tk.END)

def verifier_nombre():
    global essais
    try:
        guess = int(entree_nombre.get())
    except ValueError:
        label_resultat.config(text="⚠️ Entre un nombre valide.")
        return
    essais += 1
    if guess == nombre_secret:
        label_resultat.config(text=f"🎉 Bravo ! Trouvé en {essais} essais.")
    elif essais >= limite_essais:
        label_resultat.config(text=f"😢 Perdu ! Le nombre était {nombre_secret}.")
    elif guess < nombre_secret:
        label_resultat.config(text="C'est plus grand ⬆️")
    else:
        label_resultat.config(text="C'est plus petit ⬇️")
    entree_nombre.delete(0, tk.END)

def calculer_addition():
    try:
        a = int(entree_a.get())
        b = int(entree_b.get())
        resultat_addition.config(text=f"Résultat : {a + b}")
    except ValueError:
        resultat_addition.config(text="⚠️ Entrez des nombres valides")

fenetre = tk.Tk()
fenetre.title("Mon programme")
fenetre.geometry("1280x720")

frame_page1 = tk.Frame(fenetre)
tk.Label(frame_page1, text="Bienvenue dans mon logiciel !", font=("Arial", 20)).pack(pady=10)
frame_page1.pack(fill="both", expand=True)

frame_page2 = tk.Frame(fenetre, bg="lightgreen")
tk.Label(frame_page2, text="Menu Principal", font=("Arial", 20)).pack(pady=20)
tk.Button(frame_page2, text="Jeux", command=afficher_page4).pack(pady=10)
tk.Button(frame_page2, text="Outils", command=afficher_page5).pack(pady=10)
tk.Button(frame_page2, text="Information", command=afficher_page3).pack(pady=10)
tk.Button(frame_page1, text="Menu Principal", command=afficher_page2).pack(pady=20)

frame_page3 = tk.Frame(fenetre)
tk.Label(frame_page3, text="Information", font=("Arial", 20)).pack(pady=20)
tk.Label(frame_page3, text="Logiciel en maintenance...", font=("Arial", 14)).pack(pady=10)
tk.Button(frame_page3, text="Retour", command=retour_page2).pack(pady=20)

frame_page4 = tk.Frame(fenetre)
tk.Label(frame_page4, text="Jeux", font=("Arial", 20)).pack(pady=20)
tk.Button(frame_page4, text="🎯 Devine le nombre", command=afficher_page_devine).pack(pady=5)
tk.Button(frame_page4, text="Retour", command=retour_page2).pack(pady=20)

frame_devine = tk.Frame(fenetre)
tk.Label(frame_devine, text="🎯 Devine le nombre", font=("Arial", 20)).pack(pady=20)
label_resultat = tk.Label(frame_devine, text="", font=("Arial", 14))
label_resultat.pack(pady=10)
entree_nombre = tk.Entry(frame_devine, font=("Arial", 14))
entree_nombre.pack(pady=10)
tk.Button(frame_devine, text="Vérifier", command=verifier_nombre).pack(pady=5)
tk.Button(frame_devine, text="Nouvelle partie", command=nouvelle_partie).pack(pady=5)
tk.Button(frame_devine, text="Retour", command=retour_page2).pack(pady=20)

frame_page5 = tk.Frame(fenetre)
tk.Label(frame_page5, text="Outils", font=("Arial", 20)).pack(pady=20)
tk.Button(frame_page5, text="🧮 Addition", command=afficher_addition).pack(pady=5)
tk.Button(frame_page5, text="Retour", command=retour_page2).pack(pady=20)

frame_addition = tk.Frame(fenetre)
tk.Label(frame_addition, text="🧮 Calculatrice Addition", font=("Arial", 20)).pack(pady=20)
entree_a = tk.Entry(frame_addition, font=("Arial", 14))
entree_a.pack(pady=5)
entree_b = tk.Entry(frame_addition, font=("Arial", 14))
entree_b.pack(pady=5)
tk.Button(frame_addition, text="Calculer", command=calculer_addition).pack(pady=5)
resultat_addition = tk.Label(frame_addition, text="", font=("Arial", 14))
resultat_addition.pack(pady=10)
tk.Button(frame_addition, text="Retour", command=retour_page2).pack(pady=20)

fenetre.mainloop()
