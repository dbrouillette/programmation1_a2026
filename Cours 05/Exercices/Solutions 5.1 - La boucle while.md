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

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
a.  while continuer:
b.  while not trouve:
c.  while not partie_terminee:
d.  continuer = (reponse == "o")
```

**Pourquoi** : une variable booléenne **est** déjà la condition. La comparer à `True` ou à `False` n'ajoute aucune information et allonge la lecture.

- En **a**, `continuer == True` vaut exactement ce que vaut `continuer`.
- En **b** et en **c**, `not` exprime la négation plus clairement que `== False` ou `!= True`.
- En **d**, le ternaire est inutile : `reponse == "o"` produit **déjà** `True` ou `False`. On range directement ce résultat dans la variable. Les parenthèses ne sont pas obligatoires, mais elles aident à voir qu'on affecte le résultat d'une comparaison.

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

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

## 🟢 Exercice 5 : Facile-Moyen

### ✅ Solution 5

```python
while True:
    mot_de_passe = input("Entrez le mot de passe : ").strip()
    if mot_de_passe == "python123":
        break
    print("Accès refusé.")
print("Accès autorisé !")
```

## 🟢 Exercice 6 : Facile-Moyen

### ✅ Solution 6

```python
continuer = True

while continuer:
    nombre = float(input("Entrez un nombre : "))
    print("Son carré est", nombre ** 2)

    reponse = input("Un autre ? (o/n) ").strip().lower()
    continuer = (reponse == "o")

print("Au revoir !")
```

> Toute réponse autre que `o` met `continuer` à `False` et termine la boucle. Si on voulait redemander en cas de réponse invalide, il faudrait valider `reponse` dans une boucle imbriquée avant l'affectation.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

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

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

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

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

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

## 🟡 Exercice 10 : Moyen

### ✅ Solution 10

```python
VOYELLES = "aeiouy"

voyelle_trouvee = False
nombre_de_caracteres = 0

while not voyelle_trouvee:
    caractere = input("Entrez un caractère : ").strip().lower()
    nombre_de_caracteres += 1

    if caractere in VOYELLES:
        voyelle_trouvee = True

print("Voyelle trouvée après", nombre_de_caracteres, "caractère(s).")
```

> `caractere in VOYELLES` produit déjà un booléen : on pourrait donc écrire directement `voyelle_trouvee = caractere in VOYELLES`. Attention cependant — cette version-là **remettrait le drapeau à `False`** à chaque consonne, ce qui est correct ici parce que la boucle s'arrête dès la première voyelle, mais deviendrait un bogue si on voulait retenir qu'une voyelle est déjà passée. Le `if` est plus sûr : un drapeau qu'on lève ne se rabaisse pas tout seul.

## 🟡 Exercice 11 : Moyen

### ✅ Solution 11

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

## 🟡 Exercice 12 : Moyen

### ✅ Solution 12

```python
essais_restants = 3
acces_autorise = False

while essais_restants > 0 and not acces_autorise:
    mot_de_passe = input("Entrez le mot de passe : ").strip()

    if mot_de_passe == "python123":
        acces_autorise = True
    else:
        essais_restants -= 1
        print("Accès refusé. Essais restants :", essais_restants)

if acces_autorise:
    print("Accès autorisé !")
else:
    print("Compte bloqué.")
```

> Comparez avec la solution 5 : le `break` sort de la boucle, mais ne laisse aucune trace de la raison de la sortie. Le drapeau, lui, survit à la boucle et sert encore dans le `if` final.

## 🟡 Exercice 13 : Moyen-Difficile

### ✅ Solution 13

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

## 🔴 Exercice 14 : Moyen-Difficile

### ✅ Solution 14

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

## 🔴 Exercice 15 : Difficile

### ✅ Solution 15

```python
rejouer = True

while rejouer:
    nombre_secret = 42
    nombre_essais = 0
    trouve = False

    while not trouve:
        essai = int(input("Devinez le nombre : "))
        nombre_essais += 1

        if essai < nombre_secret:
            print("Trop petit.")
        elif essai > nombre_secret:
            print("Trop grand.")
        else:
            trouve = True

    print("Trouvé en", nombre_essais, "essais.")

    reponse = input("Voulez-vous rejouer ? (o/n) ").strip().lower()
    rejouer = (reponse == "o")

print("Merci d'avoir joué !")
```

> Le drapeau `trouve` règle au passage le problème d'amorçage : avec une condition comme `while essai != nombre_secret:`, il faudrait donner à `essai` une valeur bidon avant d'entrer dans la boucle. Ici, `trouve = False` dit exactement ce qu'on veut dire — on n'a encore rien trouvé.
