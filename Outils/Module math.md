# Le module `math` et les fonctions mathématiques en Python

## Objectifs

- Savoir importer le module `math`.
- Utiliser les fonctions mathématiques les plus courantes.
- Comprendre la différence entre fonctions natives et fonctions du module `math`.

## Référence

Le module `math` fait partie de la bibliothèque standard de Python. Il fournit un accès aux fonctions mathématiques définies par le standard C, comme les racines carrées, les fonctions trigonométriques, les logarithmes et plusieurs constantes utiles (`pi`, `e`, etc.).

> **Documentation officielle** : Pour la liste complète des fonctions et constantes disponibles, voir la documentation officielle : [docs.python.org/3/library/math.html](https://docs.python.org/fr/3.14/library/math.html).

## 1. Importer le module `math`

```python
import math
```

Toutes les fonctions du module `math` doivent être préfixées par `math.`.

## 2. Fonctions natives utiles et constantes

Python inclut déjà plusieurs fonctions mathématiques, qui ne nécessitent pas le module `math` :

| Nom | Description | Paramètres | Retour | Exemple(s) |
| --- | --- | --- | --- | --- |
| `abs(x)` | Retourne la valeur absolue de `x`. | `x` : nombre (`int` ou `float`) | Même type que `x` | `abs(-5)` → `5` |
| `max(a, b, ...)` | Retourne la plus grande valeur parmi les arguments. | Deux valeurs ou plus | La plus grande valeur reçue | `max(3, 7, 2)` → `7` |
| `min(a, b, ...)` | Retourne la plus petite valeur parmi les arguments. | Deux valeurs ou plus | La plus petite valeur reçue | `min(3, 7, 2)` → `2` |
| `round(x)` | Arrondit `x` à l'entier le plus proche. | `x` : nombre à arrondir | `int` | `round(4.6)` → `5` |
| `pow(a, b)` | Calcule `a` élevé à la puissance `b`. | `a` : base, `b` : exposant | Résultat de `a ** b` | `pow(2, 3)` → `8` |
| | | | | `2 ** 3` → `8` |

## 3. Fonctions du module `math`

| Nom | Description | Paramètres | Retour | Exemple(s) |
| --- | --- | --- | --- | --- |
| `math.sqrt(x)` | Calcule la racine carrée de `x`. | `x` : nombre ≥ 0 | `float` | `math.sqrt(25)` → `5.0` |
| `math.ceil(x)` | Arrondit `x` à l'entier supérieur. | `x` : nombre | `int` | `math.ceil(4.1)` → `5` |
| `math.floor(x)` | Arrondit `x` à l'entier inférieur. | `x` : nombre | `int` | `math.floor(4.9)` → `4` |
| `math.trunc(x)` | Tronque `x` en supprimant la partie décimale (sans arrondir). | `x` : nombre | `int` | `math.trunc(4.9)` → `4` |
| | | | | `math.trunc(-4.9)` → `-4` |
| `math.factorial(x)` | Calcule la factorielle de `x` (`x!`). | `x` : entier ≥ 0 | `int` | `math.factorial(5)` → `120` |
| `math.log(x, base)` | Calcule le logarithme de `x`. Sans `base`, calcule le logarithme naturel. | `x` : nombre > 0, `base` (optionnel) | `float` | `math.log(math.e)` → `1.0` |
| | | | | `math.log(8, 2)` → `3.0` |
| `math.log10(x)` | Calcule le logarithme en base 10 de `x`. | `x` : nombre > 0 | `float` | `math.log10(100)` → `2.0` |
| `math.sin(x)` | Calcule le sinus de `x`. | `x` : angle en radians | `float` | `math.sin(math.pi / 2)` → `1.0` |
| `math.cos(x)` | Calcule le cosinus de `x`. | `x` : angle en radians | `float` | `math.cos(0)` → `1.0` |
| `math.tan(x)` | Calcule la tangente de `x`. | `x` : angle en radians | `float` | `math.tan(math.pi / 4)` → `1.0` |
| `math.degrees(x)` | Convertit un angle de radians en degrés. | `x` : angle en radians | `float` | `math.degrees(math.pi)` → `180.0` |
| `math.radians(x)` | Convertit un angle de degrés en radians. | `x` : angle en degrés | `float` | `math.radians(180)` → `3.141592653589793` |
| `math.gcd(a, b)` | Calcule le plus grand commun diviseur de `a` et `b`. | `a`, `b` : entiers | `int` | `math.gcd(12, 18)` → `6` |

### Constantes utiles

- `math.pi` : la valeur de π (`3.141592653589793`).
- `math.e` : la base du logarithme naturel (`2.718281828459045`).

## 4. Remarques importantes

- `math.sqrt(n)` provoque une erreur `ValueError` si `n` est négatif.
- Toutes les fonctions du module `math` retournent généralement un `float`, sinon un `int`.
- `math.pi` fournit une constante précise pour π.

## 5. Résumé

- Les fonctions natives `abs(x)`, `min(a, b, ...)`, `max(a, b, ...)`, `round(x)` et `pow(a, b)` sont disponibles sans import.
- Utiliser `import math` pour avoir accès au module et à ses fonctions.
- `math.sqrt(x)`, `math.sin(x)`, `math.cos(x)`, `math.log(x)` sont des exemples clés.

## 🎥 Vidéo explicative

[![Regarder](https://img.youtube.com/vi/Vxr6Z4unG7Q/maxresdefault.jpg)](https://youtu.be/Vxr6Z4unG7Q)

*Cette vidéo montre comment importer et utiliser le module `math` en Python.*
