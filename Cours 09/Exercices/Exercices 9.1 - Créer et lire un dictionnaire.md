# Exercices — Créer et lire un dictionnaire (fiche 9.1)

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

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.1 - Créer et lire un dictionnaire](Solutions%209.1%20-%20Cr%C3%A9er%20et%20lire%20un%20dictionnaire.md).
