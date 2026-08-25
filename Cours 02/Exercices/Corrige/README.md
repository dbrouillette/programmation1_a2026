# Corrigé — Exercices du Cours 02

> ⚠️ **Ce dossier est visible par les étudiants s'ils clonent le dépôt.** Voir la section *Diffusion* plus bas.

## Le corrigé principal est dans les messages de test

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

L'étudiant se corrige donc seul, sans avoir accès à ce dossier.

**Nuance importante :** tant qu'une réponse vaut encore `None`, le test affiche seulement *« la question n'a pas été répondue »*, **sans dévoiler la réponse**. L'explication n'apparaît qu'après une tentative erronée. C'est un choix volontaire : sans ce garde-fou, il suffirait de lancer les tests sur le fichier vierge pour obtenir toutes les réponses.

## Contenu de ce dossier

|Fichier|Rôle|
|---|---|
|`exercice_1.py`|Solution complète et commentée de l'exercice 1|
|`exercice_2.py`|Solution complète et commentée de l'exercice 2|
|`exercice_2_debogage.py`|Version débogée, avec les 6 corrections annotées|
|`test_exercice_1.py`, `test_exercice_2.py`|Copies des suites de tests, pour rendre ce dossier auto-vérifiable|

## Vérifier le corrigé

```bash
cd "Cours 02/Exercices/Corrige"
python -m unittest discover -p "test_*.py"
```

Résultat attendu : `Ran 46 tests` … `OK`.

Cette vérification sert aussi de **test de non-régression** : si tu modifies un énoncé ou un test, relance-la pour confirmer que le corrigé reste valide.

## Barème suggéré

|Exercice|Partie|Tests|Suggestion|
|---|---|:---:|:---:|
|1|A — Choix multiple|6|6 pts|
|1|B — Constantes|3|6 pts|
|1|C — Variables et calculs|7|14 pts|
|1|D — Affichage|4|4 pts|
|2|A — Prédiction|6|6 pts|
|2|B — Affectation combinée|5|5 pts|
|2|C — Conversion et facture|8|16 pts|
|2|D — Affichage|2|2 pts|
|2|E — Débogage|5|10 pts|

Pour obtenir un décompte automatique par étudiant :

```bash
python -m unittest discover -p "test_*.py" 2>&1 | tail -3
```

La ligne `FAILED (failures=N)` donne le nombre de tests ratés sur 46.

## Diffusion

Si tu ne veux pas que les étudiants voient ce dossier, deux options :

- **Le retirer du dépôt public** et le garder localement — ajoute `Cours 02/Exercices/Corrige/` au fichier `.gitignore` à la racine.
- **Le publier après la remise**, en le committant seulement une fois l'exercice terminé.

Les messages explicatifs des tests, eux, restent disponibles en tout temps : c'est ce qui permet à l'étudiant de progresser sans le corrigé.
