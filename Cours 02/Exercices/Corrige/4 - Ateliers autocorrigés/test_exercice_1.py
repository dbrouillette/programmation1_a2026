# =============================================================
# Tests de correction de l'exercice 1 - NE PAS MODIFIER CE FICHIER
#
# Chaque test qui echoue AFFICHE L'EXPLICATION de la bonne reponse :
# les messages d'erreur tiennent lieu de corrige.
#
# Utilisation :  python -m unittest test_exercice_1.py
#           ou :  python -m unittest -v test_exercice_1.py   (mode detaille)
# =============================================================

import io
import importlib.util
import contextlib
import pathlib
import traceback
import unittest

# Masque les lignes internes de ce fichier dans les traces d'erreur,
# pour que seule l'explication de la bonne reponse reste visible.
__unittest = True

FICHIER = pathlib.Path(__file__).with_name("exercice_1.py")


def explication(titre, texte, section):
    """Met en forme un message d'echec qui explique la bonne reponse."""
    return (
        f"\n\n>>> {titre}\n"
        f">>> {texte}\n"
        f">>> (revois la section {section})\n"
    )


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


def ligne_fautive(err, nom_fichier):
    """Retrouve le numero de ligne de l'erreur DANS le fichier de l'etudiant."""
    for cadre in reversed(traceback.extract_tb(err.__traceback__)):
        if pathlib.Path(cadre.filename).name == nom_fichier:
            return cadre.lineno
    return None


_ETAT = {}


def setUpModule():
    """Charge le fichier UNE SEULE FOIS pour toute la suite.

    Si le chargement echoue, l'explication est affichee une seule fois
    plutot qu'une fois par classe de test.
    """
    try:
        _ETAT["module"], _ETAT["sortie"] = charger_exercice()
    except SyntaxError as err:
        raise AssertionError(
            f"\n\n>>> ERREUR DE SYNTAXE dans exercice_1.py, ligne {err.lineno} : {err.msg}\n"
            f">>> Python n'a meme pas pu demarrer le fichier : aucune ligne ne s'est executee.\n"
            f">>> Corrige cette erreur, puis relance les tests (section 2.6).\n"
        ) from None
    except Exception as err:
        ligne = ligne_fautive(err, "exercice_1.py")
        emplacement = f", ligne {ligne}" if ligne else ""
        raise AssertionError(
            f"\n\n>>> Le fichier exercice_1.py s'interrompt en cours d'execution{emplacement}.\n"
            f">>> {type(err).__name__} : {err}\n"
            f">>> C'est une erreur d'EXECUTION : le programme a demarre, puis a plante.\n"
            f">>> Corrige cette ligne, puis relance les tests.\n"
        ) from None


class BaseExercice1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ex = _ETAT["module"]
        cls.sortie = _ETAT["sortie"]

    def valeur(self, nom):
        self.assertTrue(
            hasattr(self.ex, nom),
            f"\n\n>>> La variable '{nom}' n'existe pas.\n"
            f">>> Tu l'as supprimee ou mal orthographiee. Les tests s'appuient sur ce nom exact.\n",
        )
        valeur = getattr(self.ex, nom)
        self.assertIsNotNone(
            valeur,
            f"\n\n>>> La variable '{nom}' vaut encore None : la question n'a pas ete repondue.\n",
        )
        return valeur

    def verifier_choix(self, nom, attendu, titre, texte, section):
        reponse = self.valeur(nom)
        self.assertIsInstance(
            reponse,
            str,
            explication(
                titre,
                f"Ta reponse doit etre la LETTRE du choix, entre guillemets : \"{attendu}\". "
                f"Tu as ecrit une valeur de type {type(reponse).__name__}.",
                section,
            ),
        )
        self.assertEqual(reponse.strip().upper(), attendu, explication(titre, texte, section))


class PartieA(BaseExercice1):
    """Partie A - Questions a choix multiple."""

    def test_a1_nombre_instructions(self):
        """A1 - Nombre d'instructions"""
        self.verifier_choix(
            "reponse_a1",
            "C",
            "A1 - La bonne reponse est C) 3 instructions.",
            "Le point-virgule SEPARE des instructions sur une meme ligne, il n'en supprime pas. "
            "'x = 10' et 'y = 20' comptent pour 2, et 'print(x + y)' pour une troisieme.",
            "2.1 - Instruction Python",
        )

    def test_a2_sensibilite_casse(self):
        """A2 - Sensibilite a la casse"""
        self.verifier_choix(
            "reponse_a2",
            "B",
            "A2 - La bonne reponse est B) Python est sensible a la casse.",
            "Pour Python, 'Print' et 'print' sont deux noms differents. La fonction native "
            "s'appelle 'print' en minuscules; 'Print' n'existe pas, d'ou une NameError.",
            "2.1 - Python est sensible a la casse",
        )

    def test_a3_nom_de_variable(self):
        """A3 - Nom de variable (snake_case)"""
        self.verifier_choix(
            "reponse_a3",
            "C",
            "A3 - La bonne reponse est C) nb_etudiants.",
            "La convention PEP 8 pour une variable est le snake_case : tout en minuscules, "
            "les mots separes par des soulignements. 'nbEtudiants' et 'NbEtudiants' sont d'autres "
            "conventions (camelCase et PascalCase), et '2_etudiants' est carrement invalide : "
            "un nom ne peut jamais commencer par un chiffre.",
            "2.2 - Nomenclature des variables",
        )

    def test_a4_nom_de_constante(self):
        """A4 - Nom de constante"""
        self.verifier_choix(
            "reponse_a4",
            "B",
            "A4 - La bonne reponse est B) TAUX_TPS.",
            "Une constante s'ecrit en SCREAMING_SNAKE_CASE : majuscules et soulignements. "
            "En Python c'est une CONVENTION, pas une protection : rien n'empeche techniquement "
            "de reaffecter la valeur, mais on ne le fait pas.",
            "2.3 - Nomenclature",
        )

    def test_a5_type_de_true(self):
        """A5 - Type de True"""
        self.verifier_choix(
            "reponse_a5",
            "C",
            "A5 - La bonne reponse est C) bool.",
            "True et False sont les deux seules valeurs du type bool. Attention a la majuscule : "
            "'true' en minuscules n'existe pas en Python.",
            "2.2 - Autres types de base",
        )

    def test_a6_type_de_3_point_0(self):
        """A6 - Type de 3.0"""
        self.verifier_choix(
            "reponse_a6",
            "B",
            "A6 - La bonne reponse est B) <class 'float'>.",
            "Des qu'un nombre s'ecrit avec un point decimal, c'est un float, meme si la partie "
            "decimale est nulle. 3 est un int, 3.0 est un float.",
            "2.2 - Types numeriques",
        )


class PartieB(BaseExercice1):
    """Partie B - Constantes."""

    def test_b1_nom_cegep(self):
        """B1 - NOM_CEGEP"""
        valeur = self.valeur("NOM_CEGEP")
        self.assertIsInstance(
            valeur,
            str,
            explication(
                "B1 - NOM_CEGEP doit etre une chaine de caracteres (str).",
                "Une chaine s'ecrit entre guillemets simples ou doubles : \"Cegep de Trois-Rivieres\".",
                "2.2 - Chaines de caracteres",
            ),
        )
        self.assertEqual(
            valeur,
            "Cegep de Trois-Rivieres",
            explication(
                "B1 - La valeur attendue est exactement : Cegep de Trois-Rivieres",
                "Recopie-la telle quelle, sans accent et sans espace en trop.",
                "2.3 - Exemples concrets",
            ),
        )

    def test_b2_nombre_credits(self):
        """B2 - NOMBRE_CREDITS_PROGRAMME"""
        valeur = self.valeur("NOMBRE_CREDITS_PROGRAMME")
        self.assertIsInstance(
            valeur,
            int,
            explication(
                "B2 - NOMBRE_CREDITS_PROGRAMME doit etre un entier (int).",
                "Un nombre de credits se compte : ecris 90, et non 90.0 (qui serait un float) "
                "ni \"90\" (qui serait une chaine).",
                "2.2 - Types numeriques",
            ),
        )
        self.assertEqual(
            valeur,
            90,
            explication("B2 - La valeur attendue est 90.", "Relis l'enonce du fichier.", "2.3"),
        )

    def test_b3_cout_par_credit(self):
        """B3 - COUT_PAR_CREDIT"""
        valeur = self.valeur("COUT_PAR_CREDIT")
        self.assertIsInstance(
            valeur,
            float,
            explication(
                "B3 - COUT_PAR_CREDIT doit etre un float.",
                "Un montant en dollars a des decimales : ecris 2.75. Si tu ecris 2, Python en "
                "fait un int, ce qui n'est pas le type demande.",
                "2.2 - Types numeriques",
            ),
        )
        self.assertAlmostEqual(
            valeur,
            2.75,
            places=6,
            msg=explication("B3 - La valeur attendue est 2.75.", "Relis l'enonce du fichier.", "2.3"),
        )


class PartieC(BaseExercice1):
    """Partie C - Variables et calculs."""

    def test_c1a_prenom(self):
        """C1 - prenom (str)"""
        valeur = self.valeur("prenom")
        self.assertIsInstance(
            valeur,
            str,
            explication(
                "C1 - 'prenom' doit etre une chaine de caracteres (str).",
                "Entoure ta valeur de guillemets : prenom = \"Alex\".",
                "2.2 - Chaines de caracteres",
            ),
        )
        self.assertGreaterEqual(
            len(valeur.strip()),
            2,
            explication(
                "C1 - 'prenom' doit contenir au moins 2 caracteres.",
                "Mets un vrai prenom, pas une chaine vide.",
                "2.2",
            ),
        )

    def test_c1b_nom_famille(self):
        """C1 - nom_famille (str)"""
        valeur = self.valeur("nom_famille")
        self.assertIsInstance(
            valeur,
            str,
            explication(
                "C1 - 'nom_famille' doit etre une chaine de caracteres (str).",
                "Entoure ta valeur de guillemets : nom_famille = \"Tremblay\".",
                "2.2 - Chaines de caracteres",
            ),
        )
        self.assertGreaterEqual(
            len(valeur.strip()),
            2,
            explication(
                "C1 - 'nom_famille' doit contenir au moins 2 caracteres.",
                "Mets un vrai nom, pas une chaine vide.",
                "2.2",
            ),
        )

    def test_c1c_age(self):
        """C1 - age (int)"""
        valeur = self.valeur("age")
        self.assertFalse(
            isinstance(valeur, bool),
            explication(
                "C1 - 'age' doit etre un int, pas un bool.",
                "Attention : en Python, True et False sont acceptes la ou un entier est attendu, "
                "mais ce n'est pas le type demande ici.",
                "2.2 - Autres types de base",
            ),
        )
        self.assertIsInstance(
            valeur,
            int,
            explication(
                "C1 - 'age' doit etre un entier (int).",
                "Un age se compte en annees entieres : ecris 18, et non 18.0 (float) ni \"18\" (str). "
                "Une valeur entre guillemets est une chaine, meme si elle ressemble a un nombre.",
                "2.2 - Types numeriques",
            ),
        )
        self.assertGreater(
            valeur,
            0,
            explication("C1 - 'age' doit etre strictement positif.", "Un age ne peut pas etre nul ou negatif.", "2.2"),
        )

    def test_c1d_moyenne_generale(self):
        """C1 - moyenne_generale (float)"""
        valeur = self.valeur("moyenne_generale")
        self.assertIsInstance(
            valeur,
            float,
            explication(
                "C1 - 'moyenne_generale' doit etre un float.",
                "Une moyenne comporte des decimales : ecris 85.5, ou 85.0 si elle tombe juste. "
                "85 tout court serait un int, ce qui n'est pas le type demande.",
                "2.2 - Types numeriques",
            ),
        )
        self.assertGreaterEqual(
            valeur,
            0.0,
            explication("C1 - 'moyenne_generale' doit etre entre 0.0 et 100.0.", "Ta valeur est negative.", "2.2"),
        )
        self.assertLessEqual(
            valeur,
            100.0,
            explication("C1 - 'moyenne_generale' doit etre entre 0.0 et 100.0.", "Ta valeur depasse 100.", "2.2"),
        )

    def test_c1e_est_inscrit(self):
        """C1 - est_inscrit (bool)"""
        valeur = self.valeur("est_inscrit")
        self.assertIsInstance(
            valeur,
            bool,
            explication(
                "C1 - 'est_inscrit' doit etre un bool.",
                "Ecris True ou False, SANS guillemets et AVEC la majuscule. "
                "\"True\" entre guillemets est une chaine de caracteres, pas un booleen.",
                "2.2 - Autres types de base",
            ),
        )

    def test_c2_nom_complet(self):
        """C2 - nom_complet (f-string)"""
        attendu = f"{self.valeur('prenom')} {self.valeur('nom_famille')}"
        self.assertEqual(
            self.valeur("nom_complet"),
            attendu,
            explication(
                f"C2 - 'nom_complet' devrait valoir : {attendu}",
                "Construis-le avec un f-string : nom_complet = f\"{prenom} {nom_famille}\". "
                "Le prefixe f devant le guillemet permet de remplacer {prenom} par la valeur de "
                "la variable. Il faut exactement un espace entre les deux.",
                "2.2 - Exemple pratique",
            ),
        )

    def test_c3_cout_total(self):
        """C3 - cout_total_programme"""
        credits = self.valeur("NOMBRE_CREDITS_PROGRAMME")
        cout = self.valeur("COUT_PAR_CREDIT")
        attendu = credits * cout
        self.assertAlmostEqual(
            self.valeur("cout_total_programme"),
            attendu,
            places=6,
            msg=explication(
                f"C3 - 'cout_total_programme' devrait valoir {attendu}.",
                "Ecris cout_total_programme = NOMBRE_CREDITS_PROGRAMME * COUT_PAR_CREDIT. "
                "Passe TOUJOURS par le nom des constantes, jamais par leurs valeurs recopiees : "
                "si le cout du credit change, un seul endroit est a modifier.",
                "2.3 - Bonnes pratiques",
            ),
        )


class PartieD(BaseExercice1):
    """Partie D - Affichage."""

    def test_d1_affiche_cegep(self):
        """D1 - Afficher le cegep"""
        self.assertIn(
            str(self.valeur("NOM_CEGEP")),
            self.sortie,
            explication(
                "D1 - L'affichage doit contenir le nom du cegep.",
                "print(\"Cegep :\", NOM_CEGEP) - print() accepte plusieurs arguments separes "
                "par des virgules et insere automatiquement un espace entre eux.",
                "2.2 - Exemple pratique",
            ),
        )

    def test_d2_affiche_nom_complet(self):
        """D2 - Afficher le nom complet"""
        self.assertIn(
            str(self.valeur("nom_complet")),
            self.sortie,
            explication(
                "D2 - L'affichage doit contenir le nom complet de l'etudiant.",
                "Decommente la ligne et ecris : print(f\"Etudiant : {nom_complet}\")",
                "2.2 - Exemple pratique",
            ),
        )

    def test_d3_affiche_cout_total(self):
        """D3 - Afficher le cout total"""
        self.assertIn(
            str(self.valeur("cout_total_programme")),
            self.sortie,
            explication(
                "D3 - L'affichage doit contenir le cout total du programme.",
                "Decommente la ligne et ecris : print(f\"Cout total : {cout_total_programme} $\")",
                "2.2 - Exemple pratique",
            ),
        )

    def test_d4_affiche_les_trois_types(self):
        """D4 - Afficher les trois types"""
        manquants = [
            attendu
            for attendu in ("<class 'int'>", "<class 'float'>", "<class 'bool'>")
            if attendu not in self.sortie
        ]
        self.assertFalse(
            manquants,
            explication(
                f"D4 - Il manque a l'affichage : {', '.join(manquants)}",
                "La fonction native type() retourne le type d'une valeur, sous la forme "
                "<class 'nom_du_type'>. Ecris print(type(age)), print(type(moyenne_generale)) "
                "et print(type(est_inscrit)). Si un type est incorrect, c'est la Partie C "
                "qu'il faut revoir.",
                "2.2 - La fonction native type()",
            ),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
