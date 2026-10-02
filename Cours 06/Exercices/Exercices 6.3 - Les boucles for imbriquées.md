# Exercices — Les boucles `for` imbriquées et les listes à deux dimensions (fiche 6.3)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande.

## 🟢 Exercice 1 : Facile

**But** : Prédire l'exécution d'une boucle imbriquée à l'aide d'un tableau de trace.

**Énoncé** : Sans exécuter de code, réponds aux questions suivantes pour le programme ci-dessous. Vérifie ensuite tes réponses dans VS Code.

```python
compteur = 0
for i in range(1, 4):
    for j in range(i, 4):
        compteur += 1
        print(i, j)
print("compteur =", compteur)
```

a. Construis le tableau de trace (`i`, `j`, `compteur`).

b. Combien de fois la ligne `print(i, j)` est-elle exécutée?

c. Qu'est-ce qui changerait si la boucle intérieure était `for j in range(1, 4):`?

## 🟢 Exercice 2 : Facile

**But** : Afficher une grille avec `end=""` et `print()`.

**Énoncé** : Demande un entier `n` entre 1 et 9 à l'utilisateur, puis affiche un carré de `n` lignes et `n` colonnes, dans lequel chaque ligne contient son numéro de ligne (à partir de 1).

*Exemple d'exécution :*

```text
Taille (1 à 9) : x
Ce n'est pas un nombre entier.
Taille (1 à 9) : 0
La taille doit être entre 1 et 9.
Taille (1 à 9) : 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

## 🟢 Exercice 3 : Facile

**But** : Faire dépendre la boucle intérieure de la boucle extérieure.

**Énoncé** : Demande une hauteur entre 1 et 20 à l'utilisateur, puis affiche un triangle d'étoiles **aligné à droite**.

> **Indice** : chaque ligne contient d'abord des espaces, puis des étoiles. Combien de chaque pour la ligne numéro `ligne`?

*Exemple d'exécution :*

```text
Hauteur (1 à 20) : -2
La hauteur doit être entre 1 et 20.
Hauteur (1 à 20) : 5
    *
   **
  ***
 ****
*****
```

## 🟢 Exercice 4 : Facile-Moyen

**But** : Produire un tableau formaté avec des en-têtes.

**Énoncé** : Demande un entier `n` entre 1 et 12, puis affiche la table de multiplication de 1 à `n` avec une ligne d'en-tête, une colonne d'en-tête et des séparateurs, comme dans l'exemple. Chaque nombre occupe 4 caractères.

*Exemple d'exécution :*

```text
Taille de la table (1 à 12) : 13
La taille doit être entre 1 et 12.
Taille de la table (1 à 12) : 6
   x |   1   2   3   4   5   6
-----+------------------------
   1 |   1   2   3   4   5   6
   2 |   2   4   6   8  10  12
   3 |   3   6   9  12  15  18
   4 |   4   8  12  16  20  24
   5 |   5  10  15  20  25  30
   6 |   6  12  18  24  30  36
```

## 🟡 Exercice 5 : Moyen

**But** : Utiliser les numéros de ligne et de colonne dans une condition.

**Énoncé** : Demande une taille `n` entre 2 et 20, puis affiche un damier de `n` × `n` cases qui alterne `#` et `.`. La case en haut à gauche est un `#`.

> **Indice** : regarde la parité de `ligne + colonne`.

*Exemple d'exécution :*

```text
Taille (2 à 20) : abc
Ce n'est pas un nombre entier.
Taille (2 à 20) : 6
# . # . # .
. # . # . #
# . # . # .
. # . # . #
# . # . # .
. # . # . #
```

## 🟡 Exercice 6 : Moyen

**But** : Calculer le nombre de caractères de chaque ligne d'un motif.

**Énoncé** : Demande une hauteur entre 1 et 20, puis affiche une pyramide d'étoiles centrée.

> **Indice** : la ligne `ligne` (de 1 à `hauteur`) contient `hauteur - ligne` espaces, puis `2 * ligne - 1` étoiles.

*Exemple d'exécution :*

```text
Hauteur (1 à 20) : vingt-cinq
Ce n'est pas un nombre entier.
Hauteur (1 à 20) : 25
La hauteur doit être entre 1 et 20.
Hauteur (1 à 20) : 5
    *
   ***
  *****
 *******
*********
```

**Bonus** : affiche ensuite la pyramide à l'envers sous la première, pour former un losange.

## 🟡 Exercice 7 : Moyen

**But** : Comparer chaque élément d'une liste à chaque élément d'une autre.

**Énoncé** : Deux amis ont chacun leur liste de films préférés. À l'aide de **deux boucles imbriquées** (sans utiliser l'opérateur `in` pour comparer les listes), construis la liste des films qu'ils aiment tous les deux, puis affiche-la avec le nombre de comparaisons effectuées.

```python
films_ana = ["Dune", "Up", "Coco", "Matrix", "Shrek"]
films_ben = ["Shrek", "Alien", "Dune", "Cars"]
```

*Sortie attendue :*

```text
Films en commun : ['Dune', 'Shrek']
Comparaisons effectuées : 20
```

## 🟡 Exercice 8 : Moyen

**But** : Parcourir une liste 2D par ligne et rechercher des positions.

**Énoncé** : L'inventaire d'un entrepôt est rangé dans une liste 2D : chaque ligne est une **allée** et chaque colonne une **tablette**. La valeur indique le nombre de boîtes sur la tablette.

```python
entrepot = [
    [12, 0, 7, 15],
    [3, 8, 0, 0],
    [20, 14, 9, 6],
]
```

a. Affiche le nombre total de boîtes dans chaque allée, puis dans tout l'entrepôt.

b. Affiche la position (allée et tablette, en comptant à partir de 1) de chaque tablette vide.

c. Ajoute 5 boîtes sur chaque tablette vide, puis affiche l'entrepôt sous forme de grille alignée.

*Sortie attendue :*

```text
Allée 1 : 34 boîtes
Allée 2 : 11 boîtes
Allée 3 : 49 boîtes
Total de l'entrepôt : 94
Tablette vide : allée 1, tablette 2
Tablette vide : allée 2, tablette 3
Tablette vide : allée 2, tablette 4
  12   5   7  15
   3   8   5   5
  20  14   9   6
```

## 🟡 Exercice 9 : Moyen

**But** : Construire une liste 2D à partir de saisies.

**Énoncé** : Demande à l'utilisateur un nombre de lignes et un nombre de colonnes (chacun entre 1 et 5), puis chacune des valeurs (entières) de la grille, ligne par ligne. Range les valeurs dans une liste 2D, puis affiche :

a. la grille;

b. sa **transposée** (les lignes deviennent des colonnes);

c. la somme de chaque colonne.

*Exemple d'exécution :*

```text
Nombre de lignes (1 à 5) : 2
Nombre de colonnes (1 à 5) : trois
Ce n'est pas un nombre entier.
Nombre de colonnes (1 à 5) : 8
Le nombre doit être entre 1 et 5.
Nombre de colonnes (1 à 5) : 3
Valeur [0][0] : 1
Valeur [0][1] : 2
Valeur [0][2] : x
Ce n'est pas un nombre entier.
Valeur [0][2] : 3
Valeur [1][0] : 4
Valeur [1][1] : 5
Valeur [1][2] : 6
Grille :
   1   2   3
   4   5   6
Transposée :
   1   4
   2   5
   3   6
Somme de la colonne 0 : 5
Somme de la colonne 1 : 7
Somme de la colonne 2 : 9
```

## 🔴 Exercice 10 : Moyen-Difficile

**But** : Modifier une liste 2D au fil d'une boucle `while`.

**Énoncé** : Le plan d'une petite salle de cinéma est représenté par une liste 2D de 4 rangées et 6 sièges, où `"L"` signifie libre et `"X"` signifie occupé.

```python
salle = [
    ["L", "L", "X", "X", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["X", "X", "L", "L", "X", "L"],
    ["L", "L", "L", "L", "L", "L"],
]
```

Tant que l'utilisateur veut réserver (il entre `q` pour quitter) :

- affiche le plan, avec les numéros de rangées et de sièges à partir de 1;
- demande une rangée, puis un siège. La rangée doit être `q` ou un entier qui correspond à une rangée existante; le siège doit être un entier qui correspond à un siège existant;
- si le siège est déjà occupé, affiche un message; sinon, réserve-le.

À la fin, affiche le nombre de sièges encore libres.

*Exemple d'exécution :*

```text
     1 2 3 4 5 6
R1 : L L X X L L
R2 : L L L L L L
R3 : X X L L X L
R4 : L L L L L L
Rangée (1 à 4, q pour quitter) : 2
Siège (1 à 6) : 3
Siège réservé!

     1 2 3 4 5 6
R1 : L L X X L L
R2 : L L X L L L
R3 : X X L L X L
R4 : L L L L L L
Rangée (1 à 4, q pour quitter) : 1
Siège (1 à 6) : 3
Ce siège est déjà occupé.

     1 2 3 4 5 6
R1 : L L X X L L
R2 : L L X L L L
R3 : X X L L X L
R4 : L L L L L L
Rangée (1 à 4, q pour quitter) : 9
Cette rangée n'existe pas.
Rangée (1 à 4, q pour quitter) : abc
Ce n'est pas un nombre entier.
Rangée (1 à 4, q pour quitter) : 4
Siège (1 à 6) : 10
Ce siège n'existe pas.
Siège (1 à 6) : 1
Siège réservé!

     1 2 3 4 5 6
R1 : L L X X L L
R2 : L L X L L L
R3 : X X L L X L
R4 : X L L L L L
Rangée (1 à 4, q pour quitter) : q
Sièges encore libres : 17
```

## 🔴 Exercice 11 : Difficile

**But** : Implémenter un algorithme de tri avec des boucles imbriquées.

**Énoncé** : Le **tri à bulles** trie une liste en comparant les éléments voisins deux à deux et en les échangeant s'ils sont dans le mauvais ordre. Après un premier passage complet, le plus grand élément est rendu à la fin; on recommence alors avec le reste de la liste.

a. Trie la liste ci-dessous en ordre croissant avec le tri à bulles, **sans** utiliser `sort()` ni `sorted()`. Affiche la liste après chaque passage.

b. Ajoute un drapeau qui arrête le tri dès qu'un passage complet n'a fait **aucun** échange (la liste est alors déjà triée).

```python
nombres = [29, 10, 14, 37, 13, 5]
```

> **Indice** : pour échanger deux éléments, `nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]`.

*Sortie attendue :*

```text
Départ : [29, 10, 14, 37, 13, 5]
Passage 1 : [10, 14, 29, 13, 5, 37]
Passage 2 : [10, 14, 13, 5, 29, 37]
Passage 3 : [10, 13, 5, 14, 29, 37]
Passage 4 : [10, 5, 13, 14, 29, 37]
Passage 5 : [5, 10, 13, 14, 29, 37]
Triée : [5, 10, 13, 14, 29, 37]
```

## 🔴 Exercice 12 : Difficile

**But** : Examiner les voisins de chaque case d'une liste 2D.

**Énoncé** : Dans le jeu du démineur, chaque case qui ne contient pas de mine affiche le nombre de mines dans les 8 cases qui l'entourent (horizontalement, verticalement et en diagonale).

À partir de la grille ci-dessous (`"*"` = mine, `"."` = case vide), construis une **nouvelle** liste 2D dans laquelle chaque case vide est remplacée par le nombre de mines voisines (sous forme de chaîne). Les mines restent `"*"`. Affiche ensuite la nouvelle grille.

```python
grille = [
    ["*", ".", ".", "."],
    [".", ".", "*", "."],
    [".", ".", ".", "."],
    ["*", "*", ".", "."],
]
```

> **Indices** :
>
> - Pour la case `[l][c]`, les voisins sont aux lignes `l - 1` à `l + 1` et aux colonnes `c - 1` à `c + 1` : deux boucles de plus!
> - Attention aux bords : un voisin n'existe que si ses index sont entre `0` et la taille de la grille moins 1.

*Sortie attendue :*

```text
* 2 1 1
1 2 * 1
2 3 2 1
* * 1 0
```
