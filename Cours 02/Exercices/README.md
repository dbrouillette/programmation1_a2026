# Exercices — Cours 02

Les exercices sont classés **par niveau de difficulté**. Commence par le niveau *Facile* et monte graduellement : chaque niveau suppose que le précédent est acquis.

## Nomenclature

```
E2.4 - Opérateurs arithmétiques par niveaux.md
│ │
│ └── numéro séquentiel, du plus facile au plus difficile
└──── E = Exercice, 2 = Cours 02
```

Le corrigé de chaque exercice porte le **même nom suffixé de ` - RÉPONSES`**, dans le dossier [Corrige/](./Corrige/) qui reprend la même arborescence.

## 🟢 [1 - Facile](./1%20-%20Facile/)

Reconnaissance et application directe. Aucun calcul en chaîne.

|Exercice|Sections|Notion|
|---|:---:|---|
|[E2.1 — Noms de variables](./1%20-%20Facile/E2.1%20-%20Noms%20de%20variables.md)|2.2|Identifiants valides ou non|
|[E2.2 — Types de données](./1%20-%20Facile/E2.2%20-%20Types%20de%20données.md)|2.2|`int`, `float`, `bool`, `str`|
|[E2.3 — Opérateurs félins](./1%20-%20Facile/E2.3%20-%20Opérateurs%20félins.md)|2.4, 2.5|Mise en situation, une opération à la fois|

## 🟡 [2 - Moyen](./2%20-%20Moyen/)

Priorité des opérations, pièges de types, affectation combinée.

|Exercice|Sections|Notion|
|---|:---:|---|
|[E2.4 — Opérateurs arithmétiques par niveaux](./2%20-%20Moyen/E2.4%20-%20Opérateurs%20arithmétiques%20par%20niveaux.md)|2.4, 2.5|Prédire l'affichage, difficulté croissante|
|[E2.5 — La Chatterie du Ronron Doré](./2%20-%20Moyen/E2.5%20-%20La%20Chatterie%20du%20Ronron%20Doré.md)|2.4, 2.5|Parcours ludique complet + petit programme|

## 🔴 [3 - Difficile](./3%20-%20Difficile/)

Expressions longues, cas limites, valeurs négatives.

|Exercice|Sections|Notion|
|---|:---:|---|
|[E2.6 — Expressions indépendantes](./3%20-%20Difficile/E2.6%20-%20Expressions%20indépendantes.md)|2.4, 2.5|10 expressions autonomes, niveaux avancé à expert|
|[E2.7 — Expressions cumulatives](./3%20-%20Difficile/E2.7%20-%20Expressions%20cumulatives.md)|2.4, 2.5|État partagé entre les 10 étapes, dont une exception|

> ⚠️ **E2.7 est le plus exigeant** : les résultats se propagent d'une ligne à l'autre, et une étape provoque volontairement une `ZeroDivisionError`. Fais-le en dernier.

## ⚙️ [4 - Ateliers autocorrigés](./4%20-%20Ateliers%20autocorrigés/)

Deux ateliers d'une heure, corrigés automatiquement par des tests unitaires.

|Atelier|Sections|Durée|Fichier à compléter|
|---|:---:|:---:|---|
|[Exercice 1 — Structure, variables et constantes](./4%20-%20Ateliers%20autocorrigés/Exercice%201%20-%20Structure,%20variables%20et%20constantes.md)|2.1 à 2.3|60 min|`exercice_1.py`|
|[Exercice 2 — Opérateurs et erreurs de syntaxe](./4%20-%20Ateliers%20autocorrigés/Exercice%202%20-%20Opérateurs%20et%20erreurs%20de%20syntaxe.md)|2.4 à 2.6|60 min|`exercice_2.py`, `exercice_2_debogage.py`|

### Marche à suivre

**1. Récupérer les fichiers**

```bash
git clone <adresse-du-depot>
cd "programmation1_a2026/Cours 02/Exercices/4 - Ateliers autocorrigés"
```

Si tu as déjà cloné le dépôt, mets-le simplement à jour :

```bash
git pull
```

**2. Compléter l'atelier**

Ouvre le fichier `.py` correspondant et remplace chaque `None` par ta réponse. **Ne renomme aucune variable** : les tests s'appuient sur ces noms exacts.

**3. Se corriger**

⚠️ **Place-toi d'abord dans le dossier `4 - Ateliers autocorrigés`.** C'est l'erreur la plus fréquente :

```bash
cd "Cours 02/Exercices/4 - Ateliers autocorrigés"
python -m unittest test_exercice_1.py
python -m unittest test_exercice_2.py
```

Si tu lances la commande depuis un autre dossier, tu obtiendras :

```text
ModuleNotFoundError: No module named 'test_exercice_1'
```

Ce message ne veut **pas** dire que ton travail est mauvais : Python ne trouve simplement pas le fichier. Fais `cd` dans le bon dossier et relance.

**Méthode qui fonctionne depuis n'importe où** — donne le chemin complet du fichier de test :

```bash
python "Cours 02/Exercices/4 - Ateliers autocorrigés/test_exercice_1.py"
```

Ajoute `-v` pour voir le résultat de chaque test un par un :

```bash
python -m unittest -v test_exercice_1.py
```

Pour lancer les deux suites d'un coup :

```bash
python -m unittest discover -p "test_*.py"
```

**3bis. Affichage coloré (recommandé)**

Le lanceur `verifier.py` affiche **en vert** chaque test réussi et en rouge ceux qui restent à faire, avec une barre de progression :

```bash
python verifier.py        # les deux ateliers
python verifier.py 1      # atelier 1 seulement
python verifier.py 2      # atelier 2 seulement
```

```text
  Partie A - Questions a choix multiple
    [OK] A1 - Nombre d'instructions
    [  ] A2 - Sensibilite a la casse
        >>> A2 - La bonne reponse est B) Python est sensible a la casse.
        >>> Pour Python, 'Print' et 'print' sont deux noms differents.
        >>> (revois la section 2.1 - Python est sensible a la casse)

  ##############################  20 / 20

  Bravo! Tout est reussi (46/46).
```

Lui aussi doit être lancé depuis le dossier `4 - Ateliers autocorrigés`.

**4. Lire le résultat et te corriger**

**Les messages d'erreur sont ton corrigé.** Chaque test raté explique la bonne réponse et te renvoie à la section de théorie concernée :

```text
FAIL: test_a4_division_entiere_negative
----------------------------------------------------------------------
AssertionError: -3 != -4 :

>>> A4 - -17 // 5 vaut -4
>>> C'est le piege classique : // tronque vers le BAS (vers l'infini negatif),
>>> pas vers zero. -17 / 5 donne -3.4, et l'entier immediatement INFERIEUR
>>> a -3.4 est -4, pas -3.
>>> (revois la section 2.4 - Remarques importantes)
```

Tant qu'une réponse vaut `None`, le test dit simplement que la question n'a pas été répondue : **tente d'abord ta chance**, l'explication apparaît ensuite.

Quand tout est réussi :

```text
Ran 20 tests in 0.021s

OK
```

`OK` signifie que tout est réussi : 20 tests pour l'atelier 1, 26 pour l'atelier 2.

## Notes

- Aucune installation n'est requise : `unittest` fait partie de la bibliothèque standard de Python.
- Les fichiers `test_*.py` et `verifier.py` **ne doivent pas être modifiés** : ils servent à la correction.
- Un test qui échoue n'efface rien de ton travail — relance-le autant de fois que nécessaire.
- Les exercices n'utilisent que des notions vues aux sections 2.1 à 2.6 : ni conditions, ni boucles, ni fonctions.
- Le dossier [Corrige/](./Corrige/) contient les solutions complètes et le barème suggéré.
