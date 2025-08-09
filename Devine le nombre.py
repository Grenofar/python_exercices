import random

def generer_nombre():
    """Génère un nombre secret entre 1 et 100."""
    return random.randint(1, 100)

def demander_nombre():
    """Demande à l'utilisateur de saisir un nombre."""
    return int(input("Devine le nombre (1-100) : "))

def jouer():
    nombre_secret = generer_nombre()
    essais = 0
    limite_essais = 15

    print("Bienvenue dans Devine le nombre !")

    while essais < limite_essais:
        guess = demander_nombre()
        essais += 1

        if guess == nombre_secret:
            print("Bravo ! Tu as trouvé en", essais, "essais.")
            return
        elif guess < nombre_secret:
            print("C'est plus grand.")
        else:
            print("C'est plus petit.")

    print("Dommage ! Le nombre était", nombre_secret)

# Lancer le jeu
jouer()
