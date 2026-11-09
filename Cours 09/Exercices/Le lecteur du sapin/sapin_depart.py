"""Le lecteur du sapin — VERSION DE DÉPART.

Auteur(s) : <?>
Date      : <?>

Le programme principal (main) est déjà écrit : complétez les fonctions
marquées « À COMPLÉTER », dans l'ordre des parties de l'énoncé.

Joue les chansons de bibliotheque.json en simulant le spectacle de Noël :
l'afficheur LCD 16 x 2, les lumières (en couleurs dans la console) et le son
(style haut-parleur de PC sous Windows, silence ailleurs).
Les paramètres du lecteur sont conservés dans parametres.json.
"""

import json
from pathlib import Path

from colorama import Fore, Style, init

from utilitaires import jouer_son, lire_entier, lire_oui_non

init(autoreset=True)

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
DOSSIER = Path(__file__).parent
CHEMIN_BIBLIOTHEQUE = DOSSIER / "bibliotheque.json"
CHEMIN_PARAMETRES = DOSSIER / "parametres.json"

FREQUENCES = {
    "DO4": 262, "RE4": 294, "MI4": 330, "FA4": 349,
    "SOL4": 392, "LA4": 440, "SI4": 494, "DO5": 523,
}
GAMME = ["DO4", "RE4", "MI4", "FA4", "SOL4", "LA4", "SI4", "DO5"]

COULEURS_CONSOLE = {
    "DO": Fore.RED,
    "RE": Fore.YELLOW,
    "MI": Fore.YELLOW + Style.BRIGHT,
    "FA": Fore.GREEN,
    "SOL": Fore.BLUE,
    "LA": Fore.CYAN,
    "SI": Fore.MAGENTA,
}

SYMBOLE = "●"
LARGEUR_LCD = 16
SILENCE = "-"

PARAMETRES_DEFAUT = {
    "muet": False,
    "vitesse": 100,             # en %, de 50 à 400
    "derniere_chanson": "",
}
VITESSE_MIN = 50
VITESSE_MAX = 400


# ---------------------------------------------------------------------------
# Partie 1 — Fichiers
# ---------------------------------------------------------------------------
def charger_bibliotheque(chemin):
    """Renvoie la liste des chansons du fichier JSON, ou une liste vide en cas de problème."""
    # À COMPLÉTER (partie 1)
    return []


# ---------------------------------------------------------------------------
# Partie 2 — Catalogue et afficheur
# ---------------------------------------------------------------------------
def calculer_duree(chanson):
    """Renvoie la durée totale de la chanson, en millisecondes."""
    # À COMPLÉTER (partie 2)
    return 0


def afficher_catalogue(bibliotheque):
    """Affiche les chansons numérotées à partir de 1, avec leur auteur et leur durée."""
    # À COMPLÉTER (partie 2)
    pass


def afficher_lcd(ligne1, ligne2):
    """Simule l'afficheur LCD 16 x 2 du sapin."""
    # À COMPLÉTER (partie 2)
    pass


# ---------------------------------------------------------------------------
# Partie 3 — Une note : son et lumière
# ---------------------------------------------------------------------------
def frequence_de(note):
    """Renvoie la fréquence de la note, ou 0 pour un silence ou une note inconnue."""
    # À COMPLÉTER (partie 3)
    return 0


def couleur_console(note):
    """Renvoie le code colorama de la note, sans tenir compte de l'octave."""
    # À COMPLÉTER (partie 3)
    return Fore.WHITE


def afficher_note(numero, note):
    """Affiche une ligne : numéro, note, fréquence et une barre de lumière.

    La barre compte un symbole par tranche de 10 % d'intensité.
    """
    # À COMPLÉTER (partie 3)
    pass


# ---------------------------------------------------------------------------
# Partie 4 — Jouer une chanson
# ---------------------------------------------------------------------------
def jouer_chanson(chanson, parametres):
    """Joue toute la chanson et renvoie un compteur {note: nombre de fois jouée}."""
    # À COMPLÉTER (partie 4)
    return {}


def afficher_bilan(chanson, compteur, parametres):
    """Affiche le nombre de notes jouées, la durée réelle et un histogramme coloré par note."""
    # À COMPLÉTER (partie 4)
    pass


# ---------------------------------------------------------------------------
# Partie 5 — Paramètres du lecteur
# ---------------------------------------------------------------------------
def charger_parametres():
    """Renvoie les paramètres : valeurs par défaut, remplacées par celles du fichier si valides."""
    # À COMPLÉTER (partie 5)
    return PARAMETRES_DEFAUT.copy()


def sauvegarder_parametres(parametres):
    """Écrit les paramètres dans parametres.json."""
    # À COMPLÉTER (partie 5)
    pass


def modifier_parametres(parametres):
    """Demande le mode muet et la vitesse, puis sauvegarde les paramètres."""
    # À COMPLÉTER (partie 5)
    pass


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    bibliotheque = charger_bibliotheque(CHEMIN_BIBLIOTHEQUE)
    if len(bibliotheque) == 0:
        print("Aucune chanson à jouer.")
        return

    parametres = charger_parametres()
    afficher_lcd("Spectacle de", "Noel du Cegep!")
    if parametres["derniere_chanson"] != "":
        print(f"Dernière chanson jouée : {parametres['derniere_chanson']}")

    choix = -1
    while choix != 0:
        etat = "muet" if parametres["muet"] else "son"
        print(f"\n1. Jouer une chanson  2. Paramètres ({etat}, {parametres['vitesse']} %)  0. Quitter")
        choix = lire_entier("Choix : ", 0, 2)

        if choix == 1:
            afficher_catalogue(bibliotheque)
            numero = lire_entier("Chanson : ", 1, len(bibliotheque))
            chanson = bibliotheque[numero - 1]
            compteur = jouer_chanson(chanson, parametres)
            afficher_bilan(chanson, compteur, parametres)
            parametres["derniere_chanson"] = chanson["titre"]
            sauvegarder_parametres(parametres)
        elif choix == 2:
            modifier_parametres(parametres)

    afficher_lcd("Joyeux Noel!", "")


main()
