"""Inventaire du Café Le Binaire — version CSV « à la main » (split / join).

Le menu est lu dans menu.csv au démarrage, modifié en mémoire dans une liste 2D,
puis sauvegardé dans le même fichier après chaque modification.

Aucune librairie pour le CSV : seulement split() pour lire et une f-string pour écrire.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
CHEMIN_MENU = Path(__file__).parent / "menu.csv"
EN_TETE = "produit,categorie,prix,stock"
NB_COLONNES = 4

COL_PRODUIT = 0
COL_CATEGORIE = 1
COL_PRIX = 2
COL_STOCK = 3

PRIX_MAX = 100.0
STOCK_MAX = 500


# ---------------------------------------------------------------------------
# Fichier CSV
# ---------------------------------------------------------------------------
def charger_menu():
    """Renvoie le menu sous forme de liste 2D : [[produit, categorie, prix, stock], ...].

    Les lignes vides ou mal formées sont ignorées avec un avertissement.
    Si le fichier n'existe pas, renvoie une liste vide.
    """
    menu = []
    try:
        with open(CHEMIN_MENU, "r", encoding="utf-8") as fichier:
            fichier.readline()                          # on saute l'en-tête
            numero = 1
            for ligne in fichier:
                numero += 1
                ligne = ligne.strip()
                if ligne != "":
                    champs = ligne.split(",")
                    if len(champs) != NB_COLONNES:
                        print(f"Ligne {numero} ignorée : {len(champs)} colonnes au lieu de {NB_COLONNES}.")
                    else:
                        try:
                            prix = float(champs[COL_PRIX])
                            stock = int(champs[COL_STOCK])
                            menu.append([champs[COL_PRODUIT], champs[COL_CATEGORIE], prix, stock])
                        except ValueError:
                            print(f"Ligne {numero} ignorée : prix ou stock invalide.")
    except FileNotFoundError:
        print(f"Avertissement : {CHEMIN_MENU.name} introuvable, le menu est vide.")
    return menu


def sauvegarder_menu(menu):
    """Réécrit menu.csv au complet à partir de la liste 2D."""
    with open(CHEMIN_MENU, "w", encoding="utf-8") as fichier:
        fichier.write(EN_TETE + "\n")
        for rangee in menu:
            # Version avec join() : chaque champ doit d'abord être converti en chaîne
            champs = [rangee[COL_PRODUIT], rangee[COL_CATEGORIE],
                      f"{rangee[COL_PRIX]:.2f}", str(rangee[COL_STOCK])]
            fichier.write(",".join(champs) + "\n")


# ---------------------------------------------------------------------------
# Saisies validées
# ---------------------------------------------------------------------------
def lire_entier(message, minimum, maximum):
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return valeur


def lire_reel(message, minimum, maximum):
    valide = False
    while not valide:
        try:
            valeur = float(input(message).replace(",", "."))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre.")
    return valeur


def lire_texte_sans_virgule(message):
    """Une virgule briserait notre CSV « à la main » : on la refuse."""
    texte = input(message).strip()
    while texte == "" or "," in texte:
        print("Erreur : le texte ne doit être ni vide, ni contenir de virgule.")
        texte = input(message).strip()
    return texte


# ---------------------------------------------------------------------------
# Affichage et actions
# ---------------------------------------------------------------------------
def afficher_menu(menu):
    print()
    print(f"{'#':>2}  {'Produit':<18}{'Catégorie':<12}{'Prix':>8}{'Stock':>7}")
    print("-" * 49)
    for i in range(len(menu)):
        rangee = menu[i]
        print(f"{i + 1:>2}  {rangee[COL_PRODUIT]:<18}{rangee[COL_CATEGORIE]:<12}"
              f"{rangee[COL_PRIX]:>6.2f} ${rangee[COL_STOCK]:>7}")
    print()


def calculer_valeur_stock(menu):
    valeur = 0.0
    for rangee in menu:
        valeur += rangee[COL_PRIX] * rangee[COL_STOCK]
    return valeur


def vendre(menu):
    afficher_menu(menu)
    numero = lire_entier("Numéro du produit vendu : ", 1, len(menu))
    rangee = menu[numero - 1]
    if rangee[COL_STOCK] == 0:
        print(f"Désolé, il ne reste plus de {rangee[COL_PRODUIT]}.")
    else:
        quantite = lire_entier("Quantité : ", 1, rangee[COL_STOCK])
        rangee[COL_STOCK] -= quantite
        print(f"Vente : {quantite} x {rangee[COL_PRODUIT]} = {quantite * rangee[COL_PRIX]:.2f} $")
        sauvegarder_menu(menu)


def ajouter_produit(menu):
    produit = lire_texte_sans_virgule("Nom du produit : ")
    categorie = lire_texte_sans_virgule("Catégorie : ")
    prix = lire_reel("Prix : ", 0.01, PRIX_MAX)
    stock = lire_entier("Stock initial : ", 0, STOCK_MAX)
    menu.append([produit, categorie, prix, stock])
    sauvegarder_menu(menu)
    print(f"{produit} ajouté au menu.")


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    menu = charger_menu()
    choix = -1
    while choix != 0:
        print("=== Inventaire du Café Le Binaire ===")
        print("1. Afficher le menu")
        print("2. Enregistrer une vente")
        print("3. Ajouter un produit")
        print("4. Valeur du stock")
        print("0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 4)

        if choix == 1:
            afficher_menu(menu)
        elif choix == 2:
            if len(menu) == 0:
                print("Le menu est vide.")
            else:
                vendre(menu)
        elif choix == 3:
            ajouter_produit(menu)
        elif choix == 4:
            print(f"Valeur du stock : {calculer_valeur_stock(menu):.2f} $\n")

    print("Au revoir!")


main()
