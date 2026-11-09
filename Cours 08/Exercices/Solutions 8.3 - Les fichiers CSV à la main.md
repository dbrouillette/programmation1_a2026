# Solutions — Les fichiers CSV à la main (fiche 8.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Variable | Valeur | Problème? |
| --- | --- | --- |
| `a` | `['Tremblay', 'Marie', '87\n']` | ⚠️ Le `\n` reste collé au dernier champ : il manque le `strip()`. (`int('87\n')` fonctionne quand même, mais une comparaison de texte échouerait.) |
| `b` | `['Tremblay', 'Marie', '87']` | ✅ Correct |
| `c` | `['Gagnon', 'Luc', '']` | ⚠️ Le dernier champ est vide : `int('')` lèverait une `ValueError`. Il faut valider. |
| `d` | `['Roy', 'Anne-Sophie', '91', 'bonus']` | ⚠️ 4 champs au lieu de 3 : il faut vérifier `len(champs)`. |
| `e` | `['"Côté', ' Jr"', 'Paul', '75']` | ❌ `split()` ne connaît pas les guillemets : la virgule entre guillemets coupe le nom en deux. |
| `f` | `'Tremblay;Marie;87'` | ✅ Correct (délimiteur point-virgule) |
| `g` | `'Tremblay,Marie,87'` | ✅ `join()` est l'inverse de `split()` |
| `h` | `1` | ⚠️ Il n'y a aucun `;` dans la ligne : on obtient une liste d'**un seul** élément, la ligne complète. Signe qu'on utilise le mauvais délimiteur. |

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from pathlib import Path

CHEMIN_ETUDIANTS = Path(__file__).parent / "etudiants.csv"
SEUIL_REUSSITE = 60


def main():
    total = 0
    nb_etudiants = 0

    print(f"{'Nom':<13}{'Prénom':<14}{'Note':>5}")
    print("-" * 32)
    with open(CHEMIN_ETUDIANTS, "r", encoding="utf-8") as fichier:
        fichier.readline()                       # en-tête
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne != "":
                champs = ligne.split(",")
                nom = champs[0]
                prenom = champs[1]
                note = int(champs[2])

                mention = "  Échec" if note < SEUIL_REUSSITE else ""
                print(f"{nom:<13}{prenom:<14}{note:>5}{mention}")

                total += note
                nb_etudiants += 1
    print("-" * 32)
    print(f"Moyenne du groupe : {total / nb_etudiants:.1f}")


main()
```

- `readline()` lit l'en-tête avant la boucle; la boucle commence donc à la première vraie rangée.
- L'opérateur ternaire (vu en 4.4) choisit la mention en une ligne.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
from pathlib import Path

CHEMIN_VENTES = Path(__file__).parent / "ventes.csv"

COL_HEURE = 0
COL_PRODUIT = 1
COL_QUANTITE = 2
COL_PRIX = 3


def charger_ventes(chemin):
    """Renvoie une liste 2D : [[heure, produit, quantite, prix_unitaire], ...]."""
    ventes = []
    with open(chemin, "r", encoding="utf-8") as fichier:
        fichier.readline()
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne != "":
                champs = ligne.split(",")
                ventes.append([champs[COL_HEURE], champs[COL_PRODUIT],
                               int(champs[COL_QUANTITE]), float(champs[COL_PRIX])])
    return ventes


def calculer_montant(vente):
    return vente[COL_QUANTITE] * vente[COL_PRIX]


def calculer_total(ventes):
    total = 0.0
    for vente in ventes:
        total += calculer_montant(vente)
    return total


def trouver_plus_grosse_vente(ventes):
    plus_grosse = ventes[0]
    for vente in ventes:
        if calculer_montant(vente) > calculer_montant(plus_grosse):
            plus_grosse = vente
    return plus_grosse


def compter_produit(ventes, produit):
    quantite = 0
    for vente in ventes:
        if vente[COL_PRODUIT].lower() == produit.lower():
            quantite += vente[COL_QUANTITE]
    return quantite


def trouver_nom_exact(ventes, produit):
    """Renvoie le nom du produit tel qu'écrit dans le fichier, ou la saisie si introuvable."""
    for vente in ventes:
        if vente[COL_PRODUIT].lower() == produit.lower():
            return vente[COL_PRODUIT]
    return produit


def main():
    ventes = charger_ventes(CHEMIN_VENTES)
    print(f"Total des ventes : {calculer_total(ventes):.2f} $")

    vente = trouver_plus_grosse_vente(ventes)
    print(f"Plus grosse vente : {vente[COL_QUANTITE]} x {vente[COL_PRODUIT]} "
          f"à {vente[COL_HEURE]} ({calculer_montant(vente):.2f} $)")

    produit = input("Produit à rechercher : ").strip()
    quantite = compter_produit(ventes, produit)
    print(f"{trouver_nom_exact(ventes, produit)} : {quantite} vendu(s)")


main()
```

- Les constantes `COL_...` rendent le code lisible : `vente[COL_PRIX]` est beaucoup plus clair que `vente[3]`.
- La petite fonction `calculer_montant()` évite de répéter `quantite * prix` à trois endroits.
- Une fois le fichier chargé dans une liste 2D, tout le reste est du travail sur les listes, comme au cours 6.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
from pathlib import Path

CHEMIN_BULLETIN = Path(__file__).parent / "bulletin.csv"
EN_TETE = ["nom", "prenom", "note"]


def lire_texte_csv(message, vide_permis):
    """Demande un texte sans virgule. Si vide_permis est vrai, une saisie vide est acceptée."""
    valide = False
    while not valide:
        texte = input(message).strip()
        if "," in texte:
            print("Erreur : la virgule est interdite.")
        elif texte == "" and not vide_permis:
            print("Erreur : le texte ne doit pas être vide.")
        else:
            valide = True
    return texte


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


def sauvegarder_bulletin(chemin, etudiants):
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(",".join(EN_TETE) + "\n")
        for etudiant in etudiants:
            champs = [etudiant[0], etudiant[1], str(etudiant[2])]
            fichier.write(",".join(champs) + "\n")


def main():
    etudiants = []
    nom = lire_texte_csv("Nom (Entrée pour terminer) : ", True)
    while nom != "":
        prenom = lire_texte_csv("Prénom : ", False)
        note = lire_entier("Note : ", 0, 100)
        etudiants.append([nom, prenom, note])
        nom = lire_texte_csv("Nom (Entrée pour terminer) : ", True)

    sauvegarder_bulletin(CHEMIN_BULLETIN, etudiants)
    print(f"\n{len(etudiants)} étudiant(s) écrit(s) dans {CHEMIN_BULLETIN.name}.")


main()
```

- La note est un `int` dans la liste 2D : il faut la convertir avec `str()` avant le `join()`.
- Refuser la virgule à la saisie est la seule façon de garantir que notre CSV « à la main » restera lisible. C'est une limite importante de l'approche naïve.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_SOURCE = DOSSIER / "depenses_excel.csv"
CHEMIN_DESTINATION = DOSSIER / "depenses.csv"

COL_DATE = 0
COL_CATEGORIE = 1
COL_DESCRIPTION = 2
COL_MONTANT = 3


def charger_depenses_excel(chemin):
    """Lit un CSV Excel français (; et virgule décimale). Renvoie une liste 2D."""
    depenses = []
    with open(chemin, "r", encoding="utf-8-sig") as fichier:
        fichier.readline()
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne != "":
                champs = ligne.split(";")
                montant = float(champs[COL_MONTANT].replace(",", "."))
                depenses.append([champs[COL_DATE], champs[COL_CATEGORIE],
                                 champs[COL_DESCRIPTION], montant])
    return depenses


def sauvegarder_depenses(chemin, depenses):
    """Écrit un CSV standard (virgule, point décimal)."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write("date,categorie,description,montant\n")
        for depense in depenses:
            description = depense[COL_DESCRIPTION].replace(",", " ")
            fichier.write(f"{depense[COL_DATE]},{depense[COL_CATEGORIE]},"
                          f"{description},{depense[COL_MONTANT]:.2f}\n")


def calculer_total(depenses, categorie):
    """Total des dépenses d'une catégorie, ou de toutes si categorie est vide."""
    total = 0.0
    for depense in depenses:
        if categorie == "" or depense[COL_CATEGORIE] == categorie:
            total += depense[COL_MONTANT]
    return total


def main():
    depenses = charger_depenses_excel(CHEMIN_SOURCE)
    sauvegarder_depenses(CHEMIN_DESTINATION, depenses)
    print(f"{len(depenses)} dépenses converties dans {CHEMIN_DESTINATION.name}.")
    print(f"Total : {calculer_total(depenses, ''):.2f} $")
    print(f"Épicerie : {calculer_total(depenses, 'épicerie'):.2f} $")


main()
```

- Dans le fichier source, la virgule de `IGA, commande de la semaine` ne pose **aucun** problème : on découpe sur `;`.
- Le `replace(",", ".")` doit être fait **avant** `float()` : `float("143,27")` lève une `ValueError`.
- 🤔 **Réponse à la réflexion** : le module `csv` (fiche « Module csv » des outils) entoure automatiquement de guillemets une valeur qui contient le délimiteur. La description serait conservée telle quelle : `"IGA, commande de la semaine"`.
