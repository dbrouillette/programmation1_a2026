# Exercices — Boucles `for` et nombres aléatoires (exercices supplémentaires)

> 📌 Ces exercices supplémentaires mettent en pratique la fiche [6.1 - La boucle for](../6.1%20-%20La%20boucle%20for.md) et le module [`random`](../../Outils/Nombres%20aléatoires%20-%20Module%20random.md).
>
> **Validation obligatoire** : chaque saisie doit être **validée** (type et valeur) à l'aide des recettes de la fiche [5.3 - La validation de données](../../Cours%2005/5.3%20-%20La%20validation%20de%20données.md). Comme les résultats sont aléatoires, ta sortie sera différente des exemples.
>
> 💡 Pendant le développement, tu peux ajouter `random.seed(...)` au début de ton programme pour obtenir toujours les mêmes tirages.

## 🟢 Exercice 1 : Facile

**But** : Tirer des nombres dans une boucle et accumuler des résultats.

**Énoncé** : Tire 10 nombres entiers aléatoires entre 1 et 100 et affiche-les sur une même ligne. Affiche ensuite :

- la somme des nombres tirés;
- le nombre de nombres pairs;
- le plus grand nombre tiré.

Contrainte : n'utilise **pas** de liste ni la fonction `max()`.

*Sortie attendue :*

```text
31 76 70 17 48 78 61 81 75 9
Somme : 546
Nombres pairs : 4
Plus grand : 81
```

## 🟢 Exercice 2 : Facile

**But** : Réagir à certaines valeurs particulières d'un tirage.

**Énoncé** : Dans plusieurs jeux de rôle, on lance un dé à 20 faces. Un 20 est un **coup critique** et un 1, un **échec critique**.

Demande combien de lancers effectuer (entre 1 et 30), puis affiche chaque lancer. Ajoute `Coup critique!` à côté d'un 20 et `Échec critique!` à côté d'un 1. À la fin, affiche le nombre de coups critiques, le nombre d'échecs critiques et la moyenne des lancers (1 décimale).

*Exemple d'exécution :*

```text
Nombre de lancers (1 à 30) : 0
Le nombre doit être entre 1 et 30.
Nombre de lancers (1 à 30) : douze
Ce n'est pas un nombre entier.
Nombre de lancers (1 à 30) : 12
Lancer  1 : 15
Lancer  2 : 18
Lancer  3 : 15
Lancer  4 : 15
Lancer  5 : 17
Lancer  6 : 19
Lancer  7 :  7
Lancer  8 :  6
Lancer  9 : 17
Lancer 10 : 16
Lancer 11 : 20  Coup critique!
Lancer 12 :  6
Coups critiques : 1
Échecs critiques : 0
Moyenne : 14.2
```

## 🟢 Exercice 3 : Facile

**But** : Générer des nombres réels aléatoires et les associer à une liste de noms.

**Énoncé** : Simule les températures d'une semaine d'hiver : pour chaque jour de la liste ci-dessous, tire une température réelle entre -15 et 5 °C, arrondie à 1 décimale. Affiche la température de chaque jour, puis :

- la moyenne de la semaine (1 décimale);
- le jour le plus froid et sa température;
- le nombre de jours sous zéro.

```python
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
```

*Sortie attendue :*

```text
lundi      -10.3 °C
mardi      -12.9 °C
mercredi    -7.1 °C
jeudi      -11.9 °C
vendredi   -13.7 °C
samedi      -7.0 °C
dimanche     3.4 °C
Moyenne : -8.5 °C
Jour le plus froid : vendredi (-13.7 °C)
Jours sous zéro : 6
```

## 🟢 Exercice 4 : Facile-Moyen

**But** : Construire des chaînes à partir de caractères choisis au hasard.

**Énoncé** : Une plaque d'immatriculation est formée de 3 lettres majuscules, d'un espace et de 3 chiffres (par exemple `KDT 482`).

Demande combien de plaques générer (entre 1 et 10), puis affiche-les, numérotées. Indique ensuite combien de plaques contiennent au moins un `7`.

> **Indice** : `random.choice()` fonctionne avec une chaîne : `random.choice("0123456789")` retourne un chiffre au hasard.

*Exemple d'exécution :*

```text
Nombre de plaques (1 à 10) : 50
Le nombre doit être entre 1 et 10.
Nombre de plaques (1 à 10) : 6
 1. HSR 259
 2. PUS 190
 3. PIR 337
 4. RRP 623
 5. UEQ 601
 6. FYS 040
Plaques contenant un 7 : 1
```

## 🟡 Exercice 5 : Moyen

**But** : Repérer une suite de résultats identiques dans une série de tirages.

**Énoncé** : Demande combien de fois lancer une pièce de monnaie (entre 10 et 100). Affiche les résultats sur une même ligne, sous forme de `P` (pile) et de `F` (face). Trouve ensuite la **plus longue série** de résultats identiques consécutifs et affiche sa longueur et le côté concerné.

Contrainte : n'utilise pas de liste. Garde seulement le résultat précédent en mémoire.

*Exemple d'exécution :*

```text
Nombre de lancers (10 à 100) : 5
Le nombre doit être entre 10 et 100.
Nombre de lancers (10 à 100) : 40
FFFPFPFFFFPPPFFPFPPPPFFPPPPPFFPFPFPPPPFF
Plus longue série : 5 « pile » de suite
```

## 🟡 Exercice 6 : Moyen

**But** : Afficher l'évolution d'une position aléatoire et interrompre la boucle.

**Énoncé** : Un promeneur distrait traverse un pont étroit. Il part du centre (position 0) et, à chaque pas, se décale au hasard d'une case vers la gauche (-1) ou vers la droite (+1). Les bords du pont sont à 4 cases de chaque côté du centre : s'il atteint la position -5 ou +5, il tombe à l'eau!

Simule 20 pas. Après chaque pas, affiche le pont avec la position du promeneur (`o`) parmi les planches (`=`), comme dans l'exemple. Si le promeneur tombe, affiche `Plouf!` avec le numéro du pas et arrête la simulation. S'il fait les 20 pas sans tomber, félicite-le.

*Sortie attendue :*

```text
Pas  1 : |===o=====|
Pas  2 : |====o====|
Pas  3 : |=====o===|
Pas  4 : |====o====|
Pas  5 : |===o=====|
Pas  6 : |==o======|
Pas  7 : |=o=======|
Pas  8 : |o========|
Pas  9 : Plouf! Le promeneur est tombé à l'eau.
```

## 🟡 Exercice 7 : Moyen

**But** : Combiner une boucle `for`, des saisies validées et des probabilités.

**Énoncé** : Un héros (30 points de vie) affronte un monstre (25 points de vie) pendant au plus 8 rondes. À chaque ronde :

- Le joueur choisit d'**attaquer** (`a`) ou de **se soigner** (`s`).
- **Attaque** : le héros inflige de 3 à 8 points de dégâts. Dans 20 % des cas, c'est un coup critique et les dégâts sont doublés.
- **Soin** : le héros récupère de 4 à 8 points de vie, sans dépasser son maximum de 30.
- Si le monstre est encore debout, il riposte et inflige de 2 à 7 points de dégâts.

Affiche les points de vie des deux combattants au début de chaque ronde. Le combat s'arrête dès qu'un combattant n'a plus de points de vie. Après 8 rondes, si les deux sont encore debout, le monstre s'enfuit.

*Exemple d'exécution :*

```text
--- Ronde 1 --- Héros : 30 PV | Monstre : 25 PV
Attaquer (a) ou se soigner (s)? a
Coup critique! Le héros inflige 8 points de dégâts.
Le monstre riposte et inflige 7 points de dégâts.

--- Ronde 2 --- Héros : 23 PV | Monstre : 17 PV
Attaquer (a) ou se soigner (s)? attaque
Choix invalide.
Attaquer (a) ou se soigner (s)? a
Coup critique! Le héros inflige 6 points de dégâts.
Le monstre riposte et inflige 3 points de dégâts.

--- Ronde 3 --- Héros : 20 PV | Monstre : 11 PV
Attaquer (a) ou se soigner (s)? s
Le héros récupère des forces (24 PV).
Le monstre riposte et inflige 2 points de dégâts.

--- Ronde 4 --- Héros : 22 PV | Monstre : 11 PV
Attaquer (a) ou se soigner (s)? a
Coup critique! Le héros inflige 16 points de dégâts.

Victoire! Le monstre est vaincu.
```

## 🟡 Exercice 8 : Moyen

**But** : Comparer deux chaînes position par position.

**Énoncé** : Un cadenas est verrouillé par un code secret de 4 chiffres, généré au hasard (un même chiffre peut revenir plusieurs fois, et le code peut commencer par 0). Le joueur a 10 essais pour l'ouvrir.

- Chaque essai doit contenir **exactement 4 caractères**, et ce doivent tous être des chiffres. Sinon, affiche un message et redemande l'essai.
- Après chaque essai, affiche un indice d'une ligne : `✓` sous chaque chiffre bien placé et `✗` sous les autres.
- Si le joueur trouve le code, affiche le nombre d'essais utilisés. Sinon, révèle le code à la fin.

> **Indice** : construis le code comme une **chaîne** de 4 caractères. La comparaison se fait ensuite avec `essai[i] == code[i]`.

*Exemple d'exécution :*

```text
Essai 1/10 : 1234
             ✗✗✗✗
Essai 2/10 : 12a4
Le code ne contient que des chiffres.
Essai 2/10 : 567
Le code contient 4 chiffres.
Essai 2/10 : 0000
             ✓✗✗✗
Essai 3/10 : 0111
             ✓✓✓✗
Essai 4/10 : 0115
             ✓✓✓✓
Cadenas ouvert en 4 essai(s)!
```

## 🟡 Exercice 9 : Moyen

**But** : Estimer une valeur par simulation (méthode de Monte-Carlo).

**Énoncé** : On peut estimer π avec des nombres aléatoires! On lance des points au hasard dans un carré de côté 1 : leurs coordonnées `x` et `y` sont deux réels entre 0 et 1. Un point tombe dans le quart de cercle de rayon 1 si `x² + y² <= 1`. Comme l'aire du quart de cercle est π/4 et celle du carré, 1 :

> π ≈ 4 × (nombre de points dans le quart de cercle) / (nombre total de points)

Demande le nombre de points à lancer (entre 100 et 1 000 000), puis affiche l'estimation de π (5 décimales) et l'écart avec la valeur réelle `math.pi`. Affiche aussi l'estimation intermédiaire tous les 10 % des points lancés.

*Exemple d'exécution :*

```text
Nombre de points (100 à 1000000) : 50
Le nombre doit être entre 100 et 1000000.
Nombre de points (100 à 1000000) : 100000
    10000 points : π ≈ 3.14160
    20000 points : π ≈ 3.13820
    30000 points : π ≈ 3.13520
    40000 points : π ≈ 3.13570
    50000 points : π ≈ 3.13992
    60000 points : π ≈ 3.13800
    70000 points : π ≈ 3.13634
    80000 points : π ≈ 3.13880
    90000 points : π ≈ 3.13556
   100000 points : π ≈ 3.13784
Estimation finale : 3.13784
Valeur réelle     : 3.14159
Écart             : 0.00375
```

## 🔴 Exercice 10 : Moyen-Difficile

**But** : Vérifier un résultat surprenant de probabilités par simulation.

**Énoncé** : Le **problème de Monty Hall** : dans un jeu télévisé, une voiture est cachée derrière l'une de 3 portes. Le joueur choisit une porte au hasard. L'animateur, qui sait où est la voiture, ouvre alors une **autre** porte, derrière laquelle il n'y a rien. Le joueur peut garder son choix ou changer pour la porte qui reste fermée.

Vaut-il mieux garder ou changer? Demande un nombre de parties à simuler (entre 100 et 100 000). Pour chaque partie, place la voiture au hasard, fais choisir le joueur au hasard, ouvre une porte selon la règle de l'animateur, puis compte combien de fois le joueur aurait gagné en **gardant** et en **changeant**. Affiche les deux pourcentages de victoire.

> **Indice** : les portes sont numérotées 1, 2 et 3. Pour trouver la porte que l'animateur ouvre (ou celle qui reste fermée), parcours les 3 portes avec une boucle `for` et garde celle qui respecte les conditions.

*Exemple d'exécution :*

```text
Nombre de parties (100 à 100000) : dix
Ce n'est pas un nombre entier.
Nombre de parties (100 à 100000) : 10000
En gardant sa porte  : 33.8 % de victoires
En changeant de porte : 66.2 % de victoires
```

## 🔴 Exercice 11 : Moyen-Difficile

**But** : Imbriquer une boucle `while` contrôlée par le hasard et par l'utilisateur dans une boucle `for`.

**Énoncé** : Le jeu du **cochon** se joue avec un seul dé, en 5 tours. À chaque tour, le joueur lance le dé autant de fois qu'il le veut et additionne les résultats dans ses points du tour :

- s'il obtient un **1**, il perd tous les points du tour et son tour se termine;
- sinon, il choisit de **relancer** (`r`) pour accumuler plus de points, ou de **garder** (`g`) ses points du tour, qui s'ajoutent alors à son score.

Affiche chaque lancer et les points du tour en cours. À la fin des 5 tours, affiche le score total et la moyenne de points par tour.

*Exemple d'exécution :*

```text
=== Tour 1 (score : 0) ===
Lancer : 5 → points du tour : 5
Relancer (r) ou garder (g)? r
Lancer : 4 → points du tour : 9
Relancer (r) ou garder (g)? x
Choix invalide.
Relancer (r) ou garder (g)? r
Lancer : 3 → points du tour : 12
Relancer (r) ou garder (g)? g

=== Tour 2 (score : 12) ===
Lancer : 3 → points du tour : 3
Relancer (r) ou garder (g)? r
Lancer : 3 → points du tour : 6
Relancer (r) ou garder (g)? g

=== Tour 3 (score : 18) ===
Lancer : 2 → points du tour : 2
Relancer (r) ou garder (g)? r
Lancer : 6 → points du tour : 8
Relancer (r) ou garder (g)? r
Lancer : 6 → points du tour : 14
Relancer (r) ou garder (g)? g

=== Tour 4 (score : 32) ===
Lancer : 5 → points du tour : 5
Relancer (r) ou garder (g)? r
Lancer : 6 → points du tour : 11
Relancer (r) ou garder (g)? r
Lancer : 3 → points du tour : 14
Relancer (r) ou garder (g)? g

=== Tour 5 (score : 46) ===
Lancer : 1 → Cochon! Tu perds les 0 points du tour.

Score final : 46 points
Moyenne par tour : 9.2
```

## 🔴 Exercice 12 : Difficile

**But** : Simuler un système qui évolue minute par minute.

**Énoncé** : Un café étudiant a un seul barista. On veut simuler l'heure de pointe, minute par minute, pendant 60 minutes :

- au début de chaque minute, un nouveau client arrive avec une certaine probabilité, saisie par l'utilisateur en pourcentage (entre 10 et 90);
- les clients font la file. Si le barista est libre et que quelqu'un attend, il commence à servir le premier client de la file;
- chaque service dure de 1 à 4 minutes, au hasard.

Toutes les 10 minutes, affiche la minute, le nombre de personnes dans la file et l'état du barista pendant cette minute (`occupé` ou `libre`). À la fin, affiche le nombre de clients arrivés et servis, le nombre de personnes encore en file, la plus longue file observée et le pourcentage du temps où le barista a été occupé.

> **Indice** : pas besoin de liste! Deux compteurs suffisent pour représenter la situation : le nombre de personnes dans la `file` et le nombre de minutes restantes au service en cours (`0` si le barista est libre).

*Exemple d'exécution :*

```text
Probabilité d'arrivée en % (10 à 90) : cent
Ce n'est pas un nombre entier.
Probabilité d'arrivée en % (10 à 90) : 95
Le nombre doit être entre 10 et 90.
Probabilité d'arrivée en % (10 à 90) : 45
Minute 10 : 2 personne(s) en file, barista occupé
Minute 20 : 2 personne(s) en file, barista occupé
Minute 30 : 1 personne(s) en file, barista occupé
Minute 40 : 3 personne(s) en file, barista occupé
Minute 50 : 4 personne(s) en file, barista occupé
Minute 60 : 5 personne(s) en file, barista occupé

Clients arrivés : 26
Clients servis : 20
Encore en file : 5
Plus longue file : 6
Barista occupé : 100 % du temps
```

**Bonus** : quelle probabilité d'arrivée fait exploser la file? Essaie 20 %, 40 % et 60 %. Ajoute ensuite un deuxième barista et compare.
