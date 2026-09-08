# Solutions — Erreurs courantes et bonnes pratiques (fiche 4.5)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

L'erreur : `if niveau = 3:` utilise `=` (affectation) au lieu de `==` (comparaison), ce qui provoque une `SyntaxError`.

```python
niveau = 3
if niveau == 3:
    print("Niveau maximal atteint")
```

## 🟢 Exercice 2 : Facile-Moyen

### ✅ Solution 2

La ligne `print("Habille-toi chaudement")` a une indentation différente (6 espaces) de la ligne précédente du même bloc (4 espaces).

```python
temperature = 15
if temperature < 0:
    print("Il gèle")
    print("Habille-toi chaudement")
else:
    print("Il ne gèle pas")
```

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
if note >= 60 and presence >= 75:
    print("Cours réussi")
```

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
if 15 <= temperature <= 25:
    print("Température agréable")
```

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
def valider_inscription(age, a_paye, place_disponible):
    if age < 18:
        print("Âge minimum non atteint")
        return
    if not a_paye:
        print("Paiement requis")
        return
    if not place_disponible:
        print("Aucune place disponible")
        return
    print("Inscription confirmée")
```

*Remarque : chaque cas d'échec est traité et suivi d'un `return` dès qu'il est détecté; il ne reste, à la toute fin, que le seul cas de succès — sans aucune imbrication.*
