# Exercices — Sauvegarder et recharger une liste (fiche 8.5)

> 📌 **À savoir** : fais ces exercices dans VS Code. Après chaque exécution, **ouvre le fichier produit** dans VS Code pour vérifier son contenu. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Construire un chemin fiable avec `Path(__file__).parent`.

**Énoncé** : Écris un programme qui :

1. construit le chemin de `notes.txt`, placé **à côté du programme**;
2. affiche le nom du dossier du programme (`DOSSIER.name`), le nom du fichier cherché et s'il existe (`CHEMIN_NOTES.exists()` renvoie `True` ou `False`);
3. ajoute la ligne `Une ligne de plus` à la fin de `notes.txt`;
4. relit le fichier et affiche son nombre de lignes.

Lance ensuite ton programme **depuis un autre dossier** (dans le terminal de VS Code : `cd ..`, puis `python dossier/programme.py`). Le fichier modifié est-il toujours le même?

*Exemple de sortie (le dossier du programme s'appelle ici `nouveaux`) :*

```text
Dossier du programme : nouveaux
Fichier cherché      : notes.txt
Le fichier existe?   True
notes.txt contient maintenant 2 ligne(s).
```

## 🟡 Exercice 2 : Moyen

**But** : Sauvegarder une liste et la recharger au démarrage suivant.

**Énoncé** : Écris un programme de **liste d'épicerie** qui se souvient de son contenu d'une exécution à l'autre. Il utilise le duo de fonctions vu en 8.5 :

- `charger_epicerie(chemin)` **renvoie** la liste des articles du fichier (liste vide si le fichier n'existe pas);
- `sauvegarder_epicerie(chemin, articles)` écrit un article par ligne.

Le menu offre trois choix : ajouter un article, retirer un article (par son numéro) et quitter. La liste est affichée au début de chaque tour, et **sauvegardée après chaque modification**.

*Exemple d'exécution :*

```text
Liste d'épicerie :
  1. lait
  2. pain

1. Ajouter  2. Retirer  0. Quitter
Choix : 1
Article : fromage

Liste d'épicerie :
  1. lait
  2. pain
  3. fromage

1. Ajouter  2. Retirer  0. Quitter
Choix : 2
Numéro de l'article à retirer : 1

Liste d'épicerie :
  1. pain
  2. fromage

1. Ajouter  2. Retirer  0. Quitter
Choix : 0
```

> 💡 Pour retirer un élément selon sa position : `articles.pop(index)`. Si la liste est vide, afficher « (vide) » et refuser le retrait.

## 🔴 Exercice 3 : Moyen-Difficile

**But** : Maintenir un fichier de meilleurs scores.

**Énoncé** : Le fichier `meilleurs_scores.txt` contient les 5 meilleurs scores d'un jeu, un entier par ligne, du plus grand au plus petit. Il peut contenir moins de 5 scores, ou ne pas exister du tout.

Écris un programme qui :

1. charge les scores (liste vide si le fichier n'existe pas);
2. demande le score de la partie qui vient de se terminer (entier entre 0 et 99 999);
3. si ce score fait partie des 5 meilleurs, l'insère **à la bonne position** et l'annonce (« Nouveau record! » s'il est premier, sinon « Tu entres au palmarès en position N! »);
4. ne garde que les 5 meilleurs scores et sauvegarde le fichier;
5. affiche le palmarès.

*Exemple d'exécution (fichier contenant 900, 750, 600, 400, 200) :*

```text
Ton score : 680
Tu entres au palmarès en position 3!

--- Palmarès ---
1.   900
2.   750
3.   680
4.   600
5.   400
```

> 💡 Interdiction d'utiliser `sort()` : trouve toi-même la position où insérer le nouveau score avec une boucle, puis utilise `scores.insert(position, score)`. Pour ne garder que les 5 premiers : `scores = scores[:5]`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.5 - Sauvegarder et recharger une liste](Solutions%208.5%20-%20Sauvegarder%20et%20recharger%20une%20liste.md).
