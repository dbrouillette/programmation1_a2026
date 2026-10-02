# Solutions — Les boucles `for` imbriquées et les listes à deux dimensions (fiche 6.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
a.
    i   j   compteur
    1   1   1
    1   2   2
    1   3   3
    2   2   4
    2   3   5
    3   3   6

b.  6 fois

c.  La boucle intérieure ferait toujours 3 tours : 3 × 3 = 9 exécutions,
    et compteur vaudrait 9.
```

Comme la boucle intérieure commence à `i`, elle fait de moins en moins de tours : 3, puis 2, puis 1. C'est le même principe que les triangles de la fiche 6.3 (section 5) et que les paires `range(i + 1, n)`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
TAILLE_MIN = 1
TAILLE_MAX = 9

valide = False
while not valide:
    try:
        n = int(input(f"Taille ({TAILLE_MIN} à {TAILLE_MAX}) : "))
        if TAILLE_MIN <= n <= TAILLE_MAX:
            valide = True
        else:
            print(f"La taille doit être entre {TAILLE_MIN} et {TAILLE_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

for ligne in range(1, n + 1):
    for colonne in range(n):
        print(ligne, end=" ")
    print()
```

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
HAUTEUR_MIN = 1
HAUTEUR_MAX = 20
SYMBOLE = "*"

valide = False
while not valide:
    try:
        hauteur = int(input(f"Hauteur ({HAUTEUR_MIN} à {HAUTEUR_MAX}) : "))
        if HAUTEUR_MIN <= hauteur <= HAUTEUR_MAX:
            valide = True
        else:
            print(f"La hauteur doit être entre {HAUTEUR_MIN} et {HAUTEUR_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

for ligne in range(1, hauteur + 1):
    for _ in range(hauteur - ligne):
        print(" ", end="")
    for _ in range(ligne):
        print(SYMBOLE, end="")
    print()
```

Une ligne peut contenir **deux boucles intérieures l'une après l'autre** : une pour les espaces, une pour les étoiles. À la ligne `ligne`, il y a `hauteur - ligne` espaces et `ligne` étoiles, pour un total de `hauteur` caractères.

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

```python
TAILLE_MIN = 1
TAILLE_MAX = 12

valide = False
while not valide:
    try:
        n = int(input(f"Taille de la table ({TAILLE_MIN} à {TAILLE_MAX}) : "))
        if TAILLE_MIN <= n <= TAILLE_MAX:
            valide = True
        else:
            print(f"La taille doit être entre {TAILLE_MIN} et {TAILLE_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

# Ligne d'en-tête
print("   x |", end="")
for colonne in range(1, n + 1):
    print(f"{colonne:4}", end="")
print()

# Ligne de séparation
print("-----+", end="")
for _ in range(n):
    print("----", end="")
print()

# Corps de la table
for ligne in range(1, n + 1):
    print(f"{ligne:4} |", end="")
    for colonne in range(1, n + 1):
        print(f"{ligne * colonne:4}", end="")
    print()
```

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
TAILLE_MIN = 2
TAILLE_MAX = 20
CASE_FONCEE = "#"
CASE_PALE = "."

valide = False
while not valide:
    try:
        n = int(input(f"Taille ({TAILLE_MIN} à {TAILLE_MAX}) : "))
        if TAILLE_MIN <= n <= TAILLE_MAX:
            valide = True
        else:
            print(f"La taille doit être entre {TAILLE_MIN} et {TAILLE_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

for ligne in range(n):
    for colonne in range(n):
        if (ligne + colonne) % 2 == 0:
            print(CASE_FONCEE, end=" ")
        else:
            print(CASE_PALE, end=" ")
    print()
```

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
HAUTEUR_MIN = 1
HAUTEUR_MAX = 20
SYMBOLE = "*"

valide = False
while not valide:
    try:
        hauteur = int(input(f"Hauteur ({HAUTEUR_MIN} à {HAUTEUR_MAX}) : "))
        if HAUTEUR_MIN <= hauteur <= HAUTEUR_MAX:
            valide = True
        else:
            print(f"La hauteur doit être entre {HAUTEUR_MIN} et {HAUTEUR_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

for ligne in range(1, hauteur + 1):
    for _ in range(hauteur - ligne):
        print(" ", end="")
    for _ in range(2 * ligne - 1):
        print(SYMBOLE, end="")
    print()
```

**Bonus** : il suffit de répéter les mêmes boucles avec `for ligne in range(hauteur - 1, 0, -1):` (on commence à `hauteur - 1` pour ne pas répéter la ligne la plus large).

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
films_ana = ["Dune", "Up", "Coco", "Matrix", "Shrek"]
films_ben = ["Shrek", "Alien", "Dune", "Cars"]

communs = []
nb_comparaisons = 0
for film_a in films_ana:
    for film_b in films_ben:
        nb_comparaisons += 1
        if film_a == film_b:
            communs.append(film_a)

print("Films en commun :", communs)
print("Comparaisons effectuées :", nb_comparaisons)
```

Chaque film d'Ana est comparé à chaque film de Ben : 5 × 4 = 20 comparaisons. L'opérateur `in` fait exactement ce travail « en cachette » : `film_a in films_ben` parcourt la liste de Ben jusqu'à trouver le film.

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

```python
TABLETTE_VIDE = 0
BOITES_REMPLISSAGE = 5

entrepot = [
    [12, 0, 7, 15],
    [3, 8, 0, 0],
    [20, 14, 9, 6],
]

# a.
total_general = 0
for allee in range(len(entrepot)):
    total_allee = sum(entrepot[allee])
    total_general += total_allee
    print(f"Allée {allee + 1} : {total_allee} boîtes")
print("Total de l'entrepôt :", total_general)

# b.
for allee in range(len(entrepot)):
    for tablette in range(len(entrepot[allee])):
        if entrepot[allee][tablette] == TABLETTE_VIDE:
            print(f"Tablette vide : allée {allee + 1}, tablette {tablette + 1}")

# c.
for allee in range(len(entrepot)):
    for tablette in range(len(entrepot[allee])):
        if entrepot[allee][tablette] == TABLETTE_VIDE:
            entrepot[allee][tablette] = BOITES_REMPLISSAGE
for rangee in entrepot:
    for quantite in rangee:
        print(f"{quantite:4}", end="")
    print()
```

Pour **lire** les valeurs (affichage en **c**), le parcours par élément suffit. Pour connaître une **position** (**b**) ou **modifier** une case (**c**), il faut le parcours par index.

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

```python
DIMENSION_MIN = 1
DIMENSION_MAX = 5

valide = False
while not valide:
    try:
        nb_lignes = int(input(f"Nombre de lignes ({DIMENSION_MIN} à {DIMENSION_MAX}) : "))
        if DIMENSION_MIN <= nb_lignes <= DIMENSION_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {DIMENSION_MIN} et {DIMENSION_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

valide = False
while not valide:
    try:
        nb_colonnes = int(input(f"Nombre de colonnes ({DIMENSION_MIN} à {DIMENSION_MAX}) : "))
        if DIMENSION_MIN <= nb_colonnes <= DIMENSION_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {DIMENSION_MIN} et {DIMENSION_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

grille = []
for l in range(nb_lignes):
    ligne = []
    for c in range(nb_colonnes):
        valide = False
        while not valide:
            try:
                valeur = int(input(f"Valeur [{l}][{c}] : "))
                valide = True
            except ValueError:
                print("Ce n'est pas un nombre entier.")
        ligne.append(valeur)
    grille.append(ligne)

# a.
print("Grille :")
for ligne in grille:
    for valeur in ligne:
        print(f"{valeur:4}", end="")
    print()

# b. La boucle extérieure parcourt maintenant les COLONNES
print("Transposée :")
for c in range(nb_colonnes):
    for l in range(nb_lignes):
        print(f"{grille[l][c]:4}", end="")
    print()

# c.
for c in range(nb_colonnes):
    total = 0
    for l in range(nb_lignes):
        total += grille[l][c]
    print(f"Somme de la colonne {c} : {total}")
```

La saisie de chaque valeur combine **trois** boucles : deux `for` pour parcourir la grille, et un `while` pour valider la valeur (fiche 6.3, section 8).

## 🔴 Exercice 10 : Moyen-Difficile

### ✅ Solution 10

```python
LIBRE = "L"
OCCUPE = "X"
QUITTER = "q"

salle = [
    ["L", "L", "X", "X", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["X", "X", "L", "L", "X", "L"],
    ["L", "L", "L", "L", "L", "L"],
]

saisie = ""
while saisie != QUITTER:
    # Affichage du plan
    print("     ", end="")
    for siege in range(1, len(salle[0]) + 1):
        print(siege, end=" ")
    print()
    for rangee in range(len(salle)):
        print(f"R{rangee + 1} :", end=" ")
        for siege in range(len(salle[rangee])):
            print(salle[rangee][siege], end=" ")
        print()

    # Validation de la rangée (ou de la demande de quitter)
    valide = False
    while not valide:
        saisie = input(f"Rangée (1 à {len(salle)}, {QUITTER} pour quitter) : ").strip().lower()
        if saisie == QUITTER:
            valide = True
        else:
            try:
                rangee = int(saisie) - 1
                if 0 <= rangee < len(salle):
                    valide = True
                else:
                    print("Cette rangée n'existe pas.")
            except ValueError:
                print("Ce n'est pas un nombre entier.")

    if saisie != QUITTER:
        # Validation du siège
        valide = False
        while not valide:
            try:
                siege = int(input(f"Siège (1 à {len(salle[rangee])}) : ")) - 1
                if 0 <= siege < len(salle[rangee]):
                    valide = True
                else:
                    print("Ce siège n'existe pas.")
            except ValueError:
                print("Ce n'est pas un nombre entier.")

        if salle[rangee][siege] == OCCUPE:
            print("Ce siège est déjà occupé.\n")
        else:
            salle[rangee][siege] = OCCUPE
            print("Siège réservé!\n")

nb_libres = 0
for rangee in salle:
    nb_libres += rangee.count(LIBRE)
print("Sièges encore libres :", nb_libres)
```

- La saisie de la rangée accepte **deux types** de réponses : la lettre `q` ou un entier. On vérifie d'abord le cas `q`, et on ne tente la conversion avec `int()` que dans le cas contraire.
- L'utilisateur compte à partir de 1, mais les index commencent à 0 : on soustrait 1 dès la saisie, ce qui simplifie toutes les vérifications qui suivent.
- Un siège occupé n'est pas une saisie **invalide** : la position existe. C'est un résultat possible de la réservation, traité après la validation.

## 🔴 Exercice 11 : Difficile

### ✅ Solution 11

```python
nombres = [29, 10, 14, 37, 13, 5]
print("Départ :", nombres)

for passage in range(len(nombres) - 1):
    echange = False
    # Les « passage » derniers éléments sont déjà à leur place
    for j in range(len(nombres) - 1 - passage):
        if nombres[j] > nombres[j + 1]:
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
            echange = True
    print(f"Passage {passage + 1} :", nombres)
    if not echange:
        break

print("Triée :", nombres)
```

- La boucle intérieure compare chaque paire de voisins (`j` et `j + 1`) : elle s'arrête à `len(nombres) - 1 - passage` pour ne pas dépasser la fin de la liste et pour ignorer les éléments déjà placés.
- Avec le drapeau `echange`, une liste déjà triée ne demande qu'un seul passage.

## 🔴 Exercice 12 : Difficile

### ✅ Solution 12

```python
MINE = "*"

grille = [
    ["*", ".", ".", "."],
    [".", ".", "*", "."],
    [".", ".", ".", "."],
    ["*", "*", ".", "."],
]

resultat = []
for l in range(len(grille)):
    nouvelle_ligne = []
    for c in range(len(grille[l])):
        if grille[l][c] == MINE:
            nouvelle_ligne.append(MINE)
        else:
            nb_mines = 0
            for voisin_l in range(l - 1, l + 2):
                for voisin_c in range(c - 1, c + 2):
                    if 0 <= voisin_l < len(grille) and 0 <= voisin_c < len(grille[l]):
                        if grille[voisin_l][voisin_c] == MINE:
                            nb_mines += 1
            nouvelle_ligne.append(str(nb_mines))
    resultat.append(nouvelle_ligne)

for ligne in resultat:
    for case in ligne:
        print(case, end=" ")
    print()
```

Ce programme contient **quatre** niveaux de boucles : deux pour parcourir la grille et deux pour parcourir les voisins de chaque case. C'est un cas où dépasser deux niveaux est justifié; plus tard dans la session, les **fonctions** permettront d'isoler le comptage des voisins pour rendre le code plus lisible.

La case elle-même fait partie du carré 3 × 3 parcouru, mais comme on ne compte que les cases vides, elle ne contient jamais de mine : elle n'est donc jamais comptée.
