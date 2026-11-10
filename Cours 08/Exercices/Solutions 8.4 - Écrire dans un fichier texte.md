# Solutions — Écrire dans un fichier texte (fiche 8.4)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
from pathlib import Path

DOSSIER = Path(__file__).parent

def lire_entier(message, minimum, maximum):
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return valeur

def ecrire_table(chemin, nombre):
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(f"Table de {nombre}\n")
        for i in range(1, 11):
            fichier.write(f"{i:>2} x {nombre} = {i * nombre:>2}\n")

def main():
    nombre = lire_entier("Quelle table (1 à 12)? ", 1, 12)
    nom_fichier = f"table_{nombre}.txt"
    ecrire_table(DOSSIER / nom_fichier, nombre)
    print(f"Table de {nombre} écrite dans {nom_fichier}.")

main()
```

- Chaque `write()` se termine par `\n`, sinon toute la table serait sur une seule ligne.
- Le formatage `:>2` aligne les nombres, exactement comme avec `print()`. Pour la table de 12, `:>3` serait plus joli pour le produit.
- Relancer le programme avec le même nombre **remplace** le fichier : c'est le comportement du mode `"w"`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from datetime import datetime
from pathlib import Path

CHEMIN_JOURNAL = Path(__file__).parent / "journal.txt"

def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le message ne doit pas être vide.")
        texte = input(message).strip()
    return texte

def ajouter_entree(chemin, message):
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(chemin, "a", encoding="utf-8") as fichier:
        fichier.write(f"{horodatage} | {message}\n")

def afficher_journal(chemin):
    print("\n--- Journal ---")
    with open(chemin, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")

def main():
    message = lire_texte("Message : ")
    ajouter_entree(CHEMIN_JOURNAL, message)
    afficher_journal(CHEMIN_JOURNAL)

main()
```

- Le mode `"a"` crée le fichier à la première exécution, puis ajoute à la fin aux exécutions suivantes.
- On n'a pas besoin de gérer `FileNotFoundError` à la lecture : le fichier vient tout juste d'être créé ou complété.
- `end=""` évite une ligne vide de trop : le contenu lu se termine déjà par `\n`.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_SOURCE = DOSSIER / "poeme.txt"
CHEMIN_DESTINATION = DOSSIER / "poeme_numerote.txt"

def numeroter(chemin_source, chemin_destination):
    """Écrit une copie numérotée du fichier source. Renvoie (nb_lignes, nb_mots)."""
    nb_lignes = 0
    nb_mots = 0
    with open(chemin_source, "r", encoding="utf-8") as source, \
         open(chemin_destination, "w", encoding="utf-8") as destination:
        for ligne in source:
            texte = ligne.strip()
            if texte == "":
                destination.write("\n")
            else:
                nb_lignes += 1
                nb_mots += len(texte.split())
                destination.write(f"{nb_lignes:>3} | {texte}\n")
        destination.write(f"--- {nb_lignes} lignes, {nb_mots} mots ---\n")
    return nb_lignes, nb_mots

def main():
    try:
        nb_lignes, nb_mots = numeroter(CHEMIN_SOURCE, CHEMIN_DESTINATION)
        print(f"{CHEMIN_DESTINATION.name} créé : {nb_lignes} lignes, {nb_mots} mots.")
    except FileNotFoundError:
        print(f"Erreur : {CHEMIN_SOURCE.name} est introuvable.")

main()
```

- Les deux fichiers sont ouverts dans le même `with`; le `\` permet de continuer l'instruction sur la ligne suivante.
- `split()` **sans argument** découpe sur n'importe quel nombre d'espaces : c'est la bonne façon de compter des mots.
- La fonction renvoie un tuple, comme vu en 7.4, pour que le programme principal puisse afficher une confirmation.
