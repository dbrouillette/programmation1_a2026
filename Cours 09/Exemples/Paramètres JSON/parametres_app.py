"""Paramètres d'une application, sauvegardés en JSON — la version moderne du fichier .ini.

Au démarrage, l'application lit parametres.json. Si le fichier est absent, invalide
ou incomplet, les valeurs par défaut sont utilisées : l'application démarre toujours.
Chaque modification est sauvegardée immédiatement.

Essaie ceci :
  1. Lance le programme une première fois : parametres.json n'existe pas encore.
  2. Change quelques paramètres, quitte, puis relance : tes choix sont conservés.
  3. Ouvre parametres.json dans VS Code et modifie-le à la main
     (ex. : "volume": "fort", ou supprime une ligne, ou ajoute une erreur de syntaxe).
     Relance : l'application démarre quand même.
"""

import json
from pathlib import Path

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
CHEMIN_PARAMETRES = Path(__file__).parent / "parametres.json"
# Pour une vraie application, on utiliserait plutôt le dossier de l'utilisateur :
# DOSSIER_APP = Path.home() / ".cafe_binaire"
# DOSSIER_APP.mkdir(exist_ok=True)
# CHEMIN_PARAMETRES = DOSSIER_APP / "parametres.json"

PARAMETRES_DEFAUT = {
    "nom_utilisateur": "",
    "theme": "clair",
    "volume": 5,
    "sons_actifs": True,
}

THEMES = ("clair", "sombre", "contraste")
VOLUME_MIN = 0
VOLUME_MAX = 10


# ---------------------------------------------------------------------------
# Fichier de paramètres
# ---------------------------------------------------------------------------
def charger_parametres():
    """Renvoie les paramètres : valeurs par défaut, remplacées par celles du fichier si valides."""
    lus = {}
    try:
        with open(CHEMIN_PARAMETRES, "r", encoding="utf-8") as fichier:
            lus = json.load(fichier)
    except FileNotFoundError:
        print("(Première exécution : paramètres par défaut.)")
    except json.JSONDecodeError:
        print("Avertissement : parametres.json est invalide, paramètres par défaut utilisés.")

    if type(lus) != dict:              # ex. : le fichier contient une liste au lieu d'un objet
        lus = {}

    parametres = {}
    for cle in PARAMETRES_DEFAUT:
        defaut = PARAMETRES_DEFAUT[cle]
        valeur = lus.get(cle, defaut)
        if type(valeur) == type(defaut):
            parametres[cle] = valeur
        else:
            print(f"Avertissement : valeur invalide pour « {cle} », valeur par défaut utilisée.")
            parametres[cle] = defaut

    # Validation des valeurs elles-mêmes (pas seulement du type)
    if parametres["theme"] not in THEMES:
        parametres["theme"] = PARAMETRES_DEFAUT["theme"]
    if not VOLUME_MIN <= parametres["volume"] <= VOLUME_MAX:
        parametres["volume"] = PARAMETRES_DEFAUT["volume"]

    return parametres


def sauvegarder_parametres(parametres):
    """Écrit les paramètres dans parametres.json, de façon lisible pour un humain."""
    with open(CHEMIN_PARAMETRES, "w", encoding="utf-8") as fichier:
        json.dump(parametres, fichier, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Saisies validées
# ---------------------------------------------------------------------------
def lire_entier(message, minimum, maximum):
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return valeur


def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le texte ne doit pas être vide.")
        texte = input(message).strip()
    return texte


# ---------------------------------------------------------------------------
# Affichage
# ---------------------------------------------------------------------------
def afficher_parametres(parametres):
    sons = "oui" if parametres["sons_actifs"] else "non"
    print()
    print(f"  Nom         : {parametres['nom_utilisateur']}")
    print(f"  Thème       : {parametres['theme']}")
    print(f"  Volume      : {parametres['volume']} / {VOLUME_MAX}")
    print(f"  Sons actifs : {sons}")
    print()


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    parametres = charger_parametres()

    if parametres["nom_utilisateur"] == "":
        parametres["nom_utilisateur"] = lire_texte("Bienvenue! Quel est votre nom? ")
        sauvegarder_parametres(parametres)

    print(f"Bonjour {parametres['nom_utilisateur']}!")

    choix = -1
    while choix != 0:
        afficher_parametres(parametres)
        print("1. Changer de nom")
        print("2. Changer de thème")
        print("3. Changer le volume")
        print("4. Activer / désactiver les sons")
        print("5. Réinitialiser les paramètres")
        print("0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 5)

        if choix == 1:
            parametres["nom_utilisateur"] = lire_texte("Nouveau nom : ")
        elif choix == 2:
            for i in range(len(THEMES)):
                print(f"  {i + 1}. {THEMES[i]}")
            numero = lire_entier("Thème : ", 1, len(THEMES))
            parametres["theme"] = THEMES[numero - 1]
        elif choix == 3:
            parametres["volume"] = lire_entier(f"Volume ({VOLUME_MIN} à {VOLUME_MAX}) : ",
                                               VOLUME_MIN, VOLUME_MAX)
        elif choix == 4:
            parametres["sons_actifs"] = not parametres["sons_actifs"]
        elif choix == 5:
            for cle in PARAMETRES_DEFAUT:
                parametres[cle] = PARAMETRES_DEFAUT[cle]
            parametres["nom_utilisateur"] = lire_texte("Quel est votre nom? ")

        if choix != 0:
            sauvegarder_parametres(parametres)     # on sauvegarde dès qu'un paramètre change

    print(f"À bientôt, {parametres['nom_utilisateur']}!")


main()
