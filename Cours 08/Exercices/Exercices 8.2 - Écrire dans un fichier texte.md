# Exercices — Écrire dans un fichier texte (fiche 8.2)

> 📌 **À savoir** : fais ces exercices dans VS Code. Après chaque exécution, **ouvre le fichier produit** dans VS Code pour vérifier son contenu. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Écrire plusieurs lignes dans un fichier avec le mode `"w"`.

**Énoncé** : Écris un programme qui demande un nombre entier entre 1 et 12, puis écrit sa table de multiplication (de 1 à 10) dans un fichier nommé `table_N.txt`, où `N` est le nombre choisi. Le programme affiche ensuite un message de confirmation.

*Exemple d'exécution :*

```text
Quelle table (1 à 12)? 7
Table de 7 écrite dans table_7.txt.
```

*Contenu de `table_7.txt` :*

```text
Table de 7
 1 x 7 =  7
 2 x 7 = 14
 3 x 7 = 21
...
10 x 7 = 70
```

> 💡 Le nom du fichier peut lui-même être construit avec une f-string : `f"table_{nombre}.txt"`.

## 🟢 Exercice 2 : Facile

**But** : Ajouter à la fin d'un fichier avec le mode `"a"`.

**Énoncé** : Écris un programme de **journal de bord**. À chaque exécution, il demande un message (non vide) et l'ajoute à la fin du fichier `journal.txt`, précédé de la date et de l'heure (voir [Date et heure - Module datetime](../../Outils/Date%20et%20heure%20-%20Module%20datetime.md)). Il affiche ensuite **tout** le contenu du journal.

*Exemple d'exécution (3e exécution) :*

```text
Message : Labo 8 terminé!

--- Journal ---
2026-11-08 09:12 | Début du cours 8
2026-11-08 10:47 | J'ai compris le mode "a"
2026-11-08 11:30 | Labo 8 terminé!
```

> 💡 `datetime.now().strftime("%Y-%m-%d %H:%M")` donne la date et l'heure dans ce format.

## 🟡 Exercice 3 : Moyen

**But** : Sauvegarder une liste et la recharger au démarrage suivant.

**Énoncé** : Écris un programme de **liste d'épicerie** qui se souvient de son contenu d'une exécution à l'autre. Il utilise le duo de fonctions vu en 8.2 :

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

## 🟡 Exercice 4 : Moyen

**But** : Lire un fichier, le transformer et écrire le résultat dans un autre fichier.

**Énoncé** : Crée le fichier `poeme.txt` avec quelques lignes de texte (incluant des lignes vides). Écris un programme qui produit le fichier `poeme_numerote.txt`, dans lequel :

- chaque ligne non vide est précédée de son numéro sur 3 positions et d'une barre verticale;
- les lignes vides sont conservées, mais non numérotées;
- une dernière ligne indique le nombre de lignes non vides et le nombre total de mots.

*Exemple : `poeme.txt`*

```text
Le Python est un serpent
Mais aussi un langage

Qui fait danser les données
Sur l'écran du cégep
```

*`poeme_numerote.txt` produit :*

```text
  1 | Le Python est un serpent
  2 | Mais aussi un langage

  3 | Qui fait danser les données
  4 | Sur l'écran du cégep
--- 4 lignes, 18 mots ---
```

> 💡 On peut ouvrir **deux fichiers** dans le même `with` : `with open(a, "r", encoding="utf-8") as source, open(b, "w", encoding="utf-8") as destination:`. Pour compter les mots d'une ligne : `len(ligne.split())`.

## 🔴 Exercice 5 : Moyen-Difficile

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

➡️ Les solutions se trouvent dans [Solutions 8.2 - Écrire dans un fichier texte](Solutions%208.2%20-%20Écrire%20dans%20un%20fichier%20texte.md).
