# Exercices — Une liste d'objets (fiche 10.3)

> 📌 **Pour toute la série**, utilise cette version de la classe `Renard` : celle de la fiche 10.3, avec en plus `courir()` (fiche 10.2) et `est_affame()`.

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

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.3 - Une liste d'objets](Solutions%2010.3%20-%20Une%20liste%20d%27objets.md).
