# Exercices — Erreurs courantes et bonnes pratiques (fiche 4.5)

## 🟢 Exercice 1 : Facile

**But** : Repérer et corriger une confusion `=`/`==`.

**Énoncé** :
L'extrait suivant contient une erreur. Identifie-la et corrige-la.

```python
niveau = 3
if niveau = 3:
    print("Niveau maximal atteint")
```

## 🟢 Exercice 2 : Facile-Moyen

**But** : Repérer une erreur d'indentation.

**Énoncé** :
L'extrait suivant provoque une `IndentationError`. Identifie la ligne fautive et corrige-la.

```python
temperature = 15
if temperature < 0:
    print("Il gèle")
      print("Habille-toi chaudement")
else:
    print("Il ne gèle pas")
```

## 🟡 Exercice 3 : Moyen

**But** : Simplifier une imbrication inutile.

**Énoncé** :
Réécris l'extrait suivant en une seule condition, sans imbrication, en utilisant `and` :

```python
if note >= 60:
    if presence >= 75:
        print("Cours réussi")
```

## 🟡 Exercice 4 : Moyen

**But** : Utiliser une comparaison enchaînée.

**Énoncé** :
Réécris la condition suivante à l'aide d'une comparaison enchaînée à la Python :

```python
if temperature >= 15 and temperature <= 25:
    print("Température agréable")
```

## 🔴 Exercice 5 : Difficile

**But** : Refactoriser une fonction imbriquée avec des sorties anticipées (guard clauses).

**Énoncé** :
Voici une fonction qui valide l'inscription à un cours :

```python
def valider_inscription(age, a_paye, place_disponible):
    if age >= 18:
        if a_paye:
            if place_disponible:
                print("Inscription confirmée")
            else:
                print("Aucune place disponible")
        else:
            print("Paiement requis")
    else:
        print("Âge minimum non atteint")
```

Réécris cette fonction en utilisant des sorties anticipées (`return` après chaque `print` d'échec), comme montré à la section 2.3 de la fiche 4.5, de façon à éliminer toute imbrication.
