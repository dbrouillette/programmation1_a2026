# Exercices — Écrire dans un fichier texte (fiche 8.4)

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

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.4 - Écrire dans un fichier texte](Solutions%208.4%20-%20%C3%89crire%20dans%20un%20fichier%20texte.md).
