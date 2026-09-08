# Solutions — L'opérateur ternaire (fiche 4.4)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
nombre = int(input("Entrez un nombre entier : "))

print("Pair" if nombre % 2 == 0 else "Impair")
```

## 🟢 Exercice 2 : Facile-Moyen

### ✅ Solution 2

```python
age = int(input("Entrez votre âge : "))

statut = "Majeur" if age >= 18 else "Mineur"
print(statut)
```

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

print(a if a > b else b)
```

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
etat = "Au-dessus de zéro" if temperature >= 0 else "Sous zéro"
```

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

**a.**

```python
if note >= 90:
    mention = "Excellent"
elif note >= 60:
    mention = "Bien"
else:
    mention = "Échec"
```

**b.** La version `if`/`elif`/`else` est préférable dès qu'il y a plus de deux issues possibles : elle évite d'empiler des ternaires les uns dans les autres, ce qui devient rapidement difficile à lire et à déboguer, surtout si on ajoute encore des paliers plus tard.
