# =============================================================
# Exercice 1 - Structure, variables et constantes (sections 2.1 a 2.3)
#
# Auteur : (inscris ton nom ici)
# Date   : (inscris la date ici, format aaaa/mm/jj)
# Sujet  : Exercice 1 du cours 02
#
# CONSIGNE : remplace chaque None par ta reponse.
#            Ne change PAS les noms de variables : les tests s'en servent.
#            Verifie ton travail avec :  python -m unittest test_exercice_1.py
# =============================================================


# -------------------------------------------------------------
# PARTIE A - Questions a choix multiple                (15 min)
# -------------------------------------------------------------
# Reponds avec la lettre de ton choix, entre guillemets.
# Exemple :  reponse_a1 = "B"

# A1) Combien d'INSTRUCTIONS contient ce code ?
#         x = 10; y = 20
#         print(x + y)
#     A) 1     B) 2     C) 3     D) 4
reponse_a1 = None

# A2) Pourquoi Print("Bonjour") ne fonctionne-t-il pas ?
#     A) La fonction print() n'existe pas en Python
#     B) Python est sensible a la casse
#     C) Il manque un point-virgule a la fin
#     D) La chaine de caracteres est mal fermee
reponse_a2 = None

# A3) Quel nom de VARIABLE respecte la convention PEP 8 ?
#     A) nbEtudiants     B) NbEtudiants     C) nb_etudiants     D) 2_etudiants
reponse_a3 = None

# A4) Quel nom convient a une CONSTANTE ?
#     A) taux_tps        B) TAUX_TPS        C) TauxTps          D) tauxTPS
reponse_a4 = None

# A5) Quel est le type de la valeur True ?
#     A) str             B) int             C) bool             D) float
reponse_a5 = None

# A6) Que retourne type(3.0) ?
#     A) <class 'int'>   B) <class 'float'> C) <class 'str'>    D) une erreur
reponse_a6 = None


# -------------------------------------------------------------
# PARTIE B - Declarer des constantes                   (10 min)
# -------------------------------------------------------------
# Declare les trois constantes ci-dessous en respectant la convention
# vue a la section 2.3 (SCREAMING_SNAKE_CASE) et le type demande.

# B1) Le nom de ton college, une chaine de caracteres (str).
#     Valeur exacte attendue : Cegep de Trois-Rivieres
NOM_CEGEP = None

# B2) Le nombre de credits du programme, un entier (int).
#     Valeur attendue : 90
NOMBRE_CREDITS_PROGRAMME = None

# B3) Le cout d'un credit, un nombre a virgule (float).
#     Valeur attendue : 2.75
COUT_PAR_CREDIT = None


# -------------------------------------------------------------
# PARTIE C - Declarer des variables et calculer         (20 min)
# -------------------------------------------------------------
# C1) Cree cinq variables decrivant un etudiant.
#     Les VALEURS sont libres (mets les tiennes!), mais le TYPE est impose.

prenom = None            # str, au moins 2 caracteres
nom_famille = None       # str, au moins 2 caracteres
age = None               # int, strictement positif
moyenne_generale = None  # float, entre 0.0 et 100.0
est_inscrit = None       # bool (True ou False)

# C2) Construis le nom complet a l'aide d'un f-string : "prenom nom_famille"
#     (un seul espace entre les deux)
nom_complet = None

# C3) Calcule le cout total du programme.
#     Utilise les CONSTANTES de la partie B, jamais leurs valeurs directement.
cout_total_programme = None


# -------------------------------------------------------------
# PARTIE D - Afficher les resultats                    (15 min)
# -------------------------------------------------------------
# Complete les appels a print() ci-dessous.
# Chaque ligne affichee doit contenir la valeur demandee.

# D1) Affiche le nom du cegep, precede de "Cegep : "
print("Cegep :", NOM_CEGEP)

# D2) Affiche le nom complet de l'etudiant, precede de "Etudiant : "
#     Utilise un f-string.
# print(...)

# D3) Affiche le cout total du programme, precede de "Cout total : "
#     et suivi de " $"
# print(...)

# D4) Affiche le TYPE de chacune des variables age, moyenne_generale
#     et est_inscrit, en utilisant la fonction native type().
# print(...)
# print(...)
# print(...)
