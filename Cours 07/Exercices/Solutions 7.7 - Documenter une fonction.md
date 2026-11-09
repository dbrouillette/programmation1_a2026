# Solutions — Documenter une fonction (fiche 7.7)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Extrait | Nature | S'adresse à… | Affiché par `help()` / survol? |
| --- | --- | --- | --- |
| A | Commentaire | la personne qui **lit le code** : il explique un détail de fonctionnement | ❌ Non |
| B | Docstring de fonction | la personne qui **utilise** la fonction | ✅ Oui |
| C | Docstring de fichier (module) | la personne qui **utilise** le fichier | ✅ Oui (`help()` sur le module, ou au survol de l'`import`) |
| D | **Aucun des deux** | personne | ❌ Non |
| E | Commentaire | la personne qui **lit le code** (ici, un rappel pour le programmeur) | ❌ Non |
| F | Une docstring (1re ligne du corps) **et** un commentaire (2e ligne) | la docstring : l'**utilisateur**; le commentaire : le **lecteur du code** | ✅ La docstring seulement |

- L'extrait **D** est le piège : une chaîne entre `"""` n'est une docstring que si elle est la **toute première** instruction du corps de la fonction (ou du fichier). Placée après `total = 0`, c'est une simple chaîne que Python évalue et ignore. Pour expliquer le fonctionnement, il fallait un commentaire `#`.
- L'extrait **F** montre que les deux se complètent : la docstring dit **ce que fait** la fonction; le commentaire explique **un choix** dans son code.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

**A. Elle répète le nom de la fonction** et n'apprend rien. Elle ne mentionne ni le paramètre ni la valeur renvoyée.

```python
def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes.

    Args:
        notes (list): Les notes, une liste non vide de nombres.

    Returns:
        float: La moyenne des notes.
    """
    return sum(notes) / len(notes)
```

**B. Elle décrit le code ligne par ligne** au lieu de dire ce que fait la fonction. Celui qui utilise la fonction veut savoir qu'elle convertit des °C en °F, pas comment.

```python
def convertir_en_fahrenheit(celsius):
    """Convertit une température de degrés Celsius en degrés Fahrenheit.

    Args:
        celsius (float): La température en °C.

    Returns:
        float: La température en °F.
    """
    return celsius * 9 / 5 + 32
```

**C. Elle oublie deux paramètres** (`est_etudiant` et `jour`), justement ceux qui sont optionnels et dont il faut connaître les valeurs possibles.

```python
def calculer_prix_billet(age, est_etudiant=False, jour="semaine"):
    """Calcule le prix d'un billet de cinéma.

    Args:
        age (int): L'âge du client.
        est_etudiant (bool, optional): True si le client a sa carte étudiante. Par défaut False.
        jour (str, optional): Le jour de la séance; « mardi » donne droit au rabais.
            Par défaut « semaine ».

    Returns:
        float: Le prix du billet.
    """
```

**D. Elle n'est plus à jour** : les noms des paramètres ont changé (`msg_saisie`, `val_min`, `val_max`), et la fonction renvoie un `int`, pas un `float`.

```python
def valider_entier(msg_saisie, val_min, val_max):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        msg_saisie (str): Le message affiché à l'utilisateur.
        val_min (int): La plus petite valeur acceptée.
        val_max (int): La plus grande valeur acceptée.

    Returns:
        int: L'entier saisi, compris entre val_min et val_max.
    """
```

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

Le code des fonctions ne change pas; seules les docstrings sont ajoutées (le corps est remplacé ici par `...`).

```python
def valider_texte(msg_saisie, longueur_min=1, longueur_max=100):
    """Demande un texte jusqu'à ce que sa longueur soit valide.

    Les espaces au début et à la fin de la saisie sont retirées.

    Args:
        msg_saisie (str): Le message affiché à l'utilisateur.
        longueur_min (int, optional): Le nombre minimal de caractères. Par défaut 1.
        longueur_max (int, optional): Le nombre maximal de caractères. Par défaut 100.

    Returns:
        str: Le texte saisi, sans espaces superflues.
    """
    ...


def est_bissextile(annee):
    """Indique si une année est bissextile (calendrier grégorien).

    Args:
        annee (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, False sinon.
    """
    ...


def trouver_min_max(valeurs):
    """Trouve la plus petite et la plus grande valeur d'une séquence.

    Args:
        valeurs (list): Une liste (ou un tuple) de nombres, non vide.

    Returns:
        tuple: Le minimum et le maximum, dans cet ordre.
    """
    ...


def calculer_refroidissement(temperature, vitesse_vent):
    """Calcule l'indice de refroidissement éolien d'Environnement Canada.

    Args:
        temperature (float): La température de l'air, en °C.
        vitesse_vent (float): La vitesse du vent, en km/h.

    Returns:
        int: L'indice de refroidissement éolien, arrondi à l'entier.
    """
    ...
```

- Pour `trouver_min_max()`, la fonction renvoie **un seul** tuple qui contient deux valeurs : on indique donc `tuple` et on précise son contenu dans la description.
- Les mentions anglaises `Defaults to 1.` générées par l'extension peuvent être traduites (`Par défaut 1.`) pour que toute la description soit en français.
- La docstring de `trouver_min_max()` précise que la séquence doit être **non vide** : c'est une condition d'utilisation importante, puisque `valeurs[0]` provoquerait une `IndexError`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
# (copier ici le contenu de fonctions_mystere.py)

print(calculer_pourboire(42.60, 0.18))                       # a
print(calculer_pourboire(42.60, arrondir=False))             # b
print(formater_telephone("8193761721"))                      # c
print(formater_telephone("8193761721", " "))                 # d
print(compter_lettre("Trois-Rivières", "r"))                 # e
print(compter_lettre("Trois-Rivières", "r", ignorer_casse=False))  # f
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20calculer_pourboire%28montant%2C%20taux%3D0.15%2C%20arrondir%3DTrue%29%3A%0A%20%20%20%20%22%22%22Calcule%20le%20pourboire%20%C3%A0%20laisser%20sur%20une%20addition.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20montant%20%28float%29%3A%20Le%20montant%20de%20l%27addition%2C%20taxes%20incluses.%0A%20%20%20%20%20%20%20%20taux%20%28float%2C%20optional%29%3A%20Le%20taux%20du%20pourboire%20%28ex.%200.18%20pour%2018%20%25%29.%20Par%20d%C3%A9faut%200.15.%0A%20%20%20%20%20%20%20%20arrondir%20%28bool%2C%20optional%29%3A%20Si%20True%2C%20arrondit%20le%20pourboire%20au%20dollar%20sup%C3%A9rieur.%0A%20%20%20%20%20%20%20%20%20%20%20%20Par%20d%C3%A9faut%20True.%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20float%3A%20Le%20montant%20du%20pourboire%2C%20en%20dollars.%0A%20%20%20%20%22%22%22%0A%20%20%20%20pourboire%20%3D%20montant%20%2A%20taux%0A%20%20%20%20if%20arrondir%20and%20pourboire%20%21%3D%20int%28pourboire%29%3A%0A%20%20%20%20%20%20%20%20pourboire%20%3D%20float%28int%28pourboire%29%20%2B%201%29%0A%20%20%20%20return%20round%28pourboire%2C%202%29%0A%0A%0Adef%20formater_telephone%28numero%2C%20separateur%3D%22-%22%29%3A%0A%20%20%20%20%22%22%22Met%20en%20forme%20un%20num%C3%A9ro%20de%20t%C3%A9l%C3%A9phone%20nord-am%C3%A9ricain%20de%2010%20chiffres.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20numero%20%28str%29%3A%20Les%2010%20chiffres%20du%20num%C3%A9ro%2C%20sans%20espaces%20ni%20symboles%20%28ex.%20%C2%AB%208193761721%20%C2%BB%29.%0A%20%20%20%20%20%20%20%20separateur%20%28str%2C%20optional%29%3A%20Le%20caract%C3%A8re%20plac%C3%A9%20entre%20les%20groupes%20de%20chiffres.%20Par%20d%C3%A9faut%20%C2%AB%20-%20%C2%BB.%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20str%3A%20Le%20num%C3%A9ro%20mis%20en%20forme%20%28ex.%20%C2%AB%20819-376-1721%20%C2%BB%29.%0A%20%20%20%20%22%22%22%0A%20%20%20%20return%20numero%5B%3A3%5D%20%2B%20separateur%20%2B%20numero%5B3%3A6%5D%20%2B%20separateur%20%2B%20numero%5B6%3A%5D%0A%0A%0Adef%20compter_lettre%28texte%2C%20lettre%2C%20ignorer_casse%3DTrue%29%3A%0A%20%20%20%20%22%22%22Compte%20le%20nombre%20de%20fois%20qu%27une%20lettre%20appara%C3%AEt%20dans%20un%20texte.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20texte%20%28str%29%3A%20Le%20texte%20dans%20lequel%20on%20cherche.%0A%20%20%20%20%20%20%20%20lettre%20%28str%29%3A%20La%20lettre%20%C3%A0%20compter%20%28un%20seul%20caract%C3%A8re%29.%0A%20%20%20%20%20%20%20%20ignorer_casse%20%28bool%2C%20optional%29%3A%20Si%20True%2C%20les%20majuscules%20et%20les%20minuscules%0A%20%20%20%20%20%20%20%20%20%20%20%20sont%20consid%C3%A9r%C3%A9es%20comme%20identiques.%20Par%20d%C3%A9faut%20True.%0A%0A%20%20%20%20Returns%3A%0A%20%20%20%20%20%20%20%20int%3A%20Le%20nombre%20d%27occurrences%20de%20la%20lettre.%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20ignorer_casse%3A%0A%20%20%20%20%20%20%20%20texte%20%3D%20texte.lower%28%29%0A%20%20%20%20%20%20%20%20lettre%20%3D%20lettre.lower%28%29%0A%20%20%20%20nb%20%3D%200%0A%20%20%20%20for%20caractere%20in%20texte%3A%0A%20%20%20%20%20%20%20%20if%20caractere%20%3D%3D%20lettre%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nb%20%2B%3D%201%0A%20%20%20%20return%20nb%0A%0A%0Aprint%28calculer_pourboire%2842.60%2C%200.18%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20a%0Aprint%28calculer_pourboire%2842.60%2C%20arrondir%3DFalse%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20b%0Aprint%28formater_telephone%28%228193761721%22%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20c%0Aprint%28formater_telephone%28%228193761721%22%2C%20%22%20%22%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20d%0Aprint%28compter_lettre%28%22Trois-Rivi%C3%A8res%22%2C%20%22r%22%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20e%0Aprint%28compter_lettre%28%22Trois-Rivi%C3%A8res%22%2C%20%22r%22%2C%20ignorer_casse%3DFalse%29%29%20%20%23%20f&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

```text
8.0
6.39
819-376-1721
819 376 1721
3
2
```

- **a.** `0.18` peut aussi s'écrire `taux=0.18`, ce qui est plus clair.
- **b.** On saute le taux (valeur par défaut) grâce à l'argument nommé `arrondir=False`.
- **d.** `formater_telephone("8193761721", separateur=" ")` est la version la plus lisible.
- **f.** Seuls les deux « r » minuscules de « Trois » et « Rivières » sont comptés; le « R » majuscule est ignoré.
- Tout ce qu'il fallait savoir se trouvait dans les docstrings : le rôle de chaque paramètre, son type et sa valeur par défaut. C'est exactement ce qu'on fait avec les fonctions de Python, comme `round()` ou `print()`.

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

a. Les trois problèmes :

1. Le résumé parle seulement d'**astérisques**, alors que le symbole est maintenant un paramètre.
2. Les paramètres `symbole` et `marge` ne sont **pas documentés** (ni leur valeur par défaut).
3. La section `Returns:` est **fausse** : la fonction **affiche** le cadre et ne renvoie rien (`None`). Il faut retirer cette section.

b. Docstring à jour :

```python
def afficher_cadre(texte, symbole="*", marge=1):
    """Affiche un texte entouré d'un cadre.

    Args:
        texte (str): Le texte à encadrer.
        symbole (str, optional): Le caractère qui forme le cadre. Par défaut « * ».
        marge (int, optional): Le nombre d'espaces entre le texte et chaque côté
            du cadre. Par défaut 1.
    """
    largeur = len(texte) + 2 * marge + 2
    print(symbole * largeur)
    print(symbole + " " * marge + texte + " " * marge + symbole)
    print(symbole * largeur)
```
<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20afficher_cadre%28texte%2C%20symbole%3D%22%2A%22%2C%20marge%3D1%29%3A%0A%20%20%20%20%22%22%22Affiche%20un%20texte%20entour%C3%A9%20d%27un%20cadre.%0A%0A%20%20%20%20Args%3A%0A%20%20%20%20%20%20%20%20texte%20%28str%29%3A%20Le%20texte%20%C3%A0%20encadrer.%0A%20%20%20%20%20%20%20%20symbole%20%28str%2C%20optional%29%3A%20Le%20caract%C3%A8re%20qui%20forme%20le%20cadre.%20Par%20d%C3%A9faut%20%C2%AB%20%2A%20%C2%BB.%0A%20%20%20%20%20%20%20%20marge%20%28int%2C%20optional%29%3A%20Le%20nombre%20d%27espaces%20entre%20le%20texte%20et%20chaque%20c%C3%B4t%C3%A9%0A%20%20%20%20%20%20%20%20%20%20%20%20du%20cadre.%20Par%20d%C3%A9faut%201.%0A%20%20%20%20%22%22%22%0A%20%20%20%20largeur%20%3D%20len%28texte%29%20%2B%202%20%2A%20marge%20%2B%202%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%20%20%20%20print%28symbole%20%2B%20%22%20%22%20%2A%20marge%20%2B%20texte%20%2B%20%22%20%22%20%2A%20marge%20%2B%20symbole%29%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%0A%0Aafficher_cadre%28%22Bienvenue%21%22%2C%20%22%3D%22%2C%203%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

