# Exercices — Les listes (fiche 6.2)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande.

## 🟢 Exercice 1 : Facile

**But** : Accéder aux éléments d'une liste par index et par tranche.

**Énoncé** : Sans exécuter de code, donne la valeur de chacune des expressions suivantes. Vérifie ensuite tes réponses dans VS Code.

```python
valeurs = [5, 10, 15, 20, 25, 30]

a.  valeurs[1]
b.  valeurs[-2]
c.  valeurs[1:4]
d.  valeurs[:3]
e.  valeurs[::-1]
f.  len(valeurs)
g.  15 in valeurs
h.  valeurs.index(20)
i.  valeurs[6]
```

## 🟢 Exercice 2 : Facile

**But** : Suivre l'effet des méthodes qui modifient une liste.

**Énoncé** : Sans exécuter de code, donne le contenu de la liste `sac` **après chaque ligne**, ainsi que la valeur de `objet` à la fin.

```python
sac = ["gourde", "livre"]
sac.append("crayon")
sac.insert(1, "lunch")
sac.remove("livre")
sac[0] = "bouteille"
objet = sac.pop()
sac.append(objet.upper())
```

## 🟢 Exercice 3 : Facile

**But** : Construire une liste avec `append()` dans une boucle `for`.

**Énoncé** : Demande à l'utilisateur 4 articles d'épicerie (non vides) et range-les dans une liste. Affiche ensuite la liste numérotée à partir de 1, puis le nombre d'articles.

*Exemple d'exécution :*

```text
Article 1 : lait
Article 2 :
L'article ne peut pas être vide.
Article 2 : pain
Article 3 : pommes
Article 4 : fromage

Liste d'épicerie :
1. lait
2. pain
3. pommes
4. fromage
4 articles
```

## 🟢 Exercice 4 : Facile-Moyen

**But** : Utiliser les fonctions natives sur une liste de nombres.

**Énoncé** : Demande 5 nombres entiers à l'utilisateur et range-les dans une liste. Affiche ensuite, à l'aide des fonctions et méthodes de la fiche (aucune boucle pour les calculs) :

- la liste telle que saisie;
- la somme, la moyenne (2 décimales), le minimum et le maximum;
- la liste triée en ordre croissant, puis en ordre décroissant;
- la liste originale une dernière fois, pour montrer qu'elle n'a **pas** été modifiée.

*Exemple d'exécution :*

```text
Nombre 1 : 12
Nombre 2 : -4
Nombre 3 : trente
Ce n'est pas un nombre entier.
Nombre 3 : 37
Nombre 4 : 8
Nombre 5 : 21
Liste : [12, -4, 37, 8, 21]
Somme : 74
Moyenne : 14.80
Minimum : -4 | Maximum : 37
Croissant : [-4, 8, 12, 21, 37]
Décroissant : [37, 21, 12, 8, -4]
Originale : [12, -4, 37, 8, 21]
```

## 🟡 Exercice 5 : Moyen

**But** : Parcourir une liste pour calculer soi-même une somme, un minimum et un maximum.

**Énoncé** : Avec la liste ci-dessous, calcule et affiche la somme, le minimum, le maximum ainsi que **l'index** du maximum.

Contrainte : n'utilise **aucune** des fonctions `sum()`, `min()`, `max()` ni la méthode `index()`.

```python
ventes = [420, 385, 510, 290, 610, 475, 330]
```

*Sortie attendue :*

```text
Somme : 3020
Minimum : 290
Maximum : 610 (index 4)
```

## 🟡 Exercice 6 : Moyen

**But** : Filtrer une liste en deux nouvelles listes.

**Énoncé** : À partir de la liste de notes ci-dessous, construis deux nouvelles listes : `reussites` (notes de 60 et plus) et `echecs` (notes sous 60). Affiche les deux listes, puis le taux de réussite en pourcentage (1 décimale).

```python
notes = [78, 45, 92, 58, 88, 60, 34, 71, 59, 83]
```

*Sortie attendue :*

```text
Réussites : [78, 92, 88, 60, 71, 83]
Échecs : [45, 58, 34, 59]
Taux de réussite : 60.0 %
```

## 🟡 Exercice 7 : Moyen

**But** : Modifier les éléments d'une liste par leur index.

**Énoncé** : Une boutique applique un rabais de 20 % sur tous ses prix de plus de 50 $. Les autres prix ne changent pas.

a. Modifie **directement** la liste `prix` ci-dessous (ne crée pas de nouvelle liste). Arrondis chaque nouveau prix à 2 décimales.

b. Affiche la liste avant et après les rabais, ainsi que le nombre de prix modifiés.

```python
prix = [19.99, 74.50, 120.00, 49.99, 55.00, 8.25]
```

*Sortie attendue :*

```text
Avant : [19.99, 74.5, 120.0, 49.99, 55.0, 8.25]
Après : [19.99, 59.6, 96.0, 49.99, 44.0, 8.25]
Prix modifiés : 3
```

## 🟡 Exercice 8 : Moyen

**But** : Gérer une liste à l'aide d'un menu.

**Énoncé** : Crée un petit gestionnaire de liste de tâches avec le menu suivant, qui se réaffiche tant que l'utilisateur ne choisit pas `4` :

```text
1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
```

- Le choix du menu doit être validé : seuls `1`, `2`, `3` et `4` sont acceptés.
- Une tâche vide ne doit pas être acceptée.
- Pour retirer une tâche, l'utilisateur entre son **numéro** (à partir de 1). Le numéro doit être un entier qui correspond à une tâche existante. Affiche la tâche retirée.
- Si la liste est vide, les options 2 et 3 affichent `Aucune tâche.`

*Exemple d'exécution :*

```text
1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 1
Tâche : Faire le TP2

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 1
Tâche :
Une tâche ne peut pas être vide.
Tâche : Étudier pour le quiz

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 1
Tâche : Lire la fiche 6.3

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 3
1. Faire le TP2
2. Étudier pour le quiz
3. Lire la fiche 6.3

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 7
Choix invalide.
Choix : 2
Numéro de la tâche à retirer (1 à 3) : deux
Ce n'est pas un nombre entier.
Numéro de la tâche à retirer (1 à 3) : 5
Ce numéro n'existe pas.
Numéro de la tâche à retirer (1 à 3) : 1
Tâche retirée : Faire le TP2

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 3
1. Étudier pour le quiz
2. Lire la fiche 6.3

1. Ajouter une tâche
2. Retirer une tâche
3. Afficher les tâches
4. Quitter
Choix : 4

Au revoir!
```

## 🟡 Exercice 9 : Moyen

**But** : Travailler avec deux listes associées par leur index.

**Énoncé** : Un inventaire est représenté par deux listes de même longueur : les noms des produits et les quantités en stock.

```python
produits = ["vis", "clous", "boulons", "écrous", "rondelles"]
quantites = [250, 0, 75, 0, 410]
```

a. Affiche l'inventaire sous forme de tableau aligné.

b. Affiche la liste des produits en rupture de stock (quantité 0) et le nombre total d'unités en stock.

c. Demande un produit (non vide) à l'utilisateur et affiche sa quantité, ou `Produit inconnu.` s'il n'existe pas.

*Exemple d'exécution :*

```text
vis           250
clous           0
boulons        75
écrous          0
rondelles     410
Rupture de stock : clous, écrous
Total en stock : 735
Produit recherché :
Le nom du produit ne peut pas être vide.
Produit recherché : boulons
boulons : 75 en stock
```

## 🔴 Exercice 10 : Moyen-Difficile

**But** : Construire une liste sans doublons et compter des occurrences.

**Énoncé** : Demande une phrase (non vide) à l'utilisateur. Affiche ensuite chaque mot **distinct** de la phrase (sans tenir compte de la casse), dans l'ordre de sa première apparition, avec son nombre d'occurrences.

> **Indice** : découpe la phrase avec `split()`, puis construis une liste `mots_distincts` en n'ajoutant un mot que s'il n'y est pas déjà (`not in`). La méthode `count()` fera le reste.

*Exemple d'exécution :*

```text
Phrase :
La phrase ne peut pas être vide.
Phrase : Le chat voit le chien et le chien voit le chat
le      4
chat    2
voit    2
chien   2
et      1
```
