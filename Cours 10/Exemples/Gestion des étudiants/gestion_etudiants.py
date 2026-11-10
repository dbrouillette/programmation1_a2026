"""Gestion des étudiants d'un groupe-cours (fiche 10.3).

Les étudiants sont des objets Etudiant, rangés dans une liste. La liste est
sauvegardée dans etudiants.json après chaque modification et rechargée au
démarrage : les données sont conservées d'une exécution à l'autre.

Auteur : 420-116-RI, Introduction à la programmation
"""

import json
from pathlib import Path

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
CHEMIN_ETUDIANTS = Path(__file__).parent / "etudiants.json"
CLES_ETUDIANT = ["da", "prenom", "nom", "notes"]
NOTE_MIN = 0
NOTE_MAX = 100
LONGUEUR_DA = 7


# ---------------------------------------------------------------------------
# La classe Etudiant
# ---------------------------------------------------------------------------
class Etudiant:
    """Un étudiant du groupe-cours."""

    def __init__(self, da, prenom, nom):
        self.da = da
        self.prenom = prenom
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        """Ajoute une note, si elle est entre NOTE_MIN et NOTE_MAX."""
        if NOTE_MIN <= note <= NOTE_MAX:
            self.notes.append(note)

    def moyenne(self):
        """Renvoie la moyenne des notes, ou 0 s'il n'y en a aucune."""
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    def vers_dict(self):
        """Renvoie un dictionnaire qui représente l'étudiant (pour JSON)."""
        return {
            "da": self.da,
            "prenom": self.prenom,
            "nom": self.nom,
            "notes": self.notes,
        }

    def __str__(self):
        return f"{self.da} - {self.prenom} {self.nom}"


# ---------------------------------------------------------------------------
# Fichier JSON
# ---------------------------------------------------------------------------
def etudiant_depuis_dict(donnees):
    """Crée un objet Etudiant à partir d'un dictionnaire lu dans le fichier JSON."""
    etudiant = Etudiant(donnees["da"], donnees["prenom"], donnees["nom"])
    for note in donnees["notes"]:
        etudiant.ajouter_note(note)
    return etudiant


def etudiant_valide(donnees):
    """Renvoie True si le dictionnaire a la forme attendue pour un étudiant."""
    if type(donnees) != dict:
        return False
    for cle in CLES_ETUDIANT:
        if cle not in donnees:
            return False
    if type(donnees["da"]) != str or type(donnees["prenom"]) != str or type(donnees["nom"]) != str:
        return False
    if type(donnees["notes"]) != list:
        return False
    for note in donnees["notes"]:
        if type(note) != int:
            return False
    return True


def charger_etudiants(chemin):
    """Renvoie la liste des étudiants du fichier JSON (liste vide en cas de problème)."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Avertissement : {chemin.name} est invalide. Groupe vide.")
        return []
    if type(donnees) != list:
        print(f"Avertissement : {chemin.name} ne contient pas une liste. Groupe vide.")
        return []

    etudiants = []
    for i in range(len(donnees)):
        if etudiant_valide(donnees[i]):
            etudiants.append(etudiant_depuis_dict(donnees[i]))
        else:
            print(f"Avertissement : l'étudiant no {i + 1} est invalide et a été ignoré.")
    return etudiants


def sauvegarder_etudiants(chemin, etudiants):
    """Écrit la liste des étudiants dans le fichier JSON."""
    donnees = []
    for etudiant in etudiants:
        donnees.append(etudiant.vers_dict())
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Saisies
# ---------------------------------------------------------------------------
def lire_entier(message, minimum, maximum):
    """Demande un entier entre minimum et maximum, jusqu'à ce qu'il soit valide."""
    while True:
        texte = input(message).strip()
        try:
            valeur = int(texte)
            if minimum <= valeur <= maximum:
                return valeur
            print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")


def lire_texte(message):
    """Demande un texte non vide et le renvoie sans espaces autour."""
    texte = input(message).strip()
    while texte == "":
        print("Erreur : ce champ est obligatoire.")
        texte = input(message).strip()
    return texte


# ---------------------------------------------------------------------------
# Opérations sur le groupe
# ---------------------------------------------------------------------------
def chercher_etudiant(etudiants, da):
    """Renvoie l'étudiant qui a ce DA, ou None s'il n'existe pas."""
    for etudiant in etudiants:
        if etudiant.da == da:
            return etudiant
    return None


def afficher_groupe(etudiants):
    """Affiche le tableau des étudiants."""
    print()
    if len(etudiants) == 0:
        print("Aucun étudiant dans le groupe.")
        return
    print(f"{'DA':<9}{'Prénom':<12}{'Nom':<14}{'Notes':>6}{'Moyenne':>9}")
    for etudiant in etudiants:
        print(f"{etudiant.da:<9}{etudiant.prenom:<12}{etudiant.nom:<14}"
              f"{len(etudiant.notes):>6}{etudiant.moyenne():>9.1f}")


def ajouter_etudiant(etudiants):
    """Demande un nouvel étudiant et l'ajoute au groupe (DA unique de 7 chiffres)."""
    da = lire_texte("DA (7 chiffres) : ")
    if len(da) != LONGUEUR_DA or not da.isdigit():
        print("Erreur : un DA contient exactement 7 chiffres.")
        return
    if chercher_etudiant(etudiants, da) is not None:
        print("Erreur : ce DA existe déjà.")
        return
    prenom = lire_texte("Prénom : ")
    nom = lire_texte("Nom : ")
    nouvel = Etudiant(da, prenom, nom)
    etudiants.append(nouvel)
    print(f"{nouvel.prenom} {nouvel.nom} ajouté(e) au groupe.")


def ajouter_note(etudiants):
    """Ajoute une note à un étudiant choisi par son DA."""
    etudiant = chercher_etudiant(etudiants, lire_texte("DA de l'étudiant : "))
    if etudiant is None:
        print("Erreur : aucun étudiant avec ce DA.")
        return
    note = lire_entier(f"Note ({NOTE_MIN} à {NOTE_MAX}) : ", NOTE_MIN, NOTE_MAX)
    etudiant.ajouter_note(note)
    print(f"Note ajoutée à {etudiant.prenom} {etudiant.nom} (moyenne {etudiant.moyenne():.1f}).")


def retirer_etudiant(etudiants):
    """Retire un étudiant choisi par son DA."""
    etudiant = chercher_etudiant(etudiants, lire_texte("DA de l'étudiant : "))
    if etudiant is None:
        print("Erreur : aucun étudiant avec ce DA.")
        return
    etudiants.remove(etudiant)
    print(f"{etudiant.prenom} {etudiant.nom} a été retiré(e) du groupe.")


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Charge le groupe, affiche le menu et sauvegarde après chaque modification."""
    groupe = charger_etudiants(CHEMIN_ETUDIANTS)
    print(f"{len(groupe)} étudiant(s) chargé(s).")

    choix = -1
    while choix != 0:
        print("\n1. Afficher  2. Ajouter un étudiant  3. Ajouter une note  4. Retirer  0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 4)
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


main()
