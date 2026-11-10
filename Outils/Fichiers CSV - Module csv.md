# Le module `csv` : la version rapide

## Objectifs

- Lire un fichier CSV avec `csv.reader`.
- Écrire un fichier CSV avec `csv.writer`.
- Comprendre pourquoi on ouvre un fichier CSV avec `newline=""`.
- Lire et écrire des CSV à la française (point-virgule).

## 1. Principe

En [8.6](../Cours%2008/8.6%20-%20Les%20fichiers%20CSV%20à%20la%20main.md), on a tout fait à la main avec `split()` et `join()`. Ça fonctionne, mais ça casse dès qu'une valeur contient une virgule ou des guillemets.

Le module `csv` fait **partie de Python** (rien à installer) et connaît toutes les règles du format. Il fait le découpage et l'assemblage à notre place. Tout le reste (les boucles, la liste 2D, les conversions) **ne change pas**.

```python
import csv
```

## 2. Lire : `csv.reader`

```python
import csv

with open("menu.csv", "r", encoding="utf-8", newline="") as fichier:
    lecteur = csv.reader(fichier)
    for champs in lecteur:
        print(champs)
```

```text
['produit', 'categorie', 'prix', 'stock']
['Café filtre', 'boisson', '2.25', '40']
['Latté', 'boisson', '4.50', '25']
...
```

Comparons avec la version à la main :

```python
# Version à la main (8.6)
for ligne in fichier:
    champs = ligne.strip().split(",")

# Version module csv
for champs in csv.reader(fichier):
    ...
```

Le lecteur donne **directement la liste des champs** : plus besoin de `strip()` ni de `split()`.

> ⚠️ Les champs sont **toujours des chaînes**, comme avant. Le module `csv` ne convertit rien : `int()` et `float()` restent ton travail.

### Sauter l'en-tête : `next()`

La fonction `next()` lit **une seule** rangée du lecteur. C'est l'équivalent de `readline()` :

```python
import csv


def charger_menu(nom_fichier):
    """Renvoie une liste 2D : [[produit, categorie, prix, stock], ...]."""
    menu = []
    with open(nom_fichier, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)                              # en-tête
        for champs in lecteur:
            if len(champs) == 4:                   # ignore les lignes vides ou incomplètes
                menu.append([champs[0], champs[1], float(champs[2]), int(champs[3])])
    return menu
```

Et le fameux `Muffin, bleuets`?

```text
"Muffin, bleuets",patisserie,3.50,8
```

```text
['Muffin, bleuets', 'patisserie', '3.50', '8']
```

Quatre champs, guillemets retirés. Problème réglé.

## 3. Écrire : `csv.writer`

```python
import csv


def sauvegarder_menu(nom_fichier, menu):
    """Écrit la liste 2D du menu dans un fichier CSV, avec l'en-tête."""
    with open(nom_fichier, "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["produit", "categorie", "prix", "stock"])   # une rangée
        ecrivain.writerows(menu)                                       # toutes les rangées
```

| Méthode | Écrit… |
| --- | --- |
| `writerow(liste)` | **une** rangée |
| `writerows(liste_2d)` | **toutes** les rangées d'une liste 2D |

Avantages par rapport à `join()` :

- les **nombres** sont convertis automatiquement (pas de `TypeError`);
- le `\n` est ajouté automatiquement;
- une valeur qui contient une virgule est automatiquement entourée de guillemets.

> 💡 Pour contrôler le nombre de décimales d'un prix, on peut quand même le formater avant l'écriture : `ecrivain.writerow([produit, categorie, f"{prix:.2f}", stock])`.

## 4. Pourquoi `newline=""`?

Le format CSV gère lui-même ses fins de ligne. Si on oublie `newline=""`, sous Windows, chaque rangée écrite est suivie d'une **ligne vide** quand on ouvre le fichier dans Excel.

> 📌 **Règle pratique** : avec le module `csv`, on ouvre **toujours** le fichier avec `newline=""`, en lecture comme en écriture. La documentation officielle le recommande.

## 5. Les CSV à la française : `delimiter=";"`

Pour lire ou écrire un fichier avec des points-virgules (Excel en français), on précise le délimiteur :

```python
lecteur = csv.reader(fichier, delimiter=";")
ecrivain = csv.writer(fichier, delimiter=";")
```

> ⚠️ Le module `csv` ne touche pas aux nombres : `"4,50"` reste `"4,50"`. Pour le convertir : `float(champs[2].replace(",", "."))`.

Pour un fichier exporté par Excel, l'encodage `"utf-8-sig"` (voir [8.6, section 6](../Cours%2008/8.6%20-%20Les%20fichiers%20CSV%20à%20la%20main.md)) évite d'avoir un caractère invisible au début du premier en-tête. En **écriture**, `"utf-8-sig"` aide aussi Excel à afficher correctement les accents.

## 6. Pour aller plus loin : `csv.DictReader`

> 📋 Le module `csv` offre aussi `csv.DictReader` et `csv.DictWriter`, qui permettent d'accéder aux colonnes **par leur nom** (`rangee["prix"]`) plutôt que par un index (`rangee[2]`). Ils utilisent les **dictionnaires**, que nous verrons au cours 9.

## 7. À la main ou avec le module?

| | À la main (`split`/`join`) | Module `csv` |
| --- | --- | --- |
| Comprendre le format | ✅ Idéal | Cache les détails |
| Valeurs avec virgules ou guillemets | ❌ Casse | ✅ Géré |
| Conversion des nombres | À faire soi-même | À faire soi-même |
| Fichiers venant d'Excel, d'un site web, etc. | ⚠️ Risqué | ✅ Recommandé |
| Quantité de code | Un peu plus | Un peu moins |

> 📌 Dans un vrai programme, on utilise le module `csv`. Savoir le faire à la main reste utile pour comprendre ce que le module fait… et pour les examens!

## En résumé

- `import csv` donne accès au module, déjà inclus dans Python.
- On ouvre le fichier avec `encoding="utf-8"` **et** `newline=""`.
- `csv.reader(fichier)` donne une liste de champs par rangée; `next(lecteur)` saute l'en-tête.
- `csv.writer(fichier)` écrit avec `writerow()` (une rangée) ou `writerows()` (une liste 2D).
- Les champs lus sont toujours des chaînes : on convertit soi-même.
- `delimiter=";"` permet de lire et d'écrire les CSV d'Excel en français.

## 📚 Documentation officielle

- [Le module `csv`](https://docs.python.org/fr/3.14/library/csv.html) — `reader`, `writer`, `DictReader`, `DictWriter`
- [La fonction `next()`](https://docs.python.org/fr/3.14/library/functions.html#next)

## Exercices

➡️ Des exercices d'application se trouvent dans [Exercices - Module csv](Exercices/Exercices%20-%20Module%20csv.md) et [Solutions - Module csv](Exercices/Solutions%20-%20Module%20csv.md).

Un exemple complet se trouve dans [Exemples/Module csv](Exemples/Module%20csv/).
