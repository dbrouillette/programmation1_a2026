# Le format JSON

## Objectifs

- Reconnaître la syntaxe JSON et sa correspondance avec Python.
- Sauvegarder une liste (simple ou 2D) dans un fichier JSON avec `json.dump()`.
- Recharger les données avec `json.load()`, **avec leurs types**.
- Gérer un fichier JSON absent ou invalide.
- Choisir entre CSV et JSON.

> 📋 Dans ce cours, on utilise JSON uniquement avec des **listes**. JSON permet aussi de représenter des **objets** (entre accolades `{ }`), qui correspondent aux **dictionnaires** de Python. Nous les verrons au cours 9.

## 1. Principe

Avec un fichier texte ou un CSV, tout ce qu'on relit est une **chaîne** : il faut découper avec `split()`, puis convertir chaque champ avec `int()` ou `float()`. C'est long, et c'est une source d'erreurs.

Le format **JSON** (*JavaScript Object Notation*) règle ce problème : il garde la **structure** des données (listes, listes de listes) et leurs **types** (nombres, booléens, chaînes). Une liste sauvegardée en JSON est relue… comme la même liste, en une seule ligne de code.

Né avec le Web, JSON est aujourd'hui **le** format d'échange entre programmes : API Web, fichiers de configuration (VS Code utilise `settings.json`!), sauvegardes de jeux…

## 2. La syntaxe JSON

Voici un fichier `menu.json` qui contient une liste 2D :

```json
[
    ["Café filtre", "boisson", 2.25, 40, true],
    ["Latté", "boisson", 4.50, 25, true],
    ["Muffin", "patisserie", 3.25, 0, false]
]
```

Ça ressemble énormément à une liste Python! La correspondance est presque parfaite :

| JSON | Python | Exemple JSON |
| --- | --- | --- |
| tableau `[ ]` | liste `list` | `[1, 2, 3]` |
| chaîne | `str` | `"Latté"` |
| nombre entier | `int` | `25` |
| nombre réel | `float` | `4.50` |
| `true` / `false` | `True` / `False` | `true` |
| `null` | `None` | `null` |
| objet `{ }` | dictionnaire `dict` (cours 9) | `{"volume": 7}` |

Les différences à surveiller quand on écrit du JSON à la main :

- les chaînes utilisent **uniquement** des guillemets doubles `"…"` (jamais `'…'`);
- `true`, `false` et `null` s'écrivent en **minuscules**;
- **aucune virgule** après le dernier élément d'un tableau;
- **aucun commentaire** n'est permis.

> 💡 VS Code reconnaît les fichiers `.json` : il colore la syntaxe et souligne en rouge les erreurs (virgule de trop, guillemet simple…).

## 3. Sauvegarder : `json.dump()`

Le module `json` fait partie de Python (rien à installer). La fonction `json.dump(donnees, fichier)` convertit une valeur Python (ici, une liste) en texte JSON et l'écrit dans le fichier.

```python
import json

meilleurs_scores = [
    ["Abby", 1250],
    ["Éloi", 980],
    ["Zoé", 875],
]

with open("scores.json", "w", encoding="utf-8") as fichier:
    json.dump(meilleurs_scores, fichier, indent=4, ensure_ascii=False)
```

Fichier `scores.json` obtenu :

```json
[
    [
        "Abby",
        1250
    ],
    [
        "Éloi",
        980
    ],
    [
        "Zoé",
        875
    ]
]
```

Deux paramètres facultatifs, mais qu'on met presque toujours :

| Paramètre | Effet | Sans lui… |
| --- | --- | --- |
| `indent=4` | Indente le fichier pour qu'il soit lisible par un humain | Tout est sur une seule ligne |
| `ensure_ascii=False` | Écrit les accents tels quels | `"Éloi"` devient `"Éloi"` |

> 💡 Avec `indent`, chaque élément est mis sur sa propre ligne, ce qui étire les listes 2D. C'est normal : le fichier est un peu long, mais parfaitement valide et relu sans problème.

## 4. Recharger : `json.load()`

`json.load(fichier)` fait l'inverse : il lit le texte JSON et **renvoie** la valeur Python correspondante.

```python
import json

with open("scores.json", "r", encoding="utf-8") as fichier:
    meilleurs_scores = json.load(fichier)

for rangee in meilleurs_scores:
    print(f"{rangee[0]:<10}{rangee[1]:>6}")

print(type(meilleurs_scores[0][1]))
```

```text
Abby        1250
Éloi         980
Zoé          875
<class 'int'>
```

Le score relu est déjà un `int` : **aucune conversion** n'est nécessaire.

Comparons le code nécessaire pour recharger une liste 2D, en CSV et en JSON :

```python
# CSV : il faut parcourir, sauter l'en-tête, convertir chaque champ...
menu = []
with open("menu.csv", "r", encoding="utf-8", newline="") as fichier:
    lecteur = csv.reader(fichier)
    next(lecteur)
    for champs in lecteur:
        menu.append([champs[0], champs[1], float(champs[2]), int(champs[3])])

# JSON : une seule ligne, types conservés
with open("menu.json", "r", encoding="utf-8") as fichier:
    menu = json.load(fichier)
```

## 5. Gérer les erreurs

Deux problèmes peuvent survenir à la lecture :

| Exception | Cause |
| --- | --- |
| `FileNotFoundError` | Le fichier n'existe pas (souvent : première exécution) |
| `json.JSONDecodeError` | Le fichier existe, mais ce n'est pas du JSON valide (modifié à la main avec une erreur) |

On reprend le duo `charger_...()` / `sauvegarder_...()` de [8.5](../Cours%2008/8.5%20-%20Sauvegarder%20et%20recharger%20une%20liste.md) :

```python
import json
from pathlib import Path

CHEMIN_SCORES = Path(__file__).parent / "scores.json"


def charger_scores():
    """Renvoie la liste des meilleurs scores, ou une liste vide en cas de problème."""
    try:
        with open(CHEMIN_SCORES, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Avertissement : scores.json est corrompu. Les scores repartent à zéro.")
        return []


def sauvegarder_scores(scores):
    with open(CHEMIN_SCORES, "w", encoding="utf-8") as fichier:
        json.dump(scores, fichier, indent=4, ensure_ascii=False)
```

> 💡 Le `return` à l'intérieur du `with` est permis : le fichier est quand même fermé correctement.

> ⚠️ `json.load()` renvoie ce que contient le fichier, quel qu'il soit. Si quelqu'un a remplacé la liste par un simple nombre, `charger_scores()` renverra ce nombre! Pour un programme robuste, on vérifie le type obtenu : `if type(scores) != list:`.

## 6. Bonus : `json.dumps()` et `json.loads()`

Avec un **s** à la fin (pour *string*), ces fonctions travaillent avec une **chaîne** plutôt qu'un fichier. C'est ce qu'on utilise pour échanger avec un site Web :

```python
import json

texte = json.dumps([["Latté", 4.5, True], ["Muffin", 3.25, False]], ensure_ascii=False)
print(texte)            # [["Latté", 4.5, true], ["Muffin", 3.25, false]]

liste = json.loads("[1, 2.5, true, null]")
print(liste)            # [1, 2.5, True, None]
```

| Fonction | De → vers |
| --- | --- |
| `json.dump(donnees, fichier)` | Python → fichier JSON |
| `json.load(fichier)` | fichier JSON → Python |
| `json.dumps(donnees)` | Python → chaîne JSON |
| `json.loads(chaine)` | chaîne JSON → Python |

## 7. CSV ou JSON?

| Situation | Format conseillé |
| --- | --- |
| Un tableau simple à ouvrir dans Excel | CSV |
| Des données échangées avec un tableur ou un autre logiciel de bureau | CSV |
| Conserver les types (nombres, booléens) sans conversion | JSON |
| Des données imbriquées (une liste qui contient des listes de longueurs variables) | JSON |
| Échanger avec un site Web ou une API | JSON |
| Les paramètres d'une application | JSON, avec des dictionnaires (cours 9) |

## En résumé

- JSON est un format texte qui correspond presque exactement aux listes, chaînes, nombres, booléens et `None` de Python.
- `json.dump(donnees, fichier, indent=4, ensure_ascii=False)` sauvegarde une liste dans un fichier ouvert en `"w"`.
- `json.load(fichier)` renvoie les données lues, **avec leurs types** : plus de `split()` ni de conversion.
- On gère `FileNotFoundError` (fichier absent) et `json.JSONDecodeError` (fichier invalide).
- Les objets JSON `{ }` correspondent aux dictionnaires Python, vus au cours 9.

## 📚 Documentation officielle

- [Sauvegarder des données structurées avec `json`](https://docs.python.org/fr/3.14/tutorial/inputoutput.html#saving-structured-data-with-json) — dans le tutoriel officiel
- [Le module `json`](https://docs.python.org/fr/3.14/library/json.html) — `dump`, `load`, `dumps`, `loads`
- [json.org](https://www.json.org/json-fr.html) — la description complète du format, en français

## Exercices

➡️ Des exercices d'application se trouvent dans [Exercices - Module json](Exercices/Exercices%20-%20Module%20json.md) et [Solutions - Module json](Exercices/Solutions%20-%20Module%20json.md).
