# Solutions — Les dictionnaires (fiche 9.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
5
1867
True
False
False
0
True
{'titre': 'Vive le vent', 'auteur': 'J. Pierpont', 'annee': 1857, 'tempo': 140}
Vive
Traceback (most recent call last):
  ...
KeyError: 'duree'
```

| Instruction | Affichage | Explication |
| --- | --- | --- |
| `len(chanson)` | `5` | 4 clés au départ, plus `favori`. Modifier `tempo` n'ajoute pas de clé. |
| `chanson["annee"] + 10` | `1867` | La valeur est un `int` : on peut calculer avec. |
| `"auteur" in chanson` | `True` | `in` vérifie les clés. |
| `"Auteur" in chanson` | `False` | Les clés sont sensibles à la casse. |
| `1857 in chanson` | `False` | `in` cherche dans les **clés**, pas dans les valeurs. |
| `chanson.get("duree", 0)` | `0` | Clé absente : `get()` renvoie la valeur par défaut, sans erreur. |
| `chanson.pop("favori")` | `True` | `pop()` supprime la paire et **renvoie** sa valeur. |
| `print(chanson)` | le dictionnaire | `favori` a disparu; `tempo` vaut 140. |
| `chanson["titre"][:4]` | `Vive` | `chanson["titre"]` est une chaîne : on peut lui appliquer le *slicing*. |
| `chanson["duree"]` | `KeyError: 'duree'` | Clé absente lue avec des crochets : erreur. |

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from utilitaires import lire_entier, lire_texte

LARGEUR_LCD = 16


def creer_fiche(titre, auteur, annee):
    """Renvoie la fiche d'une chanson sous forme de dictionnaire."""
    return {"titre": titre, "auteur": auteur, "annee": annee}


def afficher_lcd(chanson):
    """Simule l'afficheur 16 x 2 : titre sur la ligne 1, auteur sur la ligne 2."""
    print("+" + "-" * LARGEUR_LCD + "+")
    print(f"|{chanson['titre'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print(f"|{chanson['auteur'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print("+" + "-" * LARGEUR_LCD + "+")


def main():
    titre = lire_texte("Titre : ")
    auteur = lire_texte("Auteur : ")
    annee = lire_entier("Année : ", 1500, 2026)

    fiche = creer_fiche(titre, auteur, annee)
    print(fiche)
    afficher_lcd(fiche)


main()
```

- La fonction `creer_fiche()` renvoie directement un dictionnaire construit avec ses paramètres.
- `afficher_lcd()` ne reçoit qu'**un seul** paramètre, le dictionnaire, plutôt que trois. Si on ajoute une clé à la fiche plus tard, la signature de la fonction ne change pas.
- La largeur peut être une variable dans le format : `:<{LARGEUR_LCD}`. On peut aussi écrire `:<16` directement.
- Un afficheur réel recevrait exactement ces deux chaînes de 16 caractères.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
FREQUENCES = {
    "DO4": 262,
    "RE4": 294,
    "MI4": 330,
    "FA4": 349,
    "SOL4": 392,
    "LA4": 440,
    "SI4": 494,
    "DO5": 523,
}


def frequence_de(note):
    """Renvoie la fréquence (Hz) de la note, ou 0 (silence) si elle est inconnue."""
    return FREQUENCES.get(note.strip().upper(), 0)


def main():
    note = input("Note (Entrée pour terminer) : ").strip().upper()
    while note != "":
        frequence = frequence_de(note)
        if frequence == 0:
            print(f"{note} : note inconnue (silence)")
        else:
            print(f"{note} : {frequence} Hz")
        note = input("Note (Entrée pour terminer) : ").strip().upper()


main()
```

- `get(cle, 0)` remplace un `if note in FREQUENCES: ... else: ...` en une seule ligne.
- La normalisation (`strip()` et `upper()`) est faite dans la fonction : n'importe quel appelant en profite.

**Bonus** : on remplace l'octave 5 par l'octave 4, puis on double la fréquence.

```python
def frequence_de(note):
    """Renvoie la fréquence (Hz) de la note, ou 0 (silence) si elle est inconnue.

    Les notes de l'octave 5 absentes de la table sont calculées à partir de l'octave 4.
    """
    note = note.strip().upper()
    if note in FREQUENCES:
        return FREQUENCES[note]
    if note != "" and note[-1] == "5":
        note_octave_4 = note[:-1] + "4"
        return FREQUENCES.get(note_octave_4, 0) * 2
    return 0
```

- `RE5` → `RE4` (294 Hz) → 588 Hz. Une note inconnue comme `ZZ5` donne `0 * 2`, donc `0`.
- Le test `note != ""` évite une `IndexError` sur `note[-1]` si on reçoit une chaîne vide.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

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

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

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
