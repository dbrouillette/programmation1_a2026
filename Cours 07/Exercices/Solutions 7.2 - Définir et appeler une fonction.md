# Solutions — Définir et appeler une fonction (fiche 7.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
--- Bibliothèque du cégep ---
Lundi au jeudi : 8 h à 21 h
Vendredi : 8 h à 17 h
Bonne session!
--- Bibliothèque du cégep ---
```

a. **Deux fois** : une fois pour chaque appel `afficher_titre()`. Le corps d'une fonction est exécuté au complet à chaque appel.

b. La fonction `afficher_heures_fin_semaine()` est **définie**, mais n'est **jamais appelée**. Définir une fonction ne fait que la mémoriser; son corps ne s'exécute que lorsqu'on l'appelle.

c. Il faut ajouter l'appel juste après celui des heures de la semaine :

```python
afficher_titre()
afficher_heures_semaine()
afficher_heures_fin_semaine()    # ← ligne ajoutée
print("Bonne session!")
afficher_titre()
```

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| # | Erreur | Explication |
| --- | --- | --- |
| 1 | `afficher_menu()` est appelée **avant** d'être définie. | Python lit le fichier de haut en bas : à la première ligne, il ne connaît pas encore la fonction (`NameError`). |
| 2 | Il manque les **deux-points** à la fin de `def afficher_menu()`. | Comme pour `if`, `while` et `for`, la ligne `def` se termine par `:` (`SyntaxError`). |
| 3 | `print("2. Retourner un livre")` n'est **pas indenté**. | Cette ligne ne fait plus partie du corps de la fonction, ce qui termine le bloc. La ligne suivante, indentée, provoque alors une `IndentationError`. |
| 4 | La fonction est définie sous le nom `Afficher_Au_Revoir`, mais appelée sous le nom `afficher_au_revoir`. | Python distingue les majuscules des minuscules : ce sont deux noms différents (`NameError`). En plus, la convention est le `snake_case`, tout en minuscules. |
| 5 | Les **parenthèses** manquent dans `afficher_au_revoir`. | Sans parenthèses, on nomme la fonction sans l'appeler. **Aucune erreur** n'est signalée, mais le message ne s'affiche pas. |

```python
def afficher_menu():
    print("1. Emprunter un livre")
    print("2. Retourner un livre")
    print("3. Quitter")


def afficher_au_revoir():
    print("Merci et à bientôt!")


afficher_menu()
afficher_au_revoir()
```

- Python signale les erreurs de syntaxe (2 et 3) **avant** d'exécuter quoi que ce soit, puis les erreurs d'exécution (1 et 4) une à la fois. Il faut donc souvent corriger, réexécuter, puis corriger encore.

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
LARGEUR = 40


def afficher_ligne():
    print("-" * LARGEUR)


def afficher_regles():
    print("1. Parler à voix basse.")
    print("2. Aucune nourriture près des ordinateurs.")
    print("3. Rapporter les livres au comptoir.")
    print("4. Réserver les salles de travail en ligne.")


afficher_ligne()
print(f"{'RÈGLES DE LA BIBLIOTHÈQUE':^{LARGEUR}}")
afficher_ligne()
afficher_regles()
afficher_ligne()
```

- `afficher_ligne()` est écrite une seule fois, mais appelée trois fois.
- Le titre est un texte littéral placé dans le f-string : on l'entoure d'apostrophes `' '` pour ne pas fermer les guillemets `" "` du f-string.
- Pour changer la largeur de l'affiche, il suffit de modifier la constante `LARGEUR` : les lignes **et** le centrage du titre s'ajustent.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
NOM_GYM = "Gym Les Diablos"
LARGEUR = 32
JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
HEURES = ("6 h - 22 h", "6 h - 22 h", "6 h - 22 h", "6 h - 22 h", "6 h - 20 h", "8 h - 18 h", "Fermé")


def afficher_banniere():
    print("=" * LARGEUR)
    print(f"{NOM_GYM:^{LARGEUR}}")
    print("=" * LARGEUR)


def afficher_horaire():
    afficher_banniere()
    for i in range(len(JOURS)):
        print(f"{JOURS[i]:<12}{HEURES[i]:>20}")


afficher_horaire()
```

- `afficher_horaire()` appelle `afficher_banniere()` : après la bannière, l'exécution **revient** dans `afficher_horaire()` et continue avec la boucle.
- Les tuples `JOURS` et `HEURES` sont associés par leur index, comme les listes associées de la fiche 6.2 : on les parcourt donc **par index** avec `range(len(JOURS))`.
- Le programme principal tient en une ligne : tout le travail est fait par les fonctions.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

a. Ordre d'exécution :

```text
1, 5, 11, 15, 16, 6, 2, 7, 8, 12, 17
```

| Ligne(s) | Ce qui se passe |
| --- | --- |
| 1, 5, 11 | Python **mémorise** les trois fonctions, sans exécuter leur corps. |
| 15 | Premier affichage. |
| 16 | Appel : saut dans `afficher_menu_du_jour()`. |
| 6 → 2 | Appel : saut dans `afficher_bonjour()`, qui affiche « Bonjour! », puis retour à la ligne 7. |
| 7 | Affichage de la soupe. |
| 8 → 12 | Appel : saut dans `afficher_dessert()`, qui affiche le dessert, puis retour. |
| 17 | `afficher_menu_du_jour()` est terminée : retour au programme principal, dernier affichage. |

b. Affichage :

```text
Cafétéria du cégep
Bonjour!
Soupe : poulet et nouilles
Dessert : pouding chômeur
Bon appétit!
```

c. **Non**, il n'y a pas d'erreur. La ligne 8 ne s'exécute qu'au moment de l'**appel** de `afficher_menu_du_jour()`, à la ligne 16. À ce moment, Python a déjà lu et mémorisé les trois définitions, y compris celle de `afficher_dessert()`. Ce qui compte, c'est que toutes les fonctions soient définies avant le **premier appel** du programme principal.

d. Avec `F11`, le débogueur entre dans chaque fonction appelée : on voit le surlignage passer de la ligne 16 à la ligne 6, puis à la ligne 2, etc., exactement dans l'ordre de la réponse **a**. Les lignes `def` (1, 5 et 11) sont déjà franchies lorsque le programme s'arrête au point d'arrêt de la ligne 15.
