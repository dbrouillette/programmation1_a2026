# Exercices — L'opérateur ternaire (fiche 4.4)

## 🟢 Exercice 1 : Facile

**But** : Écrire un premier ternaire simple.

**Énoncé** : Écris un programme qui demande un nombre entier et affiche *"Pair"* ou *"Impair"* **en une seule ligne**, à l'aide de l'opérateur ternaire.

## 🟢 Exercice 2 : Facile-Moyen

**But** : Affecter une variable avec un ternaire.

**Énoncé** : Écris un programme qui demande l'âge de l'utilisateur et affecte à une variable `statut` la valeur `"Majeur"` ou `"Mineur"` à l'aide de l'opérateur ternaire, puis affiche `statut`.

## 🟡 Exercice 3 : Moyen

**But** : Utiliser le ternaire pour comparer deux valeurs.

**Énoncé** : Écris un programme qui demande deux nombres à l'utilisateur et affiche le plus grand des deux à l'aide de l'opérateur ternaire (en une seule ligne, sans variable intermédiaire).

## 🟡 Exercice 4 : Moyen

**But** : Convertir un `if`/`else` en opérateur ternaire.

**Énoncé** : Réécris l'extrait suivant à l'aide d'un opérateur ternaire, sans changer son comportement :

```python
if temperature >= 0:
    etat = "Au-dessus de zéro"
else:
    etat = "Sous zéro"
```

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Reconnaître les limites du ternaire et savoir revenir à un `if`/`elif`/`else`.

**Énoncé** : Voici un opérateur ternaire imbriqué :

```python
mention = "Excellent" if note >= 90 else "Bien" if note >= 60 else "Échec"
```

a. Réécris cette instruction sous la forme d'un `if`/`elif`/`else` classique.
b. En une phrase, explique pourquoi la version `if`/`elif`/`else` est préférable ici.
