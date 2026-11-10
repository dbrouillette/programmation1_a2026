# Solutions — Lire un fichier texte (fiche 8.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Programme | Ce qui se passe | Correction |
| --- | --- | --- |
| A | ⚠️ Le mode `"w"` **efface** le fichier dès l'ouverture, puis la lecture provoque `io.UnsupportedOperation: not readable`. Les villes sont **perdues**. | Utiliser le mode `"r"`. |
| B | Sans `encoding`, Python utilise l'encodage par défaut de l'ordinateur. Sous Windows (souvent `cp1252`), `Trois-Rivières` peut s'afficher `Trois-RiviÃ¨res`. Ailleurs, ça fonctionne : c'est celui qui ne pose problème que sur certains ordinateurs. | Ajouter `encoding="utf-8"`. |
| C | Chaque ligne contient son `\n` : le crochet fermant s'affiche sur la ligne suivante (`[Trois-Rivières` puis `]`). | `print(f"[{ligne.strip()}]")` |
| D | La boucle est **après** le bloc `with` : le fichier est déjà fermé. `ValueError: I/O operation on closed file.` | Mettre la boucle dans le bloc `with` (et retirer le `read()`, qui consommerait tout le fichier avant la boucle). |

Programme D corrigé :

```python
with open("villes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())
```

> 💡 Même la boucle dans le `with` n'afficherait rien si on laissait le `read()` avant : après `read()`, on est déjà à la fin du fichier, et il ne reste plus de lignes à parcourir.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from pathlib import Path

CHEMIN_CITATIONS = Path(__file__).parent / "citations.txt"

def main():
    nb_citations = 0
    with open(CHEMIN_CITATIONS, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            citation = ligne.strip()
            if citation != "":
                nb_citations += 1
                print(f"{nb_citations}. {citation}")

    print(f"\n{nb_citations} citations.")

main()
```

- Le compteur sert à la fois à **numéroter** et à **compter** : on ne l'augmente que pour une ligne non vide.
- Sans le `strip()`, la ligne vide vaudrait `"\n"` et le test `!= ""` serait toujours vrai.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
from pathlib import Path

CHEMIN_TEMPERATURES = Path(__file__).parent / "temperatures.txt"

def lire_nombres(chemin):
    """Renvoie la liste des nombres réels du fichier, en ignorant les lignes vides."""
    nombres = []
    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne != "":
                nombres.append(float(ligne))
    return nombres

def calculer_moyenne(nombres):
    total = 0.0
    for nombre in nombres:
        total += nombre
    return total / len(nombres)

def main():
    temperatures = lire_nombres(CHEMIN_TEMPERATURES)
    print(f"{len(temperatures)} températures lues")
    print(f"Minimum : {min(temperatures):.1f} °C")
    print(f"Maximum : {max(temperatures):.1f} °C")
    print(f"Moyenne : {calculer_moyenne(temperatures):.1f} °C")

main()
```

- La fonction `lire_nombres()` **renvoie** une liste : le reste du programme travaille en mémoire, sans se soucier du fichier.
- Sans le test de la ligne vide, `float("")` provoquerait une `ValueError`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
from pathlib import Path

CHEMIN_MOTS = Path(__file__).parent / "mots_interdits.txt"

def charger_mots(chemin):
    """Renvoie la liste des mots du fichier, en minuscules (liste vide si introuvable)."""
    mots = []
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                mot = ligne.strip().lower()
                if mot != "":
                    mots.append(mot)
    except FileNotFoundError:
        print(f"Avertissement : {chemin.name} introuvable. Aucun mot de passe n'est interdit.")
    return mots

def main():
    mots_interdits = charger_mots(CHEMIN_MOTS)

    saisie = input("Mot de passe à vérifier (Entrée pour quitter) : ").strip()
    while saisie != "":
        if saisie.lower() in mots_interdits:
            print("❌ Mot de passe interdit!")
        else:
            print("✅ Ce mot de passe n'est pas dans la liste.")
        saisie = input("Mot de passe à vérifier (Entrée pour quitter) : ").strip()

main()
```

- Les mots sont mis en minuscules **une seule fois**, au chargement. Il suffit ensuite de mettre la saisie en minuscules pour comparer.
- L'opérateur `in` (vu avec les listes en 6.2) fait la recherche à notre place.
- `chemin.name` donne seulement le nom du fichier, sans le dossier : le message est plus lisible.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
from pathlib import Path

CHEMIN_NOTES = Path(__file__).parent / "notes.txt"
NOTE_MIN = 0
NOTE_MAX = 100

def lire_notes(chemin):
    """Renvoie la liste des notes valides du fichier.

    Affiche un avertissement, avec le numéro de ligne, pour chaque ligne invalide.
    """
    notes = []
    numero = 0
    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            numero += 1
            texte = ligne.strip()
            if texte != "":
                try:
                    note = float(texte)
                    if NOTE_MIN <= note <= NOTE_MAX:
                        notes.append(note)
                    else:
                        print(f"Ligne {numero} ignorée : {note} n'est pas entre {NOTE_MIN} et {NOTE_MAX}.")
                except ValueError:
                    print(f"Ligne {numero} ignorée : « {texte} » n'est pas un nombre.")
    return notes

def calculer_moyenne(nombres):
    total = 0.0
    for nombre in nombres:
        total += nombre
    return total / len(nombres)

def main():
    notes = lire_notes(CHEMIN_NOTES)
    print()
    if len(notes) == 0:
        print("Aucune note valide.")
    else:
        print(f"{len(notes)} notes valides, moyenne : {calculer_moyenne(notes):.1f}")

main()
```

- Le compteur `numero` est augmenté **avant** le test de ligne vide : il correspond ainsi au vrai numéro de ligne dans le fichier, comme dans VS Code.
- On retrouve exactement la recette de validation de 5.3 (`try` / `except` pour le type, `if` pour l'intervalle), appliquée à une ligne de fichier plutôt qu'à une saisie.
- Le cas « aucune note valide » évite une division par zéro.
