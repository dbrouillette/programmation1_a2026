# Exercices — La boucle `while` (fiche 5.1)

## 🟢 Exercice 1 : Facile

**But** : Écrire une première boucle `while` avec un compteur.

**Énoncé** : Écris un programme qui affiche un compte à rebours de 10 à 1 (un nombre par ligne), puis affiche `Décollage !` à la fin.

## 🟢 Exercice 2 : Facile

**But** : Utiliser une boucle `while` pour valider une saisie.

**Énoncé** : Demande à l'utilisateur d'entrer une note entière entre 0 et 100 inclusivement. Tant que la valeur entrée n'est pas dans cet intervalle, redemande-la avec un message d'erreur. Affiche la note une fois qu'elle est valide.

## 🟢 Exercice 3 : Facile

**But** : Écrire correctement une condition portant sur un booléen.

**Énoncé** : Réécris chacune des lignes suivantes sous sa forme recommandée, sans changer son comportement. Aucun programme à exécuter : il s'agit d'un exercice d'écriture.

```python
a.  while continuer == True:
b.  while trouve == False:
c.  while partie_terminee != True:
d.  continuer = True if reponse == "o" else False
```

## 🟢 Exercice 4 : Facile-Moyen

**But** : Utiliser la variable de contrôle comme compteur.

**Énoncé** : Demande à l'utilisateur un nombre entier entre 1 et 12 (valide la saisie). Affiche ensuite sa table de multiplication de 1 à 12, une ligne par produit, sous la forme `7 x 3 = 21`. La boucle d'affichage doit être une boucle `while`.

## 🟢 Exercice 5 : Facile-Moyen

**But** : Appliquer le patron `while True:` / `break`.

**Énoncé** : Demande un mot de passe à l'utilisateur, encore et encore, jusqu'à ce qu'il entre `python123`. Utilise le patron `while True:` avec un `break`. Affiche `Accès refusé.` après chaque tentative ratée et `Accès autorisé !` à la sortie de la boucle.

## 🟢 Exercice 6 : Facile-Moyen

**But** : Utiliser une variable de contrôle **booléenne**.

**Énoncé** : Écris un programme qui demande un nombre à l'utilisateur et affiche son carré, puis lui demande `Un autre ? (o/n)`. Le programme recommence tant que l'utilisateur répond `o`.

Contraintes :

- la variable de contrôle doit être un booléen nommé `continuer`, initialisé à `True` ;
- elle doit être mise à jour par une **affectation directe du résultat d'une comparaison** (pas de `if`) ;
- interdit d'utiliser `break` ; interdit d'écrire `while continuer == True:`.

## 🟡 Exercice 7 : Moyen

**But** : Accumuler des valeurs jusqu'à une sentinelle.

**Énoncé** : Demande à l'utilisateur d'entrer des notes une à une. L'utilisateur entre `-1` pour arrêter. Calcule et affiche la moyenne des notes entrées (en excluant le `-1`). Si aucune note n'a été entrée, affiche `Aucune note entrée.` plutôt que de faire une division par zéro.

## 🟡 Exercice 8 : Moyen

**But** : Sauter une itération avec `continue`.

**Énoncé** : Demande à l'utilisateur 10 nombres entiers. Additionne uniquement les nombres **positifs** : si le nombre entré est négatif ou nul, affiche `Ignoré.` et passe au suivant à l'aide de `continue`. À la fin, affiche la somme des nombres retenus.

## 🟡 Exercice 9 : Moyen

**But** : Construire un menu qui se répète.

**Énoncé** : Crée un menu qui propose deux choix :

- `1` pour additionner deux nombres saisis par l'utilisateur ;
- `2` pour quitter.

Le menu doit se réafficher tant que l'utilisateur n'a pas choisi `2`. Un choix invalide affiche un message d'erreur, puis le menu réapparaît.

## 🟡 Exercice 10 : Moyen

**But** : Lever un **drapeau** depuis l'intérieur de la boucle.

**Énoncé** : L'utilisateur entre des caractères un à la fois. La boucle s'arrête dès qu'il entre une **voyelle** (`a`, `e`, `i`, `o`, `u`, `y`, sans tenir compte de la casse ni des accents). Affiche ensuite combien de caractères ont été entrés en tout, voyelle comprise.

Contraintes : utilise un drapeau booléen nommé `voyelle_trouvee`, initialisé à `False`, et une boucle qui commence par `while not voyelle_trouvee:`. Pas de `break`.

## 🟡 Exercice 11 : Moyen

**But** : Conserver un maximum et un minimum au fil des itérations.

**Énoncé** : Demande des nombres à l'utilisateur un à la fois. La saisie s'arrête lorsqu'il entre `0`. Affiche ensuite le plus grand et le plus petit des nombres entrés (sans compter le `0`). Si aucun nombre n'a été entré, affiche `Aucun nombre entré.`

## 🟡 Exercice 12 : Moyen

**But** : Combiner un compteur et un drapeau dans une **condition composée**.

**Énoncé** : Reprends l'exercice 5, mais l'utilisateur n'a droit qu'à **3 essais**. Indique à chaque tentative ratée le nombre d'essais qu'il lui reste. Après le troisième échec, affiche `Compte bloqué.`

Contraintes : la boucle doit s'arrêter **par sa condition seulement**, sans `break`. Il te faut donc un compteur `essais_restants` et un drapeau `acces_autorise`, combinés avec `and` dans l'en-tête du `while`.

> **Indice** : après la boucle, le drapeau est toujours là. Il permet de savoir si on en est sorti par un bon mot de passe ou parce qu'il n'y avait plus d'essais — ce qu'un `break` seul ne dirait pas.

## 🟡 Exercice 13 : Moyen-Difficile

**But** : Répéter jusqu'à l'atteinte d'un objectif.

**Énoncé** : Le programme choisit un nombre secret fixe (par exemple `42`). Demande à l'utilisateur de deviner ce nombre. Tant que sa réponse est incorrecte, indique si le nombre à trouver est plus grand ou plus petit que sa réponse, puis redemande un essai. Affiche `Bravo, vous avez trouvé !` à la fin.

## 🔴 Exercice 14 : Moyen-Difficile

**But** : Utiliser une boucle `while` pour décomposer un nombre.

**Énoncé** : Demande un entier positif à l'utilisateur, puis calcule la somme de ses chiffres à l'aide d'une boucle `while` (par exemple, `472` donne `4 + 7 + 2 = 13`).

> **Indice** : `nombre % 10` donne le dernier chiffre et `nombre // 10` retire ce dernier chiffre. Répète tant que `nombre > 0`.

## 🔴 Exercice 15 : Difficile

**But** : Imbriquer deux boucles `while` pilotées par des booléens.

**Énoncé** : Améliore le jeu de l'exercice 13 :

a. Compte le nombre d'essais et affiche-le à la fin (`Trouvé en 4 essais.`).
b. Une fois le nombre trouvé, demande à l'utilisateur s'il veut rejouer (`o`/`n`) et recommence une partie complète s'il répond `o`.

Contraintes : les deux boucles doivent être pilotées par des variables de contrôle **booléennes** (`rejouer` pour la partie externe, `trouve` pour la partie interne), et non par des comparaisons de chaînes ou de nombres dans l'en-tête du `while`.
