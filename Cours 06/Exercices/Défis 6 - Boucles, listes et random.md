# Défis — Boucles, listes et nombres aléatoires (Cours 06)

> 🚀 Ces défis s'adressent à ceux et celles qui ont terminé les séries d'exercices des fiches 6.1 à 6.3. Ils combinent les boucles `for`, les listes (simples et à deux dimensions) et le module [`random`](../../Outils/Nombres%20aléatoires%20-%20Module%20random.md).
>
> 📌 **Validation obligatoire** : chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Comme les résultats sont aléatoires, ta sortie sera différente des exemples.
>
> 💡 Pendant la mise au point, ajoute `random.seed(...)` au début de ton programme pour obtenir toujours les mêmes tirages. N'oublie pas de le retirer ensuite!

## ⭐ Défi 1 : Roche-papier-ciseaux

**But** : Comparer un choix saisi à un choix aléatoire et conserver un historique dans une liste.

**Énoncé** : Programme une partie de roche-papier-ciseaux de 5 manches contre l'ordinateur.

- À chaque manche, l'ordinateur choisit au hasard parmi `roche`, `papier` et `ciseaux`. Le joueur entre son choix, qui doit être l'une de ces trois valeurs (sans tenir compte de la casse).
- Rappel des règles : la roche brise les ciseaux, les ciseaux coupent le papier, le papier enveloppe la roche. Deux choix identiques donnent une égalité.
- Affiche le résultat de chaque manche, puis ajoute une description de la manche à une liste `historique` (par exemple `"roche vs ciseaux : gagné"`).
- À la fin, affiche le score (victoires, défaites, égalités), l'historique complet, puis le verdict de la partie.

*Exemple d'exécution :*

```text
Manche 1 - roche, papier ou ciseaux? roche
L'ordinateur a choisi roche : égalité!
Manche 2 - roche, papier ou ciseaux? lézard
Choix invalide.
Manche 2 - roche, papier ou ciseaux? PAPIER
L'ordinateur a choisi roche : gagné!
Manche 3 - roche, papier ou ciseaux? ciseaux
L'ordinateur a choisi roche : perdu!
Manche 4 - roche, papier ou ciseaux? roche
L'ordinateur a choisi papier : perdu!
Manche 5 - roche, papier ou ciseaux? papier
L'ordinateur a choisi roche : gagné!

Score : 2 victoire(s), 2 défaite(s), 1 égalité(s)
Historique :
  Manche 1 : roche vs roche : égalité
  Manche 2 : papier vs roche : gagné
  Manche 3 : ciseaux vs roche : perdu
  Manche 4 : roche vs papier : perdu
  Manche 5 : papier vs roche : gagné
Partie nulle!
```

## ⭐ Défi 2 : Anagramme

**But** : Mélanger les lettres d'un mot en passant par une liste.

**Énoncé** : L'ordinateur choisit un mot au hasard dans une liste d'au moins 10 mots, puis en mélange les lettres. Le joueur a 3 essais pour retrouver le mot d'origine.

- Le mot mélangé ne doit **jamais** être identique au mot d'origine : s'il l'est, mélange-le de nouveau.
- Une réponse vide n'est pas acceptée (elle ne compte pas comme un essai).
- La comparaison ne tient pas compte de la casse.
- Si le joueur échoue, révèle le mot à la fin.

> **Indices** :
>
> - `list(mot)` transforme une chaîne en liste de caractères, que `random.shuffle()` peut mélanger.
> - `"".join(lettres)` rassemble une liste de caractères en une seule chaîne.

*Exemple d'exécution :*

```text
Mot mélangé : EALAERIOT
Essai 1/3 :
La réponse ne peut pas être vide.
Essai 1/3 : rotaliea
Ce n'est pas ça.
Essai 2/3 : aleatoire
Bravo! Trouvé en 2 essai(s).
```

## ⭐ Défi 3 : Bulletin aléatoire

**But** : Générer une liste 2D de valeurs aléatoires et l'analyser par ligne et par colonne.

**Énoncé** : On veut tester un programme de bulletin sans saisir de vraies notes.

a. Génère une liste 2D `notes` de 6 lignes (étudiants) et 4 colonnes (évaluations), remplie de notes entières aléatoires entre 40 et 100. Les noms des étudiants sont dans une liste associée.

b. Affiche un tableau aligné : une ligne par étudiant avec ses 4 notes et sa moyenne (1 décimale), puis une dernière ligne avec la moyenne de chaque évaluation.

c. Indique l'étudiant qui a la meilleure moyenne et l'évaluation la plus difficile (celle qui a la moyenne la plus basse).

```python
NOMS = ["Léa", "Noah", "Ana", "Ben", "Chloé", "Dev"]
```

*Exemple de sortie :*

```text
Étudiant     Év1   Év2   Év3   Év4     Moy
Léa           90    76    92    45    75.8
Noah          71    88    56    42    64.2
Ana           40    49    82    77    62.0
Ben           70    88    87    63    77.0
Chloé         60    89    41    57    61.8
Dev           71    91    52    86    75.0
Moyenne     67.0  80.2  68.3  61.7

Meilleure moyenne : Ben (77.0)
Évaluation la plus difficile : Év4 (61.7)
```

## ⭐⭐ Défi 4 : Chasse au trésor

**But** : Utiliser une liste 2D pour afficher l'état d'un jeu et calculer une distance entre deux cases.

**Énoncé** : Un trésor est caché dans une case aléatoire d'une grille de 6 × 6. Le joueur a 8 essais pour le trouver.

- À chaque essai, affiche la grille : `?` pour une case inexplorée et `x` pour une case déjà essayée. Les lignes et les colonnes sont numérotées à partir de 1.
- Le joueur entre une ligne, puis une colonne. Chacune doit être un entier entre 1 et 6. Une case déjà essayée est refusée et ne compte pas comme un essai.
- Si le joueur trouve le trésor, affiche le nombre d'essais utilisés. Sinon, donne un indice selon la distance entre l'essai et le trésor :
    - distance de 1 : `Brûlant!`
    - distance de 2 : `Chaud!`
    - distance de 3 ou plus : `Froid.`
- À la fin de la partie, affiche la grille finale avec le trésor indiqué par un `T`.

La distance entre deux cases est le nombre de déplacements horizontaux et verticaux nécessaires pour aller de l'une à l'autre : `abs(ligne1 - ligne2) + abs(colonne1 - colonne2)`.

*Exemple d'exécution :*

```text

   1 2 3 4 5 6
1 : ? ? ? ? ? ?
2 : ? ? ? ? ? ?
3 : ? ? ? ? ? ?
4 : ? ? ? ? ? ?
5 : ? ? ? ? ? ?
6 : ? ? ? ? ? ?
Ligne (1 à 6) : 5
Colonne (1 à 6) : 1
Froid.

   1 2 3 4 5 6
1 : ? ? ? ? ? ?
2 : ? ? ? ? ? ?
3 : ? ? ? ? ? ?
4 : ? ? ? ? ? ?
5 : x ? ? ? ? ?
6 : ? ? ? ? ? ?
Ligne (1 à 6) : 3
Colonne (1 à 6) : 3
Chaud!

   1 2 3 4 5 6
1 : ? ? ? ? ? ?
2 : ? ? ? ? ? ?
3 : ? ? x ? ? ?
4 : ? ? ? ? ? ?
5 : x ? ? ? ? ?
6 : ? ? ? ? ? ?
Ligne (1 à 6) : 3
Colonne (1 à 6) : 3
Tu as déjà essayé cette case.
Ligne (1 à 6) : huit
Ce n'est pas un nombre entier.
Ligne (1 à 6) : 8
La ligne doit être entre 1 et 6.
Ligne (1 à 6) : 2
Colonne (1 à 6) : 5
Brûlant!

   1 2 3 4 5 6
1 : ? ? ? ? ? ?
2 : ? ? ? ? x ?
3 : ? ? x ? ? ?
4 : ? ? ? ? ? ?
5 : x ? ? ? ? ?
6 : ? ? ? ? ? ?
Ligne (1 à 6) : 2
Colonne (1 à 6) : 4
Trésor trouvé en 4 essai(s)!

Grille finale :
? ? ? ? ? ?
? ? ? T x ?
? ? x ? ? ?
? ? ? ? ? ?
x ? ? ? ? ?
? ? ? ? ? ?
```

## ⭐⭐ Défi 5 : Carte de bingo

**But** : Construire une liste 2D colonne par colonne et détecter une ligne ou une colonne complète.

**Énoncé** : Une carte de bingo compte 5 colonnes, identifiées par les lettres `B`, `I`, `N`, `G` et `O`, et 5 lignes. Chaque colonne contient 5 numéros différents tirés dans une plage qui lui est propre :

| Colonne | B | I | N | G | O |
| --- | --- | --- | --- | --- | --- |
| Numéros | 1 à 15 | 16 à 30 | 31 à 45 | 46 à 60 | 61 à 75 |

La case du centre (ligne 3, colonne `N`) est une case libre, déjà marquée au départ.

a. Génère une carte aléatoire et affiche-la sous ses lettres, avec `**` pour la case libre.

b. Simule le tirage : mélange les 75 boules, puis tire-les une à une. Chaque numéro tiré qui se trouve sur la carte est marqué. Dès qu'une **ligne** ou une **colonne** est complètement marquée, le tirage s'arrête.

c. Affiche les numéros tirés, le nombre de boules nécessaires, ce qui a été complété (par exemple `Ligne 2` ou `Colonne G`) et la carte finale, où les cases marquées sont remplacées par `X`.

> **Indices** :
>
> - `random.sample(range(debut, fin + 1), 5)` donne les 5 numéros d'une colonne. Comme la carte est une liste de **lignes**, place ensuite chaque numéro à la bonne ligne.
> - Garde une deuxième liste 2D de booléens, `marquees`, de la même taille que la carte.

*Exemple de sortie :*

```text
Carte :
   B   I   N   G   O
   8  18  39  54  63
  10  29  38  55  72
   6  26  **  57  68
   5  16  32  46  74
   3  21  36  52  67

Numéros tirés : 42 45 62 41 53 58 36 73 11 48 20 33 23 10 12 24 75 34 63 54 72 39 40 19 30 70 43 52 5 56 29 37 60 35 49 69 61 8 28 16 2 68 32 25 4 59 1 46 13 3 74
BINGO après 51 boules! (Ligne 4)

Carte finale :
   X  18   X   X   X
   X   X  38  55   X
   6  26   X  57   X
   X   X   X   X   X
   X  21   X   X  67
```
