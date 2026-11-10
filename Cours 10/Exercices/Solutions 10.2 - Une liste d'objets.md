# Solutions — Une liste d'objets (fiche 10.2)

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

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
class Refuge:
    """Un refuge faunique et ses renards."""

    def __init__(self, nom):
        self.nom = nom
        self.renards = []

    def chercher(self, nom):
        """Renvoie le renard qui porte ce nom (sans tenir compte des majuscules), ou None."""
        for renard in self.renards:
            if renard.nom.lower() == nom.strip().lower():
                return renard
        return None

    def accueillir(self, renard):
        """Ajoute le renard, sauf si son nom existe déjà. Renvoie True si ajouté."""
        if self.chercher(renard.nom) is not None:
            return False
        self.renards.append(renard)
        return True

    def relacher(self, nom):
        """Retire le renard qui porte ce nom. Renvoie True s'il a été trouvé."""
        renard = self.chercher(nom)
        if renard is None:
            return False
        self.renards.remove(renard)
        return True

    def renards_affames(self):
        """Renvoie la liste des renards affamés."""
        affames = []
        for renard in self.renards:
            if renard.est_affame():
                affames.append(renard)
        return affames

    def afficher(self):
        """Affiche le nom du refuge et le tableau de ses renards."""
        print(f"{self.nom} ({len(self.renards)} renards)")
        for renard in self.renards:
            alerte = "  ⚠ affamé" if renard.est_affame() else ""
            print(f"  {renard.nom:<10}énergie {renard.energie:>3}{alerte}")


def main():
    refuge = Refuge("Refuge du Lac-Saint-Pierre")
    for renard in [Renard("Roux", "roux", 3), Renard("Flocon", "arctique", 2),
                   Renard("Cendre", "argenté", 4), Renard("roux", "argenté", 6)]:
        if not refuge.accueillir(renard):
            print(f"Refusé : un renard s'appelle déjà « {renard.nom} ».")

    refuge.chercher("Flocon").courir(4)
    refuge.chercher("Cendre").courir(3)
    refuge.chercher("Cendre").chasser("mulot")
    refuge.afficher()

    affames = refuge.renards_affames()
    print(f"À nourrir en priorité : {len(affames)} renard(s)")
    print(f"Relâcher Roux : {refuge.relacher('ROUX')}")
    print(f"Relâcher Goupil : {refuge.relacher('Goupil')}")
    refuge.afficher()


main()
```

- `accueillir()` et `relacher()` s'appuient sur `chercher()` : la règle « sans tenir compte des majuscules » est écrite **une seule fois**.
- `relacher()` cherche d'abord, puis retire avec `remove()` : jamais de `remove()` sur un objet absent.
- `renards_affames()` utilise la méthode `est_affame()` de chaque renard : le `Refuge` ne connaît pas le seuil de faim, c'est l'affaire de la classe `Renard`.
- La boucle du programme principal parcourt une liste de renards créés sur place, et affiche un message pour chaque refus.

## 🔴 Exercice 4 : Moyen-Difficile

### ✅ Solution 4

La classe `Refuge` est celle de l'exercice 3 (sans son `main()`). Le reste du programme :

```python
AGE_MAX = 15
DISTANCE_MAX = 10


def lire_entier(message, minimum, maximum):
    """Demande un entier entre minimum et maximum."""
    while True:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                return valeur
            print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")


def lire_texte(message):
    """Demande un texte non vide."""
    texte = input(message).strip()
    while texte == "":
        print("Erreur : ce champ est obligatoire.")
        texte = input(message).strip()
    return texte


def choisir_renard(refuge):
    """Demande un nom et renvoie le renard correspondant, ou None (avec un message)."""
    renard = refuge.chercher(lire_texte("Nom du renard : "))
    if renard is None:
        print("Erreur : aucun renard de ce nom au refuge.")
    return renard


def accueillir_renard(refuge):
    """Demande un nouveau renard et l'accueille au refuge."""
    nom = lire_texte("Nom : ")
    if refuge.chercher(nom) is not None:
        print(f"Erreur : un renard s'appelle déjà « {nom} ».")
        return
    couleur = lire_texte("Couleur : ")
    age = lire_entier(f"Âge (0 à {AGE_MAX}) : ", 0, AGE_MAX)
    refuge.accueillir(Renard(nom, couleur, age))
    print(f"Bienvenue à {nom}!")


def main():
    refuge = Refuge("Refuge du Lac-Saint-Pierre")
    refuge.accueillir(Renard("Roux", "roux", 3))
    refuge.accueillir(Renard("Flocon", "arctique", 2))

    choix = -1
    while choix != 0:
        print("\n1. Afficher  2. Accueillir  3. Chasser  4. Courir  5. Relâcher  0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 5)
        if choix == 1:
            refuge.afficher()
        elif choix == 2:
            accueillir_renard(refuge)
        elif choix == 3:
            renard = choisir_renard(refuge)
            if renard is not None:
                renard.chasser(lire_texte("Proie : "))
                print(f"{renard.nom} a maintenant {renard.energie} d'énergie.")
        elif choix == 4:
            renard = choisir_renard(refuge)
            if renard is not None:
                distance = lire_entier(f"Distance (1 à {DISTANCE_MAX} km) : ", 1, DISTANCE_MAX)
                if renard.courir(distance):
                    print(f"{renard.nom} a couru {distance} km.")
                else:
                    print(f"{renard.nom} est trop fatigué.")
        elif choix == 5:
            nom = lire_texte("Nom du renard : ")
            if refuge.relacher(nom):
                print(f"{nom} est relâché en forêt.")
            else:
                print("Erreur : aucun renard de ce nom au refuge.")
    print("Le refuge ferme ses portes. Bonne nuit, les renards!")


main()
```

- `choisir_renard()` évite de répéter la recherche et le message d'erreur dans les choix 3 et 4.
- `accueillir_renard()` vérifie le nom **avant** de demander la couleur et l'âge : l'utilisateur ne remplit pas tout pour rien.
- Le programme principal ne modifie jamais `refuge.renards` directement : il passe par `accueillir()` et `relacher()`.
- Les constantes `AGE_MAX` et `DISTANCE_MAX` servent à la fois dans le message et dans la validation.
