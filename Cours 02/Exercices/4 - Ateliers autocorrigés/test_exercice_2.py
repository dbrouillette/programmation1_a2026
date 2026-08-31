# =============================================================
# Tests de correction de l'exercice 2 - NE PAS MODIFIER CE FICHIER
#
# Chaque test qui echoue AFFICHE L'EXPLICATION de la bonne reponse :
# les messages d'erreur tiennent lieu de corrige.
#
# Utilisation :  python -m unittest test_exercice_2.py
#           ou :  python -m unittest -v test_exercice_2.py   (mode detaille)
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

DOSSIER = pathlib.Path(__file__).parent


def explication(titre, texte, section):
    """Met en forme un message d'echec qui explique la bonne reponse."""
    return (
        f"\n\n>>> {titre}\n"
        f">>> {texte}\n"
        f">>> (revois la section {section})\n"
    )


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


def ligne_fautive(err, nom_fichier):
    """Retrouve le numero de ligne de l'erreur DANS le fichier de l'etudiant."""
    for cadre in reversed(traceback.extract_tb(err.__traceback__)):
        if pathlib.Path(cadre.filename).name == nom_fichier:
            return cadre.lineno
    return None


_ETAT = {}
FICHIER_EXERCICE = "exercice_2.py"


def setUpModule():
    """Charge le fichier UNE SEULE FOIS pour toute la suite.

    Si le chargement echoue, l'explication est affichee une seule fois
    plutot qu'une fois par classe de test.
    """
    try:
        _ETAT["module"], _ETAT["sortie"] = charger(FICHIER_EXERCICE, "exercice_2")
    except SyntaxError as err:
        raise AssertionError(
            f"\n\n>>> ERREUR DE SYNTAXE dans {FICHIER_EXERCICE}, ligne {err.lineno} : {err.msg}\n"
            f">>> Python n'a meme pas pu demarrer le fichier : aucune ligne ne s'est executee.\n"
            f">>> Corrige cette erreur, puis relance les tests (section 2.6).\n"
        ) from None
    except Exception as err:
        ligne = ligne_fautive(err, FICHIER_EXERCICE)
        emplacement = f", ligne {ligne}" if ligne else ""
        raise AssertionError(
            f"\n\n>>> Le fichier {FICHIER_EXERCICE} s'interrompt en cours d'execution{emplacement}.\n"
            f">>> {type(err).__name__} : {err}\n"
            f">>> C'est une erreur d'EXECUTION : le programme a demarre, puis a plante.\n"
            f">>> Corrige cette ligne, puis relance les tests.\n"
        ) from None


class BaseExercice2(unittest.TestCase):
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

    def verifier_nombre(self, nom, attendu, titre, texte, section):
        """Verifie la valeur ET le type (5 et 5.0 ne sont pas equivalents)."""
        obtenu = self.valeur(nom)
        message = explication(titre, texte, section)
        self.assertIsInstance(obtenu, (int, float), message)
        self.assertIs(
            type(obtenu),
            type(attendu),
            explication(
                titre,
                f"{texte} Le TYPE compte : on attend un {type(attendu).__name__} "
                f"({attendu!r}), tu as fourni un {type(obtenu).__name__} ({obtenu!r}).",
                section,
            ),
        )
        self.assertAlmostEqual(obtenu, attendu, places=6, msg=message)


class PartieA(BaseExercice2):
    """Partie A - Predire le resultat des operateurs arithmetiques."""

    def test_a1_division_reelle(self):
        """A1 - 17 / 5"""
        self.verifier_nombre(
            "reponse_a1",
            3.4,
            "A1 - 17 / 5 vaut 3.4",
            "L'operateur / effectue une division REELLE et retourne TOUJOURS un float, "
            "meme entre deux entiers.",
            "2.4 - Le comportement de la division /",
        )

    def test_a2_division_entiere(self):
        """A2 - 17 // 5"""
        self.verifier_nombre(
            "reponse_a2",
            3,
            "A2 - 17 // 5 vaut 3",
            "L'operateur // effectue une division ENTIERE : la partie decimale est tronquee. "
            "17 divise par 5 donne 3.4, donc 3.",
            "2.4 - Le comportement de la division /",
        )

    def test_a3_modulo(self):
        """A3 - 17 % 5"""
        self.verifier_nombre(
            "reponse_a3",
            2,
            "A3 - 17 % 5 vaut 2",
            "Le modulo donne le RESTE de la division : 5 x 3 = 15, et il reste 2 pour "
            "atteindre 17.",
            "2.4 - Les operateurs arithmetiques",
        )

    def test_a4_division_entiere_negative(self):
        """A4 - -17 // 5"""
        self.verifier_nombre(
            "reponse_a4",
            -4,
            "A4 - -17 // 5 vaut -4",
            "C'est le piege classique : // tronque vers le BAS (vers l'infini negatif), "
            "pas vers zero. -17 / 5 donne -3.4, et l'entier immediatement INFERIEUR a -3.4 "
            "est -4, pas -3.",
            "2.4 - Remarques importantes",
        )

    def test_a5_division_exacte_donne_un_float(self):
        """A5 - 10 / 2"""
        self.verifier_nombre(
            "reponse_a5",
            5.0,
            "A5 - 10 / 2 vaut 5.0",
            "Meme quand la division tombe juste, / retourne un float. La reponse est donc "
            "5.0 et non 5.",
            "2.4 - Le comportement de la division /",
        )

    def test_a6_type_du_resultat(self):
        """A6 - Type de 10 / 2"""
        reponse = self.valeur("reponse_a6")
        message = explication(
            "A6 - Le type du resultat de 10 / 2 est float.",
            "L'operateur / retourne TOUJOURS un float, quels que soient les operandes. "
            "Pour obtenir un int, il faut l'operateur dedie // .",
            "2.4 - Le comportement de la division /",
        )
        self.assertIsInstance(reponse, str, message)
        self.assertEqual(reponse.strip().lower(), "float", message)


class PartieB(BaseExercice2):
    """Partie B - Affectation combinee."""

    def test_b1_plus_egal(self):
        """B1 - x += 3"""
        self.verifier_nombre(
            "reponse_b1",
            8,
            "B1 - Apres x += 3, x vaut 8",
            "x += 3 equivaut a x = x + 3. On part de 5, donc 5 + 3 = 8.",
            "2.5 - Liste des operateurs d'affectation combinee",
        )

    def test_b2_fois_egal(self):
        """B2 - x *= 2"""
        self.verifier_nombre(
            "reponse_b2",
            16,
            "B2 - Apres x *= 2, x vaut 16",
            "x *= 2 equivaut a x = x * 2. On part de la valeur precedente (8), donc 8 x 2 = 16.",
            "2.5 - Liste des operateurs d'affectation combinee",
        )

    def test_b3_division_entiere_egal(self):
        """B3 - x //= 3"""
        self.verifier_nombre(
            "reponse_b3",
            5,
            "B3 - Apres x //= 3, x vaut 5",
            "x //= 3 equivaut a x = x // 3, une division ENTIERE. 16 // 3 donne 5.33..., "
            "tronque a 5. Le resultat reste un int.",
            "2.5 - Liste des operateurs d'affectation combinee",
        )

    def test_b4_modulo_egal(self):
        """B4 - x %= 4"""
        self.verifier_nombre(
            "reponse_b4",
            1,
            "B4 - Apres x %= 4, x vaut 1",
            "x %= 4 equivaut a x = x % 4, le reste de la division. 5 % 4 : 4 entre une fois "
            "dans 5, et il reste 1.",
            "2.5 - Liste des operateurs d'affectation combinee",
        )

    def test_b5_division_egal_donne_un_float(self):
        """B5 - y /= 7"""
        self.verifier_nombre(
            "reponse_b5",
            1.0,
            "B5 - Apres y /= 7, y vaut 1.0",
            "C'est le piege de la section 2.5 : /= fait une division REELLE. Meme si 7 / 7 "
            "tombe juste, le resultat est le float 1.0, et non l'entier 1. Pour obtenir 1, "
            "il aurait fallu //= .",
            "2.5 - Attention a la ligne /=",
        )


class PartieC(BaseExercice2):
    """Partie C - Conversion de duree et calcul de facture."""

    def test_c1a_heures(self):
        """C1 - nb_heures"""
        self.verifier_nombre(
            "nb_heures",
            2,
            "C1 - nb_heures vaut 2",
            "Une heure compte 3600 secondes. Ecris "
            "nb_heures = DUREE_TOTALE_SECONDES // SECONDES_PAR_HEURE : "
            "10000 // 3600 donne 2.",
            "2.4 - Les operateurs arithmetiques",
        )

    def test_c1b_minutes(self):
        """C1 - nb_minutes"""
        self.verifier_nombre(
            "nb_minutes",
            46,
            "C1 - nb_minutes vaut 46",
            "Il faut d'abord isoler ce qui reste apres les heures completes avec %, puis le "
            "convertir en minutes avec // : "
            "nb_minutes = (DUREE_TOTALE_SECONDES % SECONDES_PAR_HEURE) // SECONDES_PAR_MINUTE. "
            "10000 % 3600 = 2800, et 2800 // 60 = 46.",
            "2.4 - Les operateurs arithmetiques",
        )

    def test_c1c_secondes(self):
        """C1 - nb_secondes"""
        self.verifier_nombre(
            "nb_secondes",
            40,
            "C1 - nb_secondes vaut 40",
            "Ce sont les secondes qui restent apres les minutes completes : "
            "nb_secondes = DUREE_TOTALE_SECONDES % SECONDES_PAR_MINUTE. "
            "10000 % 60 = 40.",
            "2.4 - Les operateurs arithmetiques",
        )

    def test_c1d_coherence(self):
        """C1 - Coherence de la conversion"""
        total = (
            self.valeur("nb_heures") * 3600
            + self.valeur("nb_minutes") * 60
            + self.valeur("nb_secondes")
        )
        self.assertEqual(
            total,
            self.valeur("DUREE_TOTALE_SECONDES"),
            explication(
                "C1 - La conversion est incoherente.",
                f"En recomposant tes trois valeurs on obtient {total} secondes, alors que la "
                f"duree de depart est {self.valeur('DUREE_TOTALE_SECONDES')}. La bonne "
                "decomposition de 10000 secondes est 2 h 46 min 40 s.",
                "2.4 - Les operateurs arithmetiques",
            ),
        )

    def test_c2a_sous_total(self):
        """C2 - sous_total"""
        attendu = self.valeur("PRIX_UNITAIRE") * self.valeur("quantite")
        self.assertAlmostEqual(
            self.valeur("sous_total"),
            attendu,
            places=6,
            msg=explication(
                f"C2 - 'sous_total' devrait valoir {attendu}.",
                "Ecris sous_total = PRIX_UNITAIRE * quantite, en passant par les constantes.",
                "2.3 - Bonnes pratiques",
            ),
        )

    def test_c2b_montant_tps(self):
        """C2 - montant_tps"""
        attendu = self.valeur("sous_total") * self.valeur("TAUX_TPS")
        self.assertAlmostEqual(
            self.valeur("montant_tps"),
            attendu,
            places=6,
            msg=explication(
                f"C2 - 'montant_tps' devrait valoir {attendu}.",
                "Ecris montant_tps = sous_total * TAUX_TPS. Le taux est deja exprime en "
                "decimal (0.05 = 5 %), donc il n'y a pas a diviser par 100.",
                "2.3 - Pourquoi utiliser une constante",
            ),
        )

    def test_c2c_montant_tvq(self):
        """C2 - montant_tvq"""
        attendu = self.valeur("sous_total") * self.valeur("TAUX_TVQ")
        self.assertAlmostEqual(
            self.valeur("montant_tvq"),
            attendu,
            places=6,
            msg=explication(
                f"C2 - 'montant_tvq' devrait valoir {attendu}.",
                "Ecris montant_tvq = sous_total * TAUX_TVQ. La TVQ se calcule sur le "
                "sous-total, pas sur le sous-total additionne de la TPS.",
                "2.3 - Pourquoi utiliser une constante",
            ),
        )

    def test_c2d_total_facture(self):
        """C2 - total_facture"""
        attendu = self.valeur("sous_total") + self.valeur("montant_tps") + self.valeur("montant_tvq")
        self.assertAlmostEqual(
            self.valeur("total_facture"),
            attendu,
            places=6,
            msg=explication(
                f"C2 - 'total_facture' devrait valoir {attendu}.",
                "Ecris total_facture = sous_total + montant_tps + montant_tvq. "
                "Ne recopie pas les montants a la main : reutilise les variables deja calculees.",
                "2.3 - Bonnes pratiques",
            ),
        )


class PartieD(BaseExercice2):
    """Partie D - Affichage."""

    def test_d1_affiche_la_duree(self):
        """D1 - Afficher la duree"""
        manquants = [
            nom for nom in ("nb_heures", "nb_minutes", "nb_secondes")
            if str(self.valeur(nom)) not in self.sortie
        ]
        self.assertFalse(
            manquants,
            explication(
                f"D1 - L'affichage ne contient pas : {', '.join(manquants)}",
                "Decommente la ligne et utilise un f-string : "
                "print(f\"{nb_heures} h {nb_minutes} min {nb_secondes} s\"). "
                "Le resultat attendu est : 2 h 46 min 40 s",
                "2.2 - Exemple pratique",
            ),
        )

    def test_d2_affiche_le_total(self):
        """D2 - Afficher le total"""
        self.assertIn(
            str(self.valeur("total_facture")),
            self.sortie,
            explication(
                "D2 - L'affichage doit contenir le total de la facture.",
                "Decommente la ligne et ecris : print(f\"Total : {total_facture} $\")",
                "2.2 - Exemple pratique",
            ),
        )


class PartieE(BaseExercice2):
    """Partie E - Debogage du fichier exercice_2_debogage.py."""

    def test_e0_le_fichier_corrige_s_execute(self):
        """E0 - Le fichier debogue s'execute"""
        try:
            module, sortie = charger("exercice_2_debogage.py", "exercice_2_debogage")
        except SyntaxError as err:
            raise AssertionError(
                f"\n\n>>> Il reste une ERREUR DE SYNTAXE dans exercice_2_debogage.py, "
                f"ligne {err.lineno} : {err.msg}\n"
                f">>> Applique la methode : lis la derniere ligne du message, repere le numero\n"
                f">>> de ligne et le curseur ^, et si la ligne semble correcte, verifie la\n"
                f">>> ligne PRECEDENTE. Corrige, relance, recommence.\n"
                f">>> Rappel des 6 corrections attendues :\n"
                f">>>   1. guillemet fermant manquant       -> print(\"Debut du programme\")\n"
                f">>>   2. parenthese fermante manquante    -> ... {{prix_moyen}} $\")\n"
                f">>>   3. indentation a supprimer          -> aligner le print a gauche\n"
                f">>>   4. virgule manquante                -> print(\"Prix total :\", PRIX_TOTAL)\n"
                f">>>   5. affectation inversee             -> articles_restants = NOMBRE_ARTICLES % ...\n"
                f">>>   6. operateur combine mal ecrit      -> total_verification *= ...\n"
            ) from None
        except Exception as err:
            ligne = ligne_fautive(err, "exercice_2_debogage.py")
            emplacement = f", ligne {ligne}" if ligne else ""
            raise AssertionError(
                f"\n\n>>> La syntaxe de exercice_2_debogage.py est maintenant correcte, mais le "
                f"programme s'interrompt en cours d'execution{emplacement}.\n"
                f">>> {type(err).__name__} : {err}\n"
                f">>> C'est une erreur d'EXECUTION, pas de syntaxe : le programme a demarre.\n"
                f">>> Verifie que tu n'as pas renomme une variable en corrigeant la syntaxe.\n"
            ) from None

        self.assertEqual(
            module.nb_paquets,
            2,
            explication(
                "E0 - 'nb_paquets' devrait valoir 2.",
                "12 articles // 5 par paquet = 2 paquets complets. Tu as modifie un calcul : "
                "l'exercice demande de corriger UNIQUEMENT la syntaxe.",
                "2.6",
            ),
        )
        self.assertEqual(
            module.articles_restants,
            2,
            explication(
                "E0 - 'articles_restants' devrait valoir 2.",
                "12 % 5 = 2. L'erreur 5 se corrige en INVERSANT l'affectation "
                "(articles_restants = NOMBRE_ARTICLES % ARTICLES_PAR_PAQUET), sans changer "
                "le calcul lui-meme.",
                "2.6 - Une affectation impossible",
            ),
        )
        self.assertEqual(
            module.total_verification,
            12,
            explication(
                "E0 - 'total_verification' devrait valoir 12.",
                "2 paquets x 5 articles + 2 restants = 12, soit le nombre d'articles de depart. "
                "Ne modifie ni les valeurs ni les calculs, seulement la syntaxe.",
                "2.6",
            ),
        )
        self.assertEqual(
            len(sortie.strip().splitlines()),
            7,
            explication(
                "E0 - Le programme corrige doit afficher exactement 7 lignes.",
                "Tu as probablement supprime ou ajoute un appel a print() au lieu de corriger "
                "sa syntaxe.",
                "2.6",
            ),
        )

    def test_e1_type_de_la_premiere_erreur(self):
        """E1 - Type de la 1re erreur"""
        reponse = self.valeur("reponse_e1")
        message = explication(
            "E1 - La premiere erreur est de type SyntaxError.",
            "Il s'agit du guillemet fermant manquant a l'erreur 1 : Python signale "
            "'unterminated string literal'. Une chaine non terminee est une SyntaxError.",
            "2.6 - Un guillemet manquant",
        )
        self.assertIsInstance(reponse, str, message)
        self.assertEqual(reponse.strip(), "SyntaxError", message)

    def test_e2_bloc_avec_indentation(self):
        """E2 - Bloc en IndentationError"""
        self.verifier_nombre(
            "reponse_e2",
            3,
            "E2 - C'est le bloc numero 3 qui produit une IndentationError.",
            "Le print y est decale vers la droite sans raison. En Python l'indentation a un "
            "SENS : elle delimite les blocs. Une ligne indentee sans bloc ouvert declenche "
            "'IndentationError: unexpected indent'.",
            "2.6 - Une indentation inattendue",
        )

    def test_e3_ligne_exacte(self):
        """E3 - Ligne signalee"""
        reponse = self.valeur("reponse_e3")
        message = explication(
            "E3 - La reponse est False.",
            "Python signale la ligne ou il DETECTE le probleme, qui peut se situer apres la "
            "ligne reellement fautive. C'est typique de la parenthese non fermee : Python ne "
            "s'en rend compte qu'en lisant la suite. D'ou le reflexe : si la ligne signalee "
            "semble correcte, verifie la ligne PRECEDENTE.",
            "2.6 - La ligne signalee n'est pas toujours la ligne fautive",
        )
        self.assertIsInstance(reponse, bool, message)
        self.assertFalse(reponse, message)

    def test_e4_nombre_de_lignes_affichees(self):
        """E4 - Nombre de lignes affichees"""
        self.verifier_nombre(
            "reponse_e4",
            7,
            "E4 - Le programme corrige affiche 7 lignes.",
            "Compte les appels a print() une fois les 6 erreurs corrigees : debut, prix moyen, "
            "nombre d'articles, prix total, paquets complets, articles restants, verification.",
            "2.6",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
