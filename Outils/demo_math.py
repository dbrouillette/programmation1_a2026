# Auteur    : 
# Sujet     : 
# Sujet     : Démo du module `math`

import math

# --- 2. Fonctions natives utiles et constantes ---------------------------
print("=== Fonctions natives ===")
print("abs(-5) ->", abs(-5))
print("max(3, 7, 2) ->", max(3, 7, 2))
print("min(3, 7, 2) ->", min(3, 7, 2))
print("round(4.6) ->", round(4.6))
print("pow(2, 3) ->", pow(2, 3))
print("2 ** 3 ->", 2 ** 3)

# --- 3. Fonctions du module math ------------------------------------------
print("\n=== Racines, arrondis, factorielle ===")
print("math.sqrt(25) ->", math.sqrt(25))
print("math.ceil(4.1) ->", math.ceil(4.1))
print("math.floor(4.9) ->", math.floor(4.9))
print("math.trunc(4.9) ->", math.trunc(4.9))
print("math.trunc(-4.9) ->", math.trunc(-4.9))
print("math.factorial(5) ->", math.factorial(5))

print("\n=== Logarithmes ===")
print("math.log(math.e) ->", math.log(math.e))
print("math.log(8, 2) ->", math.log(8, 2))
print("math.log10(100) ->", math.log10(100))

print("\n=== Trigonométrie et angles ===")
print("math.sin(math.pi / 2) ->", math.sin(math.pi / 2))
print("math.cos(0) ->", math.cos(0))
print("math.tan(math.pi / 4) ->", math.tan(math.pi / 4))
print("math.degrees(math.pi) ->", math.degrees(math.pi))
print("math.radians(180) ->", math.radians(180))

print("\n=== Autres fonctions ===")
print("math.gcd(12, 18) ->", math.gcd(12, 18))

# --- Constantes utiles ------------------------------------------------------
print("\n=== Constantes ===")
print("math.pi ->", math.pi)
print("math.e ->", math.e)

# --- 4. Remarques importantes : math.sqrt(-1) provoque une ValueError ------
print("\n=== Remarque : math.sqrt d'un nombre négatif ===")
try:
    math.sqrt(-1)
except ValueError as erreur:
    print("Erreur attrapée :", erreur)
