# Auteur    :
# Sujet     : Démo du module `colorama`

from colorama import Fore, Back, Style, init

init(autoreset=True)

# --- 2. Couleurs de texte avec Fore -----------------------------------------
print("=== Couleurs de texte (Fore) ===")
print(Fore.RED + "Texte en rouge")
print(Fore.GREEN + "Texte en vert")

# --- 3. Couleurs de fond avec Back -------------------------------------------
print("\n=== Couleurs de fond (Back) ===")
print(Back.RED + "Texte sur fond rouge")
print(Back.BLUE + "Texte sur fond bleu")

# --- 4. Styles de texte avec Style -------------------------------------------
print("\n=== Styles (Style) ===")
print(Style.BRIGHT + Fore.CYAN + "Texte vif en cyan")

# --- 5. Combiner Fore, Back et Style -----------------------------------------
print("\n=== Combinaison Fore + Back + Style ===")
print(Style.BRIGHT + Fore.WHITE + Back.RED + "Erreur critique")

# --- 6. De la couleur dans les saisies (input) -------------------------------
print("\n=== Colorer l'invite au complet ===")
nom = input(Fore.CYAN + "Quel est votre nom ? ")
print(f"Bonjour, {nom} !")

print("\n=== Colorer ce que l'utilisateur tape ===")
nom = input(f"Votre nom : {Fore.GREEN}")
print(end=Style.RESET_ALL)  # on remet à zéro, sinon le print suivant est aussi coloré!
print(f"Bienvenue, {Fore.GREEN}{nom}")

print("\n=== Menu de difficulté coloré ===")
print("1. Facile")
print("2. Intermédiaire")
print("3. Avancé")

choix = input("Quel est votre choix ? ")

if choix == "1":
    print(Fore.GREEN + "Vous avez choisi le niveau Facile.")
elif choix == "2":
    print(Fore.YELLOW + "Vous avez choisi le niveau Intermédiaire.")
elif choix == "3":
    print(Fore.BLUE + "Vous avez choisi le niveau Avancé.")
else:
    print(Back.WHITE + Fore.RED + Style.BRIGHT + "Choix invalide!")
