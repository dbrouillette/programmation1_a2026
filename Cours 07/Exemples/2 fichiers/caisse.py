"""Caisse du Café Le Binaire.

Prend la commande d'un client, puis affiche sa facture avec le rabais
étudiant, les taxes et le pourboire.
"""

from utilitaires import lire_entier, lire_reel, lire_oui_non

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
NOM_CAFE = "Café Le Binaire"
LARGEUR_FACTURE = 34
PRODUITS = ("Café filtre", "Latté", "Chocolat chaud", "Muffin", "Biscuit")
PRIX = (2.25, 4.50, 3.75, 3.25, 1.95)
QUANTITE_MAX = 20
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975
RABAIS_ETUDIANT = 0.10


# ---------------------------------------------------------------------------
# Fonctions d'affichage
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation de la largeur de la facture.

    Args:
        caractere (str): Le caractère répété pour former la ligne.
    """
    print(caractere * LARGEUR_FACTURE)


def afficher_entete():
    """Affiche le nom du café encadré de deux lignes."""
    afficher_separateur("=")
    print(f"{NOM_CAFE:^{LARGEUR_FACTURE}}")
    afficher_separateur("=")


def afficher_menu():
    """Affiche l'en-tête, puis la liste numérotée des produits et leur prix."""
    afficher_entete()
    for i in range(len(PRODUITS)):
        print(f"{i + 1}. {PRODUITS[i]:<20}{PRIX[i]:>9.2f} $")
    print("0. Terminer la commande")


def afficher_ligne(produit, quantite, prix_unitaire):
    """Affiche une ligne de facture : quantité, produit et montant.

    Args:
        produit (str): Le nom du produit.
        quantite (int): La quantité commandée.
        prix_unitaire (float): Le prix d'un seul exemplaire du produit.
    """
    print(f"{quantite:>2} x {produit:<18}{quantite * prix_unitaire:>9.2f} $")


def afficher_montant(libelle, montant):
    """Affiche un libellé suivi d'un montant aligné à droite.

    Args:
        libelle (str): Le texte affiché à gauche (ex. « TPS »).
        montant (float): Le montant affiché à droite.
    """
    print(f"{libelle:<23}{montant:>9.2f} $")


# ---------------------------------------------------------------------------
# Fonctions de calcul
# ---------------------------------------------------------------------------
def ajouter_au_panier(quantites, index, quantite):
    """Ajoute une quantité d'un produit au panier.

    La liste quantites est modifiée directement : rien n'est retourné.

    Args:
        quantites (list): Les quantités commandées, une par produit.
        index (int): L'index du produit dans PRODUITS.
        quantite (int): La quantité à ajouter.
    """
    quantites[index] += quantite


def calculer_sous_total(quantites):
    """Calcule le sous-total d'une commande, avant rabais et taxes.

    Args:
        quantites (list): Les quantités commandées, une par produit.

    Returns:
        float: La somme des quantités multipliées par leur prix.
    """
    sous_total = 0.0
    for i in range(len(quantites)):
        sous_total += quantites[i] * PRIX[i]
    return sous_total


def calculer_rabais(montant, taux):
    """Calcule le montant d'un rabais, arrondi au cent.

    Args:
        montant (float): Le montant sur lequel s'applique le rabais.
        taux (float): Le taux du rabais (ex. 0.10 pour 10 %).

    Returns:
        float: Le montant du rabais.
    """
    return round(montant * taux, 2)


def calculer_taxes(montant):
    """Calcule la TPS et la TVQ sur un montant, arrondies au cent.

    Args:
        montant (float): Le montant taxable.

    Returns:
        tuple: La TPS et la TVQ, dans cet ordre.
    """
    tps = round(montant * TAUX_TPS, 2)
    tvq = round(montant * TAUX_TVQ, 2)
    return tps, tvq


def calculer_total(sous_total, rabais=0.0, pourboire=0.0):
    """Calcule le total à payer.

    Args:
        sous_total (float): Le sous-total de la commande.
        rabais (float, optional): Le taux du rabais. Par défaut 0.0.
        pourboire (float, optional): Le pourboire, en dollars. Par défaut 0.0.

    Returns:
        float: Le total, rabais, taxes et pourboire inclus.
    """
    montant = sous_total - calculer_rabais(sous_total, rabais)
    tps, tvq = calculer_taxes(montant)
    return round(montant + tps + tvq + pourboire, 2)


# ---------------------------------------------------------------------------
# Facture
# ---------------------------------------------------------------------------
def afficher_facture(quantites, rabais=0.0, pourboire=0.0):
    """Affiche la facture détaillée d'une commande.

    Args:
        quantites (list): Les quantités commandées, une par produit.
        rabais (float, optional): Le taux du rabais. Par défaut 0.0.
        pourboire (float, optional): Le pourboire, en dollars. Par défaut 0.0.
    """
    afficher_entete()
    for i in range(len(PRODUITS)):
        if quantites[i] > 0:
            afficher_ligne(PRODUITS[i], quantites[i], PRIX[i])
    afficher_separateur("-")

    sous_total = calculer_sous_total(quantites)
    montant_rabais = calculer_rabais(sous_total, rabais)
    tps, tvq = calculer_taxes(sous_total - montant_rabais)

    afficher_montant("Sous-total", sous_total)
    if montant_rabais > 0:
        afficher_montant("Rabais étudiant", -montant_rabais)
    afficher_montant("TPS", tps)
    afficher_montant("TVQ", tvq)
    if pourboire > 0:
        afficher_montant("Pourboire", pourboire)
    afficher_separateur("-")
    afficher_montant("TOTAL", calculer_total(sous_total, rabais, pourboire))


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Prend la commande d'un client, puis affiche sa facture."""
    quantites = [0] * len(PRODUITS)

    afficher_menu()
    choix = lire_entier("Votre choix : ", 0, len(PRODUITS))
    while choix != 0:
        quantite = lire_entier("Quantité : ", 1, QUANTITE_MAX)
        ajouter_au_panier(quantites, choix - 1, quantite)
        choix = lire_entier("Votre choix : ", 0, len(PRODUITS))

    if sum(quantites) == 0:
        print("Aucun produit commandé. À la prochaine!")
    else:
        est_etudiant = lire_oui_non("Carte étudiante? (o/n) : ")
        rabais = RABAIS_ETUDIANT if est_etudiant else 0.0
        pourboire = lire_reel("Pourboire ($) : ")
        print()
        afficher_facture(quantites, rabais, pourboire)


main()
