# Exercices — Sauvegarder et recharger des objets en CSV (fiche 10.7)

> 📌 **À savoir** : applique le patron de la fiche 10.7 : une méthode `vers_ligne_csv()`, une fonction `..._depuis_ligne_csv()`, une fonction de chargement qui **valide** chaque ligne (avec son numéro) et une fonction de sauvegarde qui écrit l'en-tête.

## 🟢 Exercice 1 : Facile

**But** : Traduire un objet en ligne CSV, et inversement.

**Énoncé** : Ajoute à la classe `Renard` (fiche 10.3) une méthode `vers_ligne_csv()`, qui renvoie la ligne `nom,couleur,age,energie,proies`. Les proies sont séparées par des espaces. Écris ensuite la fonction `renard_depuis_ligne_csv(ligne)`, qui recrée le renard, avec son énergie et ses proies.

Programme principal : Roux attrape un mulot et un lièvre; Flocon n'attrape rien. Pour chacun, affiche la ligne CSV, recrée une copie, et vérifie que la copie donne la **même** ligne.

*Sortie attendue :*

```text
Roux,roux,3,90,mulot lièvre         → Roux, énergie 90, proies ['mulot', 'lièvre']
  Même ligne après l'aller-retour? True
Flocon,arctique,2,50,               → Flocon, énergie 50, proies []
  Même ligne après l'aller-retour? True
```

## 🟡 Exercice 2 : Moyen

**But** : Rendre une liste d'objets persistante dans un fichier CSV.

**Énoncé** : Écris `sauvegarder_renards_csv(chemin, renards)` et `charger_renards_csv(chemin)`, qui utilisent `renards.csv` (avec l'en-tête `nom,couleur,age,energie,proies`). Au chargement, une ligne est ignorée, avec un message qui donne son numéro, si :

- elle n'a pas exactement 5 colonnes;
- le nom ou la couleur est vide;
- l'âge ou l'énergie n'est pas un entier (`isdigit()`);
- l'énergie dépasse `ENERGIE_MAX`.

Le programme principal charge les renards. S'il n'y en a aucun (premier démarrage), il crée Roux et Flocon. Ensuite, Roux attrape un mulot, on affiche chaque renard, et on sauvegarde.

*Sortie attendue (deux exécutions de suite) :*

```text
Premier démarrage : deux renards arrivent au refuge.
Roux : énergie 70, proies ['mulot']
Flocon : énergie 50, proies []
--- 2e exécution
Roux : énergie 90, proies ['mulot', 'mulot']
Flocon : énergie 50, proies []
```

Ajoute ensuite ces lignes à la fin de `renards.csv`, et relance le programme :

```text
Cendre,argenté,quatre,50,
Noisette,roux,5,120,
```

```text
Ligne 4 ignorée : âge ou énergie non entier.
Ligne 5 ignorée : énergie 120 trop grande.
Roux : énergie 100, proies ['mulot', 'mulot', 'mulot']
Flocon : énergie 50, proies []
```

## 🔴 Exercice 3 : Moyen-Difficile

**But** : Offrir une exportation en JSON ou en CSV.

**Énoncé** : Copie le programme [Exemples/Gestion des étudiants](../Exemples/Gestion%20des%20étudiants/). Il continue de **conserver** ses données dans `etudiants.json`, mais ajoute au menu l'option **5. Exporter** :

- le programme demande le format : `json` ou `csv`; une réponse vide choisit **JSON par défaut**; toute autre réponse est redemandée;
- en JSON, le groupe est écrit dans `export.json` (réutilise `sauvegarder_etudiants()`);
- en CSV, il est écrit dans `export.csv`, avec l'en-tête `da,prenom,nom,notes` (notes séparées par des espaces).

*Exemple d'exécution (à partir du fichier `etudiants.json` fourni) :*

```text
2 étudiant(s) chargé(s).

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Exporter  0. Quitter
Votre choix : 5
Format d'exportation (json ou csv, Entrée = json) : xls
Erreur : répondez json ou csv.
Format d'exportation (json ou csv, Entrée = json) : csv
Groupe exporté dans export.csv.

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Exporter  0. Quitter
Votre choix : 5
Format d'exportation (json ou csv, Entrée = json) :
Groupe exporté dans export.json.

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Exporter  0. Quitter
Votre choix : 0
```

*Contenu de `export.csv` :*

```text
da,prenom,nom,notes
2345678,Abby,Tremblay,85 92
2456789,Éloi,Gagnon,64
```

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.7 - Sauvegarder et recharger des objets en CSV](Solutions%2010.7%20-%20Sauvegarder%20et%20recharger%20des%20objets%20en%20CSV.md).
