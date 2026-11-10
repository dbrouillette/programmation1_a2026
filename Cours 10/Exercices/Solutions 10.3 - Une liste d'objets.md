# Solutions — Une liste d'objets (fiche 10.3)

> 📌 Chaque solution suppose que la classe `Renard` de l'énoncé est définie au début du programme.

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
def afficher_tableau(renards):
    """Affiche le tableau aligné des renards."""
    print(f"{'Nom':<10}{'Couleur':<10}{'Âge':>4}{'Énergie':>9}{'Proies':>8}")
    for renard in renards:
        print(f"{renard.nom:<10}{renard.couleur:<10}{renard.age:>4}"
              f"{renard.energie:>9}{len(renard.proies):>8}")

def plus_jeune(renards):
    """Renvoie le premier renard le plus jeune de la liste (non vide)."""
    resultat = renards[0]
    for renard in renards:
        if renard.age < resultat.age:
            resultat = renard
    return resultat

def main():
    refuge = [
        Renard("Roux", "roux", 3),
        Renard("Flocon", "arctique", 2),
        Renard("Cendre", "argenté", 4),
        Renard("Noisette", "roux", 5),
    ]
    refuge[0].chasser("mulot")
    refuge[0].chasser("lièvre")
    refuge[3].chasser("sauterelle")
    refuge[2].courir(3)

    afficher_tableau(refuge)
    jeune = plus_jeune(refuge)
    print(f"Le plus jeune : {jeune.nom} ({jeune.age} ans)")

main()
```

- La liste est créée directement avec ses quatre objets, entre crochets : chaque `Renard(...)` crée un objet.
- `plus_jeune()` est la recette du minimum (cours 6), appliquée à l'attribut `age`. Elle renvoie l'**objet** : le programme principal peut ensuite afficher son nom **et** son âge.
- Avec `<` (et non `<=`), c'est le **premier** renard le plus jeune qui est gardé en cas d'égalité.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
def chercher_renard(renards, nom):
    """Renvoie le renard qui porte ce nom (sans tenir compte des majuscules), ou None."""
    for renard in renards:
        if renard.nom.lower() == nom.strip().lower():
            return renard
    return None

def renards_de_couleur(renards, couleur):
    """Renvoie la liste des renards de cette couleur (sans tenir compte des majuscules)."""
    resultat = []
    for renard in renards:
        if renard.couleur.lower() == couleur.strip().lower():
            resultat.append(renard)
    return resultat

def total_proies(renards):
    """Renvoie le nombre total de proies attrapées par tous les renards."""
    total = 0
    for renard in renards:
        total += len(renard.proies)
    return total

def main():
    refuge = [
        Renard("Roux", "roux", 3),
        Renard("Flocon", "arctique", 2),
        Renard("Cendre", "argenté", 4),
        Renard("Noisette", "roux", 5),
    ]
    chercher_renard(refuge, "roux").chasser("mulot")
    chercher_renard(refuge, " NOISETTE ").chasser("sauterelle")
    chercher_renard(refuge, "noisette").chasser("grillon")

    roux = renards_de_couleur(refuge, "Roux")
    print(f"{len(roux)} renard(s) roux :")
    for renard in roux:
        print(f"  {renard}")
    print(f"Total des proies : {total_proies(refuge)}")
    print(f"Goupil : {chercher_renard(refuge, 'Goupil')}")

main()
```

- On normalise les **deux** côtés de la comparaison : `renard.nom.lower()` et `nom.strip().lower()`.
- `chercher_renard(refuge, "roux").chasser("mulot")` enchaîne la recherche et la méthode. C'est permis ici parce qu'on sait que Roux existe; sinon, il faudrait d'abord tester `None`.
- `renards_de_couleur()` renvoie une **nouvelle liste** qui contient **les mêmes objets** que `refuge` : ce ne sont pas des copies.
- `print()` d'un `None` affiche simplement `None`.
