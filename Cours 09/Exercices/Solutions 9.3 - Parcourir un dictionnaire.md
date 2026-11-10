# Solutions — Parcourir un dictionnaire (fiche 9.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

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

def trouver_extremes(table):
    """Renvoie (note_grave, note_aigue) : les clés de la plus petite et de la plus grande valeur."""
    note_grave = ""
    note_aigue = ""
    for note, frequence in table.items():
        if note_grave == "" or frequence < table[note_grave]:
            note_grave = note
        if note_aigue == "" or frequence > table[note_aigue]:
            note_aigue = note
    return note_grave, note_aigue

def main():
    print(f"{'Note':<6}{'Fréquence':>10}")
    print("-" * 16)
    for note, frequence in FREQUENCES.items():
        print(f"{note:<6}{frequence:>6} Hz")
    print("-" * 16)

    note_grave, note_aigue = trouver_extremes(FREQUENCES)
    print(f"{len(FREQUENCES)} notes, de {note_grave} ({FREQUENCES[note_grave]} Hz) "
          f"à {note_aigue} ({FREQUENCES[note_aigue]} Hz)")
    print(f"Écart : {max(FREQUENCES.values()) - min(FREQUENCES.values())} Hz")

main()
```

- `items()` donne la note et sa fréquence en même temps : pas besoin d'écrire `FREQUENCES[note]` dans l'affichage.
- `trouver_extremes()` garde des **clés** en mémoire, pas des valeurs : c'est ce qui permet de savoir **quelle** note est la plus grave. La condition `note_grave == ""` traite le premier tour de boucle.
- `max(FREQUENCES.values())` donne bien la plus grande **valeur** (523), mais pas la note qui lui correspond.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
GAMME = ["DO4", "RE4", "MI4", "FA4", "SOL4", "LA4", "SI4", "DO5"]
MELODIE = [
    "MI4", "MI4", "MI4", "MI4", "MI4", "MI4", "MI4", "SOL4", "DO4", "RE4", "MI4",
    "FA4", "FA4", "FA4", "FA4", "FA4", "MI4", "MI4", "MI4", "MI4", "MI4",
    "RE4", "RE4", "MI4", "RE4", "SOL4",
]

def compter_notes(melodie):
    """Renvoie un dictionnaire {note: nombre d'apparitions}."""
    compteur = {}
    for note in melodie:
        compteur[note] = compteur.get(note, 0) + 1
    return compteur

def main():
    compteur = compter_notes(MELODIE)
    print(compteur)
    print()
    for note in GAMME:
        nombre = compteur.get(note, 0)
        print(f"{note:<5}{nombre:>3} {'#' * nombre}")
    print(f"\n{len(MELODIE)} notes, {len(compteur)} notes différentes")

main()
```

- C'est le patron compteur, mot pour mot : `compteur[note] = compteur.get(note, 0) + 1`.
- Le dictionnaire garde l'ordre de **première apparition** des notes (MI4 d'abord). Pour l'ordre musical, on parcourt la liste `GAMME`, avec `get(note, 0)` pour les notes absentes.
- `len(compteur)` donne le nombre de **notes différentes** : chaque clé est unique.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
NOTE = 0
INTENSITE = 1
DUREE = 2

CHANSON = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
    ["FA4", 70, 300], ["FA4", 70, 300], ["FA4", 70, 450], ["FA4", 50, 150],
    ["FA4", 70, 300], ["MI4", 70, 300], ["MI4", 70, 300], ["MI4", 50, 150], ["MI4", 50, 150],
    ["MI4", 80, 300], ["RE4", 80, 300], ["RE4", 80, 300], ["MI4", 80, 300],
    ["RE4", 90, 600], ["SOL4", 100, 600],
]

def additionner_par_note(chanson, colonne):
    """Renvoie {note: somme de la colonne choisie pour cette note}."""
    totaux = {}
    for rangee in chanson:
        note = rangee[NOTE]
        totaux[note] = totaux.get(note, 0) + rangee[colonne]
    return totaux

def compter_par_note(chanson):
    compteur = {}
    for rangee in chanson:
        compteur[rangee[NOTE]] = compteur.get(rangee[NOTE], 0) + 1
    return compteur

def trouver_cle_max(dictionnaire):
    """Renvoie la clé associée à la plus grande valeur."""
    cle_max = ""
    for cle, valeur in dictionnaire.items():
        if cle_max == "" or valeur > dictionnaire[cle_max]:
            cle_max = cle
    return cle_max

def main():
    durees = additionner_par_note(CHANSON, DUREE)
    intensites = additionner_par_note(CHANSON, INTENSITE)
    compteur = compter_par_note(CHANSON)

    print(f"{'Note':<6}{'Nombre':>7}{'Durée (ms)':>12}{'Intensité moy.':>16}")
    for note, nombre in compteur.items():
        moyenne = intensites[note] / nombre
        print(f"{note:<6}{nombre:>7}{durees[note]:>12}{moyenne:>15.1f}%")

    total = sum(durees.values())
    note_max = trouver_cle_max(durees)
    print(f"\nDurée totale : {total / 1000:.1f} s")
    print(f"Note dominante : {note_max} "
          f"({durees[note_max] / total * 100:.0f} % du temps)")

main()
```

- Une seule fonction `additionner_par_note()` sert pour deux colonnes : la colonne est un **paramètre**. On évite ainsi deux fonctions presque identiques.
- Les constantes `NOTE`, `INTENSITE` et `DUREE` remplacent les index « magiques ». À la fiche 9.4, chaque note deviendra un dictionnaire et ces constantes disparaîtront.
- Les trois dictionnaires ont exactement les mêmes clés, puisqu'ils viennent de la même chanson : on peut donc lire `durees[note]` et `intensites[note]` sans risque de `KeyError` dans la boucle sur `compteur`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
NOTE = 0
INTENSITE = 1
DUREE = 2
SILENCE = "-"
DUREE_MIN = 50
DUREE_MAX = 2000

FREQUENCES = {
    "DO4": 262, "RE4": 294, "MI4": 330, "FA4": 349,
    "SOL4": 392, "LA4": 440, "SI4": 494, "DO5": 523,
}

CHANSON_A_VERIFIER = [
    ["DO4", 70, 400],
    ["DO4", 70, 400],
    ["D04", 70, 400],
    ["RE4", 70, 400],
    ["MI4", 150, 800],
    ["-", 0, 400],
    ["RE4", 70, 10],
    ["DO4", 70, 400],
    ["MI4", 70, 400],
    ["RE4", -5, 5000],
    ["RE4", 70, 400],
    ["DO4", 90, 1200],
]

def trouver_erreur(rangee):
    """Renvoie un message d'erreur pour la rangée, ou une chaîne vide si elle est valide."""
    if rangee[NOTE] != SILENCE and rangee[NOTE] not in FREQUENCES:
        return f"note « {rangee[NOTE]} » inconnue"
    if not 0 <= rangee[INTENSITE] <= 100:
        return f"intensité {rangee[INTENSITE]} hors de 0 à 100"
    if not DUREE_MIN <= rangee[DUREE] <= DUREE_MAX:
        return f"durée {rangee[DUREE]} ms hors de {DUREE_MIN} à {DUREE_MAX}"
    return ""

def valider_chanson(chanson):
    """Renvoie un dictionnaire {numéro de note: message d'erreur} (numéros à partir de 1)."""
    erreurs = {}
    for i in range(len(chanson)):
        message = trouver_erreur(chanson[i])
        if message != "":
            erreurs[i + 1] = message
    return erreurs

def main():
    erreurs = valider_chanson(CHANSON_A_VERIFIER)
    if len(erreurs) == 0:
        print("✅ Chanson valide!")
    else:
        print(f"❌ {len(erreurs)} erreur(s) :")
        for numero, message in erreurs.items():
            print(f"  Note {numero:>2} : {message}")

    chanson_propre = []
    for i in range(len(CHANSON_A_VERIFIER)):
        if (i + 1) not in erreurs:
            chanson_propre.append(CHANSON_A_VERIFIER[i])
    print(f"{len(chanson_propre)} note(s) valide(s) conservée(s) sur {len(CHANSON_A_VERIFIER)}.")

main()
```

- `trouver_erreur()` utilise un `return` dans chaque `if` : la fonction s'arrête à la **première** erreur trouvée (fiche 7.4, section 7). La rangée 10 n'a donc qu'un message, même si sa durée est aussi invalide.
- Les clés du dictionnaire `erreurs` sont des **entiers** (les numéros de note) : un dictionnaire n'est pas limité aux clés chaînes.
- `(i + 1) not in erreurs` vérifie rapidement si une rangée a une erreur, sans reparcourir toute la chanson.
- Dans un vrai programme, cette validation est faite **une seule fois**, au chargement du fichier.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
from colorama import Fore, Style, init

init(autoreset=True)

NOTE = 0
DUREE = 2
SYMBOLE = "●"
MS_PAR_SYMBOLE = 150

GAMME = ["DO4", "RE4", "MI4", "FA4", "SOL4", "LA4", "SI4", "DO5"]
COULEURS_CONSOLE = {
    "DO": Fore.RED,
    "RE": Fore.YELLOW,
    "MI": Fore.YELLOW + Style.BRIGHT,
    "FA": Fore.GREEN,
    "SOL": Fore.BLUE,
    "LA": Fore.CYAN,
    "SI": Fore.MAGENTA,
}

CHANSON = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
    ["FA4", 70, 300], ["FA4", 70, 300], ["FA4", 70, 450], ["FA4", 50, 150],
    ["FA4", 70, 300], ["MI4", 70, 300], ["MI4", 70, 300], ["MI4", 50, 150], ["MI4", 50, 150],
    ["MI4", 80, 300], ["RE4", 80, 300], ["RE4", 80, 300], ["MI4", 80, 300],
    ["RE4", 90, 600], ["SOL4", 100, 600],
]

def couleur_console(note):
    """Renvoie le code colorama de la note (sans tenir compte de l'octave)."""
    return COULEURS_CONSOLE.get(note[:-1], Fore.WHITE)

def additionner_durees(chanson):
    durees = {}
    for rangee in chanson:
        durees[rangee[NOTE]] = durees.get(rangee[NOTE], 0) + rangee[DUREE]
    return durees

def afficher_histogramme(durees):
    for note in GAMME:
        duree = durees.get(note, 0)
        if duree > 0:
            barre = SYMBOLE * (duree // MS_PAR_SYMBOLE)
            print(f"{note:<5}{duree:>6} ms " + couleur_console(note) + barre)

def afficher_sapin_lumineux(chanson):
    """Affiche une « bande de DEL » : un symbole coloré par note de la chanson."""
    ligne = ""
    for rangee in chanson:
        ligne += couleur_console(rangee[NOTE]) + SYMBOLE + Style.RESET_ALL
    print(ligne)

def main():
    afficher_histogramme(additionner_durees(CHANSON))
    print()
    afficher_sapin_lumineux(CHANSON)

main()
```

- Les valeurs du dictionnaire sont des **chaînes de codes de couleur** : `Fore.YELLOW + Style.BRIGHT` est simplement une concaténation de deux codes.
- `note[:-1]` retire l'octave (série 9.2, exercice 2) : les notes `DO4` et `DO5` ont la même couleur.
- Dans `afficher_sapin_lumineux()`, chaque symbole a sa couleur : on ajoute `Style.RESET_ALL` après chacun, et on n'affiche la ligne qu'à la fin.
- La même logique servirait à allumer de vraies DEL : on remplacera simplement le code `colorama` par le tuple `(r, v, b)` de la série 9.2 (exercice 2).
