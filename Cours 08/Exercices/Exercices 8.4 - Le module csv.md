# Exercices — Le module csv (fiche 8.4)

> 📌 **Règle de la série** : utilise le module `csv` (`csv.reader` et `csv.writer`). Plus aucun `split(",")` ni `join()` pour le CSV! Ouvre toujours les fichiers avec `encoding="utf-8"` **et** `newline=""`. Chaque saisie au clavier doit être validée.

## 🟢 Exercice 1 : Facile

**But** : Remplacer le découpage à la main par `csv.reader`.

**Énoncé** : Reprends ta solution de l'exercice 2 de la [série 8.3](Exercices%208.3%20-%20Les%20fichiers%20CSV%20à%20la%20main.md) (le tableau des étudiants) et convertis-la pour qu'elle utilise `csv.reader`.

Ajoute ensuite cette ligne à la fin du fichier `etudiants.csv` et vérifie que ton programme l'affiche correctement :

```text
"Côté, Jr",Paul,79
```

Avec l'ancienne version (`split`), que se passait-il avec cette ligne?

## 🟢 Exercice 2 : Facile

**But** : Écrire un fichier CSV avec `csv.writer`.

**Énoncé** : Le programme suivant contient la liste des cours d'une session et le local de chacun. Complète-le pour qu'il écrive le fichier `horaire.csv`, avec l'en-tête `code,titre,local`, en utilisant `writerow()` pour l'en-tête et `writerows()` pour le reste.

```python
COURS = [
    ["420-116-RI", "Programmation 1, Python", "B-1234"],
    ["109-101-MQ", "Activité physique et santé", "Gymnase"],
    ["340-101-MQ", "Philosophie et rationalité", "A-2050"],
    ["601-101-MQ", "Écriture et littérature", "A-1120"],
]
```

Ouvre ensuite `horaire.csv` dans VS Code. Que remarques-tu à la ligne du cours de programmation? Pourquoi?

## 🟡 Exercice 3 : Moyen

**But** : Lire un CSV, filtrer ses rangées et écrire le résultat dans un autre CSV.

**Énoncé** : À partir du fichier `menu.csv` de la fiche 8.4 (avec la ligne `"Muffin, bleuets"`), écris un programme qui :

1. affiche les catégories présentes dans le fichier (sans doublons);
2. demande une catégorie (validée : elle doit faire partie de la liste);
3. écrit dans le fichier `menu_CATEGORIE.csv` (ex. : `menu_patisserie.csv`) l'en-tête et seulement les produits de cette catégorie;
4. affiche le nombre de produits écrits.

*Exemple d'exécution :*

```text
Catégories : boisson, patisserie
Catégorie à extraire : patisserie
3 produit(s) écrit(s) dans menu_patisserie.csv.
```

*`menu_patisserie.csv` produit :*

```text
produit,categorie,prix,stock
"Muffin, bleuets",patisserie,3.50,8
Muffin,patisserie,3.25,12
Biscuit,patisserie,1.95,30
```

## 🟡 Exercice 4 : Moyen

**But** : Ajouter des rangées à un CSV existant avec le mode `"a"`.

**Énoncé** : Écris un programme d'**inscription** à la soirée LAN du département. À chaque exécution, il demande le nom complet (les virgules sont permises, ex. : `Tremblay, Marie`), le numéro de groupe (1 à 4) et le jeu préféré, puis **ajoute** une rangée au fichier `inscriptions.csv`.

- Si le fichier n'existe pas encore, le programme écrit d'abord l'en-tête `nom,groupe,jeu`.
- Après l'ajout, le programme relit le fichier et affiche le nombre total d'inscrits.

*Exemple d'exécution :*

```text
Nom complet : Tremblay, Marie
Groupe (1 à 4) : 1
Jeu préféré : Rocket League
Inscription enregistrée! 3 inscrit(s) au total.
```

> 💡 `CHEMIN.exists()` renvoie `True` si le fichier existe. Teste-le **avant** d'ouvrir le fichier en mode `"a"`, puisque l'ouverture le crée.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Convertir un CSV d'Excel français avec le module `csv`, sans perte de données.

**Énoncé** : Refais l'exercice 5 de la [série 8.3](Exercices%208.3%20-%20Les%20fichiers%20CSV%20à%20la%20main.md) (`depenses_excel.csv` → `depenses.csv`) avec le module `csv`. Cette fois, la virgule de `IGA, commande de la semaine` doit être **conservée**.

Ajoute ensuite la fonction inverse, `exporter_pour_excel(chemin_source, chemin_destination)`, qui relit `depenses.csv` et produit `depenses_pour_excel.csv` : point-virgule, virgule décimale, encodage `"utf-8-sig"` pour qu'Excel affiche correctement les accents.

Vérifie que `depenses_pour_excel.csv` est identique (au contenu près) au fichier de départ.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.4 - Le module csv](Solutions%208.4%20-%20Le%20module%20csv.md).
