# Exercices — Les dictionnaires (fiche 9.1)

> 🎄 **Fil conducteur** : les exercices du cours 9 construisent, morceau par morceau, les outils du spectacle de Noël : la fiche d'une chanson, l'afficheur 16 × 2 du sapin, la table des fréquences pour le son et les couleurs des lumières.

> 📌 **Validation obligatoire** : chaque saisie doit être validée. Réutilise tes fonctions `lire_entier()`, `lire_texte()` et `lire_oui_non()` de ton module `utilitaires.py` (fiche 7.8).

## 🟢 Exercice 1 : Facile

**But** : Prévoir le comportement des opérations de base sur un dictionnaire.

**Énoncé** : Sans exécuter de code, écris exactement ce qu'affiche chaque `print()`. Une des lignes provoque une erreur : laquelle, et quel est son message?

```python
chanson = {"titre": "Vive le vent", "auteur": "J. Pierpont", "annee": 1857, "tempo": 120}

chanson["tempo"] = 140
chanson["favori"] = True

print(len(chanson))
print(chanson["annee"] + 10)
print("auteur" in chanson)
print("Auteur" in chanson)
print(1857 in chanson)
print(chanson.get("duree", 0))
print(chanson.pop("favori"))
print(chanson)
print(chanson["titre"][:4])
print(chanson["duree"])
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=chanson%20%3D%20%7B%22titre%22%3A%20%22Vive%20le%20vent%22%2C%20%22auteur%22%3A%20%22J.%20Pierpont%22%2C%20%22annee%22%3A%201857%2C%20%22tempo%22%3A%20120%7D%0A%0Achanson%5B%22tempo%22%5D%20%3D%20140%0Achanson%5B%22favori%22%5D%20%3D%20True%0A%0Aprint%28len%28chanson%29%29%0Aprint%28chanson%5B%22annee%22%5D%20%2B%2010%29%0Aprint%28%22auteur%22%20in%20chanson%29%0Aprint%28%22Auteur%22%20in%20chanson%29%0Aprint%281857%20in%20chanson%29%0Aprint%28chanson.get%28%22duree%22%2C%200%29%29%0Aprint%28chanson.pop%28%22favori%22%29%29%0Aprint%28chanson%29%0Aprint%28chanson%5B%22titre%22%5D%5B%3A4%5D%29%0Aprint%28chanson%5B%22duree%22%5D%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

## 🟢 Exercice 2 : Facile

**But** : Créer un dictionnaire et le passer à une fonction.

**Énoncé** : Le sapin musical a un petit **afficheur LCD de 16 × 2** : 2 lignes de **16 caractères** maximum. La première ligne montre le titre de la chanson, la deuxième, son auteur.

Écris :

- une fonction `creer_fiche(titre, auteur, annee)` qui **renvoie** un dictionnaire avec les clés `titre`, `auteur` et `annee`;
- une fonction `afficher_lcd(chanson)` qui reçoit ce dictionnaire et simule l'afficheur dans la console. Un texte trop long est **coupé** à 16 caractères; un texte trop court est complété par des espaces.

Le programme demande le titre, l'auteur et l'année (entre 1500 et 2026), crée la fiche, l'affiche avec `print()` pour vérifier son contenu, puis simule l'afficheur.

*Exemple d'exécution :*

```text
Titre : Le petit renne au nez rouge
Auteur : Johnny Marks
Année : 1949
{'titre': 'Le petit renne au nez rouge', 'auteur': 'Johnny Marks', 'annee': 1949}
+----------------+
|Le petit renne a|
|Johnny Marks    |
+----------------+
```

> 💡 Le *slicing* `texte[:16]` garde les 16 premiers caractères; le format `:<16` complète avec des espaces.

## 🟡 Exercice 3 : Moyen

**But** : Utiliser un dictionnaire comme table de correspondance.

**Énoncé** : Pour jouer une note, le haut-parleur a besoin de sa **fréquence** en hertz (Hz). Voici la table de la gamme de *do* :

```python
FREQUENCES = {
    "DO4": 262,
    "RE4": 294,
    "MI4": 330,
    "FA4": 349,
    "SOL4": 392,
    "LA4": 440,
    "SI4": 494,
    "DO5": 523,
}
```

Écris une fonction `frequence_de(note)` qui **renvoie** la fréquence de la note. Elle accepte les minuscules et les espaces autour (`" sol4 "`). Une note absente de la table renvoie `0`, qui représente un **silence**. Utilise `get()`.

Le programme demande des notes jusqu'à ce que l'utilisateur appuie sur Entrée sans rien écrire. Pour chaque note, il affiche sa fréquence, ou un message si la note est inconnue.

*Exemple d'exécution :*

```text
Note (Entrée pour terminer) : la4
LA4 : 440 Hz
Note (Entrée pour terminer) : Sol4
SOL4 : 392 Hz
Note (Entrée pour terminer) : MI9
MI9 : note inconnue (silence)
Note (Entrée pour terminer) :
```

> 💡 Bonus : une note une octave plus haut a exactement **le double** de la fréquence. Ajoute la capacité de reconnaître les notes de l'octave 5 (`RE5`, `MI5`…) à partir de celles de l'octave 4, sans les ajouter à la table.

## 🟡 Exercice 4 : Moyen

**But** : Ajouter, modifier et supprimer des paires dans un dictionnaire.

**Énoncé** : L'état du sapin est gardé dans un dictionnaire :

```python
sapin = {"nb_del": 150, "allume": False, "luminosite": 50, "couleur": "rouge"}
COULEURS = ("rouge", "vert", "bleu", "blanc", "or")
```

Écris un programme avec le menu suivant. L'état du sapin est affiché au début de chaque tour par une fonction `afficher_sapin(sapin)`.

1. Allumer / éteindre (inverse la valeur de `allume`);
2. Changer la luminosité (0 à 100);
3. Changer la couleur (choix numéroté parmi `COULEURS`);
4. Donner un nom au sapin (ajoute ou remplace la clé `nom`);
5. Retirer le nom (supprime la clé `nom`, avec un message si le sapin n'a pas de nom);
0. Quitter.

*Exemple d'exécution :*

```text
Sapin (sans nom) — éteint — 150 DEL — rouge à 50 %
1. Allumer/éteindre  2. Luminosité  3. Couleur  4. Nommer  5. Retirer le nom  0. Quitter
Choix : 4
Nom du sapin : Le Grand Pin

Sapin « Le Grand Pin » — éteint — 150 DEL — rouge à 50 %
1. Allumer/éteindre  2. Luminosité  3. Couleur  4. Nommer  5. Retirer le nom  0. Quitter
Choix : 1

Sapin « Le Grand Pin » — allumé — 150 DEL — rouge à 50 %
...
Choix : 5
Le nom « Le Grand Pin » a été retiré.
...
Choix : 5
Ce sapin n'a pas de nom.
```

> 💡 `afficher_sapin()` doit fonctionner que la clé `nom` existe ou non : pense à `in` ou à `get()`.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Combiner deux dictionnaires et des tuples pour calculer la couleur d'une lumière.

**Énoncé** : Chaque DEL de la bande du sapin reçoit une couleur sous forme d'un tuple `(rouge, vert, bleu)`, chaque composante allant de 0 à 255. Dans le spectacle, chaque note a sa couleur (un arc-en-ciel), quelle que soit son octave :

```python
COULEURS_RGB = {
    "DO": (255, 0, 0),       # rouge
    "RE": (255, 127, 0),     # orange
    "MI": (255, 255, 0),     # jaune
    "FA": (0, 255, 0),       # vert
    "SOL": (0, 0, 255),      # bleu
    "LA": (75, 0, 130),      # indigo
    "SI": (148, 0, 211),     # violet
}
```

Écris :

- `nom_de_note(note)`, qui **renvoie** le nom de la note sans son octave : `"SOL4"` → `"SOL"`, `"DO5"` → `"DO"`;
- `couleur_de(note, intensite)`, qui **renvoie** le tuple de couleur de la note, dont chaque composante est multipliée par `intensite / 100` (division entière). Une note inconnue, ou un silence (`"-"`), donne `(0, 0, 0)` : la DEL est éteinte.

Teste tes fonctions avec ce programme principal :

```python
essais = [("MI4", 100), ("SOL4", 50), ("LA4", 80), ("-", 100), ("DO5", 10), ("ZZ4", 100)]
for note, intensite in essais:
    print(f"{note:<5} à {intensite:>3} % → {couleur_de(note, intensite)}")
```

*Sortie attendue :*

```text
MI4   à 100 % → (255, 255, 0)
SOL4  à  50 % → (0, 0, 127)
LA4   à  80 % → (60, 0, 104)
-     à 100 % → (0, 0, 0)
DO5   à  10 % → (25, 0, 0)
ZZ4   à 100 % → (0, 0, 0)
```

> 💡 L'octave est toujours **le dernier caractère** de la note. Pour construire le tuple résultat : `(r * intensite // 100, v * intensite // 100, b * intensite // 100)`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.1 - Les dictionnaires](Solutions%209.1%20-%20Les%20dictionnaires.md).
