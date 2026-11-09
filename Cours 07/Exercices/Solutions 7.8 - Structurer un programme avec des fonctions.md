# Solutions — Structurer un programme avec des fonctions (fiche 7.8)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

a. **F, C, D, G, E, B, A**

```python
"""Générateur de mots de passe aléatoires."""

import random

LONGUEUR_MIN = 8
LONGUEUR_MAX = 20
CARACTERES = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!?#$%"


def valider_entier(msg_saisie, val_min, val_max):
    valide = False
    while not valide:
        try:
            nombre = int(input(msg_saisie))
            if val_min <= nombre <= val_max:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {val_min} et {val_max}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return nombre


def generer_mot_de_passe(longueur):
    mot_de_passe = ""
    for _ in range(longueur):
        mot_de_passe += CARACTERES[random.randint(0, len(CARACTERES) - 1)]
    return mot_de_passe


def main():
    longueur = valider_entier(f"Longueur ({LONGUEUR_MIN} à {LONGUEUR_MAX}) : ", LONGUEUR_MIN, LONGUEUR_MAX)
    print("Mot de passe :", generer_mot_de_passe(longueur))


main()
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=%22%22%22G%C3%A9n%C3%A9rateur%20de%20mots%20de%20passe%20al%C3%A9atoires.%22%22%22%0A%0Aimport%20random%0A%0ALONGUEUR_MIN%20%3D%208%0ALONGUEUR_MAX%20%3D%2020%0ACARACTERES%20%3D%20%22abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789%21%3F%23%24%25%22%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20generer_mot_de_passe%28longueur%29%3A%0A%20%20%20%20mot_de_passe%20%3D%20%22%22%0A%20%20%20%20for%20_%20in%20range%28longueur%29%3A%0A%20%20%20%20%20%20%20%20mot_de_passe%20%2B%3D%20CARACTERES%5Brandom.randint%280%2C%20len%28CARACTERES%29%20-%201%29%5D%0A%20%20%20%20return%20mot_de_passe%0A%0A%0Adef%20main%28%29%3A%0A%20%20%20%20longueur%20%3D%20valider_entier%28f%22Longueur%20%28%7BLONGUEUR_MIN%7D%20%C3%A0%20%7BLONGUEUR_MAX%7D%29%20%3A%20%22%2C%20LONGUEUR_MIN%2C%20LONGUEUR_MAX%29%0A%20%20%20%20print%28%22Mot%20de%20passe%20%3A%22%2C%20generer_mot_de_passe%28longueur%29%29%0A%0A%0Amain%28%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

| Ordre | Morceau | Rôle |
| --- | --- | --- |
| 1 | F | Docstring du fichier |
| 2 | C | Imports |
| 3 | D | Constantes |
| 4 | G et E | Fonctions |
| 5 | B | Fonction `main()` |
| 6 | A | Appel de `main()` |

b. **G** et **E** : l'ordre des définitions de fonctions n'a pas d'importance, pourvu qu'elles soient toutes définies avant l'appel de `main()`.

c. `main()` serait appelée avant d'être définie : `NameError: name 'main' is not defined`.

d. Le programme se termine sans rien faire : toutes les fonctions sont mémorisées, mais aucune n'est jamais appelée. Aucune erreur n'est affichée.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
"""Bureau de change du cégep : convertit des dollars canadiens en devises étrangères."""

DEVISES = ("USD", "EUR", "GBP")
NOMS_DEVISES = ("Dollar américain", "Euro", "Livre sterling")
TAUX = (0.72, 0.66, 0.55)          # taux fictifs, pour l'exercice
MONTANT_MIN = 1
MONTANT_MAX = 10000

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_menu():
    print("=== Bureau de change du cégep ===")
    for i in range(len(DEVISES)):
        print(f"{i + 1}. {NOMS_DEVISES[i]} ({DEVISES[i]})")


def convertir(montant, taux):
    return montant * taux


def afficher_conversion(montant, montant_converti, devise):
    print(f"{montant:.2f} $ CA = {montant_converti:.2f} {devise}")


def main():
    afficher_menu()
    choix = valider_entier("Devise : ", 1, len(DEVISES))
    montant = valider_nombre("Montant en dollars canadiens : ", MONTANT_MIN, MONTANT_MAX)
    index = choix - 1
    afficher_conversion(montant, convertir(montant, TAUX[index]), DEVISES[index])


main()
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=%22%22%22Bureau%20de%20change%20du%20c%C3%A9gep%20%3A%20convertit%20des%20dollars%20canadiens%20en%20devises%20%C3%A9trang%C3%A8res.%22%22%22%0A%0ADEVISES%20%3D%20%28%22USD%22%2C%20%22EUR%22%2C%20%22GBP%22%29%0ANOMS_DEVISES%20%3D%20%28%22Dollar%20am%C3%A9ricain%22%2C%20%22Euro%22%2C%20%22Livre%20sterling%22%29%0ATAUX%20%3D%20%280.72%2C%200.66%2C%200.55%29%20%20%20%20%20%20%20%20%20%20%23%20taux%20fictifs%2C%20pour%20l%27exercice%0AMONTANT_MIN%20%3D%201%0AMONTANT_MAX%20%3D%2010000%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20afficher_menu%28%29%3A%0A%20%20%20%20print%28%22%3D%3D%3D%20Bureau%20de%20change%20du%20c%C3%A9gep%20%3D%3D%3D%22%29%0A%20%20%20%20for%20i%20in%20range%28len%28DEVISES%29%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bi%20%2B%201%7D.%20%7BNOMS_DEVISES%5Bi%5D%7D%20%28%7BDEVISES%5Bi%5D%7D%29%22%29%0A%0A%0Adef%20convertir%28montant%2C%20taux%29%3A%0A%20%20%20%20return%20montant%20%2A%20taux%0A%0A%0Adef%20afficher_conversion%28montant%2C%20montant_converti%2C%20devise%29%3A%0A%20%20%20%20print%28f%22%7Bmontant%3A.2f%7D%20%24%20CA%20%3D%20%7Bmontant_converti%3A.2f%7D%20%7Bdevise%7D%22%29%0A%0A%0Adef%20main%28%29%3A%0A%20%20%20%20afficher_menu%28%29%0A%20%20%20%20choix%20%3D%20valider_entier%28%22Devise%20%3A%20%22%2C%201%2C%20len%28DEVISES%29%29%0A%20%20%20%20montant%20%3D%20valider_nombre%28%22Montant%20en%20dollars%20canadiens%20%3A%20%22%2C%20MONTANT_MIN%2C%20MONTANT_MAX%29%0A%20%20%20%20index%20%3D%20choix%20-%201%0A%20%20%20%20afficher_conversion%28montant%2C%20convertir%28montant%2C%20TAUX%5Bindex%5D%29%2C%20DEVISES%5Bindex%5D%29%0A%0A%0Amain%28%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- Les trois tuples `DEVISES`, `NOMS_DEVISES` et `TAUX` sont associés par leur index : le menu et la conversion utilisent tous les deux `index = choix - 1`.
- La recette de validation n'est plus recopiée : `valider_entier()` et `valider_nombre()` sont appelées en une ligne chacune.
- Le calcul n'est écrit qu'une seule fois, dans `convertir()`, au lieu de trois.
- Le nombre de devises n'est écrit nulle part : `valider_entier("Devise : ", 1, len(DEVISES))` s'ajuste automatiquement si on ajoute une devise aux constantes.
- `main()` se lit comme une table des matières : menu, choix, montant, conversion.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

*utilitaires.py* :

```python
"""Mes fonctions utilitaires de saisie validée.

Fonctions réutilisables dans n'importe quel programme qui lit des données
au clavier : chacune redemande la saisie jusqu'à ce qu'elle soit valide.
"""


def valider_nombre(msg_saisie, val_min, val_max):
    """Demande un nombre réel jusqu'à ce que la saisie soit valide.

    Args:
        msg_saisie (str): Le message affiché à l'utilisateur.
        val_min (float): La plus petite valeur acceptée.
        val_max (float): La plus grande valeur acceptée.

    Returns:
        float: Le nombre saisi, compris entre val_min et val_max.
    """
    valide = False
    while not valide:
        try:
            nombre = float(input(msg_saisie))
            if val_min <= nombre <= val_max:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {val_min} et {val_max}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre valide.")
    return nombre


def valider_entier(msg_saisie, val_min, val_max):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        msg_saisie (str): Le message affiché à l'utilisateur.
        val_min (int): La plus petite valeur acceptée.
        val_max (int): La plus grande valeur acceptée.

    Returns:
        int: L'entier saisi, compris entre val_min et val_max.
    """
    valide = False
    while not valide:
        try:
            nombre = int(input(msg_saisie))
            if val_min <= nombre <= val_max:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {val_min} et {val_max}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return nombre


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
    texte = input(msg_saisie).strip()
    while not longueur_min <= len(texte) <= longueur_max:
        print(f"Erreur : entrez entre {longueur_min} et {longueur_max} caractères.")
        texte = input(msg_saisie).strip()
    return texte


def valider_oui_non(msg_saisie):
    """Pose une question fermée jusqu'à obtenir « o » ou « n ».

    Args:
        msg_saisie (str): La question affichée à l'utilisateur.

    Returns:
        bool: True si la réponse est « o », False si elle est « n ».
    """
    reponses_valides = ("o", "n")
    reponse = input(msg_saisie).strip().lower()
    while reponse not in reponses_valides:
        print("Erreur : répondez par o ou n.")
        reponse = input(msg_saisie).strip().lower()
    return reponse == "o"


if __name__ == "__main__":
    print("--- Tests de utilitaires.py ---")
    print("Réel lu :", valider_nombre("Réel entre -10 et 10 : ", -10, 10))
    print("Entier lu :", valider_entier("Entier entre 1 et 5 : ", 1, 5))
    print("Texte lu :", valider_texte("Texte (défaut : 1 à 100) : "))
    print("Texte lu :", valider_texte("Texte (2 à 4) : ", 2, 4))
    print("Réponse :", valider_oui_non("Continuer? (o/n) : "))
```

*refroidissement.py* :

```python
"""Calcule l'indice de refroidissement éolien et le risque de gelures."""

from utilitaires import valider_nombre, valider_oui_non

TEMP_MIN = -50
TEMP_MAX = 0
VENT_MIN = 5
VENT_MAX = 100


def calculer_refroidissement(temperature, vitesse_vent):
    """Calcule l'indice de refroidissement éolien d'Environnement Canada.

    Args:
        temperature (float): La température de l'air, en °C.
        vitesse_vent (float): La vitesse du vent, en km/h.

    Returns:
        int: L'indice de refroidissement éolien, arrondi à l'entier.
    """
    facteur_vent = vitesse_vent ** 0.16
    indice = 13.12 + 0.6215 * temperature - 11.37 * facteur_vent + 0.3965 * temperature * facteur_vent
    return round(indice)


def classer_risque(indice):
    """Détermine le risque de gelures associé à un indice de refroidissement.

    Args:
        indice (int): L'indice de refroidissement éolien.

    Returns:
        str: Le niveau de risque (de « faible » à « extrême »).
    """
    if indice >= -9:
        return "faible"
    elif indice >= -27:
        return "modéré"
    elif indice >= -39:
        return "élevé"
    elif indice >= -47:
        return "très élevé"
    elif indice >= -54:
        return "grave"
    else:
        return "extrême"


def main():
    """Calcule le refroidissement éolien tant que l'utilisateur le souhaite."""
    continuer = True
    while continuer:
        temperature = valider_nombre("Température (°C) : ", TEMP_MIN, TEMP_MAX)
        vitesse_vent = valider_nombre("Vitesse du vent (km/h) : ", VENT_MIN, VENT_MAX)
        indice = calculer_refroidissement(temperature, vitesse_vent)
        print(f"Refroidissement éolien : {indice} (risque {classer_risque(indice)})\n")
        continuer = valider_oui_non("Autre calcul? (o/n) : ")


main()
```

- `from utilitaires import valider_nombre, valider_oui_non` n'importe que les deux fonctions utilisées. `import utilitaires`, suivi d'appels comme `utilitaires.valider_nombre(...)`, est aussi correct.
- Les tests placés sous `if __name__ == "__main__":` ne s'exécutent que si on lance `utilitaires.py` directement.
- `valider_oui_non()` suit la recette 6 de la fiche 5.3 (tuple et opérateur `in`), et **renvoie** directement l'expression booléenne `reponse == "o"`.
- `main()` utilise une boucle `while` avec un drapeau (`continuer`), mis à jour par la valeur que renvoie `valider_oui_non()`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

| Cas | Cause | Correction |
| --- | --- | --- |
| A | `utilitaires.py` est dans un **sous-dossier** (`outils/`). Python cherche les modules dans le dossier du programme exécuté et ne le trouve pas. | Déplacer `utilitaires.py` dans le même dossier que `programme.py`. |
| B | Le fichier s'appelle `random.py`, **comme le module de Python**. `import random` importe donc ce fichier lui-même, qui ne contient pas de fonction `randint()`. | Renommer le fichier, par exemple `lancer_de.py`. |
| C | Le nom `outils-saisie` contient un **tiret** : dans `import outils-saisie`, Python lit une soustraction (`outils - saisie`), d'où la `SyntaxError`. | Renommer le fichier `outils_saisie.py` et écrire `import outils_saisie`. |
| D | Le module contient un appel de test (`saluer("Test")`) **au premier niveau**. Il est exécuté au moment de l'import, avant le programme. | Placer le test sous `if __name__ == "__main__":`, ou le supprimer. |

- Le message du cas B dépend de la version de Python. Les versions récentes (3.13 et plus) suggèrent même de renommer le fichier.
- Le cas D est le plus sournois, puisque aucune erreur n'est affichée : seul un message inattendu (`Bonjour Test!`) apparaît au début du programme.

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
"""Caisse du Café Le Binaire.

Prend la commande d'un client (ajouts et retraits), puis affiche sa facture
avec les rabais, les taxes et le pourboire.
"""

from utilitaires import lire_entier, lire_reel, lire_oui_non

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
NOM_CAFE = "Café Le Binaire"
LARGEUR_FACTURE = 34
PRODUITS = ("Café filtre", "Latté", "Chocolat chaud", "Muffin", "Biscuit")
PRIX = (2.25, 4.50, 3.75, 3.25, 1.95)
QUANTITE_MAX = 20
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975
RABAIS_ETUDIANT = 0.10
RABAIS_VOLUME = 0.15
SEUIL_RABAIS_VOLUME = 30.00
CHOIX_RETIRER = len(PRODUITS) + 1


# ---------------------------------------------------------------------------
# Fonctions d'affichage
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation de la largeur de la facture.

    Args:
        caractere (str): Le caractère répété pour former la ligne.
    """
    print(caractere * LARGEUR_FACTURE)


def afficher_entete():
    """Affiche le nom du café encadré de deux lignes."""
    afficher_separateur("=")
    print(f"{NOM_CAFE:^{LARGEUR_FACTURE}}")
    afficher_separateur("=")


def afficher_menu():
    """Affiche l'en-tête, puis la liste numérotée des produits et leur prix."""
    afficher_entete()
    for i in range(len(PRODUITS)):
        print(f"{i + 1}. {PRODUITS[i]:<20}{PRIX[i]:>9.2f} $")
    print(f"{CHOIX_RETIRER}. Retirer un produit")
    print("0. Terminer la commande")


def afficher_ligne(produit, quantite, prix_unitaire):
    """Affiche une ligne de facture : quantité, produit et montant.

    Args:
        produit (str): Le nom du produit.
        quantite (int): La quantité commandée.
        prix_unitaire (float): Le prix d'un seul exemplaire du produit.
    """
    print(f"{quantite:>2} x {produit:<18}{quantite * prix_unitaire:>9.2f} $")


def afficher_montant(libelle, montant):
    """Affiche un libellé suivi d'un montant aligné à droite.

    Args:
        libelle (str): Le texte affiché à gauche (ex. « TPS »).
        montant (float): Le montant affiché à droite.
    """
    print(f"{libelle:<23}{montant:>9.2f} $")


# ---------------------------------------------------------------------------
# Fonctions de calcul
# ---------------------------------------------------------------------------
def ajouter_au_panier(quantites, index, quantite):
    """Ajoute une quantité d'un produit au panier.

    La liste quantites est modifiée directement : rien n'est retourné.

    Args:
        quantites (list): Les quantités commandées, une par produit.
        index (int): L'index du produit dans PRODUITS.
        quantite (int): La quantité à ajouter.
    """
    quantites[index] += quantite


def retirer_du_panier(quantites, index, quantite):
    """Retire une quantité d'un produit du panier.

    La liste quantites est modifiée directement : rien n'est retourné.

    Args:
        quantites (list): Les quantités commandées, une par produit.
        index (int): L'index du produit dans PRODUITS.
        quantite (int): La quantité à retirer (au plus la quantité dans le panier).
    """
    quantites[index] -= quantite


def calculer_taux_rabais(sous_total, est_etudiant):
    """Calcule le taux de rabais total auquel le client a droit.

    Le rabais étudiant et le rabais de volume (sous-total de plus de
    SEUIL_RABAIS_VOLUME) s'additionnent.

    Args:
        sous_total (float): Le sous-total de la commande.
        est_etudiant (bool): True si le client a sa carte étudiante.

    Returns:
        float: Le taux de rabais (ex. 0.25 pour 25 %).
    """
    taux = 0.0
    if est_etudiant:
        taux += RABAIS_ETUDIANT
    if sous_total > SEUIL_RABAIS_VOLUME:
        taux += RABAIS_VOLUME
    return taux


def calculer_sous_total(quantites):
    """Calcule le sous-total d'une commande, avant rabais et taxes.

    Args:
        quantites (list): Les quantités commandées, une par produit.

    Returns:
        float: La somme des quantités multipliées par leur prix.
    """
    sous_total = 0.0
    for i in range(len(quantites)):
        sous_total += quantites[i] * PRIX[i]
    return sous_total


def calculer_rabais(montant, taux):
    """Calcule le montant d'un rabais, arrondi au cent.

    Args:
        montant (float): Le montant sur lequel s'applique le rabais.
        taux (float): Le taux du rabais (ex. 0.10 pour 10 %).

    Returns:
        float: Le montant du rabais.
    """
    return round(montant * taux, 2)


def calculer_taxes(montant):
    """Calcule la TPS et la TVQ sur un montant, arrondies au cent.

    Args:
        montant (float): Le montant taxable.

    Returns:
        tuple: La TPS et la TVQ, dans cet ordre.
    """
    tps = round(montant * TAUX_TPS, 2)
    tvq = round(montant * TAUX_TVQ, 2)
    return tps, tvq


def calculer_total(sous_total, rabais=0.0, pourboire=0.0):
    """Calcule le total à payer.

    Args:
        sous_total (float): Le sous-total de la commande.
        rabais (float, optional): Le taux du rabais. Par défaut 0.0.
        pourboire (float, optional): Le pourboire, en dollars. Par défaut 0.0.

    Returns:
        float: Le total, rabais, taxes et pourboire inclus.
    """
    montant = sous_total - calculer_rabais(sous_total, rabais)
    tps, tvq = calculer_taxes(montant)
    return round(montant + tps + tvq + pourboire, 2)


# ---------------------------------------------------------------------------
# Facture
# ---------------------------------------------------------------------------
def afficher_facture(quantites, rabais=0.0, pourboire=0.0):
    """Affiche la facture détaillée d'une commande.

    Args:
        quantites (list): Les quantités commandées, une par produit.
        rabais (float, optional): Le taux du rabais. Par défaut 0.0.
        pourboire (float, optional): Le pourboire, en dollars. Par défaut 0.0.
    """
    afficher_entete()
    for i in range(len(PRODUITS)):
        if quantites[i] > 0:
            afficher_ligne(PRODUITS[i], quantites[i], PRIX[i])
    afficher_separateur("-")

    sous_total = calculer_sous_total(quantites)
    montant_rabais = calculer_rabais(sous_total, rabais)
    tps, tvq = calculer_taxes(sous_total - montant_rabais)

    afficher_montant("Sous-total", sous_total)
    if montant_rabais > 0:
        afficher_montant(f"Rabais ({rabais:.0%})", -montant_rabais)
    afficher_montant("TPS", tps)
    afficher_montant("TVQ", tvq)
    if pourboire > 0:
        afficher_montant("Pourboire", pourboire)
    afficher_separateur("-")
    afficher_montant("TOTAL", calculer_total(sous_total, rabais, pourboire))


# ---------------------------------------------------------------------------
# Retrait d'un produit
# ---------------------------------------------------------------------------
def traiter_retrait(quantites):
    """Demande quel produit retirer et en quelle quantité, puis le retire du panier.

    Args:
        quantites (list): Les quantités commandées, une par produit.
    """
    if sum(quantites) == 0:
        print("Le panier est vide.")
    else:
        choix = lire_entier("Produit à retirer : ", 1, len(PRODUITS))
        index = choix - 1
        if quantites[index] == 0:
            print(f"Aucun {PRODUITS[index].lower()} dans le panier.")
        else:
            quantite = lire_entier("Quantité à retirer : ", 1, quantites[index])
            retirer_du_panier(quantites, index, quantite)


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Prend la commande d'un client, puis affiche sa facture."""
    quantites = [0] * len(PRODUITS)

    afficher_menu()
    choix = lire_entier("Votre choix : ", 0, CHOIX_RETIRER)
    while choix != 0:
        if choix == CHOIX_RETIRER:
            traiter_retrait(quantites)
        else:
            quantite = lire_entier("Quantité : ", 1, QUANTITE_MAX)
            ajouter_au_panier(quantites, choix - 1, quantite)
        choix = lire_entier("Votre choix : ", 0, CHOIX_RETIRER)

    if sum(quantites) == 0:
        print("Aucun produit commandé. À la prochaine!")
    else:
        est_etudiant = lire_oui_non("Carte étudiante? (o/n) : ")
        rabais = calculer_taux_rabais(calculer_sous_total(quantites), est_etudiant)
        pourboire = lire_reel("Pourboire ($) : ")
        print()
        afficher_facture(quantites, rabais, pourboire)


main()
```

Résumé des modifications apportées à `caisse.py` :

| Où | Modification |
| --- | --- |
| Docstring du fichier | Mentionne les retraits et les rabais. |
| Constantes | Ajout de `RABAIS_VOLUME`, `SEUIL_RABAIS_VOLUME` et `CHOIX_RETIRER`. |
| `afficher_menu()` | Ajout de la ligne `6. Retirer un produit`. |
| Nouvelle fonction `retirer_du_panier()` | Retire une quantité de la liste `quantites` (modification directe, comme `ajouter_au_panier()`). |
| Nouvelle fonction `calculer_taux_rabais()` | Additionne le rabais étudiant et le rabais de volume, puis renvoie le taux total. |
| `afficher_facture()` | La ligne du rabais affiche le taux en pourcentage (`:.0%`, fiche 3.3). |
| Nouvelle fonction `traiter_retrait()` | Gère toute la saisie du retrait, pour garder `main()` court et lisible. |
| `main()` | Accepte le choix `CHOIX_RETIRER`, et calcule le taux de rabais avec `calculer_taux_rabais()`. |

- `lire_entier("Quantité à retirer : ", 1, quantites[index])` empêche de retirer plus d'unités qu'il y en a dans le panier : la borne maximale vient directement de la liste.
- `utilitaires.py` n'a pas changé : c'est l'avantage d'un module de fonctions générales.
- Les fonctions existantes `calculer_total()` et `afficher_facture()` n'ont presque pas changé, puisqu'elles recevaient déjà le **taux** de rabais en paramètre : seule la valeur transmise est différente.
