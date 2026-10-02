# Solutions — La boucle `for` (fiche 6.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
NOMBRE_MAX = 20

for nombre in range(1, NOMBRE_MAX + 1):
    print(nombre, end=" ")
print()

for impair in range(1, NOMBRE_MAX, 2):
    print(impair, end=" ")
print()
```

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
a.  3, 4, 5, 6, 7
b.  0, 1, 2, 3
c.  10, 7, 4, 1
d.  vide
e.  0, 4, 8
f.  vide
```

- En **a** et en **b**, la fin est toujours **exclue** : `range(3, 8)` s'arrête à `7`, `range(4)` à `3`.
- En **c**, on part de `10` et on retire `3` tant qu'on reste **plus grand** que `0`.
- En **d**, le début et la fin sont égaux : il n'y a aucun nombre « entre les deux ».
- En **e**, `12` dépasserait la fin : on s'arrête à `8`.
- En **f**, le pas est négatif, mais le début est **plus petit** que la fin : on ne peut pas descendre de `10` jusqu'à `20`.

Pour vérifier une réponse : `print(list(range(10, 0, -3)))`.

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
TABLE_MIN = 1
TABLE_MAX = 12
MULTIPLICATEUR_MAX = 12

valide = False
while not valide:
    try:
        table = int(input(f"Entrez un nombre ({TABLE_MIN} à {TABLE_MAX}) : "))
        if TABLE_MIN <= table <= TABLE_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {TABLE_MIN} et {TABLE_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

for multiplicateur in range(1, MULTIPLICATEUR_MAX + 1):
    print(f"{table} x {multiplicateur:2} = {table * multiplicateur:3}")
```

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

```python
# a.
for i in range(5):
    print(i)

# b.
for compteur in range(1, 101, 11):
    print(compteur)

# c.
for n in range(50, 0, -10):
    print(n)
```

Démarche (fiche 6.1, section 5) : la valeur initiale devient le **début**, la condition devient la **fin** (exclue) et la mise à jour devient le **pas**.

- En **a**, `i < 5` donne directement la fin `5`; le début `0` et le pas `1` sont les valeurs par défaut.
- En **b**, la condition `compteur <= 100` devient la fin `101`, puisque `100` doit pouvoir être atteint.
- En **c**, le pas est négatif : la condition `n > 0` donne la fin `0`.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
# a.
x = 3
while x < 16:
    print(x)
    x += 3

# b.
k = 20
while k > 9:
    print(k)
    k -= 2

# c.
mot = "boucle"
i = 0
while i < len(mot):
    print(i, mot[i])
    i += 1
```

- Avec un **pas positif**, la condition utilise `<` ; avec un **pas négatif**, elle utilise `>`.
- La mise à jour se place à la **fin** du bloc : si on la place avant le `print()`, la première valeur affichée serait déjà décalée.

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
NB_NOTES_MIN = 1
NOTE_MIN = 0
NOTE_MAX = 100

valide = False
while not valide:
    try:
        nb_notes = int(input("Combien de notes? "))
        if nb_notes >= NB_NOTES_MIN:
            valide = True
        else:
            print(f"Il faut au moins {NB_NOTES_MIN} note.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

total = 0
note_max = NOTE_MIN
note_min = NOTE_MAX
for i in range(1, nb_notes + 1):
    valide = False
    while not valide:
        try:
            note = float(input(f"Note {i} : "))
            if NOTE_MIN <= note <= NOTE_MAX:
                valide = True
            else:
                print(f"La note doit être entre {NOTE_MIN} et {NOTE_MAX}.")
        except ValueError:
            print("Ce n'est pas un nombre valide.")

    total += note
    if note > note_max:
        note_max = note
    if note < note_min:
        note_min = note

print(f"Moyenne : {total / nb_notes:.1f}")
print("Note la plus haute :", note_max)
print("Note la plus basse :", note_min)
```

La validation de chaque note (`while`) est placée **à l'intérieur** de la boucle `for` : c'est le patron de la fiche 6.3, section 8.

Initialiser `note_max` à `NOTE_MIN` et `note_min` à `NOTE_MAX` fonctionne parce que les notes sont bornées. Lorsque les valeurs ne le sont pas, on initialise plutôt le maximum et le minimum avec la **première valeur** saisie.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
valide = False
while not valide:
    try:
        a = int(input("Premier nombre : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre entier.")

valide = False
while not valide:
    try:
        b = int(input("Deuxième nombre : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre entier.")

if a > b:
    a, b = b, a     # échange des deux valeurs

somme_pairs = 0
somme_impairs = 0
for nombre in range(a, b + 1):
    if nombre % 2 == 0:
        somme_pairs += nombre
    else:
        somme_impairs += nombre

print(f"Entre {a} et {b} :")
print("Somme des pairs :", somme_pairs)
print("Somme des impairs :", somme_impairs)
```

`a, b = b, a` échange les deux valeurs en une seule ligne. On peut aussi passer par une variable temporaire : `temp = a`, `a = b`, `b = temp`.

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

```python
VOYELLES = "aeiouy"
SYMBOLE_REMPLACEMENT = "*"

phrase = input("Phrase : ").strip()
while phrase == "":
    print("La phrase ne peut pas être vide.")
    phrase = input("Phrase : ").strip()

resultat = ""
nb_remplacees = 0
for caractere in phrase:
    if caractere.lower() in VOYELLES:
        resultat += SYMBOLE_REMPLACEMENT
        nb_remplacees += 1
    else:
        resultat += caractere

print(resultat)
print("Voyelles remplacées :", nb_remplacees)
```

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

```python
mot = input("Mot : ").strip().lower()
while mot == "":
    print("Le mot ne peut pas être vide.")
    mot = input("Mot : ").strip().lower()

est_palindrome = True
for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot) - 1 - i]:
        est_palindrome = False
        break

if est_palindrome:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
```

Pour un mot de 5 lettres, `len(mot) // 2` vaut `2` : on compare les index 0 ↔ 4 et 1 ↔ 3. Le caractère du milieu (index 2) n'a pas besoin d'être comparé avec lui-même.

Le drapeau `est_palindrome` est nécessaire, car après la boucle, il faut savoir si on en est sorti par le `break` (différence trouvée) ou normalement (toutes les paires identiques).

## 🔴 Exercice 10 : Difficile

### ✅ Solution 10

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

message = input("Message : ").strip().lower()
while message == "":
    print("Le message ne peut pas être vide.")
    message = input("Message : ").strip().lower()

valide = False
while not valide:
    try:
        decalage = int(input("Décalage : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre entier.")

chiffre = ""
for caractere in message:
    position = ALPHABET.find(caractere)
    if position == -1:
        chiffre += caractere        # pas une lettre : inchangé
    else:
        nouvelle_position = (position + decalage) % len(ALPHABET)
        chiffre += ALPHABET[nouvelle_position]

print("Message chiffré :", chiffre)
```

Pour `y` (position 24) avec un décalage de 3 : `(24 + 3) % 26 = 1`, soit `b`. Utiliser `len(ALPHABET)` plutôt que `26` évite un « nombre magique » : le programme reste correct si on modifie l'alphabet.

**Bonus** : avec un décalage de `-3`, le même programme **déchiffre** le message (`oh frxuv hvw ilql` → `le cours est fini`). En Python, `%` retourne toujours un résultat positif avec un diviseur positif : `(0 - 3) % 26` vaut `23`, soit `x`.
