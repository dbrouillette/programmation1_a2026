# Solutions — La boucle `while` (fiche 5.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
compteur = 10
while compteur >= 1:
    print(compteur)
    compteur -= 1
print("Décollage !")
```

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
note = int(input("Entrez une note (0 à 100) : "))
while note < 0 or note > 100:
    print("Note invalide.")
    note = int(input("Entrez une note (0 à 100) : "))
print("Note valide :", note)
```

## 🟢 Exercice 3 : Facile-Moyen

### ✅ Solution 3

```python
table = int(input("Entrez un nombre entre 1 et 12 : "))
while table < 1 or table > 12:
    print("Nombre invalide.")
    table = int(input("Entrez un nombre entre 1 et 12 : "))

multiplicateur = 1
while multiplicateur <= 12:
    print(table, "x", multiplicateur, "=", table * multiplicateur)
    multiplicateur += 1
```

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

```python
while True:
    mot_de_passe = input("Entrez le mot de passe : ").strip()
    if mot_de_passe == "python123":
        break
    print("Accès refusé.")
print("Accès autorisé !")
```

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
total = 0
nombre_de_notes = 0
note = int(input("Entrez une note (-1 pour arrêter) : "))
while note != -1:
    total += note
    nombre_de_notes += 1
    note = int(input("Entrez une note (-1 pour arrêter) : "))

if nombre_de_notes > 0:
    print("Moyenne :", total / nombre_de_notes)
else:
    print("Aucune note entrée.")
```

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
compteur = 0
somme = 0

while compteur < 10:
    nombre = int(input("Entrez un nombre : "))
    compteur += 1

    if nombre <= 0:
        print("Ignoré.")
        continue

    somme += nombre

print("Somme des nombres positifs :", somme)
```

> La variable de contrôle `compteur` est mise à jour **avant** le `continue` : autrement, la boucle ne se terminerait jamais dès qu'un nombre négatif serait entré.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
choix = ""
while choix != "2":
    print("1. Additionner deux nombres")
    print("2. Quitter")
    choix = input("Votre choix : ").strip()

    if choix == "1":
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        print("Résultat :", a + b)
    elif choix != "2":
        print("Choix invalide.")
```

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

```python
nombre = int(input("Entrez un nombre (0 pour arrêter) : "))

if nombre == 0:
    print("Aucun nombre entré.")
else:
    plus_grand = nombre
    plus_petit = nombre

    while nombre != 0:
        if nombre > plus_grand:
            plus_grand = nombre
        if nombre < plus_petit:
            plus_petit = nombre
        nombre = int(input("Entrez un nombre (0 pour arrêter) : "))

    print("Plus grand :", plus_grand)
    print("Plus petit :", plus_petit)
```

> On initialise `plus_grand` et `plus_petit` avec le **premier** nombre entré, et non avec `0` : sinon, une série de nombres tous négatifs donnerait un maximum erroné de `0`.

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

```python
essais_restants = 3
acces_autorise = False

while essais_restants > 0:
    mot_de_passe = input("Entrez le mot de passe : ").strip()
    if mot_de_passe == "python123":
        acces_autorise = True
        break
    essais_restants -= 1
    print("Accès refusé. Essais restants :", essais_restants)

if acces_autorise:
    print("Accès autorisé !")
else:
    print("Compte bloqué.")
```

## 🟡 Exercice 10 : Moyen-Difficile

### ✅ Solution 10

```python
nombre_secret = 42
essai = int(input("Devinez le nombre : "))
while essai != nombre_secret:
    if essai < nombre_secret:
        print("Trop petit.")
    else:
        print("Trop grand.")
    essai = int(input("Essayez encore : "))
print("Bravo, vous avez trouvé !")
```

## 🔴 Exercice 11 : Moyen-Difficile

### ✅ Solution 11

```python
nombre = int(input("Entrez un entier positif : "))
while nombre < 0:
    print("Le nombre doit être positif.")
    nombre = int(input("Entrez un entier positif : "))

somme = 0
while nombre > 0:
    somme += nombre % 10    # ajoute le dernier chiffre
    nombre = nombre // 10   # retire le dernier chiffre

print("Somme des chiffres :", somme)
```

## 🔴 Exercice 12 : Difficile

### ✅ Solution 12

```python
rejouer = "oui"

while rejouer == "oui":
    nombre_secret = 42
    nombre_essais = 0
    essai = -1

    while essai != nombre_secret:
        essai = int(input("Devinez le nombre : "))
        nombre_essais += 1

        if essai < nombre_secret:
            print("Trop petit.")
        elif essai > nombre_secret:
            print("Trop grand.")

    print("Trouvé en", nombre_essais, "essais.")
    rejouer = input("Voulez-vous rejouer ? (oui/non) ").strip().lower()

print("Merci d'avoir joué !")
```

> `essai` est initialisé à `-1` (une valeur impossible à deviner) pour que la boucle interne démarre à coup sûr, même si le joueur devine le bon nombre du premier coup à la partie précédente.
