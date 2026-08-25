# =============================================================
# Exercice 2 - Operateurs et lecture des erreurs (sections 2.4 a 2.6)
#
# Auteur : (inscris ton nom ici)
# Date   : (inscris la date ici, format aaaa/mm/jj)
# Sujet  : Exercice 2 du cours 02
#
# CONSIGNE : remplace chaque None par ta reponse.
#            Ne change PAS les noms de variables : les tests s'en servent.
#            Verifie ton travail avec :  python -m unittest test_exercice_2.py
# =============================================================


# -------------------------------------------------------------
# PARTIE A - Predire le resultat                       (15 min)
# -------------------------------------------------------------
# Ecris la VALEUR exacte que Python produirait. Attention au type :
# 5 et 5.0 ne sont PAS la meme reponse.
# Fais l'exercice de tete AVANT de verifier dans Python.

# A1) 17 / 5
reponse_a1 = None

# A2) 17 // 5
reponse_a2 = None

# A3) 17 % 5
reponse_a3 = None

# A4) -17 // 5   (attention : la troncature se fait vers le bas)
reponse_a4 = None

# A5) 10 / 2
reponse_a5 = None

# A6) Le type du resultat de 10 / 2, sous forme de chaine : "int" ou "float"
reponse_a6 = None


# -------------------------------------------------------------
# PARTIE B - Affectation combinee                      (10 min)
# -------------------------------------------------------------
# On part de x = 5, puis on applique les operations dans l'ordre.
# Indique la valeur de x APRES chaque ligne.
#
#     x = 5
#     x += 3     -> B1
#     x *= 2     -> B2
#     x //= 3    -> B3
#     x %= 4     -> B4

reponse_b1 = None
reponse_b2 = None
reponse_b3 = None
reponse_b4 = None

# B5) On part de y = 7, puis on applique  y /= 7
#     Quelle est la valeur de y ? (attention au type!)
reponse_b5 = None


# -------------------------------------------------------------
# PARTIE C1 - Convertir des secondes                   (10 min)
# -------------------------------------------------------------
# En utilisant UNIQUEMENT la division entiere (//) et le modulo (%),
# decompose la duree ci-dessous en heures, minutes et secondes.
# N'ecris aucun nombre "en dur" : utilise les constantes.

DUREE_TOTALE_SECONDES = 10000
SECONDES_PAR_MINUTE = 60
MINUTES_PAR_HEURE = 60
SECONDES_PAR_HEURE = SECONDES_PAR_MINUTE * MINUTES_PAR_HEURE

nb_heures = None    # int
nb_minutes = None   # int, entre 0 et 59
nb_secondes = None  # int, entre 0 et 59


# -------------------------------------------------------------
# PARTIE C2 - Calculer une facture                     (15 min)
# -------------------------------------------------------------
# Calcule la facture a partir des constantes fournies.
# Utilise toujours les CONSTANTES, jamais leurs valeurs directement.

PRIX_UNITAIRE = 24.99
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

quantite = 3

sous_total = None    # prix unitaire * quantite
montant_tps = None   # sous-total * taux de TPS
montant_tvq = None   # sous-total * taux de TVQ
total_facture = None # sous-total + les deux taxes


# -------------------------------------------------------------
# PARTIE D - Afficher les resultats                    (10 min)
# -------------------------------------------------------------
# Utilise des f-strings (section 2.2).

# D1) Affiche la duree sous la forme :  2 h 46 min 40 s
# print(...)

# D2) Affiche le total de la facture, suivi de " $"
# print(...)


# -------------------------------------------------------------
# PARTIE E - Deboguer                                  (15 min)
# -------------------------------------------------------------
# Ouvre le fichier exercice_2_debogage.py : il contient 6 erreurs de
# syntaxe. Corrige-les en te servant de la methode de la section 2.6.
#
# Corrige le fichier, puis reponds aux questions suivantes.

# E1) De quel TYPE est la toute premiere erreur signalee par Python ?
#     Reponds par "SyntaxError" ou "IndentationError".
reponse_e1 = None

# E2) Parmi les 6 blocs numerotes du fichier, lequel produit une
#     IndentationError ? Reponds par le numero du bloc (un entier).
reponse_e2 = None

# E3) Vrai ou faux : Python signale toujours la ligne exacte de la faute.
#     Reponds par True ou False.
reponse_e3 = None

# E4) Combien de lignes le programme corrige affiche-t-il au total ?
#     Reponds par un entier.
reponse_e4 = None
