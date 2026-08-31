# =============================================================
# CORRIGE - Exercice 1 - Structure, variables et constantes
# Sections 2.1 a 2.3
# =============================================================


# -------------------------------------------------------------
# PARTIE A - Questions a choix multiple
# -------------------------------------------------------------

# A1) x = 10; y = 20  ->  2 instructions, + print(x + y)  ->  3 au total.
#     Le point-virgule separe des instructions; il n'en supprime pas.
reponse_a1 = "C"

# A2) Python est sensible a la casse : Print n'est pas print.
reponse_a2 = "B"

# A3) snake_case : minuscules et soulignements. (D est invalide : un nom
#     ne peut pas commencer par un chiffre.)
reponse_a3 = "C"

# A4) Une constante s'ecrit en SCREAMING_SNAKE_CASE.
reponse_a4 = "B"

# A5) True et False sont de type bool.
reponse_a5 = "C"

# A6) 3.0 est un float, meme si la partie decimale est nulle.
reponse_a6 = "B"


# -------------------------------------------------------------
# PARTIE B - Declarer des constantes
# -------------------------------------------------------------

NOM_CEGEP = "Cegep de Trois-Rivieres"
NOMBRE_CREDITS_PROGRAMME = 90
COUT_PAR_CREDIT = 2.75  # le .75 impose le type float


# -------------------------------------------------------------
# PARTIE C - Declarer des variables et calculer
# -------------------------------------------------------------

# C1) Les valeurs sont libres; seuls les TYPES sont imposes.
prenom = "Alex"
nom_famille = "Tremblay"
age = 18
moyenne_generale = 85.5  # float : 85 serait refuse
est_inscrit = True       # bool : "True" (chaine) serait refuse

# C2) f-string : un seul espace entre le prenom et le nom.
nom_complet = f"{prenom} {nom_famille}"

# C3) On passe par les CONSTANTES, jamais par leurs valeurs en dur.
#     90 * 2.75 = 247.5
cout_total_programme = NOMBRE_CREDITS_PROGRAMME * COUT_PAR_CREDIT


# -------------------------------------------------------------
# PARTIE D - Afficher les resultats
# -------------------------------------------------------------

# D1) print() accepte plusieurs arguments separes par des virgules.
print("Cegep :", NOM_CEGEP)

# D2) Ici on demande explicitement un f-string.
print(f"Etudiant : {nom_complet}")

# D3) Le " $" suit la valeur.
print(f"Cout total : {cout_total_programme} $")

# D4) type() retourne <class 'int'>, <class 'float'>, <class 'bool'>.
print(type(age))
print(type(moyenne_generale))
print(type(est_inscrit))
