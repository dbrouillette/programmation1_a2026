# Exercices — Les fichiers CSV à la main (fiche 8.3)

> 📌 **Règle de la série** : **aucun** `import csv`. Tout se fait avec `strip()`, `split()`, `join()` et des f-strings. Crée chaque fichier CSV dans VS Code, dans le dossier de ton programme. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Prévoir le résultat de `split()` et `join()`.

**Énoncé** : Sans exécuter de code, écris le résultat de chaque expression. Indique ensuite lesquelles posent un problème pour lire un fichier CSV, et pourquoi.

```python
ligne1 = "Tremblay,Marie,87\n"
ligne2 = "Gagnon,Luc,\n"
ligne3 = "Roy,Anne-Sophie,91,bonus\n"
ligne4 = '"Côté, Jr",Paul,75\n'

a = ligne1.split(",")
b = ligne1.strip().split(",")
c = ligne2.strip().split(",")
d = ligne3.strip().split(",")
e = ligne4.strip().split(",")
f = ";".join(["Tremblay", "Marie", "87"])
g = ",".join(b)
h = len(ligne1.strip().split(";"))
```

## 🟢 Exercice 2 : Facile

**But** : Lire un fichier CSV et afficher un tableau formaté.

**Énoncé** : Crée le fichier `etudiants.csv` :

```text
nom,prenom,note
Tremblay,Marie,87
Gagnon,Luc,62
Roy,Anne-Sophie,91
Bouchard,Émile,48
Côté,Léa,75
```

Écris un programme qui affiche les étudiants sous forme de tableau, avec la mention « Échec » à côté des notes sous 60, puis la moyenne du groupe.

*Sortie attendue :*

```text
Nom          Prénom         Note
--------------------------------
Tremblay     Marie            87
Gagnon       Luc              62
Roy          Anne-Sophie      91
Bouchard     Émile            48  Échec
Côté         Léa              75
--------------------------------
Moyenne du groupe : 72.6
```

## 🟡 Exercice 3 : Moyen

**But** : Charger un CSV dans une liste 2D et y faire des calculs.

**Énoncé** : Le fichier `ventes.csv` contient les ventes d'une journée au Café Le Binaire :

```text
heure,produit,quantite,prix_unitaire
08:05,Café filtre,2,2.25
08:12,Latté,1,4.50
08:30,Muffin,3,3.25
09:15,Café filtre,1,2.25
10:02,Chocolat chaud,2,3.75
11:45,Latté,2,4.50
12:10,Muffin,1,3.25
```

Écris :

- `charger_ventes(chemin)`, qui **renvoie** une liste 2D `[[heure, produit, quantite, prix_unitaire], ...]` avec les bons types (`int` pour la quantité, `float` pour le prix);
- `calculer_total(ventes)`, qui **renvoie** le montant total des ventes;
- `trouver_plus_grosse_vente(ventes)`, qui **renvoie** la rangée de la vente au montant le plus élevé;
- `compter_produit(ventes, produit)`, qui **renvoie** la quantité totale vendue d'un produit.

Le programme affiche le total, la plus grosse vente, puis demande un nom de produit et affiche la quantité vendue (0 si le produit n'a pas été vendu).

*Exemple d'exécution :*

```text
Total des ventes : 40.75 $
Plus grosse vente : 3 x Muffin à 08:30 (9.75 $)
Produit à rechercher : latté
Latté : 3 vendu(s)
```

> 💡 La recherche ne tient pas compte des majuscules. Affiche le nom du produit tel qu'il est écrit dans le fichier.

## 🟡 Exercice 4 : Moyen

**But** : Écrire un fichier CSV à partir de saisies.

**Énoncé** : Écris un programme qui permet de saisir des étudiants (nom, prénom, note entre 0 et 100) jusqu'à ce que l'utilisateur laisse le nom vide. Les étudiants sont gardés dans une liste 2D, puis écrits dans `bulletin.csv` **avec un en-tête**. Le fichier produit doit pouvoir être relu par ta solution de l'exercice 2.

Comme notre CSV est fait à la main, **refuse** toute saisie qui contient une virgule.

*Exemple d'exécution :*

```text
Nom (Entrée pour terminer) : Tremblay
Prénom : Marie
Note : 87
Nom (Entrée pour terminer) : Côté, Jr
Erreur : la virgule est interdite.
Nom (Entrée pour terminer) : Côté
Prénom : Léa
Note : 75
Nom (Entrée pour terminer) :

2 étudiant(s) écrit(s) dans bulletin.csv.
```

*`bulletin.csv` produit :*

```text
nom,prenom,note
Tremblay,Marie,87
Côté,Léa,75
```

> 💡 Écris l'en-tête et chaque rangée avec `",".join(...)`. N'oublie pas que `join()` n'accepte que des chaînes.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Convertir un CSV « à la française » produit par Excel en CSV standard.

**Énoncé** : Excel en français a exporté le fichier `depenses_excel.csv` : il utilise le **point-virgule** comme délimiteur et la **virgule** comme séparateur décimal.

```text
date;categorie;description;montant
2026-11-01;épicerie;IGA, commande de la semaine;143,27
2026-11-03;transport;Essence;62,10
2026-11-05;loisirs;Cinéma;14,50
2026-11-08;épicerie;Marché;38,95
```

Écris un programme qui :

1. lit ce fichier et convertit les montants en `float`;
2. écrit le fichier `depenses.csv` au format standard : délimiteur virgule, point décimal, 2 décimales;
3. affiche le total des dépenses et le total de la catégorie `épicerie`.

*Sortie attendue :*

```text
4 dépenses converties dans depenses.csv.
Total : 258.82 $
Épicerie : 182.22 $
```

Attention : la description `IGA, commande de la semaine` contient une virgule. Dans le fichier standard, elle briserait les colonnes. Remplace chaque virgule d'une description par un espace avant l'écriture.

> 💡 Ouvre le fichier source avec `encoding="utf-8-sig"` : si le fichier vient vraiment d'Excel, il peut commencer par une signature invisible. Avec un fichier créé dans VS Code, `"utf-8-sig"` fonctionne aussi.

> 🤔 **Réflexion** : remplacer une virgule par un espace modifie les données. Quelle meilleure solution verras-tu en 8.4?

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.3 - Les fichiers CSV à la main](Solutions%208.3%20-%20Les%20fichiers%20CSV%20à%20la%20main.md).
