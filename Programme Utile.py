import tkinter as tk

def afficher_page2():
    frame_page1.pack_forget()
    frame_page2.pack(fill="both", expand=True)

def afficher_page3():
    frame_page2.pack_forget()
    frame_page3.pack(fill="both", expand=True)

def afficher_page4():
    frame_page2.pack_forget()
    frame_page4.pack(fill="both", expand=True)

def retour_page2():
    # On cache les deux frames possibles avant d’afficher page 2
    frame_page3.pack_forget()
    frame_page4.pack_forget()
    frame_page2.pack(fill="both", expand=True)

fenetre = tk.Tk()
fenetre.title("Mon programme")
fenetre.geometry("1280x720")

frame_page1 = tk.Frame(fenetre)
tk.Label(frame_page1, text="Bienvenue dans mon logiciel !", font=("Arial", 20)).pack(pady=10)
frame_page1.pack(fill="both", expand=True)

frame_page2 = tk.Frame(fenetre, bg="lightgreen")
tk.Label(frame_page2, text="Menu Principal", font=("Arial", 20)).pack(pady=20)
tk.Button(frame_page2, text="Jeux", command=afficher_page4).pack(pady=10)
tk.Button(frame_page2, text="Information", command=afficher_page3).pack(pady=10)
bouton = tk.Button(frame_page1, text="Menu Principal", command=afficher_page2)
bouton.pack(pady=20)

frame_page3 = tk.Frame(fenetre)
tk.Label(frame_page3, text="Information", font=("Arial", 20)).pack(pady=20)
tk.Label(frame_page3, text="Logiciel en maintenance, Nous comptons faire des amelioraton, des ajouts et des changement", font=("Arial", 14)).pack(pady=10)
tk.Label(frame_page3, text="Ajoutez des mini jeux, code utile pour le travaille ou même pour la vie de tout les jours !", font=("Arial", 14)).pack(pady=10)
tk.Label(frame_page3, text="Nous faisons de notre mieux pour pouvoir terminer ce logiciel, il sera mis a jour très bientôt !", font=("Arial", 14)).pack(pady=10)
tk.Button(frame_page3, text="Retour", command=retour_page2).pack(pady=20)

frame_page4 = tk.Frame(fenetre)
tk.Label(frame_page4, text="Jeux", font=("Arial", 20)).pack(pady=20)
tk.Label(frame_page4, text="Rien pour l'instant ... ", font=("Arial", 14)).pack(pady=10)
tk.Button(frame_page4, text="Retour", command=retour_page2).pack(pady=20)

fenetre.mainloop()
