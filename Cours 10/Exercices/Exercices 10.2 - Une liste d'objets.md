# Exercices — Une liste d'objets (fiche 10.2)

> 📌 **Pour toute la série**, utilise cette version de la classe `Renard` : celle de la fiche 10.2, avec en plus `courir()` (fiche 10.1) et `est_affame()`.

```python
ENERGIE_MAX = 100
SEUIL_FAIM = 30


class Renard:
    """Un renard du refuge."""

    def __init__(self, nom, couleur, age):
        self.nom = nom
        self.couleur = couleur
        self.age = age
        self.energie = 50
        self.proies = []

    def chasser(self, proie):
        """Attrape une proie : +20 d'énergie, sans dépasser ENERGIE_MAX."""
        self.proies.append(proie)
        self.energie += 20
        if self.energie > ENERGIE_MAX:
            self.energie = ENERGIE_MAX

    def courir(self, distance):
        """Court distance km (10 d'énergie par km). Renvoie False si trop fatigué."""
        cout = distance * 10
        if cout > self.energie:
            return False
        self.energie -= cout
        return True

    def est_affame(self):
        """Renvoie True si l'énergie est sous SEUIL_FAIM."""
        return self.energie < SEUIL_FAIM

    def __str__(self):
        return f"{self.nom}, renard {self.couleur} de {self.age} ans"
```

## 🟢 Exercice 1 : Facile

**But** : Créer une liste d'objets, la parcourir et y trouver un minimum.

**Énoncé** : Crée la liste `refuge` de ces quatre renards : *Roux* (roux, 3 ans), *Flocon* (arctique, 2 ans), *Cendre* (argenté, 4 ans) et *Noisette* (roux, 5 ans). Ensuite :

1. Roux attrape un mulot et un lièvre, Noisette attrape une sauterelle, et Cendre court 3 km;
2. écris `afficher_tableau(renards)`, qui affiche le tableau aligné ci-dessous;
3. écris `plus_jeune(renards)`, qui **renvoie** le premier renard le plus jeune de la liste.

*Sortie attendue :*

```text
Nom       Couleur    Âge  Énergie  Proies
Roux      roux         3       90       2
Flocon    arctique     2       50       0
Cendre    argenté      4       20       0
Noisette  roux         5       70       1
Le plus jeune : Flocon (2 ans)
```

## 🟢 Exercice 2 : Facile

**But** : Écrire des fonctions de recherche et de filtre qui renvoient des objets.

**Énoncé** : Avec la même liste de quatre renards, écris :

- `chercher_renard(renards, nom)`, qui **renvoie** le renard qui porte ce nom, **sans tenir compte des majuscules ni des espaces autour**, ou `None`;
- `renards_de_couleur(renards, couleur)`, qui **renvoie** la liste des renards de cette couleur (sans tenir compte des majuscules);
- `total_proies(renards)`, qui **renvoie** le nombre total de proies attrapées par tous les renards.

Programme principal : Roux attrape un mulot (cherche-le avec `"roux"`), puis Noisette attrape une sauterelle (cherche-la avec `" NOISETTE "`) et un grillon (avec `"noisette"`).

*Sortie attendue :*

```text
2 renard(s) roux :
  Roux, renard roux de 3 ans
  Noisette, renard roux de 5 ans
Total des proies : 3
Goupil : None
```

## 🟡 Exercice 3 : Moyen

**But** : Enrichir une classe qui contient une liste d'objets.

**Énoncé** : Reprends la classe `Refuge` de la fiche 10.2 et modifie-la ou complète-la :

- `chercher(nom)` ne tient plus compte des majuscules ni des espaces autour;
- `accueillir(renard)` refuse donc aussi un renard nommé `roux` s'il y a déjà un `Roux`;
- `relacher(nom)` retire le renard et **renvoie** `True`, ou **renvoie** `False` s'il n'existe pas;
- `renards_affames()` **renvoie** la liste des renards affamés;
- `afficher()` affiche le nom du refuge, le nombre de renards, puis l'énergie de chacun, avec `⚠ affamé` au besoin.

Programme principal : le refuge essaie d'accueillir Roux, Flocon, Cendre, puis un deuxième `roux` (refusé). Flocon court 4 km; Cendre court 3 km, puis attrape un mulot. On affiche le refuge et le nombre de renards à nourrir en priorité, on relâche `ROUX` puis `Goupil`, et on affiche le refuge à nouveau.

*Sortie attendue :*

```text
Refusé : un renard s'appelle déjà « roux ».
Refuge du Lac-Saint-Pierre (3 renards)
  Roux      énergie  50
  Flocon    énergie  10  ⚠ affamé
  Cendre    énergie  40
À nourrir en priorité : 1 renard(s)
Relâcher Roux : True
Relâcher Goupil : False
Refuge du Lac-Saint-Pierre (2 renards)
  Flocon    énergie  10  ⚠ affamé
  Cendre    énergie  40
```

## 🔴 Exercice 4 : Moyen-Difficile

**But** : Gérer une liste d'objets avec un menu complet.

**Énoncé** : Écris un programme qui gère le refuge de l'exercice 3 avec un menu, jusqu'au choix 0. Le refuge commence avec Roux et Flocon.

1. **Afficher** : `refuge.afficher()`;
2. **Accueillir** : demande le nom (refusé s'il existe déjà), la couleur et l'âge (0 à 15);
3. **Chasser** : demande le nom du renard, puis la proie, et affiche sa nouvelle énergie;
4. **Courir** : demande le nom du renard, puis la distance (1 à 10 km);
5. **Relâcher** : demande le nom du renard et le retire du refuge.

Un nom introuvable affiche un message d'erreur. Toutes les saisies sont validées.

*Exemple d'exécution :*

```text
1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 2
Nom : flocon
Erreur : un renard s'appelle déjà « flocon ».

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 2
Nom : Noisette
Couleur : roux
Âge (0 à 15) : 20
Erreur : entrez un nombre entre 0 et 15.
Âge (0 à 15) : 1
Bienvenue à Noisette!

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 3
Nom du renard : noisette
Proie : sauterelle
Noisette a maintenant 70 d'énergie.

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 4
Nom du renard : Flocon
Distance (1 à 10 km) : 6
Flocon est trop fatigué.

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 5
Nom du renard : Roux
Roux est relâché en forêt.

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 1
Refuge du Lac-Saint-Pierre (2 renards)
  Flocon    énergie  50
  Noisette  énergie  70

1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter
Votre choix : 0
Le refuge ferme ses portes. Bonne nuit, les renards!
```

> 💡 Écris une fonction `choisir_renard(refuge)` qui demande un nom et **renvoie** le renard, ou `None` après avoir affiché l'erreur : les choix 3 et 4 l'utilisent tous les deux.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.2 - Une liste d'objets](Solutions%2010.2%20-%20Une%20liste%20d'objets.md).
