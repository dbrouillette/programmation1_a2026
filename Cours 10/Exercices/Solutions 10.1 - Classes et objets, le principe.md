# Solutions — Classes et objets, le principe (fiche 10.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
class Cours:
    """Un cours du programme d'études."""

    def __init__(self, code, titre, heures):
        self.code = code
        self.titre = titre
        self.heures = heures
        self.inscrits = 0

prog1 = Cours("420-116-RI", "Introduction à la programmation", 90)
reseau = Cours("420-113-RI", "Introduction aux réseaux", 75)

prog1.inscrits = 32
reseau.inscrits = prog1.inscrits - 4
reseau.heures += 15

print(prog1.code, prog1.inscrits, prog1.heures)
print(reseau.code, reseau.inscrits, reseau.heures)
print(f"Total des inscrits : {prog1.inscrits + reseau.inscrits}")
```

- Le constructeur a 4 paramètres (`self` + 3), mais on l'appelle avec 3 arguments : Python fournit `self`.
- `self.inscrits = 0` crée un attribut qui ne vient pas d'un paramètre : chaque cours commence à 0.
- Modifier `reseau.heures` ne change pas `prog1.heures` : chaque objet a ses propres attributs.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| Programme | Erreur | Correction |
| --- | --- | --- |
| A | `TypeError: Renard() takes no arguments` : avec un seul `_`, la méthode n'est pas le constructeur | `def __init__(self, nom):` |
| B | `AttributeError: 'Renard' object has no attribute 'nom'` : `nom = nom` ne crée pas d'attribut, seulement une variable locale | `self.nom = nom` |
| C | `TypeError: Renard.__init__() missing 1 required positional argument: 'nom'` | `Renard("Roux")` |

- Dans le programme B, Python n'affiche **aucune erreur** à la création : l'erreur n'apparaît qu'au `print()`, quand on cherche l'attribut. C'est le plus difficile à repérer!
