# Exercices — Structurer un programme avec des fonctions (fiche 7.8)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande.

## 🟢 Exercice 1 : Facile

**But** : Reconnaître l'ordre type d'un fichier Python.

**Énoncé** : Les sept morceaux d'un générateur de mots de passe ont été mélangés.

**Morceau A**

```python
main()
```

**Morceau E**

```python
def generer_mot_de_passe(longueur):
    mot_de_passe = ""
    for _ in range(longueur):
        mot_de_passe += CARACTERES[random.randint(0, len(CARACTERES) - 1)]
    return mot_de_passe
```

**Morceau C**

```python
import random
```

**Morceau B**

```python
def main():
    longueur = valider_entier(f"Longueur ({LONGUEUR_MIN} à {LONGUEUR_MAX}) : ", LONGUEUR_MIN, LONGUEUR_MAX)
    print("Mot de passe :", generer_mot_de_passe(longueur))
```

**Morceau G**

```python
def valider_entier(msg_saisie, val_min, val_max):
    ...    # (fonction fournie de la série 7.3)
```

**Morceau F**

```python
"""Générateur de mots de passe aléatoires."""
```

**Morceau D**

```python
LONGUEUR_MIN = 8
LONGUEUR_MAX = 20
CARACTERES = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!?#$%"
```

a. Donne l'ordre des morceaux (par leur lettre) qui respecte la structure type d'un programme vue dans la fiche 7.8.
b. Deux morceaux peuvent être échangés sans rien changer au programme ni à sa structure. Lesquels?
c. Que se passe-t-il si on place le morceau **A** juste avant le morceau **B**?
d. Que se passe-t-il si on oublie complètement le morceau **A**?

## 🟡 Exercice 2 : Moyen

**But** : Restructurer un programme existant en fonctions, avec une fonction `main()`.

**Énoncé** : Le programme suivant fonctionne, mais il n'utilise aucune fonction : les taux de change sont écrits directement dans le code, la recette de validation est recopiée deux fois, et le calcul est répété dans chaque branche du `if`.

```python
print("=== Bureau de change du cégep ===")
print("1. Dollar américain (USD)")
print("2. Euro (EUR)")
print("3. Livre sterling (GBP)")

valide = False
while not valide:
    try:
        choix = int(input("Devise : "))
        if 1 <= choix <= 3:
            valide = True
        else:
            print("Erreur : entrez un nombre entre 1 et 3.")
    except ValueError:
        print("Erreur : ce n'est pas un nombre entier.")

valide = False
while not valide:
    try:
        montant = float(input("Montant en dollars canadiens : "))
        if 1 <= montant <= 10000:
            valide = True
        else:
            print("Erreur : entrez un nombre entre 1 et 10000.")
    except ValueError:
        print("Erreur : ce n'est pas un nombre valide.")

if choix == 1:
    print(f"{montant:.2f} $ CA = {montant * 0.72:.2f} USD")
elif choix == 2:
    print(f"{montant:.2f} $ CA = {montant * 0.66:.2f} EUR")
else:
    print(f"{montant:.2f} $ CA = {montant * 0.55:.2f} GBP")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=print%28%22%3D%3D%3D%20Bureau%20de%20change%20du%20c%C3%A9gep%20%3D%3D%3D%22%29%0Aprint%28%221.%20Dollar%20am%C3%A9ricain%20%28USD%29%22%29%0Aprint%28%222.%20Euro%20%28EUR%29%22%29%0Aprint%28%223.%20Livre%20sterling%20%28GBP%29%22%29%0A%0Avalide%20%3D%20False%0Awhile%20not%20valide%3A%0A%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20choix%20%3D%20int%28input%28%22Devise%20%3A%20%22%29%29%0A%20%20%20%20%20%20%20%20if%201%20%3C%3D%20choix%20%3C%3D%203%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20entrez%20un%20nombre%20entre%201%20et%203.%22%29%0A%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%0Avalide%20%3D%20False%0Awhile%20not%20valide%3A%0A%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20montant%20%3D%20float%28input%28%22Montant%20en%20dollars%20canadiens%20%3A%20%22%29%29%0A%20%20%20%20%20%20%20%20if%201%20%3C%3D%20montant%20%3C%3D%2010000%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20entrez%20un%20nombre%20entre%201%20et%2010000.%22%29%0A%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%0Aif%20choix%20%3D%3D%201%3A%0A%20%20%20%20print%28f%22%7Bmontant%3A.2f%7D%20%24%20CA%20%3D%20%7Bmontant%20%2A%200.72%3A.2f%7D%20USD%22%29%0Aelif%20choix%20%3D%3D%202%3A%0A%20%20%20%20print%28f%22%7Bmontant%3A.2f%7D%20%24%20CA%20%3D%20%7Bmontant%20%2A%200.66%3A.2f%7D%20EUR%22%29%0Aelse%3A%0A%20%20%20%20print%28f%22%7Bmontant%3A.2f%7D%20%24%20CA%20%3D%20%7Bmontant%20%2A%200.55%3A.2f%7D%20GBP%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

Restructure-le selon le modèle à 1 fichier de la fiche 7.8 :

- une docstring de fichier, puis des **constantes** pour les codes, les noms et les taux des devises (des tuples associés par leur index) et pour les bornes du montant;
- les fonctions `valider_nombre()` et `valider_entier()` fournies (série 7.3);
- au moins **trois** autres fonctions, par exemple `afficher_menu()`, `convertir(montant, taux)` et `afficher_conversion(...)`;
- une fonction `main()`, appelée tout en bas du fichier.

Le comportement du programme ne doit pas changer.

*Exemple d'exécution (identique avant et après la restructuration) :*

```text
=== Bureau de change du cégep ===
1. Dollar américain (USD)
2. Euro (EUR)
3. Livre sterling (GBP)
Devise : 4
Erreur : entrez un nombre entre 1 et 3.
Devise : 2
Montant en dollars canadiens : mille
Erreur : ce n'est pas un nombre valide.
Montant en dollars canadiens : 250
250.00 $ CA = 165.00 EUR
```

> 💡 Avec des tuples, ajouter une 4e devise (le yen, par exemple) ne demande plus que de modifier les constantes : aucune ligne de code à toucher.

## 🟡 Exercice 3 : Moyen

**But** : Créer son propre module de fonctions réutilisables et l'importer dans un programme.

**Énoncé** :

**Partie 1 — Le module `utilitaires.py`**

Crée un fichier `utilitaires.py` qui regroupe tes fonctions de saisie validée :

- `valider_nombre(msg_saisie, val_min, val_max)` et `valider_entier(msg_saisie, val_min, val_max)` (série 7.3);
- `valider_texte(msg_saisie, longueur_min=1, longueur_max=100)` (exercices 7.4-4 et 7.6-4);
- une **nouvelle** fonction `valider_oui_non(msg_saisie)`, qui pose une question jusqu'à obtenir « o » ou « n » (majuscules acceptées), puis **renvoie** `True` ou `False`.

Le module commence par une docstring de fichier, et chaque fonction a sa docstring (exercice 7.7-3). À la fin du module, ajoute des tests rapides de chaque fonction sous `if __name__ == "__main__":`.

*Exemple d'exécution de `utilitaires.py` lui-même :*

```text
--- Tests de utilitaires.py ---
Réel entre -10 et 10 : 11
Erreur : entrez un nombre entre -10 et 10.
Réel entre -10 et 10 : 3.5
Réel lu : 3.5
Entier entre 1 et 5 : 0
Erreur : entrez un nombre entre 1 et 5.
Entier entre 1 et 5 : 6
Erreur : entrez un nombre entre 1 et 5.
Entier entre 1 et 5 : 3
Entier lu : 3
Texte (défaut : 1 à 100) :
Erreur : entrez entre 1 et 100 caractères.
Texte (défaut : 1 à 100) : allo
Texte lu : allo
Texte (2 à 4) : bonjour
Erreur : entrez entre 2 et 4 caractères.
Texte (2 à 4) : ok
Texte lu : ok
Continuer? (o/n) : x
Erreur : répondez par o ou n.
Continuer? (o/n) : N
Réponse : False
```

**Partie 2 — Le programme `refroidissement.py`**

Dans le **même dossier**, crée un programme `refroidissement.py` qui reprend l'exercice 7.4-5 (refroidissement éolien), selon le modèle à 2 fichiers :

- les fonctions de saisie sont **importées** de `utilitaires.py` (aucune n'est recopiée);
- les fonctions `calculer_refroidissement()` et `classer_risque()` restent dans `refroidissement.py`, avec leur docstring;
- une fonction `main()` répète les calculs tant que l'utilisateur répond « o » à la question « Autre calcul? ».

*Exemple d'exécution de `refroidissement.py` :*

```text
Température (°C) : -20
Vitesse du vent (km/h) : 30
Refroidissement éolien : -33 (risque élevé)

Autre calcul? (o/n) : peut-être
Erreur : répondez par o ou n.
Autre calcul? (o/n) : o
Température (°C) : -35
Vitesse du vent (km/h) : 40
Refroidissement éolien : -54 (risque grave)

Autre calcul? (o/n) : n
```

> 💡 Vérifie que les tests de `utilitaires.py` ne s'exécutent **pas** quand tu lances `refroidissement.py`. Garde ce module précieusement : tu pourras l'importer dans le TP2.

## 🟡 Exercice 4 : Moyen

**But** : Diagnostiquer les erreurs les plus fréquentes du modèle à 2 fichiers.

**Énoncé** : Quatre étudiants ont séparé leur programme en deux fichiers, mais rien ne fonctionne comme prévu. Pour chaque cas, explique la cause du problème et propose une correction.

**Cas A — Le projet de Léa**

```text
Projet_Lea/
├── programme.py
└── outils/
    └── utilitaires.py
```

*programme.py* :

```python
import utilitaires

utilitaires.saluer("Léa")
```

*Résultat de l'exécution de `programme.py` :*

```text
ModuleNotFoundError: No module named 'utilitaires'
```

**Cas B — Le projet de Samuel**

```text
Projet_Samuel/
└── random.py
```

*random.py* :

```python
import random

de = random.randint(1, 6)
print("Résultat du dé :", de)
```

*Résultat de l'exécution de `random.py` :*

```text
AttributeError: module 'random' has no attribute 'randint' (consider renaming 'C:\...\Projet_Samuel\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

**Cas C — Le projet de Noah**

```text
Projet_Noah/
├── programme.py
└── outils-saisie.py
```

*programme.py* :

```python
import outils-saisie

outils-saisie.saluer("Léa")
```

*Résultat de l'exécution de `programme.py` :*

```text
    import outils-saisie
                 ^
SyntaxError: invalid syntax
```

**Cas D — Le projet de Zoé**

```text
Projet_Zoe/
├── programme.py
└── utilitaires.py
```

*utilitaires.py* :

```python
def saluer(nom):
    print(f"Bonjour {nom}!")


saluer("Test")
```

*programme.py* :

```python
from utilitaires import saluer

saluer("Léa")
```

*Résultat de l'exécution de `programme.py` :*

```text
Bonjour Test!
Bonjour Léa!
```

> 💡 Le cas D ne provoque aucune erreur. Qu'est-ce qui cloche quand même?

## 🔴 Exercice 5 : Difficile

**But** : Faire évoluer un programme à 2 fichiers en ajoutant des fonctions.

**Énoncé** : Copie les deux fichiers de la caisse du Café Le Binaire, version 2 fichiers ([caisse.py](../Exemples/2%20fichiers/caisse.py) et [utilitaires.py](../Exemples/2%20fichiers/utilitaires.py)), dans un nouveau dossier. Modifie ensuite `caisse.py` pour ajouter les deux fonctionnalités suivantes.

**1. Retirer un produit du panier**

- Le menu affiche une nouvelle option, `6. Retirer un produit`, juste avant `0. Terminer la commande`. Son numéro est calculé à partir du nombre de produits (une constante `CHOIX_RETIRER`).
- Si le panier est vide, la caisse affiche « Le panier est vide. ».
- Sinon, elle demande le numéro du produit à retirer. Si ce produit n'est pas dans le panier, elle l'indique. Sinon, elle demande la quantité à retirer, entre 1 et la quantité présente dans le panier.
- Le retrait est fait par une nouvelle fonction `retirer_du_panier(quantites, index, quantite)`, qui **modifie** la liste, sur le modèle de `ajouter_au_panier()`.

**2. Rabais de volume**

- Une commande dont le sous-total dépasse **30,00 $** reçoit un rabais de **15 %**, qui s'**additionne** au rabais étudiant de 10 %.
- Une nouvelle fonction `calculer_taux_rabais(sous_total, est_etudiant)` **renvoie** le taux de rabais total (0, 0,10, 0,15 ou 0,25).
- Sur la facture, la ligne du rabais indique le taux appliqué, en pourcentage : `Rabais (25%)`.

Toutes les nouvelles valeurs sont des constantes, et chaque nouvelle fonction a sa docstring. `utilitaires.py` ne change pas.

*Exemple d'exécution :*

```text
==================================
         Café Le Binaire
==================================
1. Café filtre              2.25 $
2. Latté                    4.50 $
3. Chocolat chaud           3.75 $
4. Muffin                   3.25 $
5. Biscuit                  1.95 $
6. Retirer un produit
0. Terminer la commande
Votre choix : 6
Le panier est vide.
Votre choix : 2
Quantité : 4
Votre choix : 6
Produit à retirer : 2
Quantité à retirer : 3
Votre choix : 1
Quantité : 2
Votre choix : 6
Produit à retirer : 5
Aucun biscuit dans le panier.
Votre choix : 2
Quantité : 5
Votre choix : 0
Carte étudiante? (o/n) : o
Pourboire ($) : 3

==================================
         Café Le Binaire
==================================
 2 x Café filtre            4.50 $
 6 x Latté                 27.00 $
----------------------------------
Sous-total                 31.50 $
Rabais (25%)               -7.88 $
TPS                         1.18 $
TVQ                         2.36 $
Pourboire                   3.00 $
----------------------------------
TOTAL                      30.16 $
```


## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.8 - Structurer un programme avec des fonctions](Solutions%207.8%20-%20Structurer%20un%20programme%20avec%20des%20fonctions.md).
