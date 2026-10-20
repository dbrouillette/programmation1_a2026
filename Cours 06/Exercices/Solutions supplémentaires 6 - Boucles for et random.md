# Solutions — Boucles `for` et nombres aléatoires (exercices supplémentaires)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
import random

NB_TIRAGES = 10
NOMBRE_MIN = 1
NOMBRE_MAX = 100

somme = 0
nb_pairs = 0
plus_grand = NOMBRE_MIN
for _ in range(NB_TIRAGES):
    nombre = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    print(nombre, end=" ")
    somme += nombre
    if nombre % 2 == 0:
        nb_pairs += 1
    if nombre > plus_grand:
        plus_grand = nombre
print()

print("Somme :", somme)
print("Nombres pairs :", nb_pairs)
print("Plus grand :", plus_grand)
```

Chaque nombre est traité **au moment où il est tiré** : pas besoin de le conserver. `plus_grand` peut être initialisé à `NOMBRE_MIN`, puisqu'aucun tirage ne peut être plus petit.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
import random

NB_FACES = 20
NB_LANCERS_MIN = 1
NB_LANCERS_MAX = 30

valide = False
while not valide:
    try:
        nb_lancers = int(input(f"Nombre de lancers ({NB_LANCERS_MIN} à {NB_LANCERS_MAX}) : "))
        if NB_LANCERS_MIN <= nb_lancers <= NB_LANCERS_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_LANCERS_MIN} et {NB_LANCERS_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

total = 0
nb_coups_critiques = 0
nb_echecs_critiques = 0
for lancer in range(1, nb_lancers + 1):
    resultat = random.randint(1, NB_FACES)
    total += resultat
    message = f"Lancer {lancer:2} : {resultat:2}"
    if resultat == NB_FACES:
        message += "  Coup critique!"
        nb_coups_critiques += 1
    elif resultat == 1:
        message += "  Échec critique!"
        nb_echecs_critiques += 1
    print(message)

print("Coups critiques :", nb_coups_critiques)
print("Échecs critiques :", nb_echecs_critiques)
print(f"Moyenne : {total / nb_lancers:.1f}")
```

La moyenne théorique d'un dé à 20 faces est 10,5. Avec peu de lancers, la moyenne obtenue s'en éloigne souvent; plus on lance, plus elle s'en rapproche.

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
import random

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
TEMPERATURE_MIN = -15
TEMPERATURE_MAX = 5

total = 0
nb_jours_sous_zero = 0
temperature_min = TEMPERATURE_MAX
jour_le_plus_froid = ""
for jour in JOURS:
    temperature = round(random.uniform(TEMPERATURE_MIN, TEMPERATURE_MAX), 1)
    print(f"{jour:<10}{temperature:>6.1f} °C")
    total += temperature
    if temperature < 0:
        nb_jours_sous_zero += 1
    if temperature < temperature_min:
        temperature_min = temperature
        jour_le_plus_froid = jour

print(f"Moyenne : {total / len(JOURS):.1f} °C")
print(f"Jour le plus froid : {jour_le_plus_froid} ({temperature_min} °C)")
print("Jours sous zéro :", nb_jours_sous_zero)
```

On mémorise le **jour** en même temps que la température minimale : c'est la seule façon de savoir, après la boucle, quel jour a été le plus froid.

## 🟢 Exercice 4 : Facile-Moyen

### ✅ Solution 4

```python
import random

NB_PLAQUES_MIN = 1
NB_PLAQUES_MAX = 10
NB_LETTRES = 3
NB_CHIFFRES = 3
LETTRES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHIFFRES = "0123456789"
CHIFFRE_RECHERCHE = "7"

valide = False
while not valide:
    try:
        nb_plaques = int(input(f"Nombre de plaques ({NB_PLAQUES_MIN} à {NB_PLAQUES_MAX}) : "))
        if NB_PLAQUES_MIN <= nb_plaques <= NB_PLAQUES_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_PLAQUES_MIN} et {NB_PLAQUES_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

nb_avec_chiffre = 0
for no_plaque in range(1, nb_plaques + 1):
    plaque = ""
    for _ in range(NB_LETTRES):
        plaque += random.choice(LETTRES)
    plaque += " "
    for _ in range(NB_CHIFFRES):
        plaque += random.choice(CHIFFRES)

    print(f"{no_plaque:2}. {plaque}")
    if CHIFFRE_RECHERCHE in plaque:
        nb_avec_chiffre += 1

print(f"Plaques contenant un {CHIFFRE_RECHERCHE} : {nb_avec_chiffre}")
```

La variable `plaque` doit repartir d'une chaîne vide **à chaque** plaque : elle est donc initialisée dans la boucle extérieure. L'opérateur `in` vérifie si une sous-chaîne fait partie d'une chaîne.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
import random

NB_LANCERS_MIN = 10
NB_LANCERS_MAX = 100
PILE = "P"
FACE = "F"

valide = False
while not valide:
    try:
        nb_lancers = int(input(f"Nombre de lancers ({NB_LANCERS_MIN} à {NB_LANCERS_MAX}) : "))
        if NB_LANCERS_MIN <= nb_lancers <= NB_LANCERS_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_LANCERS_MIN} et {NB_LANCERS_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

precedent = ""
serie_courante = 0
meilleure_serie = 0
cote_meilleure = ""
for _ in range(nb_lancers):
    resultat = random.choice([PILE, FACE])
    print(resultat, end="")

    if resultat == precedent:
        serie_courante += 1
    else:
        serie_courante = 1
    precedent = resultat

    if serie_courante > meilleure_serie:
        meilleure_serie = serie_courante
        cote_meilleure = resultat
print()

if cote_meilleure == PILE:
    nom_cote = "pile"
else:
    nom_cote = "face"
print(f"Plus longue série : {meilleure_serie} « {nom_cote} » de suite")
```

- `precedent` est initialisé à une chaîne vide : le premier lancer est donc toujours différent du « précédent » et démarre une série de longueur 1.
- Les gens qui inventent une suite « au hasard » évitent les longues séries. En réalité, sur 40 lancers, une série de 5 ou plus est très fréquente!

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
import random

NB_PAS = 20
DEMI_LARGEUR = 4
PROMENEUR = "o"
PLANCHE = "="

position = 0
tombe = False
for pas in range(1, NB_PAS + 1):
    position += random.choice([-1, 1])

    if abs(position) > DEMI_LARGEUR:
        print(f"Pas {pas:2} : Plouf! Le promeneur est tombé à l'eau.")
        tombe = True
        break

    pont = ""
    for case in range(-DEMI_LARGEUR, DEMI_LARGEUR + 1):
        if case == position:
            pont += PROMENEUR
        else:
            pont += PLANCHE
    print(f"Pas {pas:2} : |{pont}|")

if not tombe:
    print(f"Bravo! Le promeneur a fait ses {NB_PAS} pas sans tomber.")
```

- La boucle intérieure parcourt les positions de `-DEMI_LARGEUR` à `DEMI_LARGEUR` : `range()` accepte des valeurs négatives.
- Le drapeau `tombe` permet de savoir, après la boucle, si on en est sorti par le `break` ou après les 20 pas.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
import random

PV_MAX_HEROS = 30
PV_MAX_MONSTRE = 25
NB_RONDES_MAX = 8
ATTAQUE_MIN = 3
ATTAQUE_MAX = 8
PROBABILITE_CRITIQUE = 0.2
SOIN_MIN = 4
SOIN_MAX = 8
ATTAQUE_MONSTRE_MIN = 2
ATTAQUE_MONSTRE_MAX = 7
ATTAQUER = "a"
SOIGNER = "s"

pv_heros = PV_MAX_HEROS
pv_monstre = PV_MAX_MONSTRE

for ronde in range(1, NB_RONDES_MAX + 1):
    print(f"\n--- Ronde {ronde} --- Héros : {pv_heros} PV | Monstre : {pv_monstre} PV")

    choix = input(f"Attaquer ({ATTAQUER}) ou se soigner ({SOIGNER})? ").strip().lower()
    while choix != ATTAQUER and choix != SOIGNER:
        print("Choix invalide.")
        choix = input(f"Attaquer ({ATTAQUER}) ou se soigner ({SOIGNER})? ").strip().lower()

    # Action du héros
    if choix == ATTAQUER:
        degats = random.randint(ATTAQUE_MIN, ATTAQUE_MAX)
        if random.random() < PROBABILITE_CRITIQUE:
            degats *= 2
            print("Coup critique!", end=" ")
        pv_monstre = max(pv_monstre - degats, 0)
        print(f"Le héros inflige {degats} points de dégâts.")
    else:
        soin = random.randint(SOIN_MIN, SOIN_MAX)
        pv_heros = min(pv_heros + soin, PV_MAX_HEROS)
        print(f"Le héros récupère des forces ({pv_heros} PV).")

    if pv_monstre == 0:
        break

    # Riposte du monstre
    degats = random.randint(ATTAQUE_MONSTRE_MIN, ATTAQUE_MONSTRE_MAX)
    pv_heros = max(pv_heros - degats, 0)
    print(f"Le monstre riposte et inflige {degats} points de dégâts.")

    if pv_heros == 0:
        break

if pv_monstre == 0:
    print("\nVictoire! Le monstre est vaincu.")
elif pv_heros == 0:
    print("\nDéfaite... Le héros est tombé au combat.")
else:
    print("\nLe monstre s'enfuit dans la forêt!")
```

- `max(pv - degats, 0)` empêche les points de vie de devenir négatifs, et `min(pv + soin, PV_MAX_HEROS)` les empêche de dépasser le maximum.
- Après la boucle, ce sont les points de vie qui indiquent comment le combat s'est terminé : il n'y a pas besoin de drapeau supplémentaire.

## 🟡 Exercice 8 : Moyen

### ✅ Solution 8

```python
import random

LONGUEUR_CODE = 4
NB_ESSAIS = 10
CHIFFRES = "0123456789"
BIEN_PLACE = "✓"
MAL_PLACE = "✗"

code = ""
for _ in range(LONGUEUR_CODE):
    code += random.choice(CHIFFRES)

ouvert = False
for no_essai in range(1, NB_ESSAIS + 1):
    # Saisie d'un essai valide
    valide = False
    while not valide:
        essai = input(f"Essai {no_essai}/{NB_ESSAIS} : ").strip()
        if len(essai) != LONGUEUR_CODE:
            print(f"Le code contient {LONGUEUR_CODE} chiffres.")
        else:
            valide = True
            for caractere in essai:
                if caractere not in CHIFFRES:
                    valide = False
            if not valide:
                print("Le code ne contient que des chiffres.")

    # Indice
    indice = ""
    for i in range(LONGUEUR_CODE):
        if essai[i] == code[i]:
            indice += BIEN_PLACE
        else:
            indice += MAL_PLACE
    print(" " * len(f"Essai {no_essai}/{NB_ESSAIS} : ") + indice)

    if essai == code:
        ouvert = True
        break

if ouvert:
    print(f"Cadenas ouvert en {no_essai} essai(s)!")
else:
    print(f"Le cadenas reste fermé. Le code était {code}.")
```

- La validation d'un essai demande deux vérifications : la **longueur**, puis le fait que **chaque** caractère soit un chiffre (une boucle `for` sur l'essai). `int(essai)` ne suffirait pas : il accepterait `-123` ou ` 12`, et il ferait perdre un `0` en début de code.
- L'indice est décalé du même nombre d'espaces que l'invite, pour s'aligner sous l'essai. `" " * n` répète une chaîne `n` fois.

## 🟡 Exercice 9 : Moyen

### ✅ Solution 9

```python
import math
import random

NB_POINTS_MIN = 100
NB_POINTS_MAX = 1_000_000
NB_ETAPES = 10

valide = False
while not valide:
    try:
        nb_points = int(input(f"Nombre de points ({NB_POINTS_MIN} à {NB_POINTS_MAX}) : "))
        if NB_POINTS_MIN <= nb_points <= NB_POINTS_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_POINTS_MIN} et {NB_POINTS_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

taille_etape = nb_points // NB_ETAPES
nb_dedans = 0
for point in range(1, nb_points + 1):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        nb_dedans += 1

    if point % taille_etape == 0:
        print(f"{point:>9} points : π ≈ {4 * nb_dedans / point:.5f}")

estimation = 4 * nb_dedans / nb_points
print(f"Estimation finale : {estimation:.5f}")
print(f"Valeur réelle     : {math.pi:.5f}")
print(f"Écart             : {abs(estimation - math.pi):.5f}")
```

- `random.random()` donne un réel entre 0 (inclus) et 1 (exclu) : exactement ce qu'il faut pour une coordonnée dans le carré.
- `point % taille_etape == 0` est vrai tous les 10 % des points : c'est un moyen simple d'afficher une progression.
- `1_000_000` s'écrit aussi `1000000` : Python ignore les `_` dans les nombres, qui servent seulement à faciliter la lecture.
- L'estimation s'améliore lentement : il faut environ 100 fois plus de points pour gagner une décimale de précision.

## 🔴 Exercice 10 : Moyen-Difficile

### ✅ Solution 10

```python
import random

NB_PORTES = 3
NB_PARTIES_MIN = 100
NB_PARTIES_MAX = 100_000

valide = False
while not valide:
    try:
        nb_parties = int(input(f"Nombre de parties ({NB_PARTIES_MIN} à {NB_PARTIES_MAX}) : "))
        if NB_PARTIES_MIN <= nb_parties <= NB_PARTIES_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {NB_PARTIES_MIN} et {NB_PARTIES_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

victoires_en_gardant = 0
victoires_en_changeant = 0
for _ in range(nb_parties):
    voiture = random.randint(1, NB_PORTES)
    choix = random.randint(1, NB_PORTES)

    # L'animateur ouvre une porte qui n'est ni le choix du joueur ni la voiture
    porte_ouverte = 0
    for porte in range(1, NB_PORTES + 1):
        if porte != choix and porte != voiture:
            porte_ouverte = porte

    # La porte restante n'est ni le choix du joueur ni la porte ouverte
    porte_restante = 0
    for porte in range(1, NB_PORTES + 1):
        if porte != choix and porte != porte_ouverte:
            porte_restante = porte

    if choix == voiture:
        victoires_en_gardant += 1
    if porte_restante == voiture:
        victoires_en_changeant += 1

print(f"En gardant sa porte  : {victoires_en_gardant / nb_parties * 100:.1f} % de victoires")
print(f"En changeant de porte : {victoires_en_changeant / nb_parties * 100:.1f} % de victoires")
```

- Changer de porte fait gagner environ **2 fois sur 3**! En gardant, on ne gagne que si le premier choix était le bon (1 chance sur 3). En changeant, on gagne chaque fois que le premier choix était **mauvais** (2 chances sur 3), car l'animateur a éliminé l'autre mauvaise porte.
- Quand le joueur a choisi la voiture du premier coup, deux portes respectent la condition de l'animateur : la boucle garde la dernière trouvée, ce qui ne change rien au résultat.

## 🔴 Exercice 11 : Moyen-Difficile

### ✅ Solution 11

```python
import random

NB_TOURS = 5
NB_FACES = 6
FACE_COCHON = 1
RELANCER = "r"
GARDER = "g"

score = 0
for tour in range(1, NB_TOURS + 1):
    print(f"\n=== Tour {tour} (score : {score}) ===")
    points_tour = 0
    tour_termine = False
    while not tour_termine:
        de = random.randint(1, NB_FACES)
        if de == FACE_COCHON:
            print(f"Lancer : {de} → Cochon! Tu perds les {points_tour} points du tour.")
            points_tour = 0
            tour_termine = True
        else:
            points_tour += de
            print(f"Lancer : {de} → points du tour : {points_tour}")
            choix = input(f"Relancer ({RELANCER}) ou garder ({GARDER})? ").strip().lower()
            while choix != RELANCER and choix != GARDER:
                print("Choix invalide.")
                choix = input(f"Relancer ({RELANCER}) ou garder ({GARDER})? ").strip().lower()
            if choix == GARDER:
                tour_termine = True
    score += points_tour

print(f"\nScore final : {score} points")
print(f"Moyenne par tour : {score / NB_TOURS:.1f}")
```

- Le nombre de **tours** est connu (`for`), mais pas le nombre de **lancers** dans un tour : il dépend du hasard et des choix du joueur (`while`).
- `points_tour` doit être remis à zéro au début de **chaque** tour, donc à l'intérieur de la boucle `for`.
- Pour aller plus loin : quelle stratégie rapporte le plus? Simule 10 000 parties sans saisie, où le joueur garde ses points dès qu'il atteint 20 dans un tour, puis compare avec un seuil de 10 ou de 30.

## 🔴 Exercice 12 : Difficile

### ✅ Solution 12

```python
import random

DUREE_MINUTES = 60
INTERVALLE_AFFICHAGE = 10
PROBABILITE_MIN = 10
PROBABILITE_MAX = 90
SERVICE_MIN = 1
SERVICE_MAX = 4

valide = False
while not valide:
    try:
        probabilite = int(input(f"Probabilité d'arrivée en % ({PROBABILITE_MIN} à {PROBABILITE_MAX}) : "))
        if PROBABILITE_MIN <= probabilite <= PROBABILITE_MAX:
            valide = True
        else:
            print(f"Le nombre doit être entre {PROBABILITE_MIN} et {PROBABILITE_MAX}.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

file = 0
minutes_restantes = 0       # 0 : le barista est libre
nb_arrives = 0
nb_servis = 0
file_max = 0
minutes_occupe = 0

for minute in range(1, DUREE_MINUTES + 1):
    # Arrivée d'un client
    if random.random() < probabilite / 100:
        file += 1
        nb_arrives += 1

    # Le barista libre prend le premier client de la file
    if minutes_restantes == 0 and file > 0:
        file -= 1
        minutes_restantes = random.randint(SERVICE_MIN, SERVICE_MAX)

    if file > file_max:
        file_max = file

    # Une minute de service s'écoule
    occupe = minutes_restantes > 0
    if occupe:
        minutes_occupe += 1
        minutes_restantes -= 1
        if minutes_restantes == 0:
            nb_servis += 1

    if minute % INTERVALLE_AFFICHAGE == 0:
        if occupe:
            etat = "occupé"
        else:
            etat = "libre"
        print(f"Minute {minute:2} : {file} personne(s) en file, barista {etat}")

print(f"\nClients arrivés : {nb_arrives}")
print(f"Clients servis : {nb_servis}")
print(f"Encore en file : {file}")
print(f"Plus longue file : {file_max}")
print(f"Barista occupé : {minutes_occupe / DUREE_MINUTES * 100:.0f} % du temps")
```

- L'ordre des étapes dans une minute est important : on accueille d'abord le client qui arrive, puis le barista libre commence un service, puis la minute de service s'écoule.
- Le booléen `occupe` mémorise si le barista a travaillé **pendant** la minute, avant que `minutes_restantes` ne soit diminué : sans lui, un service qui se termine à la minute 10 afficherait « libre » alors que le barista a été occupé toute la minute.
- Un client compte comme « servi » quand son service **se termine**. À la fin, un client peut donc être en cours de service : il n'est ni dans la file ni compté comme servi.
- Quand les clients arrivent en moyenne plus vite qu'ils ne sont servis (un service dure 2,5 minutes en moyenne), la file grandit sans arrêt : c'est ce qu'on observe à partir d'environ 40 %.
