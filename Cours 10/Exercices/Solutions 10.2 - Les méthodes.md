# Solutions — Les méthodes (fiche 10.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
70 100
3 campagnol
False
True 0
3 3
Goupil
```

| Ligne | Explication |
| --- | --- |
| `70 100` | Roux : 50 + 20. Flocon : 50 + 20 + 20 + 20 = 110, ramené à `ENERGIE_MAX` (100). |
| `3 campagnol` | Flocon a 3 proies; `[-1]` donne la dernière. |
| `False` | Courir 8 km coûte 80, mais Roux n'a que 70 d'énergie : refusé, l'énergie ne change pas. |
| `True 0` | 7 km coûtent exactement 70 : accepté, il reste 0. |
| `3 3` | Seul l'âge de Flocon change (2 → 3); Roux avait déjà 3 ans. |
| `Goupil` | `c = a` ne crée **pas** de nouveau renard : `c` et `a` désignent le **même** objet. |

- 🤔 **Réponse à la réflexion** : il n'existe que **deux** renards. `c = a` crée un deuxième nom (un alias) pour l'objet de Roux, comme `copie = liste` au cours 7. Changer `c.nom` change donc aussi `a.nom`. Seul un appel à `Renard(...)` crée un nouvel objet.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
class Livre:
    """Un livre en cours de lecture."""

    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages
        self.page_actuelle = 0

    def lire(self, pages):
        """Avance de pages pages, sans dépasser la fin du livre."""
        self.page_actuelle += pages
        if self.page_actuelle > self.nb_pages:
            self.page_actuelle = self.nb_pages

    def pourcentage(self):
        """Renvoie le pourcentage du livre déjà lu."""
        return self.page_actuelle / self.nb_pages * 100

    def est_termine(self):
        """Renvoie True si la dernière page est atteinte."""
        return self.page_actuelle == self.nb_pages

    def __str__(self):
        return f"« {self.titre} » de {self.auteur} ({self.pourcentage():.0f} % lu)"

roman = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
bd = Livre("Astérix le Gaulois", "Goscinny et Uderzo", 48)

roman.lire(30)
roman.lire(18)
bd.lire(60)

print(roman)
print(bd)
print(f"Roman terminé? {roman.est_termine()}")
print(f"BD terminée? {bd.est_termine()}")
```

- `lire()` ajoute les pages, puis corrige si on a dépassé la fin : c'est la même technique que pour l'énergie maximale du renard.
- `est_termine()` renvoie directement le résultat de la comparaison : pas besoin d'un `if`.
- `__str__()` appelle une autre méthode de l'objet, `self.pourcentage()`.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

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

    def dormir(self, heures):
        """Dort : +15 d'énergie par heure, sans dépasser ENERGIE_MAX."""
        self.energie += heures * 15
        if self.energie > ENERGIE_MAX:
            self.energie = ENERGIE_MAX

    def est_affame(self):
        """Renvoie True si l'énergie est sous SEUIL_FAIM."""
        return self.energie < SEUIL_FAIM

    def __str__(self):
        etat = " (affamé!)" if self.est_affame() else ""
        return f"{self.nom} : énergie {self.energie}, {len(self.proies)} proie(s){etat}"

def lire_entier(message, minimum, maximum):
    """Demande un entier entre minimum et maximum."""
    while True:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                return valeur
            print(f"Erreur : entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : nombre entier attendu.")

def main():
    renard = Renard("Roux", "roux", 3)
    choix = -1
    while choix != 0:
        print(renard)
        choix = lire_entier("1. Chasser  2. Courir  3. Dormir  0. Quitter : ", 0, 3)
        if choix == 1:
            proie = input("Proie : ").strip()
            renard.chasser(proie)
        elif choix == 2:
            distance = lire_entier("Distance (1 à 10 km) : ", 1, 10)
            if not renard.courir(distance):
                print(f"{renard.nom} est trop fatigué pour courir {distance} km.")
        elif choix == 3:
            renard.dormir(lire_entier("Heures de sommeil (1 à 12) : ", 1, 12))
    print(f"Bonne nuit, {renard.nom}!")

main()
```

- `dormir()` et `chasser()` utilisent la même limite `ENERGIE_MAX` : une constante évite les « nombres magiques ».
- `__str__()` utilise `est_affame()` plutôt que de répéter la comparaison avec `SEUIL_FAIM`.
- L'opérateur ternaire (fiche 4.4) choisit le texte à ajouter : `" (affamé!)"` ou rien.
- Le programme principal ne touche **jamais** directement à `renard.energie` : il passe toujours par les méthodes, qui font respecter les limites.

## 🔴 Exercice 4 : Moyen-Difficile

### ✅ Solution 4

```python
class Tirelire:
    """Une tirelire qui garde l'historique de ses opérations."""

    def __init__(self, proprietaire):
        self.proprietaire = proprietaire
        self.solde = 0.0
        self.historique = []

    def deposer(self, montant):
        """Dépose un montant positif. Renvoie True si l'opération est acceptée."""
        if montant <= 0:
            self.historique.append(f"Dépôt refusé : {montant:.2f} $")
            return False
        self.solde += montant
        self.historique.append(f"Dépôt de {montant:.2f} $")
        return True

    def retirer(self, montant):
        """Retire un montant positif, sans dépasser le solde. Renvoie True si accepté."""
        if montant <= 0 or montant > self.solde:
            self.historique.append(f"Retrait refusé : {montant:.2f} $")
            return False
        self.solde -= montant
        self.historique.append(f"Retrait de {montant:.2f} $")
        return True

    def afficher_historique(self):
        """Affiche les opérations numérotées, puis le solde."""
        print(f"Tirelire de {self.proprietaire}")
        for i in range(len(self.historique)):
            print(f"  {i + 1}. {self.historique[i]}")
        print(f"Solde : {self.solde:.2f} $")

    def __str__(self):
        return f"Tirelire de {self.proprietaire} : {self.solde:.2f} $"

abby = Tirelire("Abby")
zoe = Tirelire("Zoé")
abby.deposer(20)
abby.deposer(-5)
abby.retirer(7.50)
abby.retirer(50)
zoe.deposer(10)

print(abby)
print(zoe)
print()
abby.afficher_historique()
```

- Chaque méthode vérifie d'abord les cas refusés et sort tout de suite avec `return False` : le cas normal n'est pas imbriqué dans un `if`.
- Le solde ne peut changer **que** dans `deposer()` et `retirer()`, qui valident les montants : la tirelire ne peut jamais devenir négative par ces méthodes.
- `self.historique = []` est créé dans `__init__()` : chaque tirelire a sa propre liste. Les opérations d'Abby n'apparaissent pas dans celle de Zoé.
