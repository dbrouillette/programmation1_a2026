def calculer_pourboire(montant, taux=0.15, arrondir=True):
    """Calcule le pourboire à laisser sur une addition.

    Args:
        montant (float): Le montant de l'addition, taxes incluses.
        taux (float, optional): Le taux du pourboire (ex. 0.18 pour 18 %). Par défaut 0.15.
        arrondir (bool, optional): Si True, arrondit le pourboire au dollar supérieur.
            Par défaut True.

    Returns:
        float: Le montant du pourboire, en dollars.
    """
    pourboire = montant * taux
    if arrondir and pourboire != int(pourboire):
        pourboire = float(int(pourboire) + 1)
    return round(pourboire, 2)


def formater_telephone(numero, separateur="-"):
    """Met en forme un numéro de téléphone nord-américain de 10 chiffres.

    Args:
        numero (str): Les 10 chiffres du numéro, sans espaces ni symboles (ex. « 8193761721 »).
        separateur (str, optional): Le caractère placé entre les groupes de chiffres. Par défaut « - ».

    Returns:
        str: Le numéro mis en forme (ex. « 819-376-1721 »).
    """
    return numero[:3] + separateur + numero[3:6] + separateur + numero[6:]


def compter_lettre(texte, lettre, ignorer_casse=True):
    """Compte le nombre de fois qu'une lettre apparaît dans un texte.

    Args:
        texte (str): Le texte dans lequel on cherche.
        lettre (str): La lettre à compter (un seul caractère).
        ignorer_casse (bool, optional): Si True, les majuscules et les minuscules
            sont considérées comme identiques. Par défaut True.

    Returns:
        int: Le nombre d'occurrences de la lettre.
    """
    if ignorer_casse:
        texte = texte.lower()
        lettre = lettre.lower()
    nb = 0
    for caractere in texte:
        if caractere == lettre:
            nb += 1
    return nb
