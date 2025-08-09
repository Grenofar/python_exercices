a = int(input("Bienvenue dans mon bot calculatrice, pour cette addition choisissez un nombre"))
b = int(input("Choisissez un deuxieme"))

def addition(a, b):
    return a + b

somme = addition(a, b)
print("Le résultat est", somme)
