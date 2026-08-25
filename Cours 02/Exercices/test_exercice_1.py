# =============================================================
# Tests de correction de l'exercice 1 - NE PAS MODIFIER CE FICHIER
#
# Utilisation :  python -m unittest test_exercice_1.py
#           ou :  python -m unittest -v test_exercice_1.py   (mode detaille)
# =============================================================

import io
import importlib.util
import contextlib
import pathlib
import unittest

FICHIER = pathlib.Path(__file__).with_name("exercice_1.py")


def charger_exercice():
    """Execute exercice_1.py et retourne (module, texte affiche)."""
    if not FICHIER.exists():
        raise unittest.SkipTest(f"Fichier introuvable : {FICHIER.name}")

    spec = importlib.util.spec_from_file_location("exercice_1", FICHIER)
    module = importlib.util.module_from_spec(spec)
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        spec.loader.exec_module(module)
    return module, sortie.getvalue()


class BaseExercice1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.ex, cls.sortie = charger_exercice()
        except SyntaxError as err:
            raise AssertionError(
                f"Erreur de syntaxe dans exercice_1.py a la ligne {err.lineno} : {err.msg}"
            ) from None

    def valeur(self, nom):
        """Recupere une variable de l'exercice et refuse qu'elle soit restee a None."""
        self.assertTrue(
            hasattr(self.ex, nom),
            f"La variable '{nom}' n'existe pas. L'as-tu supprimee ou mal orthographiee ?",
        )
        valeur = getattr(self.ex, nom)
        self.assertIsNotNone(valeur, f"La variable '{nom}' est encore a None : reponds a la question.")
        return valeur

    def verifier_choix(self, nom, attendu):
        reponse = self.valeur(nom)
        self.assertIsInstance(reponse, str, f"'{nom}' doit etre une chaine, ex. \"B\".")
        self.assertEqual(
            reponse.strip().upper(), attendu, f"Mauvaise reponse pour {nom.replace('reponse_', '').upper()}."
        )


class PartieA(BaseExercice1):
    """Partie A - Questions a choix multiple."""

    def test_a1_nombre_instructions(self):
        self.verifier_choix("reponse_a1", "C")

    def test_a2_sensibilite_casse(self):
        self.verifier_choix("reponse_a2", "B")

    def test_a3_nom_de_variable(self):
        self.verifier_choix("reponse_a3", "C")

    def test_a4_nom_de_constante(self):
        self.verifier_choix("reponse_a4", "B")

    def test_a5_type_de_true(self):
        self.verifier_choix("reponse_a5", "C")

    def test_a6_type_de_3_point_0(self):
        self.verifier_choix("reponse_a6", "B")


class PartieB(BaseExercice1):
    """Partie B - Constantes."""

    def test_b1_nom_cegep(self):
        valeur = self.valeur("NOM_CEGEP")
        self.assertIsInstance(valeur, str, "NOM_CEGEP doit etre une chaine de caracteres (str).")
        self.assertEqual(valeur, "Cegep de Trois-Rivieres")

    def test_b2_nombre_credits(self):
        valeur = self.valeur("NOMBRE_CREDITS_PROGRAMME")
        self.assertIsInstance(valeur, int, "NOMBRE_CREDITS_PROGRAMME doit etre un entier (int).")
        self.assertEqual(valeur, 90)

    def test_b3_cout_par_credit(self):
        valeur = self.valeur("COUT_PAR_CREDIT")
        self.assertIsInstance(valeur, float, "COUT_PAR_CREDIT doit etre un float (ex. 2.75, pas 2).")
        self.assertAlmostEqual(valeur, 2.75, places=6)


class PartieC(BaseExercice1):
    """Partie C - Variables et calculs."""

    def test_c1_prenom(self):
        valeur = self.valeur("prenom")
        self.assertIsInstance(valeur, str, "prenom doit etre une chaine (str).")
        self.assertGreaterEqual(len(valeur.strip()), 2, "prenom doit contenir au moins 2 caracteres.")

    def test_c1_nom_famille(self):
        valeur = self.valeur("nom_famille")
        self.assertIsInstance(valeur, str, "nom_famille doit etre une chaine (str).")
        self.assertGreaterEqual(len(valeur.strip()), 2, "nom_famille doit contenir au moins 2 caracteres.")

    def test_c1_age(self):
        valeur = self.valeur("age")
        self.assertIsInstance(valeur, int, "age doit etre un entier (int), pas un float ni une chaine.")
        self.assertFalse(isinstance(valeur, bool), "age doit etre un int, pas un bool.")
        self.assertGreater(valeur, 0, "age doit etre strictement positif.")

    def test_c1_moyenne_generale(self):
        valeur = self.valeur("moyenne_generale")
        self.assertIsInstance(valeur, float, "moyenne_generale doit etre un float (ex. 85.0, pas 85).")
        self.assertGreaterEqual(valeur, 0.0)
        self.assertLessEqual(valeur, 100.0, "moyenne_generale doit etre entre 0.0 et 100.0.")

    def test_c1_est_inscrit(self):
        valeur = self.valeur("est_inscrit")
        self.assertIsInstance(valeur, bool, "est_inscrit doit etre un bool (True ou False, avec majuscule).")

    def test_c2_nom_complet(self):
        attendu = f"{self.valeur('prenom')} {self.valeur('nom_famille')}"
        self.assertEqual(
            self.valeur("nom_complet"),
            attendu,
            "nom_complet doit valoir le prenom, un espace, puis le nom de famille.",
        )

    def test_c3_cout_total(self):
        attendu = self.valeur("NOMBRE_CREDITS_PROGRAMME") * self.valeur("COUT_PAR_CREDIT")
        self.assertAlmostEqual(
            self.valeur("cout_total_programme"),
            attendu,
            places=6,
            msg="cout_total_programme doit valoir NOMBRE_CREDITS_PROGRAMME * COUT_PAR_CREDIT (247.5).",
        )


class PartieD(BaseExercice1):
    """Partie D - Affichage."""

    def test_d1_affiche_cegep(self):
        self.assertIn(
            str(self.valeur("NOM_CEGEP")), self.sortie, "L'affichage doit contenir le nom du cegep."
        )

    def test_d2_affiche_nom_complet(self):
        self.assertIn(
            str(self.valeur("nom_complet")), self.sortie, "L'affichage doit contenir le nom complet."
        )

    def test_d3_affiche_cout_total(self):
        self.assertIn(
            str(self.valeur("cout_total_programme")),
            self.sortie,
            "L'affichage doit contenir le cout total du programme.",
        )

    def test_d4_affiche_les_trois_types(self):
        for attendu in ("<class 'int'>", "<class 'float'>", "<class 'bool'>"):
            self.assertIn(
                attendu, self.sortie, f"L'affichage doit contenir {attendu} (utilise la fonction type())."
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
