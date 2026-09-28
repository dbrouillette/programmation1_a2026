# Exercices — La gestion des erreurs (fiche 5.2)

## 🟢 Exercice 1 : Facile

**But** : Écrire une première structure `try`/`except`.

**Énoncé** : Demande un nombre entier à l'utilisateur et affiche son carré. Si la saisie n'est pas un nombre entier valide, affiche `Ce n'est pas un nombre.` plutôt que de laisser le programme planter.

## 🟢 Exercice 2 : Facile

**But** : Cibler une exception précise autre que `ValueError`.

**Énoncé** : Demande deux nombres entiers à l'utilisateur et affiche le résultat de la division du premier par le second. Si le second nombre est `0`, affiche `Division par zéro impossible.` à l'aide d'un `except ZeroDivisionError`.

## 🟢 Exercice 3 : Facile

**But** : Reconnaître le type d'exception provoqué par une erreur.

**Énoncé** : Pour chacune des lignes suivantes, indique quel type d'exception serait levé (`ValueError`, `TypeError`, `ZeroDivisionError` ou `NameError`) si elle était exécutée seule. Aucun programme à exécuter : il s'agit d'un exercice d'écriture.

```python
a.  10 // 0
b.  "5" + 3
c.  print(x) # x n'est pas défini
d.  int("bonjour")
```

## 🟡 Exercice 4 : Moyen

**But** : Combiner `try`/`except` avec une boucle `while` et un drapeau.

**Énoncé** : Demande un nombre entier à l'utilisateur. Tant que la saisie n'est pas un nombre entier valide, affiche `Saisie invalide, réessayez.` et redemande-la. Affiche le nombre une fois qu'il est valide.

Contrainte : utilise un drapeau booléen nommé `valide`, initialisé à `False`, comme dans la fiche 5.1.

## 🟡 Exercice 5 : Moyen

**But** : Même si ce n'est pas recommandé dans le cours, appliquer le patron `while True:` / `break` avec `try`/`except`.

**Énoncé** : Reprends l'exercice 4, mais cette fois avec le patron `while True:` : la boucle se termine par un `break` placé immédiatement après une conversion réussie, à l'intérieur du `try`.

## 🟡 Exercice 6 : Moyen

**But** : Limiter le nombre de tentatives avec un compteur.

**Énoncé** : Demande un nombre entier à l'utilisateur, avec un maximum de **3 tentatives**. Après chaque saisie invalide, indique le nombre d'essais restants. Si les 3 essais sont épuisés sans succès, affiche `Trop d'erreurs, abandon.` Si une saisie valide est faite avant la fin des essais, affiche le nombre obtenu.

> **Indice** : combine un compteur `essais_restants` et un drapeau `valide` dans la condition du `while`, comme à l'exercice 12 de la fiche 5.1.

## 🟡 Exercice 7 : Moyen

**But** : Garder une boucle robuste face à des saisies invalides répétées.

**Énoncé** : Demande à l'utilisateur d'entrer des notes une à une, et calcule leur somme. L'utilisateur tape `fin` pour arrêter la saisie. Si une valeur entrée n'est ni un nombre entier ni `fin`, affiche `Valeur ignorée.` et continue à demander des notes, **sans planter et sans compter cette valeur**. Affiche la somme une fois `fin` reçu en entrée.

> **Indice** : le test d'arrêt (`fin`) doit se faire **avant** la conversion en entier, puisque `fin` n'est pas un nombre.

## 🔴 Exercice 8 : Difficile

**But** : Construire un menu robuste face à une saisie non numérique.

**Énoncé** : Crée un menu qui propose trois choix :

- `1` pour additionner deux nombres saisis par l'utilisateur ;
- `2` pour multiplier deux nombres saisis par l'utilisateur ;
- `3` pour quitter.

Le menu doit se réafficher tant que l'utilisateur n'a pas choisi `3`. Si l'utilisateur entre autre chose qu'un nombre entier (par exemple du texte), affiche `Choix invalide.` sans planter, puis réaffiche le menu.

**BONUS** : faire la gestion des erreurs complète pour les options 1 et 2.
