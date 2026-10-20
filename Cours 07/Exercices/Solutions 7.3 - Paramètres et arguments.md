# Solutions — Paramètres et arguments (fiche 7.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
« Kukum » : à rapporter dans 21 jours
« Le Petit Prince » : à rapporter dans 14 jours
« Kukum » : à rapporter dans 14 jours
« Bonheur d'occasion » : à rapporter dans 42 jours
« Agaguk » : à rapporter dans 6 jours
```

| Appel | `titre` reçoit | `jours` reçoit |
| --- | --- | --- |
| `afficher_emprunt(livre, duree)` | `"Kukum"` (la valeur de `livre`) | `21` (la valeur de `duree`) |
| `afficher_emprunt("Le Petit Prince", 14)` | `"Le Petit Prince"` | `14` |
| `afficher_emprunt(livre, duree - 7)` | `"Kukum"` | `14` (le calcul est fait **avant** l'appel) |
| `afficher_emprunt(titre, duree * 2)` | `"Bonheur d'occasion"` | `42` |
| `afficher_emprunt("Agaguk", len("Agaguk"))` | `"Agaguk"` | `6` (la valeur renvoyée par `len()`) |

- Les noms des variables (`livre`, `duree`) n'ont pas à être les mêmes que ceux des paramètres : c'est leur **valeur** qui est transmise.
- Dans le 4e appel, la variable `titre` du programme et le paramètre `titre` de la fonction portent le même nom, mais ce sont **deux variables distinctes**. Ça fonctionne, mais ce n'est pas nécessaire.
- Le 5e appel montre qu'un argument peut être le résultat d'une autre fonction.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| Appel | Résultat | Explication |
| --- | --- | --- |
| a. | ✅ `Léa est inscrit(e) au cours Programmation, groupe 2.` | Trois arguments, dans le bon ordre. |
| b. | ⚠️ `Programmation est inscrit(e) au cours Léa, groupe 2.` | Les deux premiers arguments sont **inversés**. Comme les deux sont des chaînes, Python ne voit aucun problème : l'association se fait **par position**, pas par sens. |
| c. | ❌ `TypeError` : `afficher_inscription() missing 1 required positional argument: 'groupe'` | Il manque un argument : le paramètre `groupe` ne reçoit rien. |
| d. | ❌ `TypeError` : `afficher_inscription() takes 3 positional arguments but 4 were given` | Il y a un argument de trop : la fonction n'a que 3 paramètres. |
| e. | ✅ `Zoé est inscrit(e) au cours Web 1, groupe 2.` | Une variable et des expressions sont des arguments valides. Python calcule `"Web " + "1"` et `1 + 1` avant l'appel. |
| f. | ❌ `NameError` : `name 'nom' is not defined` | `nom` est le nom d'un **paramètre**, qui n'existe qu'à l'intérieur de la fonction. Dans le programme principal, aucune variable `nom` n'a été créée. |

- Le cas **b** est le plus dangereux : aucune erreur n'est signalée, et seul un œil attentif voit que l'affichage est faux.
- Le cas **f** est une confusion fréquente entre **paramètre** (dans la définition) et **argument** (dans l'appel). Au moment de l'appel, il faut fournir une **valeur** : `"Léa"` ou une variable qui existe.

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
def afficher_cadre(texte):
    largeur = len(texte) + 4
    print("*" * largeur)
    print(f"* {texte} *")
    print("*" * largeur)


afficher_cadre("Bienvenue!")
afficher_cadre("Menu principal")
afficher_cadre("Merci de votre visite")
```

- Le cadre a 4 caractères de plus que le texte : l'astérisque et l'espace de chaque côté.
- La variable `largeur` est **locale** à la fonction : elle est recalculée à chaque appel, selon le texte reçu.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
REPERES = (-40, 0, 37, 100)
TEMP_MIN = -90
TEMP_MAX = 60

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_conversion(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")


print("Températures repères :")
for temperature in REPERES:
    afficher_conversion(temperature)

print()
temperature = valider_nombre("Température à convertir (°C) : ", TEMP_MIN, TEMP_MAX)
afficher_conversion(temperature)
```

- La même fonction est appelée avec les valeurs d'un tuple (dans la boucle) et avec une valeur saisie : elle ne se soucie pas de l'origine de la valeur reçue.
- Le format `:.1f` affiche `-40` sous la forme `-40.0`, même si la valeur du tuple est un entier.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
COURS = ("Programmation", "Mathématiques", "Français", "Philosophie")
MOYENNES_GROUPE = (74.5, 68.0, 77.2, 71.8)
NOTE_MIN = 0
NOTE_MAX = 100

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_ligne_releve(cours, note, moyenne_groupe):
    mention = "↑" if note >= moyenne_groupe else "↓"
    print(f"{cours:<16}{note:>8.1f}{moyenne_groupe:>8.1f}  {mention}")


notes = []
for cours in COURS:
    note = valider_nombre(f"Note en {cours} : ", NOTE_MIN, NOTE_MAX)
    notes.append(note)

print()
print(f"{'Cours':<16}{'Note':>8}{'Groupe':>8}")
print("-" * 38)
for i in range(len(COURS)):
    afficher_ligne_releve(COURS[i], notes[i], MOYENNES_GROUPE[i])
print("-" * 38)
print(f"Moyenne de l'étudiant : {sum(notes) / len(notes):.1f}")
```

- Les trois séquences `COURS`, `notes` et `MOYENNES_GROUPE` sont associées par leur index : on les parcourt donc **par index**.
- La mention est choisie avec l'opérateur ternaire vu en 4.4, directement dans la fonction.
- L'en-tête utilise les mêmes largeurs (`16`, `8`, `8`) que les lignes, pour que les colonnes s'alignent.

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
NOMBRE_MIN = 1
NOMBRE_MAX = 12
LIMITE_MIN = 1
LIMITE_MAX = 20

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_table(nombre, limite):
    print(f"Table de {nombre}")
    for i in range(1, limite + 1):
        print(f"{nombre:>2} x {i:>2} = {nombre * i:>3}")


nombre = valider_entier("Table de : ", NOMBRE_MIN, NOMBRE_MAX)
limite = valider_entier("Jusqu'à : ", LIMITE_MIN, LIMITE_MAX)
print()
afficher_table(nombre, limite)
```

- Les deux paramètres contrôlent la fonction : `nombre` change le calcul, et `limite` change le nombre de tours de la boucle.
- On utilise `valider_entier()` plutôt que `valider_nombre()`, parce que `range()` exige des entiers.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
def afficher_liste_numerotee(elements):
    for i in range(len(elements)):
        print(f"{i + 1}. {elements[i]}")
    print(f"({len(elements)} articles)")


articles = []
article = input("Article (Entrée pour terminer) : ").strip()
while article != "":
    articles.append(article)
    article = input("Article (Entrée pour terminer) : ").strip()

if len(articles) == 0:
    print("Aucun article.")
else:
    print("\nDans l'ordre de saisie :")
    afficher_liste_numerotee(articles)
    print("\nEn ordre alphabétique :")
    afficher_liste_numerotee(sorted(articles))
```

- `sorted(articles)` **renvoie une nouvelle liste** triée, qui est passée directement en argument : la liste originale n'est pas modifiée.
- Avec `articles.sort()`, la liste originale aurait été triée, et on aurait perdu l'ordre de saisie.
- La même fonction affiche deux listes différentes : c'est tout l'intérêt du paramètre.

## 🔴 Exercice 8 : Moyen-Difficile

### ✅ Solution 8

```python
MOIS = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin")
PRECIPITATIONS_MM = (74, 58, 69, 81, 93, 102)
ECHELLE_PRECIPITATIONS = 10

JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi")
VISITEURS_GYM = (240, 185, 210, 160, 95)
ECHELLE_VISITEURS = 20


def afficher_histogramme(etiquettes, valeurs, echelle):
    for i in range(len(etiquettes)):
        barre = "#" * (valeurs[i] // echelle)
        print(f"{etiquettes[i]:<10}{barre} ({valeurs[i]})")


print(f"Précipitations (1 # = {ECHELLE_PRECIPITATIONS} mm)")
afficher_histogramme(MOIS, PRECIPITATIONS_MM, ECHELLE_PRECIPITATIONS)
print()
print(f"Visiteurs au gym (1 # = {ECHELLE_VISITEURS} visiteurs)")
afficher_histogramme(JOURS, VISITEURS_GYM, ECHELLE_VISITEURS)
```

- La division entière `//` donne le nombre de tranches **complètes** : `74 // 10` vaut `7`.
- `"#" * 7` répète le caractère 7 fois, comme `"=" * 34` dans la fiche.
- La fonction ne connaît ni les mois ni les jours : elle travaille avec n'importe quelles listes (ou tuples) associées. Ses paramètres la rendent **générale**.
