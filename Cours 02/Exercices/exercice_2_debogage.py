# =============================================================
# Exercice 2 - Partie E - Fichier a deboguer
#
# Ce programme contient 6 ERREURS DE SYNTAXE, une par bloc numerote.
# Python ne signale que la PREMIERE a chaque execution : corrige-la,
# relance le programme, et recommence jusqu'a ce qu'il s'execute.
#
# Methode (section 2.6) :
#   1. lire la derniere ligne du message (le type et la description)
#   2. reperer le numero de ligne
#   3. regarder le curseur ^
#   4. si la ligne semble correcte, verifier la ligne PRECEDENTE
#
# Ne change ni les noms de variables, ni les valeurs, ni les calculs :
# corrige UNIQUEMENT la syntaxe.
#
# Verifie ton travail avec :  python -m unittest test_exercice_2.py
# =============================================================

NOMBRE_ARTICLES = 12
PRIX_TOTAL = 149.40
ARTICLES_PAR_PAQUET = 5

# --- Erreur 1 ---
print("Debut du programme)

# --- Erreur 2 ---
prix_moyen = PRIX_TOTAL / NOMBRE_ARTICLES
print(f"Prix moyen : {prix_moyen} $"

# --- Erreur 3 ---
    print("Nombre d'articles :", NOMBRE_ARTICLES)

# --- Erreur 4 ---
print("Prix total :" PRIX_TOTAL)

# --- Erreur 5 ---
nb_paquets = NOMBRE_ARTICLES // ARTICLES_PAR_PAQUET
NOMBRE_ARTICLES % ARTICLES_PAR_PAQUET = articles_restants

# --- Erreur 6 ---
total_verification = nb_paquets
total_verification * = ARTICLES_PAR_PAQUET
total_verification += articles_restants

print(f"Paquets complets : {nb_paquets}")
print(f"Articles restants : {articles_restants}")
print(f"Verification : {total_verification}")
