# Solutions — Listes de dictionnaires et données imbriquées (fiche 9.4)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Expression | Valeur | Type |
| --- | --- | --- |
| `len(bibliotheque)` | `2` | `int` |
| `bibliotheque[1]` | `{'titre': 'Au clair de la lune', 'auteur': 'Traditionnel', 'notes': []}` | `dict` |
| `bibliotheque[0]["auteur"]` | `'J. Pierpont'` | `str` |
| `bibliotheque[0]["notes"][1]` | `{'note': 'SOL4', 'intensite': 100, 'duree': 600}` | `dict` |
| `bibliotheque[0]["notes"][1]["duree"] * 2` | `1200` | `int` |
| `len(bibliotheque[1]["notes"])` | `0` | `int` |
| `bibliotheque[0]["titre"][0]` | `'V'` | `str` (premier caractère du titre) |
| `bibliotheque["titre"]` | ❌ `TypeError: list indices must be integers or slices, not str` | |
| `bibliotheque[1]["notes"][0]` | ❌ `IndexError: list index out of range` | |
| `"notes" in bibliotheque[1]` | `True` | `bool` (la clé existe, même si la liste est vide) |

- `bibliotheque` est une **liste** : on y accède avec un index entier, jamais avec une clé. Il faut d'abord choisir une chanson : `bibliotheque[0]["titre"]`.
- La liste de notes d'*Au clair de la lune* est vide : elle n'a pas d'élément no 0.
- Le type de chaque niveau dicte l'accès suivant : liste → `[index]`, dictionnaire → `["clé"]`, chaîne → `[index]` d'un caractère.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
CHANSON_2D = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
]

def convertir_en_dictionnaires(chanson_2d):
    """Renvoie la chanson sous forme de liste de dictionnaires {note, intensite, duree}."""
    chanson = []
    for rangee in chanson_2d:
        chanson.append({"note": rangee[0], "intensite": rangee[1], "duree": rangee[2]})
    return chanson

def calculer_duree_totale(chanson):
    total = 0
    for note in chanson:
        total += note["duree"]
    return total

def filtrer_par_intensite(chanson, intensite_min):
    """Renvoie la liste des notes dont l'intensité est au moins intensite_min."""
    resultat = []
    for note in chanson:
        if note["intensite"] >= intensite_min:
            resultat.append(note)
    return resultat

def main():
    chanson = convertir_en_dictionnaires(CHANSON_2D)
    print(chanson[0])
    print(f"{len(chanson)} notes, {calculer_duree_totale(chanson)} ms")

    fortes = filtrer_par_intensite(chanson, 90)
    print(f"Notes à 90 % ou plus ({len(fortes)}) :")
    for note in fortes:
        print(f"  {note['note']:<5}{note['intensite']:>4} %{note['duree']:>6} ms")

main()
```

- `convertir_en_dictionnaires()` crée un nouveau dictionnaire à chaque tour de boucle, directement dans `append()`.
- `note["duree"]` se lit tout seul, alors que `rangee[2]` obligeait à se souvenir de l'ordre des colonnes.
- `filtrer_par_intensite()` renvoie des dictionnaires **déjà existants** : ce ne sont pas des copies, mais les mêmes notes que dans `chanson`.
