# Exercice 2 — Opérateurs et erreurs de syntaxe

> **Sections couvertes :** [2.4 Opérateurs arithmétiques](../2.4%20-%20Opérateurs%20arithmétiques.md), [2.5 Opérateurs d'affectation combinée](../2.5%20-%20Opérateurs%20d'assignation.md), [2.6 Lire une erreur de syntaxe](../2.6%20-%20Lire%20une%20erreur%20de%20syntaxe.md)
> **Durée :** 60 minutes
> **Fichiers à compléter :** `exercice_2.py` et `exercice_2_debogage.py`
> **Correction :** `python -m unittest test_exercice_2.py`

## Objectifs

- Distinguer la division réelle `/` de la division entière `//` et maîtriser le modulo `%`.
- Prévoir le **type** du résultat d'une opération arithmétique.
- Utiliser les opérateurs d'affectation combinée.
- Lire un message d'erreur de syntaxe et corriger le code fautif.

## Consignes générales

1. Ouvre le fichier `exercice_2.py`.
2. Remplace chaque `None` par ta réponse.
3. **Ne change pas les noms de variables** : les tests s'en servent pour te corriger.
4. Remplis l'en-tête du fichier (ton nom, la date).

## Partie A — Prédire le résultat *(15 min)*

Six opérations à évaluer **de tête**, avant de les vérifier dans Python.

⚠️ Le **type** compte autant que la valeur : `5` et `5.0` sont deux réponses différentes, et les tests les distinguent. Relis la section 2.4 au sujet de `/` qui retourne **toujours** un `float`.

Attention aussi à `-17 // 5` : la division entière tronque **vers le bas**, pas vers zéro.

## Partie B — Affectation combinée *(10 min)*

On part de `x = 5` et on applique quatre opérations à la suite. Indique la valeur de `x` **après chaque ligne** — chaque réponse dépend de la précédente.

La question `B5` porte sur `/=` : c'est le piège signalé dans la section 2.5.

## Partie C1 — Convertir des secondes *(10 min)*

Décompose `DUREE_TOTALE_SECONDES` (10 000 secondes) en heures, minutes et secondes, en utilisant **uniquement** `//` et `%`.

- N'écris **aucun nombre en dur** : les constantes `SECONDES_PAR_MINUTE`, `MINUTES_PAR_HEURE` et `SECONDES_PAR_HEURE` sont fournies.
- Les trois résultats doivent être des `int`.
- Un test vérifie la cohérence : `heures × 3600 + minutes × 60 + secondes` doit redonner la durée de départ.

## Partie C2 — Calculer une facture *(15 min)*

À partir de `PRIX_UNITAIRE`, `quantite`, `TAUX_TPS` et `TAUX_TVQ`, calcule le sous-total, les deux montants de taxes, puis le total.

Utilise toujours les **constantes**, jamais leurs valeurs écrites en dur.

## Partie D — Afficher les résultats *(10 min)*

Avec des f-strings :

1. la durée sous la forme `2 h 46 min 40 s` ;
2. le total de la facture, suivi de ` $`.

## Partie E — Déboguer *(15 min)*

Le fichier `exercice_2_debogage.py` contient **6 erreurs de syntaxe**, une par bloc numéroté.

Python ne signale que la **première** à chaque exécution. La méthode :

1. lancer `python exercice_2_debogage.py` ;
2. lire la **dernière ligne** du message (le type et la description) ;
3. repérer le **numéro de ligne** et le curseur `^` ;
4. si la ligne semble correcte, vérifier la **ligne précédente** ;
5. corriger, relancer, recommencer.

⚠️ **Corrige uniquement la syntaxe.** Ne change ni les noms de variables, ni les valeurs, ni les calculs : les tests vérifient que le programme corrigé produit bien `nb_paquets = 2`, `articles_restants = 2` et `total_verification = 12`.

Réponds ensuite aux quatre questions `E1` à `E4` dans `exercice_2.py`.

## Corriger ton travail

Dans le dossier `Exercices`, lance le vérificateur coloré — les tests réussis apparaissent **en vert** :

```bash
python verifier.py
```

Tu peux aussi passer par unittest directement :

```bash
python -m unittest test_exercice_2.py
```

Pour voir le détail de chaque test :

```bash
python -m unittest -v test_exercice_2.py
```

Tu as terminé quand la sortie affiche `OK` et **26 tests réussis**.

## À retenir

- `/` retourne **toujours** un `float`, `//` tronque vers le bas, `%` donne le reste.
- Les opérateurs combinés s'écrivent **sans espace** : `*=` et non `* =`.
- Une erreur de syntaxe empêche **tout** le programme de s'exécuter.
- La ligne signalée par Python n'est pas toujours la ligne réellement fautive.
