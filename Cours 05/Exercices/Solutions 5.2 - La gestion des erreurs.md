# Solutions — La gestion des erreurs (fiche 5.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
try:
    nombre = int(input("Entrez un nombre entier : "))
    print("Son carré est", nombre ** 2)
except ValueError:
    print("Ce n'est pas un nombre.")
```

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
premier = int(input("Entrez le premier nombre : "))
second = int(input("Entrez le second nombre : "))

try:
    print("Résultat :", premier / second)
except ZeroDivisionError:
    print("Division par zéro impossible.")
```

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
a.  ZeroDivisionError
b.  TypeError
c.  NameError
d.  ValueError
```

**Pourquoi** :

- En **a**, `10 // 0` est une division (entière) par zéro : `ZeroDivisionError`.
- En **b**, on additionne une chaîne (`"5"`) et un entier (`3`) : deux types incompatibles pour `+`, donc `TypeError`.
- En **c**, puisque la variable `x` n'existe pas, on obtient une `NameError`
- En **d**, `"bonjour"` n'est pas convertible en entier : `int()` lève une `ValueError`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
valide = False
while not valide:
    try:
        nombre = int(input("Entrez un nombre entier : "))
        valide = True
    except ValueError:
        print("Saisie invalide, réessayez.")

print("Nombre entré :", nombre)
```

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
while True:
    try:
        nombre = int(input("Entrez un nombre entier : "))
        break # obligatoire, sinon boucle infinie
    except ValueError:
        print("Saisie invalide, réessayez.")

print("Nombre entré :", nombre)
```

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
essais_restants = 3
valide = False

# Tant qu'il reste des essais ET que le nombre est invalide
# La boucle peut donc "décrocher" si l'une OU l'autre des clause est fausse
while essais_restants > 0 and not valide:
    try:
        nombre = int(input("Entrez un nombre entier : "))
        valide = True
    except ValueError:
        essais_restants -= 1
        print("Saisie invalide. Essais restants :", essais_restants)
# sortie de la boucle si : plus aucun essai OU nombre valide
if valide:
    print("Nombre obtenu :", nombre)
else:
    print("Trop d'erreurs, abandon.")
```

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
somme = 0
saisie = input("Entrez une note (ou 'fin' pour arrêter) : ").strip().lower()

while saisie != "fin":
    try:
        somme += int(saisie)
    except ValueError:
        print("Valeur ignorée.")
    saisie = input("Entrez une note (ou 'fin' pour arrêter) : ").strip().lower()

print("Somme des notes :", somme)
```

**Pourquoi** : la comparaison `saisie != "fin"` se fait sur le texte brut, **avant** la tentative de conversion. Si la conversion échoue (texte qui n'est ni un nombre ni `fin`), l'exception est interceptée, `somme` n'est pas modifiée, et la boucle redemande une valeur.

## 🔴 Exercice 8 : Difficile

### ✅ Solution 8

```python
choix = 0
while choix != 3:
    print("1. Additionner deux nombres")
    print("2. Multiplier deux nombres")
    print("3. Quitter")

    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Choix invalide.")
        continue

    if choix == 1:
        a = int(input("Premier nombre : "))
        b = int(input("Deuxième nombre : "))
        print("Résultat :", a + b)
    elif choix == 2:
        a = int(input("Premier nombre : "))
        b = int(input("Deuxième nombre : "))
        print("Résultat :", a * b)
    elif choix != 3:
        print("Choix invalide.")
```

**Pourquoi** : le `continue` évite d'exécuter les `if`/`elif` avec une valeur de `choix` invalide après une saisie non numérique — la boucle retourne directement réafficher le menu.

Avec **BONUS**

```python
choix = 0
while choix != 3:
    print("1. Additionner deux nombres")
    print("2. Multiplier deux nombres")
    print("3. Quitter")

    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Choix invalide.")
        continue

    if choix == 1:
        try:
            a = int(input("Premier nombre : "))
            b = int(input("Deuxième nombre : "))
            print("Résultat :", a + b)
        except ValueError:
            print("Une valeur invalide a été saisie, impossible d'afficher la somme.")
    elif choix == 2:
        try:
            a = int(input("Premier nombre : "))
            b = int(input("Deuxième nombre : "))
            print("Résultat :", a * b)
        except ValueError:
            print("Une valeur invalide a été saisie, impossible d'afficher le produit.")
    elif choix != 3:
        print("Choix invalide.")
```
