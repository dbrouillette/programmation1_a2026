# Solutions — Les conditions imbriquées (fiche 4.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
age = int(input("Entrez votre âge : "))
permis = input("Avez-vous un permis de conduire? (oui/non) : ").lower() == "oui"

if age >= 18:
    if permis:
        print("Vous pouvez conduire")
    else:
        print("Vous ne pouvez pas conduire sans permis")
else:
    print("Vous êtes mineur")
```

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
age = int(input("Entrez l'âge du visiteur : "))

if age < 12:
    accompagne = input("Est-il accompagné d'un adulte? (oui/non) : ").lower() == "oui"

    if accompagne:
        print("Entrée autorisée")
    else:
        print("Entrée refusée : accompagnement requis")
else:
    print("Entrée autorisée")
```

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
presence = float(input("Entrez le taux de présence (%) : "))
note = float(input("Entrez la note finale (/100) : "))

if presence >= 80:
    if note >= 60:
        print("Cours réussi")
    else:
        print("Cours échoué : note insuffisante")
else:
    print("Cours échoué : présence insuffisante")
```

## 🔴 Exercice 4 : Moyen-Difficile

### ✅ Solution 4

```python
mot_de_passe = input("Entrez un mot de passe : ")

if len(mot_de_passe) < 8:
    print("Mot de passe trop court")
else:
    contient_chiffre = any(c.isdigit() for c in mot_de_passe)

    if contient_chiffre:
        print("Mot de passe valide")
    else:
        print("Le mot de passe doit contenir au moins un chiffre")
```

*Remarque : `any(...)` retourne `True` dès qu'au moins un élément de la séquence est vrai — ici, dès qu'un caractère est un chiffre. Cette fonction native sera revue en détail avec les boucles.*

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
identifiant_attendu = "prof2026"
mot_de_passe_attendu = "python!"

identifiant = input("Identifiant : ")
mot_de_passe = input("Mot de passe : ")

if identifiant == identifiant_attendu:
    if mot_de_passe == mot_de_passe_attendu:
        print("Connexion réussie")
    else:
        print("Mot de passe incorrect")
else:
    print("Identifiant incorrect")
```

*Remarque : ce genre de vérification en deux temps est exactement ce que la fiche 4.5 (bonnes pratiques) proposera de réécrire avec des sorties anticipées, une fois les fonctions vues.*
