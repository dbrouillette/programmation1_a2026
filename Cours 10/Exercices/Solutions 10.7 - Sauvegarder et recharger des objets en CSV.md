# Solutions — Sauvegarder et recharger des objets en CSV (fiche 10.7)

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

    def vers_ligne_csv(self):
        """Renvoie la ligne CSV : nom,couleur,age,energie,proies (proies séparées par des espaces)."""
        return f"{self.nom},{self.couleur},{self.age},{self.energie},{' '.join(self.proies)}"

def renard_depuis_ligne_csv(ligne):
    """Crée un objet Renard à partir d'une ligne CSV valide."""
    champs = ligne.strip().split(",")
    renard = Renard(champs[0], champs[1], int(champs[2]))
    renard.energie = int(champs[3])
    renard.proies = champs[4].split()
    return renard

roux = Renard("Roux", "roux", 3)
roux.chasser("mulot")
roux.chasser("lièvre")
flocon = Renard("Flocon", "arctique", 2)

for renard in [roux, flocon]:
    ligne = renard.vers_ligne_csv()
    copie = renard_depuis_ligne_csv(ligne)
    print(f"{ligne:<35} → {copie.nom}, énergie {copie.energie}, proies {copie.proies}")
    print(f"  Même ligne après l'aller-retour? {copie.vers_ligne_csv() == ligne}")
```

- Les proies sont déjà des chaînes : `" ".join(self.proies)` suffit, sans `str()`.
- L'âge et l'énergie sont relus comme des chaînes : on les convertit avec `int()`.
- `split()` sans argument sur une case vide donne `[]` : Flocon retrouve une liste de proies vide.
- Comparer les deux lignes vérifie que l'aller-retour objet → ligne → objet ne perd rien.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
from pathlib import Path

ENERGIE_MAX = 100
CHEMIN_RENARDS = Path(__file__).parent / "renards.csv"
EN_TETE = "nom,couleur,age,energie,proies"
NB_COLONNES = 5

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

    def vers_ligne_csv(self):
        """Renvoie la ligne CSV : nom,couleur,age,energie,proies (proies séparées par des espaces)."""
        return f"{self.nom},{self.couleur},{self.age},{self.energie},{' '.join(self.proies)}"

def verifier_ligne(ligne):
    """Renvoie un message d'erreur si la ligne est invalide, sinon une chaîne vide."""
    champs = ligne.strip().split(",")
    if len(champs) != NB_COLONNES:
        return f"{len(champs)} colonnes au lieu de {NB_COLONNES}"
    if champs[0].strip() == "" or champs[1].strip() == "":
        return "nom ou couleur manquant"
    if not champs[2].isdigit() or not champs[3].isdigit():
        return "âge ou énergie non entier"
    if int(champs[3]) > ENERGIE_MAX:
        return f"énergie {champs[3]} trop grande"
    return ""

def renard_depuis_ligne_csv(ligne):
    """Crée un objet Renard à partir d'une ligne CSV valide."""
    champs = ligne.strip().split(",")
    renard = Renard(champs[0], champs[1], int(champs[2]))
    renard.energie = int(champs[3])
    renard.proies = champs[4].split()
    return renard

def charger_renards_csv(chemin):
    """Renvoie la liste des renards du fichier CSV (liste vide si le fichier est absent)."""
    renards = []
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            fichier.readline()                         # en-tête
            numero = 1
            for ligne in fichier:
                numero += 1
                erreur = verifier_ligne(ligne)
                if erreur != "":
                    print(f"Ligne {numero} ignorée : {erreur}.")
                else:
                    renards.append(renard_depuis_ligne_csv(ligne))
    except FileNotFoundError:
        pass
    return renards

def sauvegarder_renards_csv(chemin, renards):
    """Écrit la liste des renards dans le fichier CSV, avec l'en-tête."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(EN_TETE + "\n")
        for renard in renards:
            fichier.write(renard.vers_ligne_csv() + "\n")

def main():
    renards = charger_renards_csv(CHEMIN_RENARDS)
    if len(renards) == 0:
        print("Premier démarrage : deux renards arrivent au refuge.")
        renards = [Renard("Roux", "roux", 3), Renard("Flocon", "arctique", 2)]

    renards[0].chasser("mulot")
    for renard in renards:
        print(f"{renard.nom} : énergie {renard.energie}, proies {renard.proies}")
    sauvegarder_renards_csv(CHEMIN_RENARDS, renards)

main()
```

- `verifier_ligne()` renvoie un **message** plutôt que `True`/`False` : `charger_renards_csv()` n'a qu'à l'afficher avec le numéro de ligne.
- `isdigit()` est vérifié **avant** `int()` : la conversion ne peut plus échouer.
- Le reste du programme est identique à la version JSON de la série 10.6 : seules les fonctions de chargement et de sauvegarde changent.

## 🔴 Exercice 3 : Moyen-Difficile

### ✅ Solution 3

Nouvelles constantes et fonctions, à placer avant le programme principal :

```python
DOSSIER_EXPORT = Path(__file__).parent
EN_TETE_CSV = "da,prenom,nom,notes"

def ligne_csv(etudiant):
    """Renvoie la ligne CSV d'un étudiant (notes séparées par des espaces)."""
    textes_notes = []
    for note in etudiant.notes:
        textes_notes.append(str(note))
    return f"{etudiant.da},{etudiant.prenom},{etudiant.nom},{' '.join(textes_notes)}"

def exporter_csv(chemin, etudiants):
    """Écrit les étudiants dans un fichier CSV, avec l'en-tête."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(EN_TETE_CSV + "\n")
        for etudiant in etudiants:
            fichier.write(ligne_csv(etudiant) + "\n")

def exporter(etudiants):
    """Demande le format (JSON par défaut, ou CSV) et exporte le groupe."""
    format_choisi = input("Format d'exportation (json ou csv, Entrée = json) : ").strip().lower()
    while format_choisi not in ("", "json", "csv"):
        print("Erreur : répondez json ou csv.")
        format_choisi = input("Format d'exportation (json ou csv, Entrée = json) : ").strip().lower()
    if format_choisi == "csv":
        chemin = DOSSIER_EXPORT / "export.csv"
        exporter_csv(chemin, etudiants)
    else:
        chemin = DOSSIER_EXPORT / "export.json"
        sauvegarder_etudiants(chemin, etudiants)
    print(f"Groupe exporté dans {chemin.name}.")
```

Le programme principal, avec l'option 5 :

```python
def main():
    """Charge le groupe, affiche le menu et sauvegarde après chaque modification."""
    groupe = charger_etudiants(CHEMIN_ETUDIANTS)
    print(f"{len(groupe)} étudiant(s) chargé(s).")

    choix = -1
    while choix != 0:
        print("\n1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Exporter  0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 5)
        if choix == 1:
            afficher_groupe(groupe)
        elif choix == 2:
            ajouter_etudiant(groupe)
            sauvegarder_etudiants(CHEMIN_ETUDIANTS, groupe)
        elif choix == 3:
            ajouter_note(groupe)
            sauvegarder_etudiants(CHEMIN_ETUDIANTS, groupe)
        elif choix == 4:
            retirer_etudiant(groupe)
            sauvegarder_etudiants(CHEMIN_ETUDIANTS, groupe)
        elif choix == 5:
            exporter(groupe)

main()
```

- L'exportation ne modifie pas le groupe : il n'y a rien à sauvegarder dans `etudiants.json`.
- L'exportation JSON réutilise `sauvegarder_etudiants()` avec un autre chemin : aucune ligne de code en double.
- `ligne_csv()` est une fonction plutôt qu'une méthode, pour ne pas modifier la classe; ajouter une méthode `vers_ligne_csv()` à `Etudiant`, comme en 10.7, serait tout aussi bon.
