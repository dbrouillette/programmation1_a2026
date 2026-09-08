# Solutions — Les conditions enchaînées (fiche 4.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
import math

nombre = float(input("Entrez un nombre : "))

if nombre < 0:
    print("Négatif")
elif math.isclose(nombre, 0):
    print("Nul")
else:
    print("Positif")
```

*Remarque : `nombre` est un `float` — on utilise donc `math.isclose(nombre, 0)` plutôt que `nombre == 0` pour éviter les problèmes de comparaison entre `float` (voir la fiche 4.5, section 1.6).*

## 🟢 Exercice 2 : Facile-Moyen

### ✅ Solution 2

```python
age = int(input("Entrez votre âge : "))

if age < 13:
    print("Enfant")
elif age < 18:
    print("Adolescent")
elif age < 65:
    print("Adulte")
else:
    print("Senior")
```

*Remarque : puisque `age < 13` a déjà éliminé tous les cas inférieurs à 13, il n'est pas nécessaire de réécrire `13 <= age < 18` — `age < 18` suffit dans une chaîne `elif`.*

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
note = float(input("Entrez une note sur 100 : "))

if note < 0 or note > 100:
    print("Note invalide")
elif note >= 90:
    print("Excellent")
elif note >= 75:
    print("Très bien")
elif note >= 60:
    print("Bien")
elif note >= 50:
    print("Passable")
else:
    print("Échec")
```

*Remarque : le test `note < 0 or note > 100` doit être placé **en premier**, sinon une note comme `150` serait faussement classée "Excellent" par `note >= 90`.*

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
jour = int(input("Entrez un numéro de jour (1-7) : "))

if jour == 1:
    print("Lundi")
elif jour == 2:
    print("Mardi")
elif jour == 3:
    print("Mercredi")
elif jour == 4:
    print("Jeudi")
elif jour == 5:
    print("Vendredi")
elif jour == 6:
    print("Samedi")
elif jour == 7:
    print("Dimanche")
else:
    print("Numéro de jour invalide")
```

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
poids = float(input("Entrez le poids (kg) : "))
taille = float(input("Entrez la taille (m) : "))

imc = poids / (taille ** 2)

if imc < 18.5:
    print("Insuffisance pondérale")
elif imc < 25:
    print("Poids normal")
elif imc < 30:
    print("Surpoids")
else:
    print("Obésité")
```

*Remarque : comme à l'exercice 3, on ordonne les conditions de la plus petite plage à la plus grande — chaque `elif` n'a besoin de tester que la borne supérieure, puisque la borne inférieure a déjà été éliminée par les conditions précédentes.*

## 🟢 Exercice 6 : Facile

### ✅ Solution 6

```python
jour = int(input("Entrez un numéro de jour (1-7) : "))

match jour:
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    case 3:
        print("Mercredi")
    case 4:
        print("Jeudi")
    case 5:
        print("Vendredi")
    case 6:
        print("Samedi")
    case 7:
        print("Dimanche")
    case _:
        print("Numéro de jour invalide")
```

*Remarque : comparée à la version avec `elif` (exercice 4), cette version en `match`/`case` reste tout aussi correcte, mais devient plus lisible en colonne dès qu'on compare une seule variable à beaucoup de valeurs précises — voir la fiche 4.2, section 5.4.*

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
mois = int(input("Entrez un numéro de mois (1-12) : "))

match mois:
    case 12 | 1 | 2:
        print("Hiver")
    case 3 | 4 | 5:
        print("Printemps")
    case 6 | 7 | 8:
        print("Été")
    case 9 | 10 | 11:
        print("Automne")
    case _:
        print("Mois invalide")
```

*Remarque : le symbole `|` regroupe plusieurs valeurs (ici, les mois d'une même saison) dans un seul `case`, évitant de répéter le même bloc pour chaque mois.*
