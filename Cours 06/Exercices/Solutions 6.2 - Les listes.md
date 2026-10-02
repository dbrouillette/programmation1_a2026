# Solutions — Les listes (fiche 6.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
a.  10
b.  25
c.  [10, 15, 20]
d.  [5, 10, 15]
e.  [30, 25, 20, 15, 10, 5]
f.  6
g.  True
h.  3
i.  IndexError: list index out of range
```

- Les index commencent à `0` : `valeurs[1]` est le **deuxième** élément.
- En **c** et en **d**, la fin de la tranche est exclue, comme pour les chaînes.
- En **i**, la liste a 6 éléments : le dernier index valide est `5`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
sac = ["gourde", "livre"]        # ['gourde', 'livre']
sac.append("crayon")             # ['gourde', 'livre', 'crayon']
sac.insert(1, "lunch")           # ['gourde', 'lunch', 'livre', 'crayon']
sac.remove("livre")              # ['gourde', 'lunch', 'crayon']
sac[0] = "bouteille"             # ['bouteille', 'lunch', 'crayon']
objet = sac.pop()                # ['bouteille', 'lunch']   objet = 'crayon'
sac.append(objet.upper())        # ['bouteille', 'lunch', 'CRAYON']
```

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
NB_ARTICLES = 4

epicerie = []
for i in range(1, NB_ARTICLES + 1):
    article = input(f"Article {i} : ").strip()
    while article == "":
        print("L'article ne peut pas être vide.")
        article = input(f"Article {i} : ").strip()
    epicerie.append(article)

print("\nListe d'épicerie :")
for i in range(len(epicerie)):
    print(f"{i + 1}. {epicerie[i]}")
print(f"{len(epicerie)} articles")
```

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

```python
NB_NOMBRES = 5

nombres = []
for i in range(1, NB_NOMBRES + 1):
    valide = False
    while not valide:
        try:
            nombre = int(input(f"Nombre {i} : "))
            valide = True
        except ValueError:
            print("Ce n'est pas un nombre entier.")
    nombres.append(nombre)

print("Liste :", nombres)
print("Somme :", sum(nombres))
print(f"Moyenne : {sum(nombres) / len(nombres):.2f}")
print("Minimum :", min(nombres), "| Maximum :", max(nombres))
print("Croissant :", sorted(nombres))
print("Décroissant :", sorted(nombres, reverse=True))
print("Originale :", nombres)
```

`sorted()` retourne une **nouvelle** liste : l'originale reste intacte. Avec `nombres.sort()`, la dernière ligne afficherait la liste triée.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
ventes = [420, 385, 510, 290, 610, 475, 330]

total = 0
minimum = ventes[0]
maximum = ventes[0]
index_max = 0
for i in range(len(ventes)):
    total += ventes[i]
    if ventes[i] < minimum:
        minimum = ventes[i]
    if ventes[i] > maximum:
        maximum = ventes[i]
        index_max = i

print("Somme :", total)
print("Minimum :", minimum)
print(f"Maximum : {maximum} (index {index_max})")
```

Le parcours **par index** est nécessaire ici, puisqu'on veut connaître la **position** du maximum, pas seulement sa valeur.

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
SEUIL_REUSSITE = 60

notes = [78, 45, 92, 58, 88, 60, 34, 71, 59, 83]

reussites = []
echecs = []
for note in notes:
    if note >= SEUIL_REUSSITE:
        reussites.append(note)
    else:
        echecs.append(note)

print("Réussites :", reussites)
print("Échecs :", echecs)
print(f"Taux de réussite : {len(reussites) / len(notes) * 100:.1f} %")
```

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
TAUX_RABAIS = 0.20
SEUIL_RABAIS = 50

prix = [19.99, 74.50, 120.00, 49.99, 55.00, 8.25]
print("Avant :", prix)

nb_modifies = 0
for i in range(len(prix)):
    if prix[i] > SEUIL_RABAIS:
        prix[i] = round(prix[i] * (1 - TAUX_RABAIS), 2)
        nb_modifies += 1

print("Après :", prix)
print("Prix modifiés :", nb_modifies)
```

Une boucle `for p in prix:` ne permettrait pas de modifier la liste : `p` n'est qu'une copie de la valeur (fiche 6.2, section 6).

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

```python
AJOUTER = "1"
RETIRER = "2"
AFFICHER = "3"
QUITTER = "4"
CHOIX_VALIDES = (AJOUTER, RETIRER, AFFICHER, QUITTER)

taches = []
choix = ""
while choix != QUITTER:
    print(f"{AJOUTER}. Ajouter une tâche")
    print(f"{RETIRER}. Retirer une tâche")
    print(f"{AFFICHER}. Afficher les tâches")
    print(f"{QUITTER}. Quitter")
    choix = input("Choix : ").strip()
    while choix not in CHOIX_VALIDES:
        print("Choix invalide.")
        choix = input("Choix : ").strip()

    if choix == AJOUTER:
        tache = input("Tâche : ").strip()
        while tache == "":
            print("Une tâche ne peut pas être vide.")
            tache = input("Tâche : ").strip()
        taches.append(tache)

    elif choix == RETIRER:
        if len(taches) == 0:
            print("Aucune tâche.")
        else:
            valide = False
            while not valide:
                try:
                    numero = int(input(f"Numéro de la tâche à retirer (1 à {len(taches)}) : "))
                    if 1 <= numero <= len(taches):
                        valide = True
                    else:
                        print("Ce numéro n'existe pas.")
                except ValueError:
                    print("Ce n'est pas un nombre entier.")
            retiree = taches.pop(numero - 1)
            print("Tâche retirée :", retiree)

    elif choix == AFFICHER:
        if len(taches) == 0:
            print("Aucune tâche.")
        else:
            for i in range(len(taches)):
                print(f"{i + 1}. {taches[i]}")
    print()
print("Au revoir!")
```

- Les options du menu sont des **constantes** : si on change la numérotation, une seule ligne est à modifier. Le tuple `CHOIX_VALIDES` sert à la validation avec `in` (fiche 5.3, recette 6).
- L'utilisateur voit des numéros qui commencent à 1, mais les index commencent à 0 : on retire donc l'élément à l'index `numero - 1`. `pop()` retourne l'élément retiré, ce qui permet de l'afficher.
- L'intervalle de validation du numéro dépend de la taille **actuelle** de la liste (`len(taches)`) : il change à chaque ajout ou retrait.

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

```python
RUPTURE = 0

produits = ["vis", "clous", "boulons", "écrous", "rondelles"]
quantites = [250, 0, 75, 0, 410]

# a.
for i in range(len(produits)):
    print(f"{produits[i]:<12}{quantites[i]:>5}")

# b.
ruptures = []
for i in range(len(produits)):
    if quantites[i] == RUPTURE:
        ruptures.append(produits[i])
print("Rupture de stock :", ", ".join(ruptures))
print("Total en stock :", sum(quantites))

# c.
recherche = input("Produit recherché : ").strip().lower()
while recherche == "":
    print("Le nom du produit ne peut pas être vide.")
    recherche = input("Produit recherché : ").strip().lower()

if recherche in produits:
    position = produits.index(recherche)
    print(f"{recherche} : {quantites[position]} en stock")
else:
    print("Produit inconnu.")
```

Un produit inconnu n'est **pas** une saisie invalide : c'est un résultat de recherche possible. On valide seulement que la saisie n'est pas vide, puis on traite les deux cas.

## 🔴 Exercice 10 : Moyen-Difficile

### ✅ Solution 10

```python
phrase = input("Phrase : ").strip().lower()
while phrase == "":
    print("La phrase ne peut pas être vide.")
    phrase = input("Phrase : ").strip().lower()

mots = phrase.split()

mots_distincts = []
for mot in mots:
    if mot not in mots_distincts:
        mots_distincts.append(mot)

for mot in mots_distincts:
    print(f"{mot:<8}{mots.count(mot)}")
```
