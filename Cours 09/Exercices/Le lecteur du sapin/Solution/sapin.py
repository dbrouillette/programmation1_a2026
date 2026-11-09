"""Le lecteur du sapin — SOLUTION.

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
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        print(Fore.RED + f"Erreur : {chemin.name} est introuvable.")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + f"Erreur : {chemin.name} n'est pas un fichier JSON valide.")
        return []


# ---------------------------------------------------------------------------
# Partie 2 — Catalogue et afficheur
# ---------------------------------------------------------------------------
def calculer_duree(chanson):
    """Renvoie la durée totale de la chanson, en millisecondes."""
    total = 0
    for note in chanson["notes"]:
        total += note["duree"]
    return total


def afficher_catalogue(bibliotheque):
    """Affiche les chansons numérotées à partir de 1, avec leur auteur et leur durée."""
    print()
    for i in range(len(bibliotheque)):
        chanson = bibliotheque[i]
        print(f"{i + 1:>2}. {chanson['titre']:<30}{chanson['auteur']:<18}"
              f"{calculer_duree(chanson) / 1000:>5.1f} s")
    print()


def afficher_lcd(ligne1, ligne2):
    """Simule l'afficheur LCD 16 x 2 du sapin."""
    print(Style.BRIGHT + "+" + "-" * LARGEUR_LCD + "+")
    print(Style.BRIGHT + f"|{ligne1[:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print(Style.BRIGHT + f"|{ligne2[:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print(Style.BRIGHT + "+" + "-" * LARGEUR_LCD + "+")


# ---------------------------------------------------------------------------
# Partie 3 — Une note : son et lumière
# ---------------------------------------------------------------------------
def frequence_de(note):
    """Renvoie la fréquence de la note, ou 0 pour un silence ou une note inconnue."""
    return FREQUENCES.get(note, 0)


def couleur_console(note):
    """Renvoie le code colorama de la note, sans tenir compte de l'octave."""
    return COULEURS_CONSOLE.get(note[:-1], Fore.WHITE)


def afficher_note(numero, note):
    """Affiche une ligne : numéro, note, fréquence et une barre de lumière.

    La barre compte un symbole par tranche de 10 % d'intensité.
    """
    nom = note["note"]
    if nom == SILENCE:
        print(f"{numero:>3}. {'—':<5} silence")
    elif nom not in FREQUENCES:
        print(Fore.RED + f"{numero:>3}. {nom:<5} note inconnue : ignorée")
    else:
        barre = SYMBOLE * (note["intensite"] // 10)
        print(f"{numero:>3}. {nom:<5}{frequence_de(nom):>4} Hz  "
              + couleur_console(nom) + barre)


# ---------------------------------------------------------------------------
# Partie 4 — Jouer une chanson
# ---------------------------------------------------------------------------
def jouer_chanson(chanson, parametres):
    """Joue toute la chanson et renvoie un compteur {note: nombre de fois jouée}."""
    afficher_lcd(chanson["titre"], chanson["auteur"])
    compteur = {}
    notes = chanson["notes"]
    for i in range(len(notes)):
        note = notes[i]
        afficher_note(i + 1, note)
        duree = note["duree"] * 100 // parametres["vitesse"]
        frequence = frequence_de(note["note"])
        if parametres["muet"]:
            frequence = 0
        jouer_son(frequence, duree)
        if note["note"] in FREQUENCES:
            compteur[note["note"]] = compteur.get(note["note"], 0) + 1
    return compteur


def afficher_bilan(chanson, compteur, parametres):
    """Affiche le nombre de notes jouées, la durée réelle et un histogramme coloré par note."""
    duree_reelle = calculer_duree(chanson) * 100 // parametres["vitesse"]
    print(f"\n♪ {sum(compteur.values())} notes jouées en {duree_reelle / 1000:.1f} s")
    for note in GAMME:
        if note in compteur:
            print(f"  {note:<5}{compteur[note]:>3} " + couleur_console(note) + SYMBOLE * compteur[note])


# ---------------------------------------------------------------------------
# Partie 5 — Paramètres du lecteur
# ---------------------------------------------------------------------------
def charger_parametres():
    """Renvoie les paramètres : valeurs par défaut, remplacées par celles du fichier si valides."""
    lus = {}
    try:
        with open(CHEMIN_PARAMETRES, "r", encoding="utf-8") as fichier:
            lus = json.load(fichier)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print(Fore.RED + "Avertissement : parametres.json invalide, valeurs par défaut utilisées.")
    if type(lus) != dict:
        lus = {}

    parametres = {}
    for cle in PARAMETRES_DEFAUT:
        valeur = lus.get(cle, PARAMETRES_DEFAUT[cle])
        if type(valeur) == type(PARAMETRES_DEFAUT[cle]):
            parametres[cle] = valeur
        else:
            parametres[cle] = PARAMETRES_DEFAUT[cle]
    if not VITESSE_MIN <= parametres["vitesse"] <= VITESSE_MAX:
        parametres["vitesse"] = PARAMETRES_DEFAUT["vitesse"]
    return parametres


def sauvegarder_parametres(parametres):
    """Écrit les paramètres dans parametres.json."""
    with open(CHEMIN_PARAMETRES, "w", encoding="utf-8") as fichier:
        json.dump(parametres, fichier, indent=4, ensure_ascii=False)


def modifier_parametres(parametres):
    """Demande le mode muet et la vitesse, puis sauvegarde les paramètres."""
    parametres["muet"] = lire_oui_non("Mode muet? (o/n) : ")
    parametres["vitesse"] = lire_entier(f"Vitesse en % ({VITESSE_MIN} à {VITESSE_MAX}) : ",
                                        VITESSE_MIN, VITESSE_MAX)
    sauvegarder_parametres(parametres)


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
