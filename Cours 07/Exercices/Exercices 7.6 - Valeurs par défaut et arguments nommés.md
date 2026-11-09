# Exercices — Valeurs par défaut et arguments nommés (fiche 7.6)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande. Pour les nombres, réutilise les fonctions fournies `valider_nombre()` et `valider_entier()` de la série [Exercices 7.3](Exercices%207.3%20-%20Paramètres%20et%20arguments.md#-fonctions-fournies).

## 🟢 Exercice 1 : Facile

**But** : Déterminer la valeur que reçoit chaque paramètre, selon la façon d'appeler la fonction.

**Énoncé** : La coopérative du cégep prend les commandes de fournitures avec la fonction suivante. Pour chacun des six appels, indique la valeur que reçoivent `article`, `quantite` et `emballage_cadeau`, puis écris ce qui est affiché.

```python
def afficher_commande(article, quantite=1, emballage_cadeau=False):
    mention = " (emballage cadeau)" if emballage_cadeau else ""
    print(f"{quantite} x {article}{mention}")


afficher_commande("Agenda")
afficher_commande("Agenda", 3)
afficher_commande("Agenda", emballage_cadeau=True)
afficher_commande("Agenda", 2, True)
afficher_commande(quantite=4, article="Stylo")
afficher_commande("Stylo", True)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20afficher_commande%28article%2C%20quantite%3D1%2C%20emballage_cadeau%3DFalse%29%3A%0A%20%20%20%20mention%20%3D%20%22%20%28emballage%20cadeau%29%22%20if%20emballage_cadeau%20else%20%22%22%0A%20%20%20%20print%28f%22%7Bquantite%7D%20x%20%7Barticle%7D%7Bmention%7D%22%29%0A%0A%0Aafficher_commande%28%22Agenda%22%29%0Aafficher_commande%28%22Agenda%22%2C%203%29%0Aafficher_commande%28%22Agenda%22%2C%20emballage_cadeau%3DTrue%29%0Aafficher_commande%28%22Agenda%22%2C%202%2C%20True%29%0Aafficher_commande%28quantite%3D4%2C%20article%3D%22Stylo%22%29%0Aafficher_commande%28%22Stylo%22%2C%20True%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

> 💡 L'un des appels ne provoque aucune erreur, mais donne un résultat absurde. Lequel, et pourquoi?

## 🟢 Exercice 2 : Facile

**But** : Reconnaître les définitions et les appels invalides.

**Énoncé** : La bibliothèque réserve ses salles de travail avec la fonction suivante :

```python
def reserver(salle, duree=60, projecteur=False):
    print(f"Salle {salle}, {duree} minutes, projecteur : {projecteur}")
```

Pour chacune des lignes ci-dessous (chacune est indépendante des autres), indique si elle est **valide** ou si elle provoque une **erreur**. Pour une erreur, précise son type (`SyntaxError`, `TypeError`, etc.) et explique-la. Pour un appel valide, écris ce qu'il affiche.

```python
a.  def reserver(salle="A-101", duree):

b.  def reserver(duree=60, salle, projecteur=False):

c.  reserver("B-204", projecteur=True)

d.  reserver(duree=90, "B-204")

e.  reserver("B-204", 90, duree=120)

f.  reserver(projecteur=True)

g.  reserver("B-204", 90, True)
```

## 🟡 Exercice 3 : Moyen

**But** : Écrire une fonction avec des paramètres optionnels et l'appeler de différentes façons.

**Énoncé** : Le cinéma du centre-ville fixe ses prix ainsi :

| Client | Prix |
| --- | --- |
| Enfant (12 ans et moins) | 9,50 $ |
| Aîné (65 ans et plus) | 10,50 $ |
| Étudiant (de 13 à 64 ans, avec carte) | 11,00 $ |
| Régulier | 14,00 $ |

Le **mardi**, tous les billets coûtent 4,00 $ de moins.

Écris une fonction `calculer_prix_billet(age, est_etudiant=False, jour="semaine")` qui **renvoie** le prix d'un billet. Tous les prix, le rabais du mardi et les âges limites sont des constantes.

Le programme principal calcule le prix des quatre billets suivants, en utilisant **au moins deux** appels avec des arguments nommés, puis affiche chaque prix et le total :

- un adulte de 30 ans, en semaine;
- un étudiant de 19 ans, en semaine;
- un enfant de 8 ans, le mardi;
- un étudiant de 22 ans, le mardi.

*Sortie attendue :*

```text
Adulte de 30 ans, en semaine : 14.00 $
Étudiant de 19 ans, en semaine : 11.00 $
Enfant de 8 ans, le mardi : 5.50 $
Étudiant de 22 ans, le mardi : 7.00 $
Total : 37.50 $
```

> 💡 Pour l'enfant du mardi, quel est l'appel le plus court possible? Les valeurs par défaut permettent d'omettre `est_etudiant`.

## 🟡 Exercice 4 : Moyen

**But** : Ajouter des valeurs par défaut à des fonctions existantes pour simplifier leurs appels.

**Énoncé** : Reprends deux de tes fonctions :

- `valider_texte(msg_saisie, longueur_min, longueur_max)` (exercice 7.4-4) : donne-lui les valeurs par défaut `longueur_min=1` et `longueur_max=100`;
- `afficher_cadre(texte)` (exercice 7.3-3) : ajoute-lui un paramètre `symbole`, dont la valeur par défaut est `"*"`, qui sert à dessiner le cadre.

Le programme principal :

1. demande un prénom (longueurs par défaut), un pseudo (3 à 12 caractères) et une devise (40 caractères au maximum, en ne précisant **que** `longueur_max` par son nom);
2. affiche le prénom dans un cadre d'astérisques (symbole par défaut), le pseudo dans un cadre de `#`, et la devise dans un cadre de `~` (en nommant l'argument `symbole`).

*Exemple d'exécution :*

```text
Prénom :
Erreur : entrez entre 1 et 100 caractères.
Prénom : Léa
Pseudo (3 à 12 caractères) : LR
Erreur : entrez entre 3 et 12 caractères.
Pseudo (3 à 12 caractères) : LaReine
Devise (40 caractères max.) : Échec et mat en trois coups, toujours!

*******
* Léa *
*******
###########
# LaReine #
###########
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Échec et mat en trois coups, toujours! ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```


## 🔴 Exercice 5 : Difficile

**But** : Écrire une fonction qui renvoie une chaîne formatée selon plusieurs options.

**Énoncé** : Écris une fonction `formater_duree(secondes, afficher_heures=True, separateur=":")` qui **renvoie** une durée exprimée en secondes sous forme de chaîne :

- si `afficher_heures` est `True`, sous la forme `h:mm:ss` (ex. `4523` → `"1:15:23"`);
- sinon, sous la forme `min:ss`, en minutes totales (ex. `4523` → `"75:23"`);
- dans les deux cas, les minutes et les secondes ont toujours 2 chiffres, et les parties sont séparées par `separateur`.

Le programme principal demande le temps de 3 coureurs d'un demi-marathon, en secondes (entre 1 et 86 399), puis affiche un tableau qui présente chaque temps dans trois formats : par défaut, en minutes seulement et avec le séparateur `"."`. Utilise des arguments nommés pour les deux derniers formats.

*Exemple d'exécution :*

```text
Temps du coureur 1 (en secondes) : 4523
Temps du coureur 2 (en secondes) : 0
Erreur : entrez un nombre entre 1 et 86399.
Temps du coureur 2 (en secondes) : 7385
Temps du coureur 3 (en secondes) : 1342

Coureur      h:mm:ss    min:ss   h.mm.ss
1            1:15:23     75:23   1.15.23
2            2:03:05    123:05   2.03.05
3            0:22:22     22:22   0.22.22
```

> 💡 La division entière `//` et le modulo `%` permettent de découper les secondes. Le format `:0>2` (fiche 3.3) complète un nombre avec des zéros à gauche : `f"{5:0>2}"` donne `"05"`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.6 - Valeurs par défaut et arguments nommés](Solutions%207.6%20-%20Valeurs%20par%20défaut%20et%20arguments%20nommés.md).
