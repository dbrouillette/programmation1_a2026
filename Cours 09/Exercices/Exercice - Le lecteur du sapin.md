# Exercice — Le lecteur du sapin 🎄

**Thèmes couverts :** fonctions et modèle à 2 fichiers (Cours 07), fichiers JSON (Cours 08), dictionnaires, parcours, patron compteur, listes de dictionnaires et paramètres d'application (Cours 09).

> 🎯 **Préparation au TP3** : cet exercice construit le **lecteur** du spectacle de Noël. Dans le TP3, on y ajoutera la création et la modification des chansons, puis on branchera le vrai sapin : bande de DEL, afficheur LCD et haut-parleur sur le Raspberry Pi.

---

## Mise en situation

Le département installe un sapin de Noël lumineux et musical dans l'agora du Cégep. Avant de brancher le matériel, on veut un programme qui **simule** le spectacle sur un ordinateur ordinaire :

- l'**afficheur LCD 16 × 2** du sapin est dessiné dans la console;
- les **lumières** sont des symboles `●` colorés avec `colorama`, une couleur par note;
- le **son** est joué par l'ordinateur, comme le haut-parleur des vieux PC (sous Windows seulement; ailleurs, le programme attend simplement la durée de la note).

Le dossier [Le lecteur du sapin](Le%20lecteur%20du%20sapin/) contient :

| Fichier | Contenu | À modifier? |
| --- | --- | --- |
| `sapin_depart.py` | Le programme : constantes, fonctions à compléter et programme principal **déjà écrit** | ✅ Renomme-le `sapin.py` et complète-le |
| `utilitaires.py` | `lire_entier()`, `lire_texte()`, `lire_oui_non()` et **`jouer_son(frequence, duree_ms)`** | ❌ Non |
| `bibliotheque.json` | 4 chansons, dont une « gamme de test » qui contient un silence et une note invalide | ❌ Non (mais tu peux y ajouter tes chansons) |

Lance `sapin_depart.py` dès le départ : il fonctionne déjà, mais affiche « Aucune chanson à jouer. » puisque `charger_bibliotheque()` renvoie une liste vide. À chaque fonction complétée, le programme en fait un peu plus.

> 💡 Teste `jouer_son()` en lançant directement `utilitaires.py` : sous Windows, tu entendras un accord do-mi-sol-do. Pense au **mode muet** (partie 5) quand vous serez 30 dans le laboratoire!

---

## Les données

Une chanson de `bibliotheque.json` est un dictionnaire qui contient une liste de notes :

```json
{
    "titre": "Au clair de la lune",
    "auteur": "Traditionnel",
    "notes": [
        {"note": "DO4", "intensite": 70, "duree": 400},
        {"note": "MI4", "intensite": 90, "duree": 800}
    ]
}
```

- `note` : le nom de la note (`"DO4"` à `"DO5"`), ou `"-"` pour un silence;
- `intensite` : l'intensité des lumières, de 0 à 100 %;
- `duree` : la durée de la note, en millisecondes.

Les constantes `FREQUENCES` (note → Hz), `GAMME` et `COULEURS_CONSOLE` (nom de note → couleur `colorama`) sont fournies au début de `sapin_depart.py`.

---

## Partie 1 — Charger la bibliothèque

Complète `charger_bibliotheque(chemin)` : elle **renvoie** la liste des chansons du fichier JSON. Si le fichier est absent ou invalide, elle affiche un message d'erreur en rouge et renvoie une liste vide.

✅ *Test* : renomme temporairement `bibliotheque.json`, puis ajoute une virgule de trop dans le fichier. Le programme ne doit jamais planter.

---

## Partie 2 — Le catalogue et l'afficheur

1. `calculer_duree(chanson)` **renvoie** la somme des durées des notes de la chanson.
2. `afficher_catalogue(bibliotheque)` affiche les chansons numérotées, avec leur auteur et leur durée en secondes.
3. `afficher_lcd(ligne1, ligne2)` dessine l'afficheur : 2 lignes de **exactement 16 caractères**, coupées ou complétées par des espaces.

```text
+----------------+
|Au clair de la l|
|Traditionnel    |
+----------------+
```

> ⚠️ Un vrai afficheur LCD 16 × 2 ne connaît que les caractères **ASCII** (voir la fiche 8.1 sur l'encodage) : il n'a pas de lettres accentuées! C'est pourquoi le programme principal affiche « Noel du Cegep! » sans accents. Dans le TP3, il faudra retirer les accents des titres avant de les envoyer à l'afficheur.

---

## Partie 3 — Une note : son et lumière

1. `frequence_de(note)` **renvoie** la fréquence de la note grâce à `FREQUENCES`, ou `0` pour un silence ou une note inconnue. Une seule ligne avec `get()`!
2. `couleur_console(note)` **renvoie** la couleur de la note **sans tenir compte de son octave** (`"DO4"` et `"DO5"` sont rouges), ou `Fore.WHITE` si elle est inconnue.
3. `afficher_note(numero, note)` affiche une ligne par note : son numéro, son nom, sa fréquence et une **barre de lumière** colorée d'un `●` par tranche de 10 % d'intensité. Un silence et une note inconnue ont leur propre message.

```text
  4. FA4   349 Hz  ●●●●●●
  5. —     silence
  6. SOL4  392 Hz  ●●●●●●●●
 10. ZZ4   note inconnue : ignorée
```

---

## Partie 4 — Jouer une chanson

1. `jouer_chanson(chanson, parametres)` :
   - affiche le titre et l'auteur sur l'afficheur LCD;
   - pour chaque note : l'affiche, puis appelle `jouer_son(frequence, duree)`;
   - compte combien de fois chaque note valide a été jouée (**patron compteur**) et **renvoie** ce dictionnaire.
2. `afficher_bilan(chanson, compteur, parametres)` affiche le nombre de notes jouées, la durée, puis un petit histogramme coloré dans l'ordre de `GAMME`.

```text
♪ 11 notes jouées en 6.0 s
  DO4    5 ●●●●●
  RE4    4 ●●●●
  MI4    2 ●●
```

> 💡 La fonction `jouer_son()` ne se termine qu'après la durée de la note : c'est elle qui donne le **rythme** au spectacle. Ton programme n'a rien d'autre à faire pour attendre.

---

## Partie 5 — Les paramètres du lecteur

On veut que le lecteur se souvienne de ses réglages d'une exécution à l'autre, dans `parametres.json`, avec le patron de la fiche 9.4 :

```python
PARAMETRES_DEFAUT = {
    "muet": False,
    "vitesse": 100,             # en %, de 50 à 400
    "derniere_chanson": "",
}
```

1. `charger_parametres()` part des valeurs par défaut et les remplace par celles du fichier, si elles sont du bon type. La vitesse doit être entre 50 et 400.
2. `sauvegarder_parametres(parametres)` écrit le fichier JSON.
3. `modifier_parametres(parametres)` demande le mode muet (o/n) et la vitesse, puis sauvegarde.
4. Retourne dans `jouer_chanson()` et `afficher_bilan()` :
   - en mode muet, la fréquence envoyée à `jouer_son()` est `0`;
   - la durée réelle de chaque note est `duree * 100 // vitesse` : à 200 %, la chanson joue deux fois plus vite.

Le programme principal mémorise déjà le titre de la dernière chanson jouée et l'affiche au démarrage.

---

## Exemple d'exécution complet

```text
+----------------+
|Spectacle de    |
|Noel du Cegep!  |
+----------------+
Dernière chanson jouée : Vive le vent

1. Jouer une chanson  2. Paramètres (muet, 200 %)  0. Quitter
Choix : 1

 1. Vive le vent                  J. Pierpont         9.6 s
 2. Au clair de la lune           Traditionnel        6.0 s
 3. Frère Jacques                 Traditionnel       10.0 s
 4. Gamme de test (avec erreurs)  Votre enseignant    2.2 s

Chanson : 2
+----------------+
|Au clair de la l|
|Traditionnel    |
+----------------+
  1. DO4   262 Hz  ●●●●●●●
  2. DO4   262 Hz  ●●●●●●●
  3. DO4   262 Hz  ●●●●●●●
  4. RE4   294 Hz  ●●●●●●●
  5. MI4   330 Hz  ●●●●●●●●●
  6. RE4   294 Hz  ●●●●●●●●●
  7. DO4   262 Hz  ●●●●●●●
  8. MI4   330 Hz  ●●●●●●●
  9. RE4   294 Hz  ●●●●●●●
 10. RE4   294 Hz  ●●●●●●●
 11. DO4   262 Hz  ●●●●●●●●●●

♪ 11 notes jouées en 3.0 s
  DO4    5 ●●●●●
  RE4    4 ●●●●
  MI4    2 ●●

1. Jouer une chanson  2. Paramètres (muet, 200 %)  0. Quitter
Choix : 0
+----------------+
|Joyeux Noel!    |
|                |
+----------------+
```

---

## Défis supplémentaires

- 🎵 Ajoute ta propre chanson à `bibliotheque.json` (une mélodie du domaine public, comme *Il est né le divin enfant* ou *Mon beau sapin*).
- 🔤 Écris une fonction `retirer_accents(texte)` (inspire-toi de `normaliser()` du TP2) et utilise-la pour que l'afficheur ne reçoive que des caractères ASCII.
- 🌈 Remplace la barre de lumière par un petit **sapin** en triangle, coloré de la couleur de la note.
- 🔀 Ajoute un choix « Lecture aléatoire » qui joue une chanson au hasard (module `random`).

## Solution

➡️ Une solution complète se trouve dans [Le lecteur du sapin/Solution](Le%20lecteur%20du%20sapin/Solution/sapin.py).
