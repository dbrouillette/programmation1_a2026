# Solutions — La validation de données (fiche 5.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
valide = False
while not valide:
    try:
        enfants = int(input("Combien d'enfants avez-vous ? "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre entier.")

print(f"Vous avez {enfants} enfant(s).")
```

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
valide = False
while not valide:
    try:
        prix = float(input("Entrez le prix de l'article : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre valide.")

print(f"Le prix de l'article est de {prix:.2f} $.")
```

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
nom = input("Entrez un nom d'utilisateur : ").strip()
while nom == "":
    print("Le nom d'utilisateur ne peut pas être vide.")
    nom = input("Entrez un nom d'utilisateur : ").strip()

print(f"Bienvenue, {nom} !")
```

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
valide = False
while not valide:
    try:
        temperature = int(input("Entrez la température (-50 à 50) : "))
        if -50 <= temperature <= 50:
            valide = True
        else:
            print("La température doit être entre -50 et 50.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

print(f"Température enregistrée : {temperature} °C")
```

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
choix_valides = (1, 2, 3, 4, 5)

print("1. Option 1")
print("2. Option 2")
print("3. Option 3")
print("4. Option 4")
print("5. Option 5")

valide = False
while not valide:
    try:
        choix = int(input("Votre choix (1 à 5) : "))
        if choix in choix_valides:
            valide = True
        else:
            print("Choix invalide.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

print(f"Vous avez choisi l'option {choix}.")
```

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
forfaits_valides = ("bronze", "argent", "or")

forfait = input("Choisissez un forfait (bronze, argent, or) : ").strip().lower()
while forfait not in forfaits_valides:
    print("Forfait invalide.")
    forfait = input("Choisissez un forfait (bronze, argent, or) : ").strip().lower()

print(f"Forfait sélectionné : {forfait}")
```

## 🔴 Exercice 7 : Difficile

### ✅ Solution 7

```python
choix_valides = (1, 2)
choix = 0

while choix != 2:
    print("1. Entrer une note d'examen")
    print("2. Quitter")

    valide = False
    while not valide:
        try:
            choix = int(input("Votre choix : "))
            if choix in choix_valides:
                valide = True
            else:
                print("Choix invalide.")
        except ValueError:
            print("Ce n'est pas un nombre entier.")

    if choix == 1:
        valide_note = False
        while not valide_note:
            try:
                note = int(input("Entrez une note (0 à 100) : "))
                if 0 <= note <= 100:
                    valide_note = True
                else:
                    print("La note doit être entre 0 et 100.")
            except ValueError:
                print("Ce n'est pas un nombre entier.")
        print("Note entrée :", note)
```

**Pourquoi** : deux drapeaux distincts (`valide` pour le menu, `valide_note` pour la note) sont nécessaires, car ce sont deux boucles de validation indépendantes, chacune avec sa propre recette.

## 🔴 Exercice 8 : Difficile

### ✅ Solution 8

**a.** Recette 6 (ensemble de valeurs, chaînes) :

```python
couleurs_valides = ("rouge", "vert", "bleu", "jaune")

couleur = input("Choisissez une couleur (rouge, vert, bleu, jaune) : ").strip().lower()
while couleur not in couleurs_valides:
    print("Couleur invalide.")
    couleur = input("Choisissez une couleur (rouge, vert, bleu, jaune) : ").strip().lower()

print(f"Couleur choisie : {couleur}")
```

**b.** Recette 5 (intervalle numérique) :

```python
valide = False
while not valide:
    try:
        annee = int(input("Entrez votre année de naissance : "))
        if 1900 < annee <= 2026:
            valide = True
        else:
            print("Année invalide.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

print(f"Année de naissance : {annee}")
```

**c.** Recette 3 (nombre réel) :

```python
valide = False
while not valide:
    try:
        taille = float(input("Entrez votre taille en mètres : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre valide.")

print(f"Taille : {taille} m")
```

**d.** Recette 4 (chaîne non vide) :

```python
mot_de_passe = input("Entrez un mot de passe : ").strip()
while mot_de_passe == "":
    print("Le mot de passe ne peut pas être vide.")
    mot_de_passe = input("Entrez un mot de passe : ").strip()

print("Mot de passe enregistré.")
```

> Le mot de passe lui-même n'est volontairement pas réaffiché à l'écran.
