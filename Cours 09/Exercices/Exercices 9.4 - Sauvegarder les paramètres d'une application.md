# Exercices — Sauvegarder les paramètres d'une application (fiche 9.4)

> 📌 **À savoir** : pour tous les exercices, applique le patron de la fiche 9.4 : un dictionnaire `PARAMETRES_DEFAUT`, une fonction `charger_parametres()` et une fonction `sauvegarder_parametres()`. Ton application doit **toujours démarrer**, même si le fichier de paramètres est absent, invalide ou incomplet. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Passer d'un fichier `.ini` à un fichier JSON.

**Énoncé** : Voici le fichier `jeu.ini` d'un vieux jeu vidéo :

```ini
; Configuration de Serpent 486
[joueur]
nom = Abby
couleur = vert

[affichage]
largeur = 640
hauteur = 480
plein_ecran = non

[son]
volume = 7
musique = oui
```

a. Écris le fichier `jeu.json` équivalent. Regroupe tous les paramètres dans un seul objet (sans sections), choisis le **bon type JSON** pour chaque valeur, et utilise des noms de clés sans ambiguïté (ex. : `affichage_largeur` ou simplement `largeur`).

b. Écris le dictionnaire `PARAMETRES_DEFAUT` Python correspondant, avec ces valeurs par défaut : nom vide, couleur verte, 800 × 600, fenêtré, volume 5, musique activée.

c. Pourquoi est-ce important que `PARAMETRES_DEFAUT` contienne `5` et non `"5"` pour le volume?

## 🟡 Exercice 2 : Moyen

**But** : Mémoriser des informations d'une exécution à l'autre.

**Énoncé** : Écris un programme qui garde, dans `statistiques.json`, le **nombre d'exécutions** du programme et la **date et l'heure de la dernière exécution**.

À chaque démarrage, le programme :

1. charge les statistiques (valeurs par défaut : `0` exécution, date vide);
2. affiche « Première utilisation! » si la date est vide, sinon le nombre d'exécutions précédentes et la date de la dernière;
3. ajoute 1 au compteur, remplace la date par la date actuelle et sauvegarde.

*Première exécution :*

```text
Première utilisation! Bienvenue.
```

*Exécutions suivantes :*

```text
Tu as utilisé ce programme 3 fois.
Dernière utilisation : 2026-11-08 à 14:32
```

Teste ensuite ton programme en remplaçant le contenu du fichier par `{"nb_executions": "beaucoup"}`. Que doit-il se passer?

## 🟡 Exercice 3 : Moyen

**But** : Ajouter un nouveau paramètre sans briser les anciens fichiers.

**Énoncé** : Pars de l'exemple [parametres_app.py](../Exemples/Paramètres%20JSON/parametres_app.py). Exécute-le une fois pour créer `parametres.json`.

Ajoute ensuite un paramètre `langue` (valeurs possibles : `"fr"` ou `"en"`, par défaut `"fr"`) :

- un nouveau choix dans le menu permet de changer de langue;
- les messages « Bonjour … ! » et « À bientôt, … ! » s'affichent dans la langue choisie (« Hello … ! » et « See you soon, … ! »).

Relance le programme **sans supprimer** l'ancien `parametres.json`, qui ne contient pas la clé `langue`. Explique pourquoi le programme démarre quand même, et ce qui arrive au fichier à la première sauvegarde.

> 💡 N'oublie pas de valider la langue lue dans le fichier, comme c'est déjà fait pour le thème.

## 🔴 Exercice 4 : Moyen-Difficile

**But** : Gérer une liste dans les paramètres : les fichiers récents.

**Énoncé** : Beaucoup d'applications affichent la liste des **fichiers récemment ouverts**. Écris un programme qui simule cette fonctionnalité. Les paramètres, dans `parametres.json`, contiennent la clé `fichiers_recents` (liste vide par défaut) et la clé `nb_recents_max` (entier, 5 par défaut).

Le programme affiche la liste des fichiers récents, puis demande le nom d'un fichier à « ouvrir » (Entrée pour quitter). Chaque fichier ouvert :

- est placé **en tête** de la liste;
- s'il était déjà dans la liste, il est **déplacé** en tête (pas de doublon);
- si la liste dépasse `nb_recents_max`, le plus ancien est retiré.

La liste est sauvegardée après chaque ouverture.

*Exemple d'exécution :*

```text
Fichiers récents :
  1. notes.csv
  2. menu.json
  3. rapport.txt

Fichier à ouvrir (Entrée pour quitter) : menu.json
Ouverture de menu.json...

Fichiers récents :
  1. menu.json
  2. notes.csv
  3. rapport.txt

Fichier à ouvrir (Entrée pour quitter) :
```

Ajoute une validation : chaque élément de `fichiers_recents` lu dans le fichier doit être une chaîne non vide; les autres sont ignorés. Et si `nb_recents_max` n'est pas entre 1 et 20, on prend la valeur par défaut.

> 💡 `liste.remove(valeur)` retire la première occurrence d'une valeur; `liste.insert(0, valeur)` insère en tête; `liste.pop()` retire le dernier élément.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 9.4 - Sauvegarder les paramètres d'une application](Solutions%209.4%20-%20Sauvegarder%20les%20paramètres%20d'une%20application.md).
