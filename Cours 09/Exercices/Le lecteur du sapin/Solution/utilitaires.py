"""Fonctions utilitaires : saisies validées et son.

Reprend le module du TP2 (lire_entier, lire_texte, lire_oui_non), avec les
messages d'erreur en rouge, et ajoute jouer_son() pour le spectacle de Noël.
Ces fonctions ne dépendent d'aucune constante du lecteur.
"""

import time

from colorama import Fore, init

init(autoreset=True)

# Le module winsound n'existe que sous Windows. Ailleurs (macOS, Linux,
# Raspberry Pi), on simule le son par un silence de la même durée.
try:
    import winsound
    SON_DISPONIBLE = True
except ImportError:
    SON_DISPONIBLE = False

FREQUENCE_MIN = 37        # limites acceptées par winsound.Beep()
FREQUENCE_MAX = 32767


def lire_entier(message, minimum=0, maximum=99):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché à l'utilisateur.
        minimum (int, optional): La plus petite valeur acceptée. Par défaut 0.
        maximum (int, optional): La plus grande valeur acceptée. Par défaut 99.

    Returns:
        int: L'entier saisi, compris entre minimum et maximum.
    """
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(Fore.RED + f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print(Fore.RED + "Erreur : ce n'est pas un nombre entier.")
    return valeur


def lire_texte(message):
    """Demande un texte jusqu'à ce qu'il ne soit pas vide.

    Args:
        message (str): Le message affiché à l'utilisateur.

    Returns:
        str: Le texte saisi, sans espaces au début ni à la fin.
    """
    texte = input(message).strip()
    while texte == "":
        print(Fore.RED + "Erreur : la réponse ne peut pas être vide.")
        texte = input(message).strip()
    return texte


def lire_oui_non(message):
    """Pose une question fermée jusqu'à obtenir « o » ou « n ».

    Args:
        message (str): La question affichée à l'utilisateur.

    Returns:
        bool: True si l'utilisateur répond « o », False s'il répond « n ».
    """
    reponse = input(message).strip().lower()
    while reponse not in ("o", "n"):
        print(Fore.RED + "Erreur : répondez par o ou n.")
        reponse = input(message).strip().lower()
    return reponse == "o"


def jouer_son(frequence, duree_ms):
    """Joue un bip à la fréquence demandée, comme le haut-parleur d'un vieux PC.

    Sous Windows, le son est réellement joué avec winsound.Beep(). Ailleurs, ou
    si la fréquence vaut 0 (un silence), le programme attend simplement la durée
    demandée. Dans les deux cas, la fonction ne se termine qu'après duree_ms.

    Args:
        frequence (int): La fréquence en hertz (Hz); 0 pour un silence.
        duree_ms (int): La durée en millisecondes.
    """
    if SON_DISPONIBLE and FREQUENCE_MIN <= frequence <= FREQUENCE_MAX:
        winsound.Beep(frequence, duree_ms)
    else:
        time.sleep(duree_ms / 1000)


# Tests rapides : exécutés seulement si on lance ce fichier directement.
if __name__ == "__main__":
    print(f"Son disponible : {SON_DISPONIBLE}")
    for frequence in (262, 330, 392, 523):      # do, mi, sol, do : un accord!
        jouer_son(frequence, 250)
    help(jouer_son)
