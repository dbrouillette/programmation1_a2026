# =============================================================
# Lanceur de tests colore - NE PAS MODIFIER CE FICHIER
#
# Affiche en VERT chaque test reussi et en ROUGE ceux qui restent
# a corriger, avec l'explication de la bonne reponse.
#
# Utilisation :
#     python verifier.py        -> les deux exercices
#     python verifier.py 1      -> exercice 1 seulement
#     python verifier.py 2      -> exercice 2 seulement
# =============================================================

import os
import sys
import pathlib
import unittest

DOSSIER = pathlib.Path(__file__).parent

TITRES = {
    "test_exercice_1": "Exercice 1 - Structure, variables et constantes",
    "test_exercice_2": "Exercice 2 - Operateurs et erreurs de syntaxe",
}


# -------------------------------------------------------------
# Couleurs
# -------------------------------------------------------------

def couleurs_actives():
    """Determine si le terminal peut afficher des couleurs."""
    if os.environ.get("NO_COLOR"):
        return False
    if not sys.stdout.isatty() and not os.environ.get("FORCE_COLOR"):
        return False
    if os.name == "nt":
        # Active les sequences ANSI sur la console Windows.
        try:
            import ctypes

            noyau = ctypes.windll.kernel32
            noyau.SetConsoleMode(noyau.GetStdHandle(-11), 7)
        except Exception:
            return False
    return True


if couleurs_actives():
    VERT, ROUGE, JAUNE, GRIS, GRAS, FIN = (
        "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[1m", "\033[0m",
    )
else:
    VERT = ROUGE = JAUNE = GRIS = GRAS = FIN = ""

COCHE = "[OK]" if os.name == "nt" else "[OK]"
CROIX = "[  ]"


# -------------------------------------------------------------
# Mise en forme
# -------------------------------------------------------------

def nom_lisible(test):
    """Libelle du test : sa docstring, sinon son nom de methode."""
    libelle = test.shortDescription()
    if libelle:
        return libelle
    nom = test.id().rsplit(".", 1)[-1]
    return nom[5:].replace("_", " ") if nom.startswith("test_") else nom


def nom_partie(test):
    doc = (test.__class__.__doc__ or test.__class__.__name__).strip()
    return doc.splitlines()[0].rstrip(".")


def indenter(texte, prefixe="        "):
    """Ne garde que l'explication, sans le prefixe technique d'unittest."""
    if ">>>" in texte:
        texte = texte[texte.index(">>>"):]
    lignes = [ligne for ligne in texte.strip().splitlines() if ligne.strip()]
    return "\n".join(prefixe + ligne.strip() for ligne in lignes)


def barre(reussis, total, largeur=30):
    if total == 0:
        return ""
    pleins = round(largeur * reussis / total)
    return VERT + "#" * pleins + FIN + GRIS + "." * (largeur - pleins) + FIN


# -------------------------------------------------------------
# Collecte des resultats
# -------------------------------------------------------------

class ResultatColore(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.details = []          # (test, None) si reussi, (test, message) sinon
        self.erreurs_globales = []  # problemes de chargement du fichier

    def addSuccess(self, test):
        self.details.append((test, None))

    def _echec(self, test, err):
        message = str(err[1])
        if isinstance(test, unittest.TestCase):
            self.details.append((test, message))
        else:
            # Erreur hors test : setUpModule, import, etc.
            self.erreurs_globales.append(message)

    def addFailure(self, test, err):
        self._echec(test, err)

    def addError(self, test, err):
        self._echec(test, err)


def executer(nom_module):
    suite = unittest.defaultTestLoader.loadTestsFromName(nom_module)
    resultat = ResultatColore()
    suite.run(resultat)
    return resultat


# -------------------------------------------------------------
# Affichage
# -------------------------------------------------------------

def afficher(nom_module, resultat):
    titre = TITRES.get(nom_module, nom_module)
    print()
    print(GRAS + titre + FIN)
    print(GRIS + "=" * len(titre) + FIN)

    if resultat.erreurs_globales:
        print()
        print(ROUGE + GRAS + "  Le fichier n'a pas pu etre charge." + FIN)
        for message in resultat.erreurs_globales:
            print(indenter(message, "    "))
        print()
        print(JAUNE + "  Corrige ce probleme, puis relance : python verifier.py" + FIN)
        return 0, 0

    partie_courante = None
    reussis = 0
    for test, message in resultat.details:
        partie = nom_partie(test)
        if partie != partie_courante:
            partie_courante = partie
            print()
            print("  " + GRAS + partie + FIN)
        if message is None:
            reussis += 1
            print(f"    {VERT}{COCHE} {nom_lisible(test)}{FIN}")
        else:
            print(f"    {ROUGE}{CROIX} {nom_lisible(test)}{FIN}")
            print(GRIS + indenter(message) + FIN)

    total = len(resultat.details)
    print()
    couleur = VERT if reussis == total else (JAUNE if reussis > total / 2 else ROUGE)
    print(f"  {barre(reussis, total)}  {couleur}{GRAS}{reussis} / {total}{FIN}")
    return reussis, total


def main():
    choix = sys.argv[1] if len(sys.argv) > 1 else None
    modules = ["test_exercice_1", "test_exercice_2"]
    if choix in ("1", "2"):
        modules = [f"test_exercice_{choix}"]

    if str(DOSSIER) not in sys.path:
        sys.path.insert(0, str(DOSSIER))

    total_reussis = total_tests = 0
    for nom_module in modules:
        if not (DOSSIER / f"{nom_module}.py").exists():
            continue
        reussis, total = afficher(nom_module, executer(nom_module))
        total_reussis += reussis
        total_tests += total

    print()
    if total_tests and total_reussis == total_tests:
        print(VERT + GRAS + f"  Bravo! Tout est reussi ({total_reussis}/{total_tests}). " + FIN)
    elif total_tests:
        restants = total_tests - total_reussis
        mot = "test" if restants == 1 else "tests"
        print(JAUNE + f"  Encore {restants} {mot} a reussir. Les explications en gris "
                     f"t'indiquent quoi corriger." + FIN)
    print()
    return 0 if total_tests and total_reussis == total_tests else 1


if __name__ == "__main__":
    sys.exit(main())
