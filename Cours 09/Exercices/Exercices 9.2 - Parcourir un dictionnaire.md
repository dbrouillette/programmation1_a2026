# Exercices — Parcourir un dictionnaire (fiche 9.2)

> 🎄 **Vers le TP3** : dans ces exercices, on analyse une vraie chanson, le refrain de *Vive le vent* (mélodie de *Jingle Bells*, J. Pierpont, 1857, domaine public). Chaque note est une rangée `[note, intensite, duree]` : la note (`"MI4"`), l'intensité lumineuse (0 à 100 %) et la durée (en millisecondes). C'est le format des chansons du TP3.

> 📌 Copie ces données au début de tes programmes lorsqu'un exercice en a besoin :

```python
FREQUENCES = {
    "DO4": 262, "RE4": 294, "MI4": 330, "FA4": 349,
    "SOL4": 392, "LA4": 440, "SI4": 494, "DO5": 523,
}
GAMME = ["DO4", "RE4", "MI4", "FA4", "SOL4", "LA4", "SI4", "DO5"]

# Refrain de Vive le vent : [note, intensite, duree]
CHANSON = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
    ["FA4", 70, 300], ["FA4", 70, 300], ["FA4", 70, 450], ["FA4", 50, 150],
    ["FA4", 70, 300], ["MI4", 70, 300], ["MI4", 70, 300], ["MI4", 50, 150], ["MI4", 50, 150],
    ["MI4", 80, 300], ["RE4", 80, 300], ["RE4", 80, 300], ["MI4", 80, 300],
    ["RE4", 90, 600], ["SOL4", 100, 600],
]
```

## 🟢 Exercice 1 : Facile

**But** : Parcourir un dictionnaire avec `items()` et retrouver la clé d'une valeur extrême.

**Énoncé** : Écris un programme qui affiche la table `FREQUENCES` sous forme de tableau, en utilisant `items()`. Écris ensuite une fonction `trouver_extremes(table)` qui **renvoie** un tuple `(note_grave, note_aigue)` : les **clés** de la plus petite et de la plus grande fréquence. Le programme termine en affichant l'écart entre les deux fréquences, calculé avec `min()` et `max()`.

*Sortie attendue :*

```text
Note   Fréquence
----------------
DO4      262 Hz
RE4      294 Hz
MI4      330 Hz
FA4      349 Hz
SOL4     392 Hz
LA4      440 Hz
SI4      494 Hz
DO5      523 Hz
----------------
8 notes, de DO4 (262 Hz) à DO5 (523 Hz)
Écart : 261 Hz
```

> 💡 La fonction ne doit **pas** supposer que la table est triée : teste-la en changeant l'ordre des paires.

## 🟢 Exercice 2 : Facile

**But** : Appliquer le patron compteur.

**Énoncé** : Voici seulement les noms des notes du refrain :

```python
MELODIE = [
    "MI4", "MI4", "MI4", "MI4", "MI4", "MI4", "MI4", "SOL4", "DO4", "RE4", "MI4",
    "FA4", "FA4", "FA4", "FA4", "FA4", "MI4", "MI4", "MI4", "MI4", "MI4",
    "RE4", "RE4", "MI4", "RE4", "SOL4",
]
```

Écris une fonction `compter_notes(melodie)` qui **renvoie** un dictionnaire `{note: nombre d'apparitions}`. Le programme affiche le dictionnaire, puis un histogramme de **toutes** les notes de la gamme, dans l'ordre de `GAMME` (même celles qui n'apparaissent pas).

*Sortie attendue :*

```text
{'MI4': 14, 'SOL4': 2, 'DO4': 1, 'RE4': 4, 'FA4': 5}

DO4    1 #
RE4    4 ####
MI4   14 ##############
FA4    5 #####
SOL4   2 ##
LA4    0
SI4    0
DO5    0

26 notes, 5 notes différentes
```

## 🟡 Exercice 3 : Moyen

**But** : Additionner des valeurs par clé et combiner plusieurs dictionnaires.

**Énoncé** : À partir de `CHANSON`, écris :

- `additionner_par_note(chanson, colonne)`, qui **renvoie** un dictionnaire `{note: somme}` pour la colonne demandée (`1` pour l'intensité, `2` pour la durée);
- `compter_par_note(chanson)`, qui **renvoie** le nombre de rangées par note;
- `trouver_cle_max(dictionnaire)`, qui **renvoie** la clé de la plus grande valeur.

Le programme affiche, pour chaque note : son nombre d'apparitions, sa durée totale et son intensité moyenne. Il termine par la durée totale de la chanson et la note qui occupe le plus de temps, avec son pourcentage.

*Sortie attendue :*

```text
Note   Nombre  Durée (ms)  Intensité moy.
MI4        14        5400           78.6%
SOL4        2         900           90.0%
DO4         1         450           90.0%
RE4         4        1350           77.5%
FA4         5        1500           66.0%

Durée totale : 9.6 s
Note dominante : MI4 (56 % du temps)
```

> 💡 L'intensité moyenne d'une note = la somme de ses intensités ÷ son nombre d'apparitions. Les trois dictionnaires ont les mêmes clés : un seul parcours avec `items()` suffit pour l'affichage.

## 🟡 Exercice 4 : Moyen

**But** : Construire un dictionnaire de résultats pendant une validation.

**Énoncé** : Dans le TP3, les chansons viendront de fichiers écrits à la main… avec des erreurs! Voici une chanson à vérifier (*Au clair de la lune*) :

```python
CHANSON_A_VERIFIER = [
    ["DO4", 70, 400],
    ["DO4", 70, 400],
    ["D04", 70, 400],
    ["RE4", 70, 400],
    ["MI4", 150, 800],
    ["-", 0, 400],
    ["RE4", 70, 10],
    ["DO4", 70, 400],
    ["MI4", 70, 400],
    ["RE4", -5, 5000],
    ["RE4", 70, 400],
    ["DO4", 90, 1200],
]
```

Une rangée est valide si :

- la note est dans `FREQUENCES`, **ou** est un silence `"-"`;
- l'intensité est entre 0 et 100;
- la durée est entre 50 et 2000 ms.

Écris :

- `trouver_erreur(rangee)`, qui **renvoie** un message décrivant la **première** erreur de la rangée, ou une chaîne vide si elle est valide;
- `valider_chanson(chanson)`, qui **renvoie** un dictionnaire `{numéro de la note: message}`, en numérotant les notes à partir de 1.

Le programme affiche les erreurs, puis construit une nouvelle liste qui ne contient que les rangées valides.

*Sortie attendue :*

```text
❌ 4 erreur(s) :
  Note  3 : note « D04 » inconnue
  Note  5 : intensité 150 hors de 0 à 100
  Note  7 : durée 10 ms hors de 50 à 2000
  Note 10 : intensité -5 hors de 0 à 100
8 note(s) valide(s) conservée(s) sur 12.
```

> 💡 Regarde bien la note 3 : c'est `D04` avec un **zéro**, pas un O. Une erreur classique dans un fichier écrit à la main! Et la note 10 a deux erreurs, mais seule la première est rapportée.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Utiliser un dictionnaire de couleurs `colorama` pour simuler les lumières du sapin.

**Énoncé** : Avant de brancher le vrai sapin, on simule ses lumières dans la console avec `colorama` (voir la fiche [Couleurs - Module colorama](../../Outils/Couleurs%20-%20Module%20colorama.md)). La console n'a que 8 couleurs; voici la correspondance choisie pour les notes :

```python
from colorama import Fore, Style, init

init(autoreset=True)

COULEURS_CONSOLE = {
    "DO": Fore.RED,
    "RE": Fore.YELLOW,
    "MI": Fore.YELLOW + Style.BRIGHT,
    "FA": Fore.GREEN,
    "SOL": Fore.BLUE,
    "LA": Fore.CYAN,
    "SI": Fore.MAGENTA,
}
```

Écris :

- `couleur_console(note)`, qui **renvoie** le code de couleur de la note, sans tenir compte de l'octave (`Fore.WHITE` si la note est inconnue);
- `additionner_durees(chanson)`, qui **renvoie** `{note: durée totale}`;
- `afficher_histogramme(durees)`, qui affiche, dans l'ordre de `GAMME` et seulement pour les notes présentes, une barre de symboles `●` **colorée**, à raison d'un symbole par 150 ms;
- `afficher_sapin_lumineux(chanson)`, qui affiche sur **une seule ligne** un `●` coloré pour chaque note de la chanson, comme une bande de DEL.

*Sortie attendue (en couleurs dans ta console) :*

```text
DO4     450 ms ●●●
RE4    1350 ms ●●●●●●●●●
MI4    5400 ms ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
FA4    1500 ms ●●●●●●●●●●
SOL4    900 ms ●●●●●●

●●●●●●●●●●●●●●●●●●●●●●●●●●
```

> 💡 Pour colorer plusieurs symboles différemment sur une même ligne, construis une chaîne : `ligne += couleur + "●" + Style.RESET_ALL`, puis affiche-la avec un seul `print()`. `autoreset=True` ne remet la couleur à zéro qu'à la fin du `print()`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.2 - Parcourir un dictionnaire](Solutions%209.2%20-%20Parcourir%20un%20dictionnaire.md).
