# Solutions — Recharger des objets depuis un fichier JSON (fiche 10.6)

## 🟡 Exercice 1 : Moyen

### ✅ Solution 1

```python
import json
from pathlib import Path

ENERGIE_MAX = 100
CHEMIN_RENARDS = Path(__file__).parent / "renards.json"

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
        return {"nom": self.nom, "couleur": self.couleur, "age": self.age,
                "energie": self.energie, "proies": self.proies}

def renard_valide(donnees):
    """Renvoie True si le dictionnaire a la forme attendue pour un renard."""
    if type(donnees) != dict:
        return False
    for cle in ["nom", "couleur", "age", "energie", "proies"]:
        if cle not in donnees:
            return False
    if type(donnees["nom"]) != str or type(donnees["couleur"]) != str:
        return False
    if type(donnees["age"]) != int or type(donnees["energie"]) != int:
        return False
    if not 0 <= donnees["energie"] <= ENERGIE_MAX:
        return False
    if type(donnees["proies"]) != list:
        return False
    for proie in donnees["proies"]:
        if type(proie) != str:
            return False
    return True

def renard_depuis_dict(donnees):
    """Crée un objet Renard à partir d'un dictionnaire validé."""
    renard = Renard(donnees["nom"], donnees["couleur"], donnees["age"])
    renard.energie = donnees["energie"]
    renard.proies = donnees["proies"]
    return renard

def charger_renards(chemin):
    """Renvoie la liste des renards du fichier (liste vide en cas de problème)."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Avertissement : {chemin.name} est invalide.")
        return []
    if type(donnees) != list:
        print(f"Avertissement : {chemin.name} ne contient pas une liste.")
        return []
    renards = []
    for i in range(len(donnees)):
        if renard_valide(donnees[i]):
            renards.append(renard_depuis_dict(donnees[i]))
        else:
            print(f"Avertissement : le renard no {i + 1} est invalide et a été ignoré.")
    return renards

def sauvegarder_renards(chemin, renards):
    """Écrit la liste des renards dans le fichier JSON."""
    donnees = []
    for renard in renards:
        donnees.append(renard.vers_dict())
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

def main():
    renards = charger_renards(CHEMIN_RENARDS)
    if len(renards) == 0:
        print("Premier démarrage : deux renards arrivent au refuge.")
        renards = [Renard("Roux", "roux", 3), Renard("Flocon", "arctique", 2)]

    renards[0].chasser("mulot")
    for renard in renards:
        print(f"{renard.nom} : énergie {renard.energie}, proies {renard.proies}")
    sauvegarder_renards(CHEMIN_RENARDS, renards)

main()
```

- `renard_valide()` vérifie les clés **avant** de lire les valeurs : sinon, `donnees["age"]` lèverait une `KeyError`.
- Comme les données sont validées, `renard_depuis_dict()` peut remettre l'énergie directement : elle est forcément entre 0 et `ENERGIE_MAX`.
- Le premier démarrage n'est pas une erreur : le programme crée simplement deux renards.
- D'une exécution à l'autre, Roux accumule ses mulots : la liste d'objets survit à la fermeture du programme.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

Nouvelles constantes et nouvelle fonction, à placer avant le programme principal :

```python
CHEMIN_BULLETIN = Path(__file__).parent / "bulletin.txt"
SEUIL_REUSSITE = 60

def exporter_bulletin(chemin, etudiants):
    """Écrit le bulletin du groupe dans un fichier texte."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write("BULLETIN DU GROUPE\n")
        fichier.write("=" * 40 + "\n")
        total = 0
        for etudiant in etudiants:
            resultat = "Réussite" if etudiant.moyenne() >= SEUIL_REUSSITE else "Échec"
            fichier.write(f"{etudiant.prenom + ' ' + etudiant.nom:<22}"
                          f"{etudiant.moyenne():>6.1f}  {resultat}\n")
            total += etudiant.moyenne()
        fichier.write("=" * 40 + "\n")
        if len(etudiants) > 0:
            fichier.write(f"Moyenne du groupe : {total / len(etudiants):.1f}\n")
```

Le programme principal, avec l'option 5 :

```python
def main():
    """Charge le groupe, affiche le menu et sauvegarde après chaque modification."""
    groupe = charger_etudiants(CHEMIN_ETUDIANTS)
    print(f"{len(groupe)} étudiant(s) chargé(s).")

    choix = -1
    while choix != 0:
        print("\n1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  5. Bulletin  0. Quitter")
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
            exporter_bulletin(CHEMIN_BULLETIN, groupe)
            print(f"Bulletin exporté dans {CHEMIN_BULLETIN.name}.")

main()
```

- Le bulletin est un simple fichier texte écrit avec `write()` (fiche 8.4) : chaque format a son usage. Le JSON sert à **conserver** les données; le texte sert à les **présenter**.
- L'option 5 ne modifie pas le groupe : il n'y a rien à sauvegarder dans `etudiants.json`.
- La moyenne n'est écrite que si le groupe n'est pas vide, pour éviter une `ZeroDivisionError`.

## 🔴 Exercice 3 : Moyen-Difficile

### ✅ Solution 3

La classe `Etudiant` (avec `vers_dict()`), `etudiant_valide()` et `etudiant_depuis_dict()` sont celles des fiches 10.5 et 10.6. Le reste du programme :

```python
CHEMIN_GROUPE = Path(__file__).parent / "groupe.json"

class Groupe:
    """Un groupe-cours et ses étudiants."""

    def __init__(self, numero):
        self.numero = numero
        self.etudiants = []

    def chercher(self, da):
        """Renvoie l'étudiant qui a ce DA, ou None."""
        for etudiant in self.etudiants:
            if etudiant.da == da:
                return etudiant
        return None

    def ajouter(self, etudiant):
        """Ajoute l'étudiant, sauf si son DA existe déjà. Renvoie True si ajouté."""
        if self.chercher(etudiant.da) is not None:
            return False
        self.etudiants.append(etudiant)
        return True

    def moyenne(self):
        """Renvoie la moyenne du groupe, ou 0 s'il est vide."""
        if len(self.etudiants) == 0:
            return 0
        total = 0
        for etudiant in self.etudiants:
            total += etudiant.moyenne()
        return total / len(self.etudiants)

    def vers_dict(self):
        """Renvoie un dictionnaire qui représente le groupe et tous ses étudiants."""
        liste = []
        for etudiant in self.etudiants:
            liste.append(etudiant.vers_dict())
        return {"numero": self.numero, "etudiants": liste}

def groupe_depuis_dict(donnees):
    """Crée un objet Groupe (et ses étudiants valides) à partir d'un dictionnaire."""
    groupe = Groupe(donnees["numero"])
    for i in range(len(donnees["etudiants"])):
        if etudiant_valide(donnees["etudiants"][i]):
            groupe.ajouter(etudiant_depuis_dict(donnees["etudiants"][i]))
        else:
            print(f"Avertissement : l'étudiant no {i + 1} est invalide et a été ignoré.")
    return groupe

def charger_groupe(chemin, numero_defaut):
    """Renvoie le groupe du fichier, ou un groupe vide en cas de problème."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        return Groupe(numero_defaut)
    except json.JSONDecodeError:
        print(f"Avertissement : {chemin.name} est invalide. Groupe vide.")
        return Groupe(numero_defaut)
    if (type(donnees) != dict or type(donnees.get("numero")) != str
            or type(donnees.get("etudiants")) != list):
        print(f"Avertissement : {chemin.name} n'a pas la forme attendue. Groupe vide.")
        return Groupe(numero_defaut)
    return groupe_depuis_dict(donnees)

def sauvegarder_groupe(chemin, groupe):
    """Écrit le groupe et ses étudiants dans le fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(groupe.vers_dict(), fichier, indent=4, ensure_ascii=False)

def main():
    groupe = charger_groupe(CHEMIN_GROUPE, "00001")
    print(f"Groupe {groupe.numero} : {len(groupe.etudiants)} étudiant(s) chargé(s).")

    if len(groupe.etudiants) == 0:
        groupe.ajouter(Etudiant("2345678", "Abby", "Tremblay"))
        groupe.ajouter(Etudiant("2456789", "Éloi", "Gagnon"))
        groupe.chercher("2345678").ajouter_note(90)
        groupe.chercher("2456789").ajouter_note(70)
        sauvegarder_groupe(CHEMIN_GROUPE, groupe)
        print("Groupe créé et sauvegardé.")

    for etudiant in groupe.etudiants:
        print(f"  {etudiant}  moyenne {etudiant.moyenne():.1f}")
    print(f"Moyenne du groupe : {groupe.moyenne():.1f}")

main()
```

- `Groupe.vers_dict()` délègue le travail : chaque étudiant sait se transformer en dictionnaire. On obtient un dictionnaire qui contient une liste de dictionnaires, que `json.dump()` écrit d'un seul coup.
- `groupe_depuis_dict()` passe par `groupe.ajouter()` : un DA en double dans le fichier est donc refusé, comme une saisie au clavier.
- `charger_groupe()` vérifie la forme de l'objet JSON (`numero` et `etudiants`) avec `get()` (fiche 9.1) : une clé absente donne `None`, qui n'est ni une `str` ni une `list`.
- C'est le même patron qu'aux fiches 10.5 et 10.6, un niveau plus haut : un objet qui contient des objets devient un dictionnaire qui contient des dictionnaires.
