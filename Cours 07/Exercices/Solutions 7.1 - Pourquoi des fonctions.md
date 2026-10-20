# Solutions — Pourquoi des fonctions? (fiche 7.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Appel | On lui donne | Elle renvoie / elle fait |
| --- | --- | --- |
| a. `len("bonjour")` | une chaîne (`str`) | renvoie `7` (`int`) |
| b. `round(2.675, 1)` | un nombre (`float`) et un nombre de décimales (`int`) | renvoie `2.7` (`float`) |
| c. `round(18.7)` | un nombre (`float`) | renvoie `19` (`int`) |
| d. `print("Allo", "toi")` | deux chaînes (`str`) | **fait** : affiche `Allo toi`; renvoie `None` |
| e. `input("Ton nom : ")` | un message (`str`) | **fait** : affiche le message et attend la saisie; renvoie `'Léa'` (`str`) |
| f. `int("42")` | une chaîne (`str`) | renvoie `42` (`int`) |
| g. `float("3.5")` | une chaîne (`str`) | renvoie `3.5` (`float`) |
| h. `str(2026)` | un entier (`int`) | renvoie `'2026'` (`str`) |
| i. `abs(-7)` | un entier (`int`) | renvoie `7` (`int`) |
| j. `max(12, 45, 8)` | trois entiers (`int`) | renvoie `45` (`int`) |
| k. `sum([2.25, 4.50, 1.95])` | une liste de nombres (`list`) | renvoie `8.7` (`float`) |
| l. `type(3.0)` | un nombre (`float`) | renvoie le type `float` (affiché `<class 'float'>`) |
| m. `"latté".upper()` | rien entre les parenthèses : elle agit sur la chaîne `"latté"` | renvoie `'LATTÉ'` (`str`) |
| n. `"  muffin  ".strip()` | rien entre les parenthèses : elle agit sur la chaîne | renvoie `'muffin'` (`str`) |
| o. `"café,thé,jus".split(",")` | le séparateur `","` (`str`) | renvoie `['café', 'thé', 'jus']` (`list`) |
| p. `epicerie.append("lait")` | la chaîne `"lait"` (`str`) | **fait** : ajoute `"lait"` à la liste, qui devient `['pain', 'lait']`; renvoie `None` |
| q. `sorted([3, 1, 2])` | une liste (`list`) | renvoie une **nouvelle** liste `[1, 2, 3]` (`list`) |
| r. `epicerie.sort()` | rien entre les parenthèses : elle agit sur la liste | **fait** : trie la liste, qui devient `['lait', 'pain']`; renvoie `None` |

- `input()` fait **les deux** : elle affiche un message **et** renvoie une valeur. C'est pour cela qu'on écrit `nom = input(...)`.
- `print()`, `append()` et `sort()` ne renvoient rien d'utile (`None`) : on ne les utilise jamais dans une affectation.
- Comparer **q** et **r** : `sorted()` **renvoie** une nouvelle liste, alors que `sort()` **modifie** la liste existante et ne renvoie rien.
- Les méthodes (**m** à **p**, **r**) sont aussi des fonctions : la valeur placée avant le point est l'élément sur lequel elles travaillent.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| Extrait | Nom | Paramètres | Arguments | Valeur de retour |
| --- | --- | --- | --- | --- |
| A | `calculer_aire_rectangle` | `largeur`, `hauteur` | `4`, `2.5` | `10.0` (rangée dans `aire`) |
| B | `afficher_bienvenue` | aucun | aucun | aucune (elle affiche) |
| C | `saluer` | `prenom` | 1er appel : `nom_etudiant` (qui vaut `"Samuel"`); 2e appel : `"Léa"` | aucune (elle affiche) |
| D | `convertir_en_minutes` | `heures`, `minutes` | 1er appel : `2`, `15`; 2e appel : `1`, `0` | 1er appel : `135` (rangée dans `duree`); 2e appel : `60` (affichée par `print`) |
| E | `calculer_prix_taxes` | `prix` | 1er appel : `prix_livre` (qui vaut `24.95`); 2e appel : `5.00` | 1er appel : `28.69`; 2e appel : `5.75` (additionnées dans `total`, qui vaut `34.44`) |
| F | `afficher_note` | `cours`, `note` | 1er appel : `"Programmation"`, `87`; 2e appel : `"Français"`, `79 + 3` (donc `82`) | aucune (elle affiche) |

- **Extrait C** : la variable `nom_etudiant` et le paramètre `prenom` n'ont pas le même nom, et ce n'est **pas** un problème. C'est la **valeur** de la variable (`"Samuel"`) qui est transmise au paramètre.
- **Extrait D** : la valeur de retour du 2e appel est directement passée en argument à `print()`. Un appel peut servir d'argument à un autre appel.
- **Extrait F** : un argument peut être un calcul. Python évalue d'abord `79 + 3`, puis transmet `82`.
- Repère le mot `return` : seules les fonctions qui en contiennent un (A, D, E) renvoient une valeur.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

**a.** Il y a deux sortes de blocs répétés :

- l'**en-tête** du groupe : lignes 3 à 5, 21 à 23 et 39 à 41 (seul le numéro du groupe change);
- la **saisie validée d'une note** : lignes 8 à 17, 26 à 35 et 44 à 53 (identiques).

On peut aussi considérer que tout le traitement d'un groupe (lignes 3 à 19, 21 à 37 et 39 à 55) est répété au complet : seul le numéro du groupe change.

**b.** Noms de fonctions possibles :

| Bloc | Nom proposé |
| --- | --- |
| En-tête | `afficher_entete_groupe` |
| Saisie validée d'une note | `lire_note` |
| Traitement complet d'un groupe | `traiter_groupe` (ou `calculer_moyenne_groupe`) |

**c.** Le programme principal pourrait ressembler à ceci :

```python
NB_ETUDIANTS = 3

traiter_groupe("Groupe 01")
traiter_groupe("Groupe 02")
traiter_groupe("Groupe 03")
```

… où `traiter_groupe()` appellerait elle-même `afficher_entete_groupe()` et, dans sa boucle, `lire_note()`.

**d.**

- **Programme actuel** : il faut modifier **6 lignes** (la condition `0 <= note <= 100` et le message d'erreur, dans chacun des trois blocs). Le risque d'en oublier une est réel.
- **Version avec fonctions** : il faut modifier **une seule fonction**, `lire_note()` (sa condition et son message). Tous les groupes profitent du changement.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

| # | Avantage | Explication |
| --- | --- | --- |
| 1 | **D. Maintenance facile** | Une seule correction, faite dans la fonction, profite à tous les appels. |
| 2 | **B. Découper un problème** | Le jeu est découpé en étapes simples, chacune devenant une fonction. |
| 3 | **A. Réutiliser** | La boucle de validation est écrite une fois et appelée six fois. |
| 4 | **C. Nommer une tâche** | Le nom `est_bissextile` dit ce que fait le calcul, sans qu'on ait à le relire. |
| 5 | **E. Faciliter les tests** | La fonction est vérifiée seule, avec des valeurs dont on connaît le résultat. |

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

Plusieurs découpages sont possibles. En voici un :

```text
Nom      : afficher_bienvenue
Reçoit   : rien
Renvoie  : rien (elle affiche)
Rôle     : Affiche le message de bienvenue de la borne.

Nom      : afficher_velos
Reçoit   : rien (les vélos et les tarifs sont des constantes)
Renvoie  : rien (elle affiche)
Rôle     : Affiche la liste numérotée des vélos offerts et leur tarif à l'heure.

Nom      : lire_entier
Reçoit   : un message, un minimum et un maximum
Renvoie  : l'entier saisi, une fois validé
Rôle     : Demande un nombre entier jusqu'à ce qu'il soit valide
           (sert pour le choix du vélo ET pour le nombre d'heures).

Nom      : lire_oui_non
Reçoit   : une question
Renvoie  : True si la réponse est « o », False si elle est « n »
Rôle     : Pose une question fermée jusqu'à obtenir une réponse valide
           (sert pour « Êtes-vous membre? » ET pour « Louer un autre vélo? »).

Nom      : calculer_cout_location
Reçoit   : le tarif à l'heure, le nombre d'heures et si l'utilisateur est membre
Renvoie  : le coût avant taxes, rabais appliqué
Rôle     : Calcule le coût de la location.

Nom      : calculer_taxes
Reçoit   : un montant
Renvoie  : la TPS et la TVQ
Rôle     : Calcule les taxes sur un montant.

Nom      : afficher_recu
Reçoit   : le nom du vélo, le nombre d'heures, le coût avant taxes et les taxes
Renvoie  : rien (elle affiche)
Rôle     : Affiche le reçu détaillé de la location.
```

Points à vérifier dans ta réponse :

- Les noms commencent par un **verbe** et sont en `snake_case`.
- Les fonctions de **saisie** (`lire_...`) sont **générales** : une même fonction sert à plusieurs saisies. Une fonction par saisie (`lire_choix_velo()`, `lire_nb_heures()`) fonctionne aussi, mais réutilise moins.
- Les **calculs** (`calculer_...`) sont séparés de l'**affichage** (`afficher_...`) : une fonction de calcul renvoie son résultat sans rien afficher.
- La boucle « Louer un autre vélo? » n'est pas une fonction en soi : elle fera partie du **programme principal**, qui appelle les autres fonctions (voir la fiche 7.8).
