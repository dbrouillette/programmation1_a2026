# Solutions des défis — Boucles, listes et nombres aléatoires (Cours 06)

## ⭐ Défi 1 : Roche-papier-ciseaux

### ✅ Solution 1

```python
import random

NB_MANCHES = 5
CHOIX = ["roche", "papier", "ciseaux"]

victoires = 0
defaites = 0
egalites = 0
historique = []

for manche in range(1, NB_MANCHES + 1):
    choix_ordi = random.choice(CHOIX)

    choix_joueur = input(f"Manche {manche} - roche, papier ou ciseaux? ").strip().lower()
    while choix_joueur not in CHOIX:
        print("Choix invalide.")
        choix_joueur = input(f"Manche {manche} - roche, papier ou ciseaux? ").strip().lower()

    if choix_joueur == choix_ordi:
        resultat = "égalité"
        egalites += 1
    elif (choix_joueur == "roche" and choix_ordi == "ciseaux") \
            or (choix_joueur == "ciseaux" and choix_ordi == "papier") \
            or (choix_joueur == "papier" and choix_ordi == "roche"):
        resultat = "gagné"
        victoires += 1
    else:
        resultat = "perdu"
        defaites += 1

    print(f"L'ordinateur a choisi {choix_ordi} : {resultat}!")
    historique.append(f"{choix_joueur} vs {choix_ordi} : {resultat}")

print(f"\nScore : {victoires} victoire(s), {defaites} défaite(s), {egalites} égalité(s)")
print("Historique :")
for i in range(len(historique)):
    print(f"  Manche {i + 1} : {historique[i]}")

if victoires > defaites:
    print("Tu remportes la partie!")
elif victoires < defaites:
    print("L'ordinateur remporte la partie.")
else:
    print("Partie nulle!")
```

- La liste `CHOIX` sert à la fois au tirage (`random.choice(CHOIX)`) et à la validation (`not in CHOIX`) : une seule source de vérité.
- La condition composée de la victoire est longue; le `\` en fin de ligne permet de la couper sur plusieurs lignes.

**Pour aller plus loin** : comme les choix sont rangés dans un ordre où chacun bat le précédent (le papier bat la roche, les ciseaux battent le papier, la roche bat les ciseaux), on peut remplacer toute la condition par un calcul sur les index :

```python
ecart = (CHOIX.index(choix_joueur) - CHOIX.index(choix_ordi)) % len(CHOIX)
# ecart == 0 : égalité, ecart == 1 : victoire, ecart == 2 : défaite
```

## ⭐ Défi 2 : Anagramme

### ✅ Solution 2

```python
import random

NB_ESSAIS = 3
MOTS = ["python", "boucle", "variable", "liste", "console",
        "clavier", "fonction", "tableau", "planete", "aleatoire"]

mot = random.choice(MOTS)

lettres = list(mot)
melange = mot
while melange == mot:
    random.shuffle(lettres)
    melange = "".join(lettres)

print("Mot mélangé :", melange.upper())

trouve = False
for essai in range(1, NB_ESSAIS + 1):
    reponse = input(f"Essai {essai}/{NB_ESSAIS} : ").strip().lower()
    while reponse == "":
        print("La réponse ne peut pas être vide.")
        reponse = input(f"Essai {essai}/{NB_ESSAIS} : ").strip().lower()

    if reponse == mot:
        trouve = True
        break
    print("Ce n'est pas ça.")

if trouve:
    print(f"Bravo! Trouvé en {essai} essai(s).")
else:
    print(f"Dommage! Le mot était « {mot} ».")
```

- `melange` est initialisé avec le mot d'origine pour **forcer** au moins un passage dans la boucle de mélange.
- Pour qu'un mot puisse être mélangé, il doit contenir au moins deux lettres différentes : sinon, la boucle `while` serait infinie. C'est le cas de tous les mots de `MOTS`.
- Après la boucle `for`, la variable `essai` contient encore la valeur du dernier tour : on peut donc l'afficher dans le message de victoire.

## ⭐ Défi 3 : Bulletin aléatoire

### ✅ Solution 3

```python
import random

NOMS = ["Léa", "Noah", "Ana", "Ben", "Chloé", "Dev"]
NB_EVALUATIONS = 4
NOTE_MIN = 40
NOTE_MAX = 100

# a. Génération des notes
notes = []
for _ in range(len(NOMS)):
    ligne = []
    for _ in range(NB_EVALUATIONS):
        ligne.append(random.randint(NOTE_MIN, NOTE_MAX))
    notes.append(ligne)

# b. Tableau : en-tête
print(f"{'Étudiant':<10}", end="")
for e in range(1, NB_EVALUATIONS + 1):
    print(f"{'Év' + str(e):>6}", end="")
print(f"{'Moy':>8}")

# b. Une ligne par étudiant
moyennes_etudiants = []
for l in range(len(NOMS)):
    print(f"{NOMS[l]:<10}", end="")
    for c in range(NB_EVALUATIONS):
        print(f"{notes[l][c]:>6}", end="")
    moyenne = sum(notes[l]) / NB_EVALUATIONS
    moyennes_etudiants.append(moyenne)
    print(f"{moyenne:>8.1f}")

# b. Moyenne de chaque évaluation (par colonne)
moyennes_evaluations = []
print(f"{'Moyenne':<10}", end="")
for c in range(NB_EVALUATIONS):
    total = 0
    for l in range(len(NOMS)):
        total += notes[l][c]
    moyenne = total / len(NOMS)
    moyennes_evaluations.append(moyenne)
    print(f"{moyenne:>6.1f}", end="")
print()

# c. Meilleur étudiant et évaluation la plus difficile
meilleur = moyennes_etudiants.index(max(moyennes_etudiants))
difficile = moyennes_evaluations.index(min(moyennes_evaluations))
print(f"\nMeilleure moyenne : {NOMS[meilleur]} ({moyennes_etudiants[meilleur]:.1f})")
print(f"Évaluation la plus difficile : Év{difficile + 1} ({moyennes_evaluations[difficile]:.1f})")
```

- Les moyennes sont rangées dans deux listes **pendant** l'affichage du tableau, ce qui évite de les recalculer en c.
- `liste.index(max(liste))` donne la **position** de la plus grande valeur : c'est elle qui permet de retrouver le nom associé dans `NOMS`.
- L'en-tête `'Év' + str(e)` est d'abord construit comme une chaîne, puis aligné dans le f-string comme n'importe quelle valeur.

## ⭐⭐ Défi 4 : Chasse au trésor

### ✅ Solution 4

```python
import random

TAILLE = 6
NB_ESSAIS = 8
INCONNU = "?"
ESSAYE = "x"
TRESOR = "T"

grille = []
for _ in range(TAILLE):
    ligne = []
    for _ in range(TAILLE):
        ligne.append(INCONNU)
    grille.append(ligne)

ligne_tresor = random.randint(0, TAILLE - 1)
colonne_tresor = random.randint(0, TAILLE - 1)

trouve = False
essai = 0
while essai < NB_ESSAIS and not trouve:
    # Affichage de la grille
    print("\n   ", end="")
    for c in range(1, TAILLE + 1):
        print(c, end=" ")
    print()
    for l in range(TAILLE):
        print(f"{l + 1} :", end=" ")
        for c in range(TAILLE):
            print(grille[l][c], end=" ")
        print()

    # Saisie d'une case valide et pas encore essayée
    case_valide = False
    while not case_valide:
        valide = False
        while not valide:
            try:
                ligne_essai = int(input(f"Ligne (1 à {TAILLE}) : "))
                if 1 <= ligne_essai <= TAILLE:
                    valide = True
                else:
                    print(f"La ligne doit être entre 1 et {TAILLE}.")
            except ValueError:
                print("Ce n'est pas un nombre entier.")

        valide = False
        while not valide:
            try:
                colonne_essai = int(input(f"Colonne (1 à {TAILLE}) : "))
                if 1 <= colonne_essai <= TAILLE:
                    valide = True
                else:
                    print(f"La colonne doit être entre 1 et {TAILLE}.")
            except ValueError:
                print("Ce n'est pas un nombre entier.")

        ligne_essai -= 1
        colonne_essai -= 1
        if grille[ligne_essai][colonne_essai] == ESSAYE:
            print("Tu as déjà essayé cette case.")
        else:
            case_valide = True

    essai += 1
    grille[ligne_essai][colonne_essai] = ESSAYE
    distance = abs(ligne_essai - ligne_tresor) + abs(colonne_essai - colonne_tresor)

    if distance == 0:
        trouve = True
        print(f"Trésor trouvé en {essai} essai(s)!")
    elif distance == 1:
        print("Brûlant!")
    elif distance == 2:
        print("Chaud!")
    else:
        print("Froid.")

if not trouve:
    print(f"\nPlus d'essais! Le trésor était à la ligne {ligne_tresor + 1}, colonne {colonne_tresor + 1}.")

# Grille finale
grille[ligne_tresor][colonne_tresor] = TRESOR
print("\nGrille finale :")
for ligne in grille:
    for case in ligne:
        print(case, end=" ")
    print()
```

- La position du trésor est gardée dans deux variables, **pas** dans la grille affichée : sinon, il faudrait éviter de l'afficher pendant la partie.
- La saisie d'une case combine trois boucles de validation : une pour la ligne, une pour la colonne, et une boucle extérieure qui recommence tant que la case a déjà été essayée.
- L'utilisateur compte à partir de 1, la grille à partir de 0 : on soustrait 1 une seule fois, juste après la saisie.

## ⭐⭐ Défi 5 : Carte de bingo

### ✅ Solution 5

```python
import random

LETTRES = "BINGO"
TAILLE = 5
NUMEROS_PAR_COLONNE = 15
NUMERO_MAX = len(LETTRES) * NUMEROS_PAR_COLONNE
CENTRE = TAILLE // 2
CASE_LIBRE = 0

# a. Génération de la carte, colonne par colonne
carte = []
marquees = []
for _ in range(TAILLE):
    carte.append([0] * TAILLE)
    marquees.append([False] * TAILLE)

for c in range(TAILLE):
    debut = c * NUMEROS_PAR_COLONNE + 1
    numeros = random.sample(range(debut, debut + NUMEROS_PAR_COLONNE), TAILLE)
    for l in range(TAILLE):
        carte[l][c] = numeros[l]

carte[CENTRE][CENTRE] = CASE_LIBRE
marquees[CENTRE][CENTRE] = True

print("Carte :")
for lettre in LETTRES:
    print(f"{lettre:>4}", end="")
print()
for ligne in carte:
    for numero in ligne:
        if numero == CASE_LIBRE:
            print(f"{'**':>4}", end="")
        else:
            print(f"{numero:>4}", end="")
    print()

# b. Tirage
boules = list(range(1, NUMERO_MAX + 1))
random.shuffle(boules)

tirees = []
complete = ""
for boule in boules:
    tirees.append(boule)

    # Marquer le numéro s'il est sur la carte
    for l in range(TAILLE):
        for c in range(TAILLE):
            if carte[l][c] == boule:
                marquees[l][c] = True

    # Vérifier les lignes
    for l in range(TAILLE):
        ligne_pleine = True
        for c in range(TAILLE):
            if not marquees[l][c]:
                ligne_pleine = False
        if ligne_pleine:
            complete = f"Ligne {l + 1}"

    # Vérifier les colonnes
    for c in range(TAILLE):
        colonne_pleine = True
        for l in range(TAILLE):
            if not marquees[l][c]:
                colonne_pleine = False
        if colonne_pleine:
            complete = f"Colonne {LETTRES[c]}"

    if complete != "":
        break

# c. Résultats
texte_tirees = ""
for n in tirees:
    texte_tirees += str(n) + " "
print("\nNuméros tirés :", texte_tirees)
print(f"BINGO après {len(tirees)} boules! ({complete})")
print("\nCarte finale :")
for l in range(TAILLE):
    for c in range(TAILLE):
        if marquees[l][c]:
            print(f"{'X':>4}", end="")
        else:
            print(f"{carte[l][c]:>4}", end="")
    print()
```

- `random.sample()` garantit des numéros **différents** dans chaque colonne. Comme `sample()` donne une colonne, et que la carte est une liste de lignes, on range chaque numéro avec `carte[l][c] = numeros[l]`.
- `[0] * TAILLE` est sans danger pour une ligne de nombres, mais `[[0] * TAILLE] * TAILLE` aurait créé 5 alias de la **même** ligne (fiche 6.3) : c'est pourquoi chaque ligne est ajoutée séparément dans une boucle.
- Mélanger toutes les boules d'avance (`shuffle()`), puis les parcourir avec un `for`, garantit qu'aucun numéro n'est tiré deux fois.
- `join()` ne fonctionne qu'avec une liste de **chaînes** : pour afficher les numéros tirés, on construit plutôt la chaîne dans une boucle, avec `str(n)`.

**Pour aller plus loin** : ajoute la vérification des deux diagonales, ou fais jouer deux cartes en même temps pour voir laquelle gagne en premier.
