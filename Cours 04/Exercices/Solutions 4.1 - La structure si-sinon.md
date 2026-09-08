# Solutions — La structure si-sinon (fiche 4.1)

## 🟢 Exercice 1 : Facile

**Énoncé** : Afficher *"Nombre négatif"* ou *"Nombre positif ou nul"*.

### ✅ Solution 1

```python
nombre = int(input("Entrez un nombre entier : "))

if nombre < 0:
    print("Nombre négatif")
else:
    print("Nombre positif ou nul")
```

## 🟢 Exercice 2 : Facile-Moyen

**Énoncé** : Afficher *"Majeur"* ou *"Mineur"* selon l'âge.

### ✅ Solution 2

```python
age = int(input("Entrez votre âge : "))

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

## 🟡 Exercice 3 : Moyen

**Énoncé** : Valider qu'un mot de passe contient au moins 8 caractères.

### ✅ Solution 3

```python
mot_de_passe = input("Entrez un mot de passe : ")

if len(mot_de_passe) >= 8:
    print("Mot de passe accepté")
else:
    print("Mot de passe trop court")
```

*Remarque : `len()` fonctionne directement sur une chaîne de caractères, comme vu à la fiche [Manipulations de chaînes](../../Outils/Manipulations%20de%20cha%C3%AEnes.md).*

## 🟡 Exercice 4 : Moyen

**Énoncé** : Vérifier si un nombre est un multiple de 3.

### ✅ Solution 4

```python
nombre = int(input("Entrez un nombre entier : "))

if nombre % 3 == 0:
    print("Multiple de 3")
else:
    print("N'est pas un multiple de 3")
```

## 🔴 Exercice 5 : Moyen-Difficile

**Énoncé** : Déterminer si un triangle est isocèle ou scalène.

### ✅ Solution 5

```python
import math

a = float(input("Longueur du côté a : "))
b = float(input("Longueur du côté b : "))
c = float(input("Longueur du côté c : "))

if math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
    print("Triangle isocèle")
else:
    print("Triangle scalène")
```

*Remarque : un triangle équilatéral (3 côtés égaux) est considéré comme un cas particulier de triangle isocèle — c'est pourquoi une seule branche `if`/`else` suffit ici. Comme `a`, `b` et `c` sont des `float`, on compare leurs longueurs avec `math.isclose()` plutôt qu'avec `==` (voir la fiche 4.5, section 1.6).*
