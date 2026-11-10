# Exercices — Listes de dictionnaires et données imbriquées (fiche 9.4)

> 🎄 **Fil conducteur** : cette série représente les chansons du spectacle avec des listes de dictionnaires et des données imbriquées. Le JSON viendra à la série 9.5.

Dans toute la série, une **note** est un dictionnaire et une **chanson** est un dictionnaire qui contient une liste de notes :

```python
note = {"note": "MI4", "intensite": 80, "duree": 300}

chanson = {
    "titre": "Vive le vent",
    "auteur": "J. Pierpont",
    "notes": [note, ...],
}
```

## 🟢 Exercice 1 : Facile

**But** : Naviguer dans une structure imbriquée.

**Énoncé** : Sans exécuter de code, donne la valeur **et le type** de chaque expression. Deux d'entre elles provoquent une erreur : lesquelles, et laquelle?

```python
bibliotheque = [
    {
        "titre": "Vive le vent",
        "auteur": "J. Pierpont",
        "notes": [
            {"note": "MI4", "intensite": 80, "duree": 300},
            {"note": "SOL4", "intensite": 100, "duree": 600},
        ],
    },
    {
        "titre": "Au clair de la lune",
        "auteur": "Traditionnel",
        "notes": [],
    },
]
```

```python
len(bibliotheque)
bibliotheque[1]
bibliotheque[0]["auteur"]
bibliotheque[0]["notes"][1]
bibliotheque[0]["notes"][1]["duree"] * 2
len(bibliotheque[1]["notes"])
bibliotheque[0]["titre"][0]
bibliotheque["titre"]
bibliotheque[1]["notes"][0]
"notes" in bibliotheque[1]
```

## 🟢 Exercice 2 : Facile

**But** : Passer d'une liste 2D à une liste de dictionnaires.

**Énoncé** : Voici le début de *Vive le vent* sous forme de liste 2D, comme dans la série 9.3 :

```python
CHANSON_2D = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
]
```

Écris :

- `convertir_en_dictionnaires(chanson_2d)`, qui **renvoie** la liste de dictionnaires équivalente;
- `calculer_duree_totale(chanson)`, qui **renvoie** la somme des durées;
- `filtrer_par_intensite(chanson, intensite_min)`, qui **renvoie** la liste des notes dont l'intensité est au moins `intensite_min`.

*Sortie attendue :*

```text
{'note': 'MI4', 'intensite': 80, 'duree': 300}
11 notes, 4800 ms
Notes à 90 % ou plus (4) :
  MI4   100 %   600 ms
  MI4   100 %   600 ms
  DO4    90 %   450 ms
  MI4   100 %  1200 ms
```

> 💡 Compare `calculer_duree_totale()` avec la même fonction écrite pour une liste 2D : laquelle se lit le mieux?

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.4 - Listes de dictionnaires et données imbriquées](Solutions%209.4%20-%20Listes%20de%20dictionnaires%20et%20donn%C3%A9es%20imbriqu%C3%A9es.md).
