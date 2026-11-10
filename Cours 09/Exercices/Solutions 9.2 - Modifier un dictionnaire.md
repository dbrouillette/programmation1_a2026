# Solutions — Modifier un dictionnaire (fiche 9.2)

## 🟡 Exercice 1 : Moyen

### ✅ Solution 1

```python
from utilitaires import lire_entier, lire_texte

COULEURS = ("rouge", "vert", "bleu", "blanc", "or")

def afficher_sapin(sapin):
    nom = f"« {sapin['nom']} »" if "nom" in sapin else "(sans nom)"
    etat = "allumé" if sapin["allume"] else "éteint"
    print(f"\nSapin {nom} — {etat} — {sapin['nb_del']} DEL — "
          f"{sapin['couleur']} à {sapin['luminosite']} %")

def choisir_couleur():
    for i in range(len(COULEURS)):
        print(f"  {i + 1}. {COULEURS[i]}")
    numero = lire_entier("Couleur : ", 1, len(COULEURS))
    return COULEURS[numero - 1]

def main():
    sapin = {"nb_del": 150, "allume": False, "luminosite": 50, "couleur": "rouge"}

    choix = -1
    while choix != 0:
        afficher_sapin(sapin)
        print("1. Allumer/éteindre  2. Luminosité  3. Couleur  4. Nommer  5. Retirer le nom  0. Quitter")
        choix = lire_entier("Choix : ", 0, 5)

        if choix == 1:
            sapin["allume"] = not sapin["allume"]
        elif choix == 2:
            sapin["luminosite"] = lire_entier("Luminosité (0 à 100) : ", 0, 100)
        elif choix == 3:
            sapin["couleur"] = choisir_couleur()
        elif choix == 4:
            sapin["nom"] = lire_texte("Nom du sapin : ")
        elif choix == 5:
            nom = sapin.pop("nom", None)
            if nom is None:
                print("Ce sapin n'a pas de nom.")
            else:
                print(f"Le nom « {nom} » a été retiré.")

main()
```

- La même instruction `sapin["nom"] = ...` **ajoute** la clé la première fois, puis la **remplace** les fois suivantes.
- `pop("nom", None)` ne provoque jamais d'erreur : si la clé n'existe pas, on obtient `None`, qu'on teste avec `is None`.
- On aurait aussi pu écrire `if "nom" in sapin: del sapin["nom"]`.
- `not sapin["allume"]` inverse un booléen : la même ligne allume et éteint.

## 🔴 Exercice 2 : Moyen-Difficile

### ✅ Solution 2

```python
COULEURS_RGB = {
    "DO": (255, 0, 0),
    "RE": (255, 127, 0),
    "MI": (255, 255, 0),
    "FA": (0, 255, 0),
    "SOL": (0, 0, 255),
    "LA": (75, 0, 130),
    "SI": (148, 0, 211),
}
ETEINT = (0, 0, 0)

def nom_de_note(note):
    """Renvoie le nom de la note sans son octave. Ex. : "SOL4" -> "SOL"."""
    return note[:-1]

def couleur_de(note, intensite):
    """Renvoie le tuple (r, v, b) de la note, atténué selon l'intensité (0 à 100)."""
    couleur = COULEURS_RGB.get(nom_de_note(note), ETEINT)
    rouge = couleur[0] * intensite // 100
    vert = couleur[1] * intensite // 100
    bleu = couleur[2] * intensite // 100
    return rouge, vert, bleu

def main():
    essais = [("MI4", 100), ("SOL4", 50), ("LA4", 80), ("-", 100), ("DO5", 10), ("ZZ4", 100)]
    for note, intensite in essais:
        print(f"{note:<5} à {intensite:>3} % → {couleur_de(note, intensite)}")

main()
```

- Le silence `"-"` n'a pas besoin de traitement spécial : `"-"[:-1]` donne `""`, qui n'est pas une clé du dictionnaire, donc `get()` renvoie `ETEINT`.
- La valeur par défaut de `get()` peut être n'importe quoi, y compris un tuple.
- `return rouge, vert, bleu` renvoie un tuple, comme en 7.4.
- On peut déballer le tuple de la couleur en une ligne : `r, v, b = COULEURS_RGB.get(...)`.
- Ce tuple est exactement ce qu'on enverrait à chaque DEL d'une vraie bande lumineuse.
