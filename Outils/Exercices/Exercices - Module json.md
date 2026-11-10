# Exercices — Le format JSON (fiche « Module json »)

> 📌 **À savoir** : utilise le module `json` et ouvre toujours les fichiers avec `encoding="utf-8"`. Écris tes fichiers avec `indent=4` et `ensure_ascii=False` pour qu'ils restent lisibles. Dans cette série, on n'utilise **que des listes** : les objets JSON `{ }` (dictionnaires) seront vus au cours 9. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Lire la syntaxe JSON et naviguer dans les données chargées.

**Énoncé** :

a. Le fichier `chanson.json` suivant contient **4 erreurs** de syntaxe JSON. Trouve-les et corrige-les.

```text
[
    "Vive le vent",
    'Traditionnel',
    120,
    True,
    [
        ["MI", 0.5],
        ["MI", 0.5],
        ["MI", 1.0],
    ],
    None
]
```

b. Une fois le fichier corrigé, on le charge avec `chanson = json.load(fichier)`. Donne la valeur **et le type Python** de chaque expression :

```python
chanson[0]
chanson[2] + 10
chanson[3]
len(chanson)
chanson[4]
len(chanson[4])
chanson[4][2]
chanson[4][2][1]
chanson[5]
```

## 🟢 Exercice 2 : Facile

**But** : Sauvegarder une liste en JSON, puis la relire.

**Énoncé** : Écris un programme qui demande à l'utilisateur ses **films préférés**, un à la fois, jusqu'à ce qu'il appuie sur Entrée sans rien écrire. La liste est sauvegardée dans `films.json`, puis relue dans une **nouvelle** variable et affichée, numérotée.

*Exemple d'exécution :*

```text
Film (Entrée pour terminer) : Retour vers le futur
Film (Entrée pour terminer) : Le Seigneur des anneaux
Film (Entrée pour terminer) : Là-haut
Film (Entrée pour terminer) :
3 film(s) sauvegardé(s) dans films.json.

1. Retour vers le futur
2. Le Seigneur des anneaux
3. Là-haut
```

*`films.json` produit :*

```json
[
    "Retour vers le futur",
    "Le Seigneur des anneaux",
    "Là-haut"
]
```

Ouvre ensuite le fichier dans VS Code, puis relance le programme en retirant `ensure_ascii=False`. Que remarques-tu dans le fichier?

## 🟡 Exercice 3 : Moyen

**But** : Convertir un fichier CSV en fichier JSON et constater que les types sont conservés.

**Énoncé** : Écris un programme qui lit le fichier `menu.csv` de la fiche « Module csv » avec le module `csv`, convertit le prix en `float` et le stock en `int`, puis sauvegarde la liste 2D obtenue (sans l'en-tête) dans `menu.json`.

Le programme recharge ensuite `menu.json` et affiche le produit le plus cher et la valeur totale du stock, **sans aucune conversion** `float()` ou `int()` dans cette deuxième partie.

*Sortie attendue :*

```text
6 produits convertis dans menu.json.
Produit le plus cher : Latté (4.50 $)
Valeur du stock : 384.25 $
```

## 🟡 Exercice 4 : Moyen

**But** : Gérer une liste 2D persistante en JSON.

**Énoncé** : Écris un **carnet de contacts** sauvegardé dans `contacts.json`. Chaque contact est une liste `[nom, courriel, telephone]`; le fichier contient la liste 2D des contacts.

Écris les fonctions `charger_contacts(chemin)` (liste vide si le fichier est absent **ou** invalide) et `sauvegarder_contacts(chemin, contacts)`. Le menu permet :

1. d'afficher les contacts;
2. d'ajouter un contact (le courriel doit contenir un `@`);
3. de rechercher un contact par une partie de son nom, sans tenir compte des majuscules;
4. de supprimer un contact par son numéro.

Le carnet est sauvegardé après chaque modification.

*Exemple de recherche :*

```text
Rechercher : trem
Marie Tremblay | marie.tremblay@exemple.ca | 819-555-0142
Luc Tremblay   | luc@exemple.ca            | 819-555-0199
```

> 💡 Définis des constantes `COL_NOM`, `COL_COURRIEL` et `COL_TELEPHONE` pour les index, comme en 8.6.

> 🤔 **Réflexion** : comparé au CSV, qu'est-ce que JSON simplifie dans cet exercice? Le téléphone devrait-il être sauvegardé comme un nombre ou comme une chaîne?

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Piloter un programme à partir de données JSON.

**Énoncé** : Écris un **quiz** dont les questions sont lues dans `quiz.json`. Chaque question est une liste `[question, choix, index_bonne_reponse]`, où `choix` est elle-même une liste :

```json
[
    [
        "Quel mode d'ouverture efface le contenu du fichier?",
        ["r", "w", "a"],
        1
    ],
    [
        "Quelle méthode enlève le \\n à la fin d'une ligne?",
        ["split()", "join()", "strip()", "read()"],
        2
    ],
    [
        "En JSON, comment écrit-on la valeur vide?",
        ["None", "null", "nil"],
        1
    ]
]
```

Le nombre de questions et le nombre de choix par question peuvent varier : ton programme ne doit rien supposer.

Le programme :

1. pose chaque question avec ses choix numérotés à partir de 1;
2. valide la réponse (entre 1 et le nombre de choix de **cette** question);
3. affiche « Bonne réponse! » ou la bonne réponse;
4. affiche le score final;
5. tient à jour le **meilleur score** dans un second fichier, `record.json`, qui contient une liste `[meilleur_score, pseudo]` (ex. : `[2, "Abby"]`). Si le record est battu, il demande le pseudo du joueur et met le fichier à jour.

*Exemple d'exécution :*

```text
1. Quel mode d'ouverture efface le contenu du fichier?
   1) r
   2) w
   3) a
Ta réponse : 2
Bonne réponse!

...

Score : 2 / 3
Record actuel : 1 (Zoé)
🏆 Nouveau record! Ton pseudo : Abby
```

> 💡 Ajoute une 4e question dans `quiz.json`, sans toucher au code Python, pour vérifier que ton programme s'adapte.

## Solutions

➡️ Les solutions se trouvent dans [Solutions - Module json](Solutions%20-%20Module%20json.md).
