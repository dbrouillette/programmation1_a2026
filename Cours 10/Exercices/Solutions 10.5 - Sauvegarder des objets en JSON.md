# Solutions — Sauvegarder des objets en JSON (fiche 10.5)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
ENERGIE_MAX = 100

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

    def vers_dict(self):
        """Renvoie un dictionnaire qui représente le renard (pour JSON)."""
        return {
            "nom": self.nom,
            "couleur": self.couleur,
            "age": self.age,
            "energie": self.energie,
            "proies": self.proies,
        }

    def __str__(self):
        return f"{self.nom}, renard {self.couleur} de {self.age} ans"

def renard_depuis_dict(donnees):
    """Crée un objet Renard à partir d'un dictionnaire lu dans un fichier JSON."""
    renard = Renard(donnees["nom"], donnees["couleur"], donnees["age"])
    renard.energie = donnees["energie"]
    renard.proies = donnees["proies"]
    return renard

roux = Renard("Roux", "roux", 3)
roux.chasser("mulot")
roux.chasser("lièvre")

dico = roux.vers_dict()
print(dico)

copie = renard_depuis_dict(dico)
print(copie)
print(f"Énergie : {copie.energie}, proies : {copie.proies}")
print(f"Même contenu? {copie.vers_dict() == roux.vers_dict()}")
print(f"Même objet? {copie is roux}")
```

- `vers_dict()` contient **tous** les attributs nécessaires pour recréer le renard, y compris l'énergie et les proies, qui ne passent pas par le constructeur.
- `renard_depuis_dict()` appelle le constructeur, puis remet les deux attributs restants.
- `==` compare le **contenu** des deux dictionnaires; `is` vérifie s'il s'agit du **même** objet. La copie a le même contenu, mais c'est un autre renard.
