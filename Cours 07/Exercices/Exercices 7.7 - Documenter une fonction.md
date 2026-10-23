# Exercices — Documenter une fonction (fiche 7.7)

## 🟢 Exercice 1 : Facile

**But** : Distinguer un commentaire d'une docstring.

**Énoncé** : Voici six extraits tirés de différents programmes. Pour chacun, indique :

1. s'il s'agit d'un **commentaire**, d'une **docstring**, ou d'**aucun des deux**;
2. à qui il s'adresse : à la personne qui **lit le code** ou à celle qui **utilise la fonction** (ou le fichier);
3. s'il sera affiché par `help()` ou au survol dans VS Code.

**Extrait A**

```python
for i in range(1, len(lignes)):   # on commence à 1 : la ligne 0 est l'en-tête
    ...
```

**Extrait B**

```python
def calculer_taxes(montant):
    """Calcule la TPS et la TVQ sur un montant, arrondies au cent."""
    ...
```

**Extrait C** (tout en haut d'un fichier)

```python
"""Gestion des emprunts de la bibliothèque du cégep.

Permet d'emprunter, de retourner et de rechercher des livres.
"""

import random
```

**Extrait D**

```python
def calculer_moyenne(notes):
    total = 0
    """Additionne toutes les notes, puis divise par leur nombre."""
    for note in notes:
        total += note
    return total / len(notes)
```

**Extrait E**

```python
# TODO : valider que la liste n'est pas vide avant de diviser
```

**Extrait F**

```python
def afficher_regles():
    """Affiche les quatre règles de la bibliothèque, numérotées."""
    # Les règles ne changent jamais : on les affiche directement.
    print("1. Parler à voix basse.")
    ...
```

> 💡 Un des extraits est un piège : il a l'air d'une docstring, mais n'en est pas une. Lequel?

## 🟢 Exercice 2 : Facile

**But** : Reconnaître et corriger une mauvaise docstring.

**Énoncé** : Chacune des docstrings suivantes a un défaut. Nomme le défaut, puis réécris la docstring correctement (format Google lorsque la fonction a des paramètres ou une valeur de retour).

**Docstring A**

```python
def calculer_moyenne(notes):
    """calculer_moyenne"""
    return sum(notes) / len(notes)
```

**Docstring B**

```python
def convertir_en_fahrenheit(celsius):
    """Multiplie celsius par 9, divise le résultat par 5, puis ajoute 32."""
    return celsius * 9 / 5 + 32
```

**Docstring C**

```python
def calculer_prix_billet(age, est_etudiant=False, jour="semaine"):
    """Calcule le prix d'un billet de cinéma.

    Args:
        age (int): L'âge du client.

    Returns:
        float: Le prix du billet.
    """
    ...
```

**Docstring D**

```python
def valider_entier(msg_saisie, val_min, val_max):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché.
        minimum (int): La plus petite valeur acceptée.
        maximum (int): La plus grande valeur acceptée.

    Returns:
        float: Le nombre saisi.
    """
    ...
```

## 🟡 Exercice 3 : Moyen

**But** : Générer un patron de docstring avec autoDocstring, puis le compléter.

**Énoncé** : Les quatre fonctions ci-dessous viennent des séries 7.4 et 7.6. Elles sont écrites et testées, mais pas encore documentées.

```python
def valider_texte(msg_saisie, longueur_min=1, longueur_max=100):
    texte = input(msg_saisie).strip()
    while not longueur_min <= len(texte) <= longueur_max:
        print(f"Erreur : entrez entre {longueur_min} et {longueur_max} caractères.")
        texte = input(msg_saisie).strip()
    return texte


def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0


def trouver_min_max(valeurs):
    minimum = valeurs[0]
    maximum = valeurs[0]
    for valeur in valeurs:
        if valeur < minimum:
            minimum = valeur
        if valeur > maximum:
            maximum = valeur
    return minimum, maximum


def calculer_refroidissement(temperature, vitesse_vent):
    facteur_vent = vitesse_vent ** 0.16
    indice = 13.12 + 0.6215 * temperature - 11.37 * facteur_vent + 0.3965 * temperature * facteur_vent
    return round(indice)
```

1. Si ce n'est pas déjà fait, installe l'extension **autoDocstring** dans VS Code (voir la fiche 7.7).
2. Copie ces fonctions dans un fichier `documentation.py`.
3. Pour chaque fonction, place le curseur sur la ligne qui suit le `def`, tape `"""` puis `Entrée` (ou `Ctrl + Maj + 2`).
4. Remplis chaque patron : remplace `_summary_`, `_type_` et `_description_` (touche `Tab` pour passer au champ suivant). Les descriptions s'écrivent en français.
5. Vérifie ton travail en survolant le nom de chaque fonction dans VS Code.

*Patron généré pour `valider_texte()` (à compléter) :*

```python
def valider_texte(msg_saisie, longueur_min=1, longueur_max=100):
    """_summary_

    Args:
        msg_saisie (_type_): _description_
        longueur_min (int, optional): _description_. Defaults to 1.
        longueur_max (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: _description_
    """
```

> 💡 Pour `trouver_min_max()`, quel type indiquer dans `Returns:` quand la fonction renvoie deux valeurs?

## 🟡 Exercice 4 : Moyen

**But** : Utiliser une fonction inconnue en ne lisant que sa documentation.

**Énoncé** : Voici la ligne `def` et la docstring de trois fonctions. Leur code est caché (`...`). Sans connaître leur code, écris l'appel qui permet d'obtenir chacun des résultats demandés, en utilisant des arguments nommés lorsque c'est utile.

```python
def calculer_pourboire(montant, taux=0.15, arrondir=True):
    """Calcule le pourboire à laisser sur une addition.

    Args:
        montant (float): Le montant de l'addition, taxes incluses.
        taux (float, optional): Le taux du pourboire (ex. 0.18 pour 18 %). Par défaut 0.15.
        arrondir (bool, optional): Si True, arrondit le pourboire au dollar supérieur.
            Par défaut True.

    Returns:
        float: Le montant du pourboire, en dollars.
    """
    ...


def formater_telephone(numero, separateur="-"):
    """Met en forme un numéro de téléphone nord-américain de 10 chiffres.

    Args:
        numero (str): Les 10 chiffres du numéro, sans espaces ni symboles (ex. « 8193761721 »).
        separateur (str, optional): Le caractère placé entre les groupes de chiffres. Par défaut « - ».

    Returns:
        str: Le numéro mis en forme (ex. « 819-376-1721 »).
    """
    ...


def compter_lettre(texte, lettre, ignorer_casse=True):
    """Compte le nombre de fois qu'une lettre apparaît dans un texte.

    Args:
        texte (str): Le texte dans lequel on cherche.
        lettre (str): La lettre à compter (un seul caractère).
        ignorer_casse (bool, optional): Si True, les majuscules et les minuscules
            sont considérées comme identiques. Par défaut True.

    Returns:
        int: Le nombre d'occurrences de la lettre.
    """
    ...
```

a. Le pourboire de 18 % sur une addition de 42,60 $, arrondi au dollar supérieur.
b. Le pourboire au taux par défaut sur la même addition, **sans** arrondi.
c. Le numéro `8193761721` mis en forme avec des tirets.
d. Le même numéro, avec des espaces comme séparateur.
e. Le nombre de « r » dans « Trois-Rivières », sans tenir compte des majuscules.
f. Le nombre de « r » minuscules seulement dans « Trois-Rivières ».

Pour vérifier tes réponses, copie le contenu du fichier [fonctions_mystere.py](fonctions_mystere.py) en haut de ton programme, **sans lire le corps des fonctions**, puis affiche le résultat de chacun de tes appels. Survole aussi le nom des fonctions dans VS Code, ou appelle `help(calculer_pourboire)`, pour voir leur documentation.

## 🔴 Exercice 5 : Difficile

**But** : Garder une docstring à jour après une modification de la fonction.

**Énoncé** : La fonction `afficher_cadre()` a été améliorée : elle accepte maintenant un symbole et une marge (le nombre d'espaces entre le texte et le cadre). Son code fonctionne, mais sa docstring n'a pas été mise à jour.

```python
def afficher_cadre(texte, symbole="*", marge=1):
    """Affiche le texte entouré d'astérisques.

    Args:
        texte (str): Le texte à encadrer.

    Returns:
        str: Le texte encadré.
    """
    largeur = len(texte) + 2 * marge + 2
    print(symbole * largeur)
    print(symbole + " " * marge + texte + " " * marge + symbole)
    print(symbole * largeur)


afficher_cadre("Bienvenue!", "=", 3)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20afficher_cadre%28texte%2C%20symbole%3D%22%2A%22%2C%20marge%3D1%29%3A%0A%20%20%20%20%22%22%22Affiche%20le%20texte%20entour%C3%A9%20d%27ast%C3%A9risques.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20texte%20%28str%29%3A%20Le%20texte%20%C3%A0%20encadrer.%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20str%3A%20Le%20texte%20encadr%C3%A9.%0A%20%20%20%20%22%22%22%0A%20%20%20%20largeur%20%3D%20len%28texte%29%20%2B%202%20%2A%20marge%20%2B%202%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%20%20%20%20print%28symbole%20%2B%20%22%20%22%20%2A%20marge%20%2B%20texte%20%2B%20%22%20%22%20%2A%20marge%20%2B%20symbole%29%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%0A%0Aafficher_cadre%28%22Bienvenue%21%22%2C%20%22%3D%22%2C%203%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

```text
==================
=   Bienvenue!   =
==================
```

a. Trouve les **trois** problèmes de la docstring.
b. Réécris la docstring pour qu'elle décrive correctement la fonction.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.7 - Documenter une fonction](Solutions%207.7%20-%20Documenter%20une%20fonction.md).
