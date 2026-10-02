# Exercices — La boucle `for` (fiche 6.1)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande.

## 🟢 Exercice 1 : Facile

**But** : Utiliser `range()` avec deux et trois arguments.

**Énoncé** : Écris un programme qui affiche, à l'aide de **deux boucles `for`** :

a. les nombres de 1 à 20, sur une même ligne;

b. les nombres impairs de 1 à 19, sur une même ligne.

*Sortie attendue :*

```text
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1 3 5 7 9 11 13 15 17 19
```

## 🟢 Exercice 2 : Facile

**But** : Prédire la suite produite par `range()`.

**Énoncé** : Sans exécuter de code, écris la suite de nombres produite par chacun des appels suivants. Si la suite est vide, écris « vide ». Vérifie ensuite tes réponses dans VS Code.

```python
a.  range(3, 8)
b.  range(4)
c.  range(10, 0, -3)
d.  range(5, 5)
e.  range(0, 10, 4)
f.  range(10, 20, -1)
```

## 🟢 Exercice 3 : Facile

**But** : Répéter un traitement un nombre de fois connu.

**Énoncé** : Reprends l'exercice 4 de la fiche 5.1, mais avec une boucle `for` : demande un nombre entier entre 1 et 12 à l'utilisateur, puis affiche sa table de multiplication de 1 à 12, une ligne par produit, sous la forme `7 x 3 = 21`. Les nombres doivent être alignés à droite.

*Exemple d'exécution :*

```text
Entrez un nombre (1 à 12) : sept
Ce n'est pas un nombre entier.
Entrez un nombre (1 à 12) : 15
Le nombre doit être entre 1 et 12.
Entrez un nombre (1 à 12) : 7
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
7 x 11 =  77
7 x 12 =  84
```

## 🟢 Exercice 4 : Facile-Moyen

**But** : Convertir une boucle `while` en boucle `for`.

**Énoncé** : Réécris chacune des boucles suivantes avec une boucle `for`, en conservant **exactement** la même sortie.

```python
# a.
i = 0
while i < 5:
    print(i)
    i += 1

# b.
compteur = 1
while compteur <= 100:
    print(compteur)
    compteur += 11

# c.
n = 50
while n > 0:
    print(n)
    n -= 10
```

## 🟡 Exercice 5 : Moyen

**But** : Convertir une boucle `for` en boucle `while`.

**Énoncé** : Réécris chacune des boucles suivantes avec une boucle `while`, en conservant **exactement** la même sortie. N'oublie pas l'initialisation et la mise à jour!

```python
# a.
for x in range(3, 16, 3):
    print(x)

# b.
for k in range(20, 9, -2):
    print(k)

# c.
mot = "boucle"
for i in range(len(mot)):
    print(i, mot[i])
```

## 🟡 Exercice 6 : Moyen

**But** : Accumuler une somme et conserver un maximum et un minimum.

**Énoncé** : Demande à l'utilisateur combien de notes il veut entrer (au moins 1), puis demande chacune des notes (`Note 1 :`, `Note 2 :`, etc.). Chaque note est un nombre réel entre 0 et 100. Affiche ensuite la moyenne (1 décimale), la note la plus haute et la note la plus basse.

Contrainte : n'utilise **pas** les fonctions `max()` et `min()`.

> **Indice** : initialise le maximum à la plus petite note possible et le minimum à la plus grande. La première note saisie remplacera forcément les deux.

*Exemple d'exécution :*

```text
Combien de notes? 0
Il faut au moins 1 note.
Combien de notes? 4
Note 1 : 78
Note 2 : abc
Ce n'est pas un nombre valide.
Note 2 : 92
Note 3 : 105
La note doit être entre 0 et 100.
Note 3 : 65
Note 4 : 88
Moyenne : 80.8
Note la plus haute : 92.0
Note la plus basse : 65.0
```

## 🟡 Exercice 7 : Moyen

**But** : Parcourir un intervalle défini par l'utilisateur.

**Énoncé** : Demande deux entiers `a` et `b` à l'utilisateur. Calcule et affiche séparément la somme des nombres **pairs** et la somme des nombres **impairs** compris entre `a` et `b` inclusivement.

Si l'utilisateur entre `a` plus grand que `b`, inverse les deux valeurs avant de faire le calcul.

*Exemple d'exécution :*

```text
Premier nombre : dix
Ce n'est pas un nombre entier.
Premier nombre : 10
Deuxième nombre : 1
Entre 1 et 10 :
Somme des pairs : 30
Somme des impairs : 25
```

## 🟡 Exercice 8 : Moyen

**But** : Construire une nouvelle chaîne caractère par caractère.

**Énoncé** : Demande une phrase (non vide) à l'utilisateur et construis une nouvelle chaîne dans laquelle chaque voyelle (`a`, `e`, `i`, `o`, `u`, `y`, majuscule ou minuscule) est remplacée par `*`. Affiche la nouvelle chaîne et le nombre de voyelles remplacées.

Contrainte : n'utilise **pas** la méthode `replace()`.

*Exemple d'exécution :*

```text
Phrase :
La phrase ne peut pas être vide.
Phrase : Les boucles sont Utiles
L*s b**cl*s s*nt *t*l*s
Voyelles remplacées : 8
```

## 🟡 Exercice 9 : Moyen

**But** : Comparer des caractères à l'aide de leurs index.

**Énoncé** : Un **palindrome** est un mot qui se lit de la même façon dans les deux sens (`radar`, `kayak`, `été`).

Demande un mot (non vide) à l'utilisateur et détermine s'il s'agit d'un palindrome, **sans** utiliser le slicing `[::-1]`. Compare plutôt le premier caractère avec le dernier, le deuxième avec l'avant-dernier, etc. Dès qu'une paire diffère, arrête la boucle avec `break`.

La comparaison ne doit pas tenir compte de la casse (`Kayak` est un palindrome).

> **Indice** : le caractère « miroir » de `mot[i]` est `mot[len(mot) - 1 - i]`. Il suffit de parcourir la **moitié** du mot.

*Exemple d'exécution :*

```text
Mot :
Le mot ne peut pas être vide.
Mot : Kayak
C'est un palindrome.
```

## 🔴 Exercice 10 : Difficile

**But** : Utiliser l'index d'un caractère dans une chaîne de référence.

**Énoncé** : Le **chiffrement de César** décale chaque lettre d'un message d'un certain nombre de positions dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e`, … et `x` devient `a` (on recommence au début de l'alphabet).

Demande un message (non vide, en minuscules, sans accents) et un décalage (entier), puis affiche le message chiffré. Les caractères qui ne sont pas des lettres (espaces, ponctuation) restent inchangés.

> **Indices** :
>
> - Utilise la constante `ALPHABET = "abcdefghijklmnopqrstuvwxyz"`.
> - `ALPHABET.find(lettre)` donne la position d'une lettre (ou `-1` si ce n'est pas une lettre).
> - L'opérateur modulo (`% len(ALPHABET)`) permet de « revenir au début » de l'alphabet.

*Exemple d'exécution :*

```text
Message :
Le message ne peut pas être vide.
Message : vive python!
Décalage : trois
Ce n'est pas un nombre entier.
Décalage : 3
Message chiffré : ylyh sbwkrq!
```

**Bonus** : déchiffre le message `oh frxuv hvw ilql` (décalage de 3). Que remarques-tu si tu utilises un décalage de `-3`?
