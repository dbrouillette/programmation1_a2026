# Corrigé — Exercices du Cours 02

Chaque test qui échoue affiche **l'explication de la bonne réponse**, avec un renvoi à la section de théorie concernée :

```text
FAIL: test_a4_division_entiere_negative
----------------------------------------------------------------------
AssertionError: -3 != -4 :

>>> A4 - -17 // 5 vaut -4
>>> C'est le piege classique : // tronque vers le BAS (vers l'infini negatif),
>>> pas vers zero. -17 / 5 donne -3.4, et l'entier immediatement INFERIEUR
>>> a -3.4 est -4, pas -3.
>>> (revois la section 2.4 - Remarques importantes)
```

## Contenu de ce dossier

Ce dossier **reprend exactement l'arborescence** du dossier `Exercices` : chaque corrigé se trouve au même endroit que son énoncé, sous le même nom suffixé de ` - RÉPONSES`.

|Dossier|Contenu|
|---|---|
|`1 - Facile/`|Corrigés de E2.1 à E2.3|
|`2 - Moyen/`|Corrigés de E2.4 et E2.5|
|`3 - Difficile/`|Corrigés de E2.6 et E2.7|
|`4 - Ateliers autocorrigés/`|Solutions Python des deux ateliers|

Dans `4 - Ateliers autocorrigés/` :

|Fichier|Rôle|
|---|---|
|`exercice_1.py`|Solution complète et commentée de l'atelier 1|
|`exercice_2.py`|Solution complète et commentée de l'atelier 2|
|`exercice_2_debogage.py`|Version débogée, avec les 6 corrections annotées|
|`test_exercice_1.py`, `test_exercice_2.py`|Copies des suites de tests, pour rendre ce dossier auto-vérifiable|
|`verifier.py`|Lanceur coloré|

## Vérifier le corrigé

```bash
cd "Cours 02/Exercices/Corrige/4 - Ateliers autocorrigés"
python -m unittest discover -p "test_*.py"
```

Résultat attendu : `Ran 46 tests` … `OK`.

Cette vérification sert aussi de **test de non-régression** : si tu modifies un énoncé ou un test, relance-la pour confirmer que le corrigé reste valide.
