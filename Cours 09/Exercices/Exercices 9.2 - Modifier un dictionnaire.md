# Exercices — Modifier un dictionnaire (fiche 9.2)

> 🎄 **Fil conducteur** : les exercices du cours 9 construisent, morceau par morceau, les outils du spectacle de Noël : la fiche d'une chanson, l'afficheur 16 × 2 du sapin, la table des fréquences pour le son et les couleurs des lumières.

> 📌 **Validation obligatoire** : chaque saisie doit être validée. Réutilise tes fonctions `lire_entier()`, `lire_texte()` et `lire_oui_non()` de ton module `utilitaires.py` (fiche 7.8).

## 🟡 Exercice 1 : Moyen

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

## 🔴 Exercice 2 : Moyen-Difficile

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

➡️ Les solutions se trouvent dans [Solutions 9.2 - Modifier un dictionnaire](Solutions%209.2%20-%20Modifier%20un%20dictionnaire.md).
