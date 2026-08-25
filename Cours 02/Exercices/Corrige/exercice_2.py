# =============================================================
# CORRIGE - Exercice 2 - Operateurs et lecture des erreurs
# Sections 2.4 a 2.6
# =============================================================


# -------------------------------------------------------------
# PARTIE A - Predire le resultat
# -------------------------------------------------------------

# A1) / est une division REELLE : retourne toujours un float.
reponse_a1 = 3.4

# A2) // tronque la partie decimale.
reponse_a2 = 3

# A3) Reste de la division : 5 x 3 = 15, il reste 2.
reponse_a3 = 2

# A4) Piege : // tronque vers le BAS, pas vers zero.
#     -17 / 5 = -3.4  ->  l'entier inferieur est -4.
reponse_a4 = -4

# A5) Meme quand la division tombe juste, / donne un float.
reponse_a5 = 5.0

# A6) Corollaire de A5.
reponse_a6 = "float"


# -------------------------------------------------------------
# PARTIE B - Affectation combinee
# -------------------------------------------------------------

# x = 5
reponse_b1 = 8   # x += 3   ->  5 + 3
reponse_b2 = 16  # x *= 2   ->  8 * 2
reponse_b3 = 5   # x //= 3  ->  16 // 3, division ENTIERE
reponse_b4 = 1   # x %= 4   ->  5 % 4

# B5) Piege de la section 2.5 : /= est une division REELLE.
#     7 / 7 donne le float 1.0, pas l'entier 1.
reponse_b5 = 1.0


# -------------------------------------------------------------
# PARTIE C1 - Convertir des secondes
# -------------------------------------------------------------

DUREE_TOTALE_SECONDES = 10000
SECONDES_PAR_MINUTE = 60
MINUTES_PAR_HEURE = 60
SECONDES_PAR_HEURE = SECONDES_PAR_MINUTE * MINUTES_PAR_HEURE

# 10000 // 3600 = 2
nb_heures = DUREE_TOTALE_SECONDES // SECONDES_PAR_HEURE

# On isole le reste apres les heures (10000 % 3600 = 2800),
# puis on le convertit en minutes (2800 // 60 = 46).
nb_minutes = (DUREE_TOTALE_SECONDES % SECONDES_PAR_HEURE) // SECONDES_PAR_MINUTE

# 10000 % 60 = 40
nb_secondes = DUREE_TOTALE_SECONDES % SECONDES_PAR_MINUTE


# -------------------------------------------------------------
# PARTIE C2 - Calculer une facture
# -------------------------------------------------------------

PRIX_UNITAIRE = 24.99
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

quantite = 3

sous_total = PRIX_UNITAIRE * quantite          # 74.97
montant_tps = sous_total * TAUX_TPS            # 3.7485
montant_tvq = sous_total * TAUX_TVQ            # 7.4782575
total_facture = sous_total + montant_tps + montant_tvq  # 86.1967575

# Note : les deux taxes se calculent sur le SOUS-TOTAL, jamais l'une sur l'autre.


# -------------------------------------------------------------
# PARTIE D - Afficher les resultats
# -------------------------------------------------------------

print(f"{nb_heures} h {nb_minutes} min {nb_secondes} s")
print(f"Total : {total_facture} $")


# -------------------------------------------------------------
# PARTIE E - Deboguer
# -------------------------------------------------------------

# E1) La 1re erreur est un guillemet non ferme : unterminated string literal.
reponse_e1 = "SyntaxError"

# E2) Le bloc 3 contient un print decale sans bloc ouvert.
reponse_e2 = 3

# E3) Python signale la ligne ou il DETECTE le probleme, pas toujours la
#     ligne fautive (cas typique de la parenthese non fermee).
reponse_e3 = False

# E4) debut, prix moyen, nb articles, prix total, paquets, restants, verification
reponse_e4 = 7
