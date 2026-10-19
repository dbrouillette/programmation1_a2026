# Auteur  : David Brouillette
# Date    : 2026/10/19
# Sujet   : Démo 6.2 - Les listes (le poulailler)

# ------------------------------------------------------------
# 1. Créer une liste
# ------------------------------------------------------------
print("=== 1. Créer une liste ===")

poules = ["Cocotte", "Roussette", "Plumette", "Grisette"]
print(poules)
print(type(poules))

# Liste vide : le poulailler du voisin, qui n'a pas encore de poules
poules_voisin = []
print("Poules du voisin :", poules_voisin)

# À partir d'une chaîne, avec split()
races = "Rhode Island,Leghorn,Chantecler".split(",")
print("Races :", races)

# ------------------------------------------------------------
# 2. Accéder aux éléments
# ------------------------------------------------------------
print("\n=== 2. Accéder aux éléments ===")

#   index :      0           1            2           3
#   négatif :   -4          -3           -2          -1
print("Première poule :", poules[0])
print("Troisième poule :", poules[2])
print("Dernière poule :", poules[-1])

# Par tranche (slicing) : produit une NOUVELLE liste
print("Les deux premières :", poules[:2])
print("Du 2e au 3e :", poules[1:3])
print("À l'envers :", poules[::-1])

# Le dernier index valide est len(poules) - 1
print("Dernier index valide :", len(poules) - 1)
# print(poules[4])    # ❌ IndexError: list index out of range

# ------------------------------------------------------------
# 3. Modifier une liste
# ------------------------------------------------------------
print("\n=== 3. Modifier une liste ===")

# Remplacer un élément par son index
poules[1] = "Rousse"
print("Roussette s'appelle maintenant Rousse :", poules)

# append() : une nouvelle poule arrive au poulailler
poules.append("Pépita")
print("Arrivée de Pépita :", poules)

# insert() : la poule de la ferme voisine prend la place no 0
poules.insert(0, "Câline")
print("Câline insérée au début :", poules)

# remove() : une poule est vendue au marché (on vérifie d'abord avec in)
vendue = "Plumette"
if vendue in poules:
    poules.remove(vendue)
    print(vendue, "a été vendue :", poules)
else:
    print(vendue, "n'est pas dans le poulailler.")

# pop() : retire ET retourne la dernière poule
partie = poules.pop()
print(partie, "s'est sauvée par le trou de la clôture :", poules)

# ⚠️ append() ne retourne rien : ne pas faire poules = poules.append(...)
resultat = poules.append("Noisette")
print("Valeur retournée par append() :", resultat)
print("Mais la liste a bien été modifiée :", poules)

# ------------------------------------------------------------
# 4. Opérations et fonctions utiles
# ------------------------------------------------------------
print("\n=== 4. Opérations et fonctions utiles ===")

# Nombre d'œufs ramassés chaque jour de la semaine
oeufs_semaine = [3, 4, 2, 4, 5, 1, 4]

print("Œufs de la semaine :", oeufs_semaine)
print("Nombre de jours :", len(oeufs_semaine))
print("Total d'œufs :", sum(oeufs_semaine))
print("Pire journée :", min(oeufs_semaine))
print("Meilleure journée :", max(oeufs_semaine))
print(f"Moyenne par jour : {sum(oeufs_semaine) / len(oeufs_semaine):.2f}")
print("Jours à 4 œufs :", oeufs_semaine.count(4))
print("Index de la première journée à 5 œufs :", oeufs_semaine.index(5))
print("Une journée sans œuf?", 0 in oeufs_semaine)

# sorted() : nouvelle liste triée, l'originale est conservée
oeufs_tries = sorted(oeufs_semaine)
print("Triés (sorted) :", oeufs_tries)
print("Originale inchangée :", oeufs_semaine)

# sort() : trie la liste elle-même
# ⚠️ Les lettres accentuées sont placées après les autres : Câline arrive après Cocotte!
poules.sort()
print("Poules en ordre alphabétique :", poules)
poules.sort(reverse=True)
print("Poules en ordre inverse :", poules)
poules.reverse()
print("Poules inversées de nouveau :", poules)

# join() : assembler une liste de chaînes
print("Au poulailler :", ", ".join(poules))

# Concaténation et répétition
nouvelles = ["Biscotte", "Praline"]
poulailler_agrandi = poules + nouvelles
print("Poulailler agrandi :", poulailler_agrandi)
print("Nids vides au départ :", [0] * 3)

# ------------------------------------------------------------
# 5. Parcourir une liste avec for
# ------------------------------------------------------------
print("\n=== 5. Parcourir une liste ===")

# Parcours par élément : le plus lisible
for poule in poules:
    print("Cot cot,", poule, "!")

# Parcours par index : quand on a besoin de la position
print("\nAppel des poules :")
for i in range(len(poules)):
    print(f"{i + 1}. {poules[i]}")

# Modifier chaque élément : il FAUT passer par l'index
# Les poules ont reçu une moulée de qualité : +1 œuf par jour
for oeufs in oeufs_semaine:
    oeufs = oeufs + 1        # ❌ ne modifie pas la liste
print("\nAprès la mauvaise boucle :", oeufs_semaine)

for i in range(len(oeufs_semaine)):
    oeufs_semaine[i] = oeufs_semaine[i] + 1    # ✅
print("Après la bonne boucle :", oeufs_semaine)

# ------------------------------------------------------------
# 6. Construire une liste dans une boucle
# ------------------------------------------------------------
print("\n=== 6. Construire une liste dans une boucle ===")

# À partir d'une autre liste : poids des poules en kg -> en grammes
poids_kg = [2.1, 1.8, 2.4, 1.6]
poids_g = []
for poids in poids_kg:
    poids_g.append(round(poids * 1000))
print("Poids en grammes :", poids_g)

# ------------------------------------------------------------
# 7. Usages typiques : deux listes associées par leur index
# ------------------------------------------------------------
print("\n=== 7. Usages typiques ===")

noms = ["Cocotte", "Rousse", "Grisette", "Câline", "Noisette"]
oeufs_pondus = [6, 4, 0, 7, 2]       # œufs pondus cette semaine, par poule

# Afficher un tableau
print(f"{'Poule':<10}{'Œufs':>5}")
for i in range(len(noms)):
    print(f"{noms[i]:<10}{oeufs_pondus[i]:>5}")

# Filtrer : les bonnes pondeuses (5 œufs et plus)
pondeuses = []
for i in range(len(noms)):
    if oeufs_pondus[i] >= 5:
        pondeuses.append(noms[i])
print("\nBonnes pondeuses :", ", ".join(pondeuses))

# Transformer : noms en majuscules pour les étiquettes des nids
etiquettes = []
for nom in noms:
    etiquettes.append(nom.upper())
print("Étiquettes des nids :", etiquettes)

# Rechercher : quelle poule a pondu le plus?
meilleure = noms[oeufs_pondus.index(max(oeufs_pondus))]
print("Championne de la semaine :", meilleure)

# Rechercher avec une boucle : la position d'une poule
recherche = "Grisette"
position = -1
for i in range(len(noms)):
    if noms[i] == recherche:
        position = i
        break
if position != -1:
    print(recherche, "est dans le nid no", position + 1)
else:
    print(recherche, "est introuvable")

# Statistiques : combien de poules n'ont rien pondu?
nb_sans_oeuf = 0
for oeufs in oeufs_pondus:
    if oeufs == 0:
        nb_sans_oeuf += 1
print("Poules qui n'ont pas pondu :", nb_sans_oeuf)

# ------------------------------------------------------------
# 8. Pièges et bonnes pratiques
# ------------------------------------------------------------
print("\n=== 8. Pièges ===")

# Piège 1 : b = a ne copie pas la liste (alias)
poulailler_a = ["Cocotte", "Rousse"]
poulailler_b = poulailler_a              # ❌ même liste, deux noms
poulailler_b.append("Intruse")
print("Alias - poulailler A :", poulailler_a)    # Intruse est aussi dans A!

poulailler_a = ["Cocotte", "Rousse"]
poulailler_b = poulailler_a.copy()       # ✅ vraie copie
poulailler_b.append("Intruse")
print("Copie - poulailler A :", poulailler_a)
print("Copie - poulailler B :", poulailler_b)

# Piège 2 : retirer des éléments pendant qu'on parcourt la liste
oeufs_par_nid = [0, 0, 3, 2]
for oeufs in oeufs_par_nid:
    if oeufs == 0:
        oeufs_par_nid.remove(oeufs)      # ❌ un nid vide est sauté
print("Mauvais retrait des nids vides :", oeufs_par_nid)

oeufs_par_nid = [0, 0, 3, 2]
nids_pleins = []
for oeufs in oeufs_par_nid:
    if oeufs != 0:
        nids_pleins.append(oeufs)        # ✅ on construit une nouvelle liste
print("Bon retrait des nids vides :", nids_pleins)

# Piège 3 : vérifier qu'une liste n'est pas vide avant de calculer
if len(poules_voisin) > 0:
    print("Poule la plus lourde du voisin :", max(poules_voisin))
else:
    print("Le voisin n'a encore aucune poule.")

# ------------------------------------------------------------
# 9. Nombre d'éléments inconnu : while avec sentinelle
# ------------------------------------------------------------
print("\n=== 9. Le ramassage des œufs ===")

ramassage = []
saisie = input("Œufs trouvés dans le nid (Entrée pour terminer) : ").strip()
while saisie != "":
    ramassage.append(int(saisie))
    saisie = input("Œufs trouvés dans le nid (Entrée pour terminer) : ").strip()

if len(ramassage) > 0:
    print(f"{len(ramassage)} nid(s) visité(s) :", ramassage)
    print("Total ramassé :", sum(ramassage))
    print(f"Moyenne par nid : {sum(ramassage) / len(ramassage):.1f}")
else:
    print("Aucun nid visité aujourd'hui.")
