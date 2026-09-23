# Auteur    : <?>
# Date      : <?>
# Sujet     : Distributrice à café - VERSION DE DÉPART
#             Aucune validation, aucune boucle : le programme sert UN seul café puis se termine.
#             La machine accepte n'importe quel montant tapé au clavier...
#             même 1.13 $, ce qui est impossible avec de vraies pièces!

# ----------------------------------------------------------------------
# Les constantes (à conserver dans votre version finale)
# ----------------------------------------------------------------------
PRIX_AVANT_TAXES = 1.00  # le café est à 1 $ plus taxes
TAUX_TPS = 0.05          # 5 %
TAUX_TVQ = 0.09975       # 9,975 %
GOBELETS_DEPART = 5      # la machine est chargée de 5 gobelets au matin
CAISSE_DEPART = 10.00    # fonds de caisse du matin, pour pouvoir rendre la monnaie

prix = PRIX_AVANT_TAXES * (1 + TAUX_TPS + TAUX_TVQ)

# ----------------------------------------------------------------------
# Les variables d'état : ce sont elles qui devront s'ajuster
# à CHAQUE transaction dans votre version finale.
# ----------------------------------------------------------------------
gobelets = GOBELETS_DEPART  # devra diminuer de 1 à chaque café servi
caisse = CAISSE_DEPART      # devra augmenter du prix de chaque café vendu
nb_cafes = 0                # devra compter les cafés vendus

print()
print("Bienvenue à la distributrice du Cégep!")
print(f"Un café coûte {prix:.2f} $, taxes incluses.")
print(f"La machine contient {gobelets} gobelet(s) et {caisse:.2f} $ en caisse.")

montant = float(input("Insérez votre montant : "))
monnaie = montant - prix

# ----------------------------------------------------------------------
# Mise à jour de l'état de la machine
# Remarquez le patron : chaque variable est réaffectée à partir d'elle-même.
# Ici, ça n'arrive qu'UNE seule fois... à vous de le répéter en boucle!
# ----------------------------------------------------------------------
gobelets = gobelets - 1
caisse = caisse + prix
nb_cafes = nb_cafes + 1

print("Voici votre café.")
print(f"Votre monnaie : {monnaie:.2f} $")
print(f"Il reste {gobelets} gobelet(s) et la caisse contient {caisse:.2f} $.")
print(f"Cafés vendus depuis le début : {nb_cafes}")
print("Merci et bonne journée!")
print()
