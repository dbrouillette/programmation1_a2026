# Exercices — Recharger des objets depuis un fichier JSON (fiche 10.6)

> 📌 **À savoir** : applique le patron des fiches 10.5 et 10.6 : une méthode `vers_dict()` dans la classe, une fonction `..._depuis_dict()` pour le chemin inverse, une fonction de chargement qui **valide** les données lues et une fonction de sauvegarde. Le programme doit **toujours démarrer**, même si le fichier est absent ou invalide.

## 🟡 Exercice 1 : Moyen

**But** : Rendre une liste d'objets persistante.

**Énoncé** : Écris `sauvegarder_renards(chemin, renards)` et `charger_renards(chemin)`, qui utilisent le fichier `renards.json`. Au chargement, un renard est ignoré (avec un avertissement qui donne son numéro) si :

- une clé manque;
- le nom ou la couleur n'est pas une chaîne, ou l'âge ou l'énergie n'est pas un entier;
- l'énergie n'est pas entre 0 et `ENERGIE_MAX`;
- les proies ne sont pas une liste de chaînes.

Le programme principal charge les renards. Si la liste est vide (premier démarrage), il crée Roux et Flocon. Ensuite, Roux attrape un mulot, on affiche chaque renard, et on sauvegarde.

*Sortie attendue (trois exécutions de suite) :*

```text
Premier démarrage : deux renards arrivent au refuge.
Roux : énergie 70, proies ['mulot']
Flocon : énergie 50, proies []
--- 2e exécution
Roux : énergie 90, proies ['mulot', 'mulot']
Flocon : énergie 50, proies []
--- 3e exécution
Roux : énergie 100, proies ['mulot', 'mulot', 'mulot']
Flocon : énergie 50, proies []
```

Modifie ensuite `renards.json` à la main pour donner 150 d'énergie à Flocon, et relance le programme :

```text
Avertissement : le renard no 2 est invalide et a été ignoré.
Roux : énergie 100, proies ['mulot', 'mulot', 'mulot', 'mulot']
```

## 🟡 Exercice 2 : Moyen

**But** : Ajouter une fonctionnalité au programme complet de la fiche.

**Énoncé** : Copie le programme [Exemples/Gestion des étudiants](../Exemples/Gestion%20des%20étudiants/) et ajoute au menu l'option **5. Bulletin**, qui exporte un fichier texte `bulletin.txt` (fiche 8.4) :

- une ligne par étudiant : son prénom et son nom, sa moyenne (1 décimale) et `Réussite` (moyenne de 60 ou plus) ou `Échec`;
- à la fin, la moyenne du groupe (seulement si le groupe n'est pas vide).

*Exemple d'exécution (à partir du fichier `etudiants.json` fourni) :*

```text
2 étudiant(s) chargé(s).

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Bulletin  0. Quitter
Votre choix : 2
DA (7 chiffres) : 2567890
Prénom : Zoé
Nom : Roy
Zoé Roy ajouté(e) au groupe.

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Bulletin  0. Quitter
Votre choix : 3
DA de l'étudiant : 2567890
Note (0 à 100) : 45
Note ajoutée à Zoé Roy (moyenne 45.0).

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Bulletin  0. Quitter
Votre choix : 5
Bulletin exporté dans bulletin.txt.

1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Bulletin  0. Quitter
Votre choix : 0
```

*Contenu de `bulletin.txt` :*

```text
BULLETIN DU GROUPE
========================================
Abby Tremblay           88.5  Réussite
Éloi Gagnon             64.0  Réussite
Zoé Roy                 45.0  Échec
========================================
Moyenne du groupe : 65.8
```

## 🔴 Exercice 3 : Moyen-Difficile

**But** : Sauvegarder un objet qui contient une liste d'objets.

**Énoncé** : Reprends la classe `Groupe` de la fiche 10.4, en version étudiants (un `numero` et une liste `etudiants`, avec `chercher()`, `ajouter()` et `moyenne()`), et la classe `Etudiant` de la fiche 10.5. Le groupe complet est sauvegardé dans **un seul** fichier, `groupe.json` :

```json
{
    "numero": "00001",
    "etudiants": [
        {"da": "2345678", "prenom": "Abby", "nom": "Tremblay", "notes": [90]},
        {"da": "2456789", "prenom": "Éloi", "nom": "Gagnon", "notes": [70]}
    ]
}
```

Écris :

- la méthode `vers_dict()` de `Groupe`, qui utilise le `vers_dict()` de chaque étudiant;
- `groupe_depuis_dict(donnees)`, qui recrée le groupe et ses étudiants **valides**;
- `charger_groupe(chemin, numero_defaut)`, qui renvoie un groupe vide (avec le numéro par défaut) si le fichier est absent, invalide ou n'a pas la forme attendue;
- `sauvegarder_groupe(chemin, groupe)`.

Au premier démarrage, le programme crée le groupe 00001 avec Abby (90) et Éloi (70), puis le sauvegarde.

*Sortie attendue (deux exécutions de suite) :*

```text
Groupe 00001 : 0 étudiant(s) chargé(s).
Groupe créé et sauvegardé.
  2345678 - Abby Tremblay  moyenne 90.0
  2456789 - Éloi Gagnon  moyenne 70.0
Moyenne du groupe : 80.0
--- 2e exécution
Groupe 00001 : 2 étudiant(s) chargé(s).
  2345678 - Abby Tremblay  moyenne 90.0
  2456789 - Éloi Gagnon  moyenne 70.0
Moyenne du groupe : 80.0
```

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.6 - Recharger des objets depuis un fichier JSON](Solutions%2010.6%20-%20Recharger%20des%20objets%20depuis%20un%20fichier%20JSON.md).
