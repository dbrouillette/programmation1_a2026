# Solutions — Paramètres et arguments (fiche 7.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
« Kukum » : à rapporter dans 21 jours
« Le Petit Prince » : à rapporter dans 14 jours
« Kukum » : à rapporter dans 14 jours
« Bonheur d'occasion » : à rapporter dans 42 jours
« Agaguk » : à rapporter dans 6 jours
```

| Appel | `titre` reçoit | `jours` reçoit |
| --- | --- | --- |
| `afficher_emprunt(livre, duree)` | `"Kukum"` (la valeur de `livre`) | `21` (la valeur de `duree`) |
| `afficher_emprunt("Le Petit Prince", 14)` | `"Le Petit Prince"` | `14` |
| `afficher_emprunt(livre, duree - 7)` | `"Kukum"` | `14` (le calcul est fait **avant** l'appel) |
| `afficher_emprunt(titre, duree * 2)` | `"Bonheur d'occasion"` | `42` |
| `afficher_emprunt("Agaguk", len("Agaguk"))` | `"Agaguk"` | `6` (la valeur renvoyée par `len()`) |

- Les noms des variables (`livre`, `duree`) n'ont pas à être les mêmes que ceux des paramètres : c'est leur **valeur** qui est transmise.
- Dans le 4e appel, la variable `titre` du programme et le paramètre `titre` de la fonction portent le même nom, mais ce sont **deux variables distinctes**. Ça fonctionne, mais ce n'est pas nécessaire.
- Le 5e appel montre qu'un argument peut être le résultat d'une autre fonction.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| Appel | Résultat | Explication |
| --- | --- | --- |
| a. | ✅ `Léa est inscrit(e) au cours Programmation, groupe 2.` | Trois arguments, dans le bon ordre. |
| b. | ⚠️ `Programmation est inscrit(e) au cours Léa, groupe 2.` | Les deux premiers arguments sont **inversés**. Comme les deux sont des chaînes, Python ne voit aucun problème : l'association se fait **par position**, pas par sens. |
| c. | ❌ `TypeError` : `afficher_inscription() missing 1 required positional argument: 'groupe'` | Il manque un argument : le paramètre `groupe` ne reçoit rien. |
| d. | ❌ `TypeError` : `afficher_inscription() takes 3 positional arguments but 4 were given` | Il y a un argument de trop : la fonction n'a que 3 paramètres. |
| e. | ✅ `Zoé est inscrit(e) au cours Web 1, groupe 2.` | Une variable et des expressions sont des arguments valides. Python calcule `"Web " + "1"` et `1 + 1` avant l'appel. |
| f. | ❌ `NameError` : `name 'nom' is not defined` | `nom` est le nom d'un **paramètre**, qui n'existe qu'à l'intérieur de la fonction. Dans le programme principal, aucune variable `nom` n'a été créée. |

- Le cas **b** est le plus dangereux : aucune erreur n'est signalée, et seul un œil attentif voit que l'affichage est faux.
- Le cas **f** est une confusion fréquente entre **paramètre** (dans la définition) et **argument** (dans l'appel). Au moment de l'appel, il faut fournir une **valeur** : `"Léa"` ou une variable qui existe.

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
def afficher_cadre(texte):
    largeur = len(texte) + 4
    print("*" * largeur)
    print(f"* {texte} *")
    print("*" * largeur)


afficher_cadre("Bienvenue!")
afficher_cadre("Menu principal")
afficher_cadre("Merci de votre visite")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20afficher_cadre%28texte%29%3A%0A%20%20%20%20largeur%20%3D%20len%28texte%29%20%2B%204%0A%20%20%20%20print%28%22%2A%22%20%2A%20largeur%29%0A%20%20%20%20print%28f%22%2A%20%7Btexte%7D%20%2A%22%29%0A%20%20%20%20print%28%22%2A%22%20%2A%20largeur%29%0A%0A%0Aafficher_cadre%28%22Bienvenue%21%22%29%0Aafficher_cadre%28%22Menu%20principal%22%29%0Aafficher_cadre%28%22Merci%20de%20votre%20visite%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- Le cadre a 4 caractères de plus que le texte : l'astérisque et l'espace de chaque côté.
- La variable `largeur` est **locale** à la fonction : elle est recalculée à chaque appel, selon le texte reçu.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
REPERES = (-40, 0, 37, 100)
TEMP_MIN = -90
TEMP_MAX = 60

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_conversion(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")


print("Températures repères :")
for temperature in REPERES:
    afficher_conversion(temperature)

print()
temperature = valider_nombre("Température à convertir (°C) : ", TEMP_MIN, TEMP_MAX)
afficher_conversion(temperature)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=REPERES%20%3D%20%28-40%2C%200%2C%2037%2C%20100%29%0ATEMP_MIN%20%3D%20-90%0ATEMP_MAX%20%3D%2060%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20afficher_conversion%28celsius%29%3A%0A%20%20%20%20fahrenheit%20%3D%20celsius%20%2A%209%20%2F%205%20%2B%2032%0A%20%20%20%20print%28f%22%7Bcelsius%3A.1f%7D%20%C2%B0C%20%3D%20%7Bfahrenheit%3A.1f%7D%20%C2%B0F%22%29%0A%0A%0Aprint%28%22Temp%C3%A9ratures%20rep%C3%A8res%20%3A%22%29%0Afor%20temperature%20in%20REPERES%3A%0A%20%20%20%20afficher_conversion%28temperature%29%0A%0Aprint%28%29%0Atemperature%20%3D%20valider_nombre%28%22Temp%C3%A9rature%20%C3%A0%20convertir%20%28%C2%B0C%29%20%3A%20%22%2C%20TEMP_MIN%2C%20TEMP_MAX%29%0Aafficher_conversion%28temperature%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- La même fonction est appelée avec les valeurs d'un tuple (dans la boucle) et avec une valeur saisie : elle ne se soucie pas de l'origine de la valeur reçue.
- Le format `:.1f` affiche `-40` sous la forme `-40.0`, même si la valeur du tuple est un entier.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
COURS = ("Programmation", "Mathématiques", "Français", "Philosophie")
MOYENNES_GROUPE = (74.5, 68.0, 77.2, 71.8)
NOTE_MIN = 0
NOTE_MAX = 100

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_ligne_releve(cours, note, moyenne_groupe):
    mention = "↑" if note >= moyenne_groupe else "↓"
    print(f"{cours:<16}{note:>8.1f}{moyenne_groupe:>8.1f}  {mention}")


notes = []
for cours in COURS:
    note = valider_nombre(f"Note en {cours} : ", NOTE_MIN, NOTE_MAX)
    notes.append(note)

print()
print(f"{'Cours':<16}{'Note':>8}{'Groupe':>8}")
print("-" * 38)
for i in range(len(COURS)):
    afficher_ligne_releve(COURS[i], notes[i], MOYENNES_GROUPE[i])
print("-" * 38)
print(f"Moyenne de l'étudiant : {sum(notes) / len(notes):.1f}")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=COURS%20%3D%20%28%22Programmation%22%2C%20%22Math%C3%A9matiques%22%2C%20%22Fran%C3%A7ais%22%2C%20%22Philosophie%22%29%0AMOYENNES_GROUPE%20%3D%20%2874.5%2C%2068.0%2C%2077.2%2C%2071.8%29%0ANOTE_MIN%20%3D%200%0ANOTE_MAX%20%3D%20100%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20afficher_ligne_releve%28cours%2C%20note%2C%20moyenne_groupe%29%3A%0A%20%20%20%20mention%20%3D%20%22%E2%86%91%22%20if%20note%20%3E%3D%20moyenne_groupe%20else%20%22%E2%86%93%22%0A%20%20%20%20print%28f%22%7Bcours%3A%3C16%7D%7Bnote%3A%3E8.1f%7D%7Bmoyenne_groupe%3A%3E8.1f%7D%20%20%7Bmention%7D%22%29%0A%0A%0Anotes%20%3D%20%5B%5D%0Afor%20cours%20in%20COURS%3A%0A%20%20%20%20note%20%3D%20valider_nombre%28f%22Note%20en%20%7Bcours%7D%20%3A%20%22%2C%20NOTE_MIN%2C%20NOTE_MAX%29%0A%20%20%20%20notes.append%28note%29%0A%0Aprint%28%29%0Aprint%28f%22%7B%27Cours%27%3A%3C16%7D%7B%27Note%27%3A%3E8%7D%7B%27Groupe%27%3A%3E8%7D%22%29%0Aprint%28%22-%22%20%2A%2038%29%0Afor%20i%20in%20range%28len%28COURS%29%29%3A%0A%20%20%20%20afficher_ligne_releve%28COURS%5Bi%5D%2C%20notes%5Bi%5D%2C%20MOYENNES_GROUPE%5Bi%5D%29%0Aprint%28%22-%22%20%2A%2038%29%0Aprint%28f%22Moyenne%20de%20l%27%C3%A9tudiant%20%3A%20%7Bsum%28notes%29%20%2F%20len%28notes%29%3A.1f%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- Les trois séquences `COURS`, `notes` et `MOYENNES_GROUPE` sont associées par leur index : on les parcourt donc **par index**.
- La mention est choisie avec l'opérateur ternaire vu en 4.4, directement dans la fonction.
- L'en-tête utilise les mêmes largeurs (`16`, `8`, `8`) que les lignes, pour que les colonnes s'alignent.

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
NOMBRE_MIN = 1
NOMBRE_MAX = 12
LIMITE_MIN = 1
LIMITE_MAX = 20

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def afficher_table(nombre, limite):
    print(f"Table de {nombre}")
    for i in range(1, limite + 1):
        print(f"{nombre:>2} x {i:>2} = {nombre * i:>3}")


nombre = valider_entier("Table de : ", NOMBRE_MIN, NOMBRE_MAX)
limite = valider_entier("Jusqu'à : ", LIMITE_MIN, LIMITE_MAX)
print()
afficher_table(nombre, limite)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=NOMBRE_MIN%20%3D%201%0ANOMBRE_MAX%20%3D%2012%0ALIMITE_MIN%20%3D%201%0ALIMITE_MAX%20%3D%2020%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20afficher_table%28nombre%2C%20limite%29%3A%0A%20%20%20%20print%28f%22Table%20de%20%7Bnombre%7D%22%29%0A%20%20%20%20for%20i%20in%20range%281%2C%20limite%20%2B%201%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bnombre%3A%3E2%7D%20x%20%7Bi%3A%3E2%7D%20%3D%20%7Bnombre%20%2A%20i%3A%3E3%7D%22%29%0A%0A%0Anombre%20%3D%20valider_entier%28%22Table%20de%20%3A%20%22%2C%20NOMBRE_MIN%2C%20NOMBRE_MAX%29%0Alimite%20%3D%20valider_entier%28%22Jusqu%27%C3%A0%20%3A%20%22%2C%20LIMITE_MIN%2C%20LIMITE_MAX%29%0Aprint%28%29%0Aafficher_table%28nombre%2C%20limite%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- Les deux paramètres contrôlent la fonction : `nombre` change le calcul, et `limite` change le nombre de tours de la boucle.
- On utilise `valider_entier()` plutôt que `valider_nombre()`, parce que `range()` exige des entiers.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
def afficher_liste_numerotee(elements):
    for i in range(len(elements)):
        print(f"{i + 1}. {elements[i]}")
    print(f"({len(elements)} articles)")


articles = []
article = input("Article (Entrée pour terminer) : ").strip()
while article != "":
    articles.append(article)
    article = input("Article (Entrée pour terminer) : ").strip()

if len(articles) == 0:
    print("Aucun article.")
else:
    print("\nDans l'ordre de saisie :")
    afficher_liste_numerotee(articles)
    print("\nEn ordre alphabétique :")
    afficher_liste_numerotee(sorted(articles))
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20afficher_liste_numerotee%28elements%29%3A%0A%20%20%20%20for%20i%20in%20range%28len%28elements%29%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bi%20%2B%201%7D.%20%7Belements%5Bi%5D%7D%22%29%0A%20%20%20%20print%28f%22%28%7Blen%28elements%29%7D%20articles%29%22%29%0A%0A%0Aarticles%20%3D%20%5B%5D%0Aarticle%20%3D%20input%28%22Article%20%28Entr%C3%A9e%20pour%20terminer%29%20%3A%20%22%29.strip%28%29%0Awhile%20article%20%21%3D%20%22%22%3A%0A%20%20%20%20articles.append%28article%29%0A%20%20%20%20article%20%3D%20input%28%22Article%20%28Entr%C3%A9e%20pour%20terminer%29%20%3A%20%22%29.strip%28%29%0A%0Aif%20len%28articles%29%20%3D%3D%200%3A%0A%20%20%20%20print%28%22Aucun%20article.%22%29%0Aelse%3A%0A%20%20%20%20print%28%22%5CnDans%20l%27ordre%20de%20saisie%20%3A%22%29%0A%20%20%20%20afficher_liste_numerotee%28articles%29%0A%20%20%20%20print%28%22%5CnEn%20ordre%20alphab%C3%A9tique%20%3A%22%29%0A%20%20%20%20afficher_liste_numerotee%28sorted%28articles%29%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- `sorted(articles)` **renvoie une nouvelle liste** triée, qui est passée directement en argument : la liste originale n'est pas modifiée.
- Avec `articles.sort()`, la liste originale aurait été triée, et on aurait perdu l'ordre de saisie.
- La même fonction affiche deux listes différentes : c'est tout l'intérêt du paramètre.

## 🔴 Exercice 8 : Moyen-Difficile

### ✅ Solution 8

```python
MOIS = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin")
PRECIPITATIONS_MM = (74, 58, 69, 81, 93, 102)
ECHELLE_PRECIPITATIONS = 10

JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi")
VISITEURS_GYM = (240, 185, 210, 160, 95)
ECHELLE_VISITEURS = 20


def afficher_histogramme(etiquettes, valeurs, echelle):
    for i in range(len(etiquettes)):
        barre = "#" * (valeurs[i] // echelle)
        print(f"{etiquettes[i]:<10}{barre} ({valeurs[i]})")


print(f"Précipitations (1 # = {ECHELLE_PRECIPITATIONS} mm)")
afficher_histogramme(MOIS, PRECIPITATIONS_MM, ECHELLE_PRECIPITATIONS)
print()
print(f"Visiteurs au gym (1 # = {ECHELLE_VISITEURS} visiteurs)")
afficher_histogramme(JOURS, VISITEURS_GYM, ECHELLE_VISITEURS)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=MOIS%20%3D%20%28%22Janvier%22%2C%20%22F%C3%A9vrier%22%2C%20%22Mars%22%2C%20%22Avril%22%2C%20%22Mai%22%2C%20%22Juin%22%29%0APRECIPITATIONS_MM%20%3D%20%2874%2C%2058%2C%2069%2C%2081%2C%2093%2C%20102%29%0AECHELLE_PRECIPITATIONS%20%3D%2010%0A%0AJOURS%20%3D%20%28%22Lundi%22%2C%20%22Mardi%22%2C%20%22Mercredi%22%2C%20%22Jeudi%22%2C%20%22Vendredi%22%29%0AVISITEURS_GYM%20%3D%20%28240%2C%20185%2C%20210%2C%20160%2C%2095%29%0AECHELLE_VISITEURS%20%3D%2020%0A%0A%0Adef%20afficher_histogramme%28etiquettes%2C%20valeurs%2C%20echelle%29%3A%0A%20%20%20%20for%20i%20in%20range%28len%28etiquettes%29%29%3A%0A%20%20%20%20%20%20%20%20barre%20%3D%20%22%23%22%20%2A%20%28valeurs%5Bi%5D%20%2F%2F%20echelle%29%0A%20%20%20%20%20%20%20%20print%28f%22%7Betiquettes%5Bi%5D%3A%3C10%7D%7Bbarre%7D%20%28%7Bvaleurs%5Bi%5D%7D%29%22%29%0A%0A%0Aprint%28f%22Pr%C3%A9cipitations%20%281%20%23%20%3D%20%7BECHELLE_PRECIPITATIONS%7D%20mm%29%22%29%0Aafficher_histogramme%28MOIS%2C%20PRECIPITATIONS_MM%2C%20ECHELLE_PRECIPITATIONS%29%0Aprint%28%29%0Aprint%28f%22Visiteurs%20au%20gym%20%281%20%23%20%3D%20%7BECHELLE_VISITEURS%7D%20visiteurs%29%22%29%0Aafficher_histogramme%28JOURS%2C%20VISITEURS_GYM%2C%20ECHELLE_VISITEURS%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- La division entière `//` donne le nombre de tranches **complètes** : `74 // 10` vaut `7`.
- `"#" * 7` répète le caractère 7 fois, comme `"=" * 34` dans la fiche.
- La fonction ne connaît ni les mois ni les jours : elle travaille avec n'importe quelles listes (ou tuples) associées. Ses paramètres la rendent **générale**.
