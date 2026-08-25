# Exercice 1 — Structure, variables et constantes

> **Sections couvertes :** [2.1 Généralités](../2.1%20-%20Généralités.md), [2.2 Variables](../2.2%20-%20Variables.md), [2.3 Constantes](../2.3%20-%20Constantes.md)
> **Durée :** 60 minutes
> **Fichier à compléter :** `exercice_1.py`
> **Correction :** `python -m unittest test_exercice_1.py`

## Objectifs

- Reconnaître les instructions et la sensibilité à la casse dans un programme Python.
- Appliquer les conventions de nomenclature `snake_case` et `SCREAMING_SNAKE_CASE`.
- Déclarer des variables des types `str`, `int`, `float` et `bool`.
- Utiliser la fonction native `type()` et les f-strings.

## Consignes générales

1. Ouvre le fichier `exercice_1.py`.
2. Remplace chaque `None` par ta réponse.
3. **Ne change pas les noms de variables** : les tests s'en servent pour te corriger.
4. Remplis l'en-tête du fichier (ton nom, la date).
5. Lance les tests aussi souvent que tu veux pour suivre ta progression.

## Partie A — Questions à choix multiple *(15 min)*

Six questions portant sur la structure d'un programme, la casse et la nomenclature. Réponds en écrivant la lettre de ton choix **entre guillemets** :

```python
reponse_a1 = "B"
```

💡 Réponds de mémoire d'abord, puis valide avec les fiches 2.1 à 2.3.

## Partie B — Déclarer des constantes *(10 min)*

Trois constantes à déclarer, avec un **nom**, un **type** et une **valeur** imposés. Attention :

- La convention pour une constante est `SCREAMING_SNAKE_CASE` (section 2.3).
- `2.75` est un `float`; `2` est un `int`. Les tests vérifient le **type** autant que la valeur.

## Partie C — Déclarer des variables et calculer *(20 min)*

Tu décris un étudiant à l'aide de cinq variables. **Les valeurs sont libres** — mets les tiennes — mais le type est imposé :

|Variable|Type|Contrainte|
|---|---|---|
|`prenom`|`str`|au moins 2 caractères|
|`nom_famille`|`str`|au moins 2 caractères|
|`age`|`int`|strictement positif|
|`moyenne_generale`|`float`|entre 0.0 et 100.0|
|`est_inscrit`|`bool`|`True` ou `False`, avec la majuscule|

Ensuite :

- **C2** — construis `nom_complet` avec un **f-string**, sous la forme `prenom nom_famille` (un seul espace).
- **C3** — calcule `cout_total_programme`. Utilise les **constantes** de la partie B, jamais leurs valeurs écrites en dur (section 2.3, *Bonnes pratiques*).

## Partie D — Afficher les résultats *(15 min)*

Complète les appels à `print()` pour afficher :

1. le nom du cégep (déjà fait, sert d'exemple) ;
2. le nom complet de l'étudiant, avec un f-string ;
3. le coût total du programme, suivi de ` $` ;
4. le **type** de `age`, de `moyenne_generale` et de `est_inscrit`, avec la fonction `type()`.

Les tests vérifient que l'affichage contient bien `<class 'int'>`, `<class 'float'>` et `<class 'bool'>`.

## Corriger ton travail

Dans le dossier `Exercices`, lance le vérificateur coloré — les tests réussis apparaissent **en vert** :

```bash
python verifier.py
```

Tu peux aussi passer par unittest directement :

```bash
python -m unittest test_exercice_1.py
```

Pour voir le détail de chaque test :

```bash
python -m unittest -v test_exercice_1.py
```

Tu as terminé quand la sortie affiche `OK` et **20 tests réussis**. Chaque échec te donne un message qui explique ce qui cloche.

## À retenir

- Une **constante** s'écrit en majuscules et se déclare en haut du fichier.
- Une **variable** s'écrit en `snake_case` et porte un nom explicite.
- `type()` permet de vérifier le type réel d'une valeur.
- `85` (un `int`) et `85.0` (un `float`) ne sont **pas** la même chose.
