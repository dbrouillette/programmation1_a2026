# Exercices — Listes de dictionnaires et données imbriquées (fiche 9.3)

> 🎄 **Fil conducteur** : cette série met en place le circuit complet des chansons du spectacle, **entièrement en JSON** : un fichier `notes.json` écrit à la main → une chanson (dictionnaire) → une **bibliothèque** de chansons → l'exportation vers une clé USB que le Raspberry Pi du sapin pourra lire.

> 📌 **Fichiers fournis** dans le dossier [Fichiers 9.3](Fichiers%209.3/) : `notes.json` (*Au clair de la lune*) et `bibliotheque.json` (2 chansons). Copie-les dans le dossier de tes programmes, avec ton module `utilitaires.py`. Chaque saisie doit être validée.

Dans toute la série, une **note** est un dictionnaire et une **chanson** est un dictionnaire qui contient une liste de notes :

```python
note = {"note": "MI4", "intensite": 80, "duree": 300}

chanson = {
    "titre": "Vive le vent",
    "auteur": "J. Pierpont",
    "notes": [note, ...],
}
```

## 🟢 Exercice 1 : Facile

**But** : Naviguer dans une structure imbriquée.

**Énoncé** : Sans exécuter de code, donne la valeur **et le type** de chaque expression. Deux d'entre elles provoquent une erreur : lesquelles, et laquelle?

```python
bibliotheque = [
    {
        "titre": "Vive le vent",
        "auteur": "J. Pierpont",
        "notes": [
            {"note": "MI4", "intensite": 80, "duree": 300},
            {"note": "SOL4", "intensite": 100, "duree": 600},
        ],
    },
    {
        "titre": "Au clair de la lune",
        "auteur": "Traditionnel",
        "notes": [],
    },
]
```

```python
len(bibliotheque)
bibliotheque[1]
bibliotheque[0]["auteur"]
bibliotheque[0]["notes"][1]
bibliotheque[0]["notes"][1]["duree"] * 2
len(bibliotheque[1]["notes"])
bibliotheque[0]["titre"][0]
bibliotheque["titre"]
bibliotheque[1]["notes"][0]
"notes" in bibliotheque[1]
```


## 🟢 Exercice 2 : Facile

**But** : Passer d'une liste 2D à une liste de dictionnaires.

**Énoncé** : Voici le début de *Vive le vent* sous forme de liste 2D, comme dans la série 9.2 :

```python
CHANSON_2D = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
]
```

Écris :

- `convertir_en_dictionnaires(chanson_2d)`, qui **renvoie** la liste de dictionnaires équivalente;
- `calculer_duree_totale(chanson)`, qui **renvoie** la somme des durées;
- `filtrer_par_intensite(chanson, intensite_min)`, qui **renvoie** la liste des notes dont l'intensité est au moins `intensite_min`.

*Sortie attendue :*

```text
{'note': 'MI4', 'intensite': 80, 'duree': 300}
11 notes, 4800 ms
Notes à 90 % ou plus (4) :
  MI4   100 %   600 ms
  MI4   100 %   600 ms
  DO4    90 %   450 ms
  MI4   100 %  1200 ms
```

> 💡 Compare `calculer_duree_totale()` avec la même fonction écrite pour une liste 2D : laquelle se lit le mieux?

## 🟡 Exercice 3 : Moyen

**But** : Lire un fichier JSON écrit à la main, le valider et sauvegarder une chanson en JSON.

**Énoncé** : Le fichier `notes.json` fourni contient les notes d'une chanson, une par ligne :

```json
[
    {"note": "DO4", "intensite": 70, "duree": 400},
    {"note": "DO4", "intensite": 70, "duree": 400},
    {"note": "DO4", "intensite": 70, "duree": 400},
    {"note": "RE4", "intensite": 70, "duree": 400},
    {"note": "MI4", "intensite": 90, "duree": 800},
    ...
]
```

Écris `lire_notes_json(chemin)`, qui lit le fichier avec `json.load()` et **renvoie** la liste des notes valides, avec le nom de la note en majuscules. Si le fichier est introuvable, contient une erreur de syntaxe JSON ou ne contient pas une liste, la fonction affiche un message et renvoie une liste vide. Sinon, une note est ignorée, avec un avertissement qui donne son **numéro** (à partir de 1), si :

- ce n'est pas un dictionnaire, ou une des clés `note`, `intensite` ou `duree` manque;
- la note n'est pas une chaîne qui se trouve dans `FREQUENCES`, ni un silence `"-"`;
- l'intensité ou la durée n'est pas un **entier** (`"70"` entre guillemets est une chaîne!);
- l'intensité n'est pas entre 0 et 100, ou la durée n'est pas entre 50 et 2000 ms.

Le programme lit le fichier, demande le titre et l'auteur, construit le dictionnaire de la chanson, le sauvegarde dans `chanson.json`, puis affiche sa durée et l'afficheur LCD de la série 9.1.

*Exemple d'exécution :*

```text
11 notes lues dans notes.json.
Titre : Au clair de la lune
Auteur : Traditionnel
Chanson sauvegardée dans chanson.json (6.0 s).
+----------------+
|Au clair de la l|
|Traditionnel    |
+----------------+
```

Ajoute ensuite ces notes à la fin de la liste dans `notes.json` pour tester ta validation (n'oublie pas la virgule après la note précédente!) :

```json
    {"note": "D04", "intensite": 70, "duree": 400},
    {"note": "MI4", "intensite": "70", "duree": 400},
    {"note": "SOL4", "intensite": 70},
    {"note": "LA4", "intensite": 120, "duree": 400}
```

```text
Note 12 ignorée : note « D04 » inconnue.
Note 13 ignorée : intensité ou durée non entière.
Note 14 ignorée : clé manquante.
Note 15 ignorée : intensité ou durée hors limites.
11 notes lues dans notes.json.
```

Enfin, ajoute une virgule après la toute dernière note et relance le programme :

```text
Erreur : notes.json contient une erreur de syntaxe JSON.
0 notes lues dans notes.json.
```

> 💡 `type(valeur) == int` vérifie qu'une valeur est un entier. Vérifie d'abord que les trois clés existent : sinon, `element["duree"]` lèverait une `KeyError`.

## 🟡 Exercice 4 : Moyen

**But** : Gérer une liste de dictionnaires persistante en JSON.

**Énoncé** : Le fichier `bibliotheque.json` fourni contient une **liste de chansons**. Écris un programme de gestion de la bibliothèque, avec ce menu :

1. **Catalogue** : affiche chaque chanson, numérotée, avec son titre, son auteur, son nombre de notes et sa durée en secondes;
2. **Importer notes.json** : lit `notes.json` avec ta fonction de l'exercice 3, demande le titre et l'auteur, puis ajoute la chanson. Un titre qui existe déjà (sans tenir compte des majuscules) est refusé;
3. **Supprimer** : supprime une chanson choisie par son numéro, après confirmation;
0. Quitter.

La bibliothèque est sauvegardée après chaque modification. Si `bibliotheque.json` est absent ou invalide, le programme démarre avec une bibliothèque vide.

*Exemple d'exécution :*

```text
1. Catalogue  2. Importer notes.json  3. Supprimer  0. Quitter
Choix : 1

 1. Vive le vent          J. Pierpont       26 notes   9.6 s
 2. Frère Jacques         Traditionnel      26 notes  10.0 s

1. Catalogue  2. Importer notes.json  3. Supprimer  0. Quitter
Choix : 2
Titre : vive le vent
Une chanson s'appelle déjà « vive le vent ». Importation annulée.
1. Catalogue  2. Importer notes.json  3. Supprimer  0. Quitter
Choix : 2
Titre : Au clair de la lune
Auteur : Traditionnel
« Au clair de la lune » ajoutée (11 notes).
```

> 💡 Écris une fonction `chercher_titre(bibliotheque, titre)` qui **renvoie** l'index de la chanson, ou `-1` si elle n'existe pas.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Exporter une chanson dans son propre fichier JSON et vérifier le résultat.

**Énoncé** : Le Raspberry Pi du sapin joue la chanson qui se trouve sur une **clé USB**. Écris un programme qui « prépare la clé » :

1. affiche la liste des chansons de `bibliotheque.json` et en fait choisir une;
2. crée le dossier `cle_usb` (s'il n'existe pas) à côté du programme;
3. y écrit `chanson.json` avec `json.dump()` : **un seul** dictionnaire, avec le titre, l'auteur et les notes de la chanson;
4. **relit** `chanson.json` avec `json.load()` et vérifie que la chanson relue est **identique** à celle de la bibliothèque.

*Exemple d'exécution :*

```text
1. Vive le vent
2. Frère Jacques
Chanson à exporter : 2
« Frère Jacques » exportée dans cle_usb/chanson.json.
✅ Vérification réussie : 26 notes identiques.
```

> 💡 Deux dictionnaires se comparent directement avec `==` : ils sont égaux s'ils ont les mêmes clés et les mêmes valeurs, y compris les listes qu'ils contiennent. Avec JSON, aucune conversion n'est nécessaire avant de comparer. Pour créer un dossier : `dossier.mkdir(exist_ok=True)` (voir fiche 9.4).

## Pour aller plus loin

➡️ L'exercice synthèse [Exercice - Le lecteur du sapin](Exercice%20-%20Le%20lecteur%20du%20sapin.md) réunit toute la matière du cours 9 : il joue les chansons de la bibliothèque en simulant le son et les lumières du sapin.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.3 - Listes de dictionnaires et données imbriquées](Solutions%209.3%20-%20Listes%20de%20dictionnaires%20et%20données%20imbriquées.md).
