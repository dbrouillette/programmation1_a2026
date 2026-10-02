# Les nombres aléatoires — Le module `random`

## Objectifs

- Savoir importer le module `random`.
- Générer des nombres entiers et réels aléatoires.
- Choisir ou mélanger aléatoirement les éléments d'une liste.
- Reproduire une suite de nombres aléatoires pour tester un programme.

## Référence

Le module `random` fait partie de la bibliothèque standard de Python. Il permet de générer des nombres **pseudo-aléatoires** : ils semblent aléatoires, mais sont produits par un calcul. C'est amplement suffisant pour des jeux, des simulations ou des données de test.

> **Documentation officielle** : Pour la liste complète des fonctions disponibles, voir la documentation officielle : [docs.python.org/fr/3/library/random.html](https://docs.python.org/fr/3.14/library/random.html).

## 1. Importer le module `random`

```python
import random
```

Toutes les fonctions du module doivent être préfixées par `random.`.

## 2. Générer des nombres entiers

| Nom | Description | Paramètres | Retour | Exemple(s) |
| --- | --- | --- | --- | --- |
| `random.randint(a, b)` | Entier aléatoire entre `a` et `b`, **les deux bornes incluses**. | `a`, `b` : entiers, `a <= b` | `int` | `random.randint(1, 6)` → `4` |
| `random.randrange(fin)` | Entier aléatoire de `0` à `fin` **exclu**. | `fin` : entier | `int` | `random.randrange(10)` → `7` |
| `random.randrange(debut, fin, pas)` | Entier aléatoire choisi parmi `range(debut, fin, pas)`. | Mêmes règles que `range()` | `int` | `random.randrange(0, 101, 5)` → `35` |

```python
import random

de = random.randint(1, 6)
print("Vous avez obtenu", de)

nombre_pair = random.randrange(0, 21, 2)    # 0, 2, 4, ..., 20
print("Nombre pair aléatoire :", nombre_pair)
```

> ⚠️ **Attention aux bornes!** `randint(1, 6)` peut retourner `6`, alors que `range(1, 6)` s'arrête à `5`. `randrange()`, lui, suit la même règle que `range()` : la fin est exclue.

## 3. Générer des nombres réels

| Nom | Description | Paramètres | Retour | Exemple(s) |
| --- | --- | --- | --- | --- |
| `random.random()` | Réel aléatoire entre `0.0` (inclus) et `1.0` (exclu). | Aucun | `float` | `random.random()` → `0.4387...` |
| `random.uniform(a, b)` | Réel aléatoire entre `a` et `b`. | `a`, `b` : nombres | `float` | `random.uniform(15, 25)` → `19.84...` |

```python
temperature = round(random.uniform(-10, 30), 1)
print(f"Température simulée : {temperature} °C")

# Événement qui se produit 30 % du temps
if random.random() < 0.3:
    print("Il pleut!")
```

## 4. Choisir dans une liste

| Nom | Description | Paramètres | Retour | Exemple(s) |
| --- | --- | --- | --- | --- |
| `random.choice(seq)` | Un élément choisi au hasard. | `seq` : liste, chaîne ou tuple **non vide** | Un élément de `seq` | `random.choice(["pile", "face"])` → `'face'` |
| `random.sample(seq, k)` | `k` éléments **différents**, choisis au hasard. | `seq` : séquence, `k` : entier `<= len(seq)` | Nouvelle `list` | `random.sample(range(1, 50), 6)` → `[12, 3, 44, 27, 8, 31]` |
| `random.shuffle(liste)` | Mélange **la liste elle-même**. Ne retourne rien. | `liste` : une liste | `None` | Voir l'exemple ci-dessous |

```python
equipes = ["Rouge", "Bleu", "Vert", "Jaune"]
print("Équipe qui commence :", random.choice(equipes))

cartes = ["As", "Roi", "Dame", "Valet", "10"]
random.shuffle(cartes)    # cartes est maintenant mélangée
print(cartes)

numeros_gagnants = random.sample(range(1, 50), 6)    # 6 numéros, sans doublon
print(sorted(numeros_gagnants))
```

> ⚠️ Comme `sort()`, `shuffle()` modifie la liste et retourne `None` : on n'écrit **jamais** `cartes = random.shuffle(cartes)`.

## 5. Reproduire les résultats avec `seed()`

Pour tester ou déboguer un programme, il est pratique d'obtenir **toujours la même suite** de nombres « aléatoires ». La fonction `random.seed(valeur)` fixe le point de départ du générateur.

```python
import random

random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))    # toujours les mêmes deux nombres

random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))    # identiques à la ligne précédente
```

> 💡 On ajoute `random.seed(...)` pendant le développement, puis **on le retire** pour que le programme redevienne imprévisible.

## 6. Usages typiques avec les boucles

### Lancer un dé plusieurs fois et compter les résultats

```python
NB_LANCERS = 1000
nb_six = 0
for _ in range(NB_LANCERS):
    if random.randint(1, 6) == 6:
        nb_six += 1
print(f"6 obtenu {nb_six} fois ({nb_six / NB_LANCERS:.1%})")
```

### Remplir une liste de valeurs aléatoires

```python
notes = []
for _ in range(10):
    notes.append(random.randint(40, 100))
print(notes)
```

### Jeu « devine le nombre »

```python
secret = random.randint(1, 100)
essai = int(input("Devinez un nombre entre 1 et 100 : "))
while essai != secret:
    if essai < secret:
        print("Plus grand!")
    else:
        print("Plus petit!")
    essai = int(input("Essayez encore : "))
print("Bravo!")
```

## 7. Remarques importantes

- `random.randint(a, b)` **inclut** `b`, contrairement à `range()` et à `randrange()`.
- `random.choice()` sur une liste vide provoque une erreur `IndexError`.
- `random.sample(seq, k)` provoque une erreur `ValueError` si `k` est plus grand que `len(seq)`.
- **Ne nommez jamais votre fichier `random.py`** : Python importerait votre fichier au lieu du module, et `random.randint` deviendrait introuvable.
- Les nombres pseudo-aléatoires ne conviennent pas à la sécurité (mots de passe, jetons); on utilise alors le module `secrets`.

## 8. Exercices

> 📌 **Validation obligatoire** : chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Comme les résultats sont aléatoires, ta sortie sera différente des exemples.

### 🟢 Exercice 1 : Facile

**But** : Simuler un événement à deux issues avec `random.choice()`.

**Énoncé** : Demande à l'utilisateur combien de fois il veut lancer une pièce de monnaie (entre 1 et 100). Simule les lancers avec `random.choice()`, affiche le résultat de chaque lancer sur une même ligne, puis le nombre et le pourcentage (1 décimale) de `pile` et de `face`.

*Exemple d'exécution :*

```text
Nombre de lancers (1 à 100) : mille
Ce n'est pas un nombre entier.
Nombre de lancers (1 à 100) : 0
Le nombre doit être entre 1 et 100.
Nombre de lancers (1 à 100) : 10
pile face pile face face pile pile pile pile face
Pile : 6 (60.0 %)
Face : 4 (40.0 %)
```

### 🟢 Exercice 2 : Facile

**But** : Tirer plusieurs nombres différents avec `random.sample()`.

**Énoncé** : Simule le Lotto 6/49 :

a. Demande à l'utilisateur combien de grilles « Mise-éclair » il veut acheter (entre 1 et 10). Pour chaque grille, tire 6 numéros **différents** entre 1 et 49 et affiche-les en ordre croissant.

b. Simule ensuite le tirage officiel : 6 numéros gagnants **et** un numéro complémentaire, tous différents. Affiche les numéros gagnants en ordre croissant, puis le numéro complémentaire.

> **Indice** : en b, un seul appel à `random.sample()` suffit pour obtenir 7 numéros différents. Le dernier sera le complémentaire.

*Exemple d'exécution :*

```text
Nombre de grilles (1 à 10) : douze
Ce n'est pas un nombre entier.
Nombre de grilles (1 à 10) : 12
Le nombre doit être entre 1 et 10.
Nombre de grilles (1 à 10) : 3
Grille 1 : [3, 9, 13, 15, 24, 25]
Grille 2 : [6, 9, 14, 16, 26, 33]
Grille 3 : [2, 25, 30, 32, 42, 47]
Numéros gagnants : [6, 13, 26, 32, 37, 49]
Numéro complémentaire : 15
```

### 🟡 Exercice 3 : Moyen

**But** : Générer des données aléatoires et les comparer à des saisies.

**Énoncé** : Crée un quiz de calcul mental de 5 questions. Pour chaque question, tire deux nombres entre 1 et 12 et une opération au hasard parmi `+`, `-` et `x`. Demande la réponse à l'utilisateur (un entier), indique si elle est bonne ou donne la bonne réponse, puis affiche le score final.

*Exemple d'exécution :*

```text
Question 1 : 8 - 9 = -1
Bravo!
Question 2 : 8 x 9 = neuf
Ce n'est pas un nombre entier.
Question 2 : 8 x 9 = 72
Bravo!
Question 3 : 4 x 3 = 12
Bravo!
Question 4 : 8 x 11 = 80
Non, la réponse était 88.
Question 5 : 3 - 2 = 1
Bravo!
Score final : 4 / 5
```

### 🟡 Exercice 4 : Moyen

**But** : Mélanger une liste et y choisir des éléments sans répétition.

**Énoncé** : Pour une présentation orale en classe :

a. Saisis les noms des étudiants un à un, jusqu'à ce que l'utilisateur appuie sur Entrée sans rien écrire. Il faut au moins 3 étudiants, et un même nom ne peut pas être entré deux fois.

b. Affiche un **ordre de passage** aléatoire (numéroté à partir de 1), sans modifier la liste originale.

c. Tire au sort 2 étudiants **différents** qui poseront les questions au premier présentateur. Ils ne doivent pas être ce présentateur.

*Exemple d'exécution :*

```text
Nom (Entrée pour terminer) : Léa
Nom (Entrée pour terminer) : Noah
Nom (Entrée pour terminer) :
Il faut au moins 3 étudiants.
Nom (Entrée pour terminer) : Léa
Ce nom a déjà été entré.
Nom (Entrée pour terminer) : Ana
Nom (Entrée pour terminer) : Ben
Nom (Entrée pour terminer) : Chloé
Nom (Entrée pour terminer) :

Ordre de passage :
1. Léa
2. Noah
3. Ben
4. Ana
5. Chloé

Questions à Léa : Noah et Ana
Liste originale : ['Léa', 'Noah', 'Ana', 'Ben', 'Chloé']
```

### 🔴 Exercice 5 : Difficile

**But** : Simuler une course à l'aide de probabilités.

**Énoncé** : Simule la course du lièvre et de la tortue sur une piste de 30 cases. À chaque tour :

- la tortue avance de 1 à 3 cases;
- le lièvre dort 40 % du temps (il n'avance pas); sinon, il avance de 2 à 6 cases.

Après chaque tour, affiche le numéro du tour et la piste de chaque coureur : un `.` par case parcourue, suivi de `T` (tortue) ou de `L` (lièvre), comme dans l'exemple. La course se termine dès qu'un coureur atteint la fin de la piste. Affiche alors le gagnant (ou `Égalité!` si les deux arrivent au même tour).

> **Indices** :
>
> - `random.random() < 0.4` est vrai 40 % du temps.
> - Un coureur ne peut pas dépasser la fin de la piste : utilise `min(position, LONGUEUR_PISTE)`.
> - Pendant la mise au point, ajoute `random.seed(...)` pour obtenir toujours la même course.

*Exemple de sortie :*

```text
Tour 1
.T
...L
Tour 2
...T
........L
Tour 3
......T
..............L
Tour 4
.......T
...................L
Tour 5
.........T
......................L
Tour 6
............T
............................L
Tour 7
..............T
............................L
Tour 8
...............T
............................L
Tour 9
................T
..............................L
Le lièvre gagne en 9 tours!
```

## 9. Résumé

- `import random` donne accès au module.
- `random.randint(a, b)` : entier entre `a` et `b` inclusivement — la fonction la plus utilisée.
- `random.random()` et `random.uniform(a, b)` : nombres réels.
- `random.choice()`, `random.sample()` et `random.shuffle()` : travailler avec des listes.
- `random.seed(valeur)` : rendre les résultats reproductibles pour les tests.

## 10. Solutions

### ✅ Solution 1

```python
import random

NB_LANCERS_MIN = 1
NB_LANCERS_MAX = 100
PILE = "pile"
FACE = "face"

valide = False
while not valide:
    try:
        nb_lancers = int(input(f"Nombre de lancers ({NB_LANCERS_MIN} à {NB_LANCERS_MAX}) : "))
        if NB_LANCERS_MIN <= nb_lancers <= NB_LANCERS_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_LANCERS_MIN} et {NB_LANCERS_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

nb_piles = 0
for _ in range(nb_lancers):
    resultat = random.choice([PILE, FACE])
    print(resultat, end=" ")
    if resultat == PILE:
        nb_piles += 1
print()

nb_faces = nb_lancers - nb_piles
print(f"Pile : {nb_piles} ({nb_piles / nb_lancers * 100:.1f} %)")
print(f"Face : {nb_faces} ({nb_faces / nb_lancers * 100:.1f} %)")
```

Inutile de compter les deux résultats dans la boucle : le nombre de `face` se déduit du nombre total de lancers.

### ✅ Solution 2

```python
import random

NB_GRILLES_MIN = 1
NB_GRILLES_MAX = 10
NUMERO_MAX = 49
NB_NUMEROS = 6

valide = False
while not valide:
    try:
        nb_grilles = int(input(f"Nombre de grilles ({NB_GRILLES_MIN} à {NB_GRILLES_MAX}) : "))
        if NB_GRILLES_MIN <= nb_grilles <= NB_GRILLES_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_GRILLES_MIN} et {NB_GRILLES_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

# a. Grilles Mise-éclair
for no_grille in range(1, nb_grilles + 1):
    grille = random.sample(range(1, NUMERO_MAX + 1), NB_NUMEROS)
    print(f"Grille {no_grille} :", sorted(grille))

# b. Tirage officiel : 6 numéros + 1 complémentaire, tous différents
tirage = random.sample(range(1, NUMERO_MAX + 1), NB_NUMEROS + 1)
complementaire = tirage.pop()
print("Numéros gagnants :", sorted(tirage))
print("Numéro complémentaire :", complementaire)
```

- `random.sample()` garantit des numéros **différents**, ce que plusieurs appels à `randint()` ne garantiraient pas.
- En b, tirer les 7 numéros d'un seul coup assure que le complémentaire ne fait pas partie des 6 numéros gagnants. `pop()` retire le dernier numéro de la liste et le retourne.

### ✅ Solution 3

```python
import random

NB_QUESTIONS = 5
NOMBRE_MIN = 1
NOMBRE_MAX = 12
OPERATIONS = ["+", "-", "x"]

score = 0
for no_question in range(1, NB_QUESTIONS + 1):
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    operation = random.choice(OPERATIONS)

    if operation == "+":
        bonne_reponse = a + b
    elif operation == "-":
        bonne_reponse = a - b
    else:
        bonne_reponse = a * b

    valide = False
    while not valide:
        try:
            reponse = int(input(f"Question {no_question} : {a} {operation} {b} = "))
            valide = True
        except ValueError:
            print("Ce n'est pas un nombre entier.")

    if reponse == bonne_reponse:
        print("Bravo!")
        score += 1
    else:
        print(f"Non, la réponse était {bonne_reponse}.")

print(f"Score final : {score} / {NB_QUESTIONS}")
```

Les nombres et l'opération sont tirés **dans** la boucle : chaque question est donc différente. Une réponse négative (pour une soustraction) est une saisie valide : il ne faut pas la refuser.

### ✅ Solution 4

```python
import random

NB_ETUDIANTS_MIN = 3
NB_QUESTIONNEURS = 2

# a. Saisie des noms
etudiants = []
fin_saisie = False
while not fin_saisie:
    nom = input("Nom (Entrée pour terminer) : ").strip()
    if nom == "":
        if len(etudiants) >= NB_ETUDIANTS_MIN:
            fin_saisie = True
        else:
            print(f"Il faut au moins {NB_ETUDIANTS_MIN} étudiants.")
    elif nom in etudiants:
        print("Ce nom a déjà été entré.")
    else:
        etudiants.append(nom)

# b. Ordre de passage aléatoire
ordre = etudiants.copy()
random.shuffle(ordre)
print("\nOrdre de passage :")
for i in range(len(ordre)):
    print(f"{i + 1}. {ordre[i]}")

# c. Questionneurs pour le premier présentateur
presentateur = ordre[0]
candidats = []
for etudiant in etudiants:
    if etudiant != presentateur:
        candidats.append(etudiant)
questionneurs = random.sample(candidats, NB_QUESTIONNEURS)
print(f"\nQuestions à {presentateur} :", " et ".join(questionneurs))
print("Liste originale :", etudiants)
```

- On mélange une **copie** (`etudiants.copy()`), puisque `shuffle()` modifie la liste elle-même.
- `random.sample()` garantit des éléments différents. Pour exclure le présentateur, on construit d'abord la liste des candidats (patron « filtrer » de la fiche 6.2).
- La condition minimale de 3 étudiants assure qu'il reste au moins 2 candidats.

### ✅ Solution 5

```python
import random

LONGUEUR_PISTE = 30
AVANCE_TORTUE_MIN = 1
AVANCE_TORTUE_MAX = 3
AVANCE_LIEVRE_MIN = 2
AVANCE_LIEVRE_MAX = 6
PROBABILITE_SIESTE = 0.4

position_tortue = 0
position_lievre = 0
tour = 0

while position_tortue < LONGUEUR_PISTE and position_lievre < LONGUEUR_PISTE:
    tour += 1
    position_tortue += random.randint(AVANCE_TORTUE_MIN, AVANCE_TORTUE_MAX)
    if random.random() >= PROBABILITE_SIESTE:
        position_lievre += random.randint(AVANCE_LIEVRE_MIN, AVANCE_LIEVRE_MAX)

    position_tortue = min(position_tortue, LONGUEUR_PISTE)
    position_lievre = min(position_lievre, LONGUEUR_PISTE)

    piste_tortue = ""
    for _ in range(position_tortue):
        piste_tortue += "."
    piste_lievre = ""
    for _ in range(position_lievre):
        piste_lievre += "."

    print(f"Tour {tour}")
    print(piste_tortue + "T")
    print(piste_lievre + "L")

if position_tortue == LONGUEUR_PISTE and position_lievre == LONGUEUR_PISTE:
    print("Égalité!")
elif position_tortue == LONGUEUR_PISTE:
    print(f"La tortue gagne en {tour} tours!")
else:
    print(f"Le lièvre gagne en {tour} tours!")
```

- Le nombre de tours n'est pas connu à l'avance : c'est un `while`. La condition composée continue tant qu'**aucun** des deux coureurs n'a atteint la fin.
- Le lièvre avance seulement si `random.random()` est **supérieur ou égal** à `PROBABILITE_SIESTE`, soit 60 % du temps.
- Les pistes sont construites avec une boucle `for`, comme les motifs de la fiche 6.3. (On pourrait aussi écrire `"." * position_tortue`.)
