# Exercices — La validation de données (fiche 5.3)

## 🟢 Exercice 1 : Facile

**But** : Appliquer la recette « Valider un entier ».

**Énoncé** : Demande à l'utilisateur combien d'enfants il a, en affichant `Ce n'est pas un nombre entier.` à chaque saisie invalide. Une fois la valeur obtenue, affiche `Vous avez X enfant(s).`

*Exemple d'exécution :*

```text
Combien d'enfants avez-vous ? deux
Ce n'est pas un nombre entier.
Combien d'enfants avez-vous ? 2
Vous avez 2 enfant(s).
```

## 🟢 Exercice 2 : Facile

**But** : Appliquer la recette « Valider un nombre réel ».

**Énoncé** : Demande le prix d'un article, en affichant `Ce n'est pas un nombre valide.` à chaque saisie invalide. Affiche ensuite `Le prix de l'article est de X $.` avec une précision de 2 décimales.

*Exemple d'exécution :*

```text
Entrez le prix de l'article : abc
Ce n'est pas un nombre valide.
Entrez le prix de l'article : 19.9
Le prix de l'article est de 19.90 $.
```

## 🟢 Exercice 3 : Facile

**But** : Appliquer la recette « Valider une chaîne non vide ».

**Énoncé** : Demande un nom d'utilisateur, en affichant `Le nom d'utilisateur ne peut pas être vide.` tant qu'il est vide (une chaîne composée uniquement d'espaces doit aussi être considérée comme vide). Affiche ensuite `Bienvenue, X !`

*Exemple d'exécution :*

```text
Entrez un nom d'utilisateur :
Le nom d'utilisateur ne peut pas être vide.
Entrez un nom d'utilisateur : alex01
Bienvenue, alex01 !
```

## 🟡 Exercice 4 : Moyen

**But** : Appliquer la recette « Valider un intervalle numérique ».

**Énoncé** : Demande une température en degrés Celsius. Affiche `Ce n'est pas un nombre entier.` si la saisie n'est pas un entier, ou `La température doit être entre -50 et 50.` si elle est hors intervalle. Affiche ensuite `Température enregistrée : X °C`

*Exemple d'exécution :*

```text
Entrez la température (-50 à 50) : chaud
Ce n'est pas un nombre entier.
Entrez la température (-50 à 50) : 120
La température doit être entre -50 et 50.
Entrez la température (-50 à 50) : -12
Température enregistrée : -12 °C
```

## 🟡 Exercice 5 : Moyen

**But** : Appliquer la recette « Valider l'appartenance à un ensemble de valeurs » avec des entiers.

**Énoncé** : Affiche un menu numéroté de 1 à 5 (le contenu des choix n'a pas d'importance). Demande à l'utilisateur son choix, en affichant `Ce n'est pas un nombre entier.` ou `Choix invalide.` selon le cas, tant qu'il n'a pas entré un nombre entier faisant partie de `1` à `5`. Affiche ensuite `Vous avez choisi l'option X.`

*Exemple d'exécution :*

```text
1. Option 1
2. Option 2
3. Option 3
4. Option 4
5. Option 5
Votre choix (1 à 5) : abc
Ce n'est pas un nombre entier.
Votre choix (1 à 5) : 9
Choix invalide.
Votre choix (1 à 5) : 3
Vous avez choisi l'option 3.
```

## 🟡 Exercice 6 : Moyen

**But** : Appliquer la recette « Valider l'appartenance à un ensemble de valeurs » avec des chaînes.

**Énoncé** : Demande à l'utilisateur de choisir un forfait parmi `bronze`, `argent` ou `or` (insensible à la casse), en affichant `Forfait invalide.` tant que la saisie ne correspond à aucun de ces trois choix. Affiche ensuite `Forfait sélectionné : X`

*Exemple d'exécution :*

```text
Choisissez un forfait (bronze, argent, or) : platine
Forfait invalide.
Choisissez un forfait (bronze, argent, or) : Argent
Forfait sélectionné : argent
```

## 🔴 Exercice 7 : Difficile

**But** : Combiner deux recettes différentes dans un même programme.

**Énoncé** : Affiche le menu suivant :

- `1` pour entrer une note d'examen ;
- `2` pour quitter.

Valide d'abord le choix du menu (recette « ensemble de valeurs », choix `1` ou `2`). Si l'utilisateur choisit `1`, demande une note et valide qu'elle est un entier compris entre 0 et 100 inclusivement (recette « intervalle »), puis affiche `Note entrée : X` avant de réafficher le menu. Le programme se termine lorsque l'utilisateur choisit `2`.

*Exemple d'exécution :*

```text
1. Entrer une note d'examen
2. Quitter
Votre choix : 5
Choix invalide.
Votre choix : 1
Entrez une note (0 à 100) : 150
La note doit être entre 0 et 100.
Entrez une note (0 à 100) : 87
Note entrée : 87
1. Entrer une note d'examen
2. Quitter
Votre choix : 2
```

## 🔴 Exercice 8 : Difficile

**But** : Choisir la bonne recette selon la situation décrite.

**Énoncé** : Pour chacune des situations suivantes, identifie la recette de la fiche 5.3 qui s'applique (par son numéro), puis écris le code correspondant. Chaque programme doit se terminer par l'affichage d'un message de confirmation.

**a.** L'utilisateur doit entrer une des quatre couleurs disponibles : `rouge`, `vert`, `bleu` ou `jaune`. Affiche ensuite `Couleur choisie : X`

**b.** L'utilisateur doit entrer son année de naissance, un nombre entier plus grand que 1900 et plus petit ou égal à 2026. Affiche ensuite `Année de naissance : X`

**c.** L'utilisateur doit entrer sa taille en mètres (un nombre avec décimales, par exemple `1.75`). Affiche ensuite `Taille : X m`

**d.** L'utilisateur doit entrer un mot de passe qui ne doit pas être vide. Affiche ensuite `Mot de passe enregistré.` (sans réafficher le mot de passe).

*Exemple d'exécution (pour la partie a) :*

```text
Choisissez une couleur (rouge, vert, bleu, jaune) : mauve
Couleur invalide.
Choisissez une couleur (rouge, vert, bleu, jaune) : Bleu
Couleur choisie : bleu
```
