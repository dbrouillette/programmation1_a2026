# =============================================================
# Tests de correction de l'exercice 2 - NE PAS MODIFIER CE FICHIER
#
# Utilisation :  python -m unittest test_exercice_2.py
#           ou :  python -m unittest -v test_exercice_2.py   (mode detaille)
# =============================================================

import io
import importlib.util
import contextlib
import pathlib
import unittest

DOSSIER = pathlib.Path(__file__).parent


def charger(nom_fichier, nom_module):
    """Execute un fichier de l'exercice et retourne (module, texte affiche)."""
    chemin = DOSSIER / nom_fichier
    if not chemin.exists():
        raise unittest.SkipTest(f"Fichier introuvable : {nom_fichier}")

    spec = importlib.util.spec_from_file_location(nom_module, chemin)
    module = importlib.util.module_from_spec(spec)
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        spec.loader.exec_module(module)
    return module, sortie.getvalue()


class BaseExercice2(unittest.TestCase):
    FICHIER = "exercice_2.py"
    MODULE = "exercice_2"

    @classmethod
    def setUpClass(cls):
        try:
            cls.ex, cls.sortie = charger(cls.FICHIER, cls.MODULE)
        except SyntaxError as err:
            raise AssertionError(
                f"Erreur de syntaxe dans {cls.FICHIER} a la ligne {err.lineno} : {err.msg}"
            ) from None

    def valeur(self, nom):
        self.assertTrue(
            hasattr(self.ex, nom),
            f"La variable '{nom}' n'existe pas. L'as-tu supprimee ou mal orthographiee ?",
        )
        valeur = getattr(self.ex, nom)
        self.assertIsNotNone(valeur, f"La variable '{nom}' est encore a None : reponds a la question.")
        return valeur

    def verifier_nombre(self, nom, attendu):
        """Verifie la valeur ET le type (5 et 5.0 ne sont pas equivalents)."""
        obtenu = self.valeur(nom)
        self.assertIsInstance(obtenu, (int, float), f"'{nom}' doit etre un nombre.")
        self.assertIs(
            type(obtenu),
            type(attendu),
            f"'{nom}' : mauvais type. Attendu {type(attendu).__name__}, "
            f"obtenu {type(obtenu).__name__}. Revois la difference entre / et //.",
        )
        self.assertAlmostEqual(obtenu, attendu, places=6, msg=f"'{nom}' : mauvaise valeur.")


class PartieA(BaseExercice2):
    """Partie A - Predire le resultat des operateurs arithmetiques."""

    def test_a1_division_reelle(self):
        self.verifier_nombre("reponse_a1", 3.4)

    def test_a2_division_entiere(self):
        self.verifier_nombre("reponse_a2", 3)

    def test_a3_modulo(self):
        self.verifier_nombre("reponse_a3", 2)

    def test_a4_division_entiere_negative(self):
        self.verifier_nombre("reponse_a4", -4)

    def test_a5_division_exacte_donne_un_float(self):
        self.verifier_nombre("reponse_a5", 5.0)

    def test_a6_type_du_resultat(self):
        reponse = self.valeur("reponse_a6")
        self.assertIsInstance(reponse, str, "reponse_a6 doit etre une chaine : \"int\" ou \"float\".")
        self.assertEqual(
            reponse.strip().lower(),
            "float",
            "En Python, / retourne toujours un float, meme quand la division tombe juste.",
        )


class PartieB(BaseExercice2):
    """Partie B - Affectation combinee."""

    def test_b1_plus_egal(self):
        self.verifier_nombre("reponse_b1", 8)

    def test_b2_fois_egal(self):
        self.verifier_nombre("reponse_b2", 16)

    def test_b3_division_entiere_egal(self):
        self.verifier_nombre("reponse_b3", 5)

    def test_b4_modulo_egal(self):
        self.verifier_nombre("reponse_b4", 1)

    def test_b5_division_egal_donne_un_float(self):
        self.verifier_nombre("reponse_b5", 1.0)


class PartieC(BaseExercice2):
    """Partie C - Conversion de duree et calcul de facture."""

    def test_c1_heures(self):
        self.verifier_nombre("nb_heures", 2)

    def test_c1_minutes(self):
        self.verifier_nombre("nb_minutes", 46)

    def test_c1_secondes(self):
        self.verifier_nombre("nb_secondes", 40)

    def test_c1_coherence_de_la_conversion(self):
        total = (
            self.valeur("nb_heures") * 3600
            + self.valeur("nb_minutes") * 60
            + self.valeur("nb_secondes")
        )
        self.assertEqual(
            total,
            self.valeur("DUREE_TOTALE_SECONDES"),
            "La somme heures + minutes + secondes doit redonner la duree de depart.",
        )

    def test_c2_sous_total(self):
        attendu = self.valeur("PRIX_UNITAIRE") * self.valeur("quantite")
        self.assertAlmostEqual(self.valeur("sous_total"), attendu, places=6)

    def test_c2_montant_tps(self):
        attendu = self.valeur("sous_total") * self.valeur("TAUX_TPS")
        self.assertAlmostEqual(self.valeur("montant_tps"), attendu, places=6)

    def test_c2_montant_tvq(self):
        attendu = self.valeur("sous_total") * self.valeur("TAUX_TVQ")
        self.assertAlmostEqual(self.valeur("montant_tvq"), attendu, places=6)

    def test_c2_total_facture(self):
        attendu = self.valeur("sous_total") + self.valeur("montant_tps") + self.valeur("montant_tvq")
        self.assertAlmostEqual(
            self.valeur("total_facture"),
            attendu,
            places=6,
            msg="total_facture doit valoir le sous-total plus les deux taxes (86.1967575).",
        )


class PartieD(BaseExercice2):
    """Partie D - Affichage."""

    def test_d1_affiche_la_duree(self):
        for valeur in ("nb_heures", "nb_minutes", "nb_secondes"):
            self.assertIn(
                str(self.valeur(valeur)),
                self.sortie,
                f"L'affichage doit contenir {valeur} (attendu : 2 h 46 min 40 s).",
            )

    def test_d2_affiche_le_total(self):
        self.assertIn(
            str(self.valeur("total_facture")),
            self.sortie,
            "L'affichage doit contenir le total de la facture.",
        )


class PartieE(BaseExercice2):
    """Partie E - Debogage du fichier exercice_2_debogage.py."""

    def test_e0_le_fichier_corrige_s_execute(self):
        try:
            module, sortie = charger("exercice_2_debogage.py", "exercice_2_debogage")
        except SyntaxError as err:
            raise AssertionError(
                f"Il reste une erreur de syntaxe dans exercice_2_debogage.py "
                f"a la ligne {err.lineno} : {err.msg}"
            ) from None
        self.assertEqual(module.nb_paquets, 2, "nb_paquets devrait valoir 2 apres correction.")
        self.assertEqual(module.articles_restants, 2, "articles_restants devrait valoir 2.")
        self.assertEqual(
            module.total_verification,
            12,
            "total_verification devrait valoir 12 : ne modifie pas les calculs, seulement la syntaxe.",
        )
        self.assertEqual(
            len(sortie.strip().splitlines()),
            7,
            "Le programme corrige doit afficher exactement 7 lignes.",
        )

    def test_e1_type_de_la_premiere_erreur(self):
        reponse = self.valeur("reponse_e1")
        self.assertIsInstance(reponse, str, "reponse_e1 doit etre une chaine de caracteres.")
        self.assertEqual(
            reponse.strip(),
            "SyntaxError",
            "La premiere erreur est un guillemet non ferme : unterminated string literal.",
        )

    def test_e2_bloc_avec_indentation(self):
        self.verifier_nombre("reponse_e2", 3)

    def test_e3_ligne_exacte(self):
        reponse = self.valeur("reponse_e3")
        self.assertIsInstance(reponse, bool, "reponse_e3 doit etre True ou False.")
        self.assertFalse(
            reponse,
            "Faux : Python signale la ligne ou il DETECTE le probleme, "
            "qui peut suivre la ligne reellement fautive.",
        )

    def test_e4_nombre_de_lignes_affichees(self):
        self.verifier_nombre("reponse_e4", 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
