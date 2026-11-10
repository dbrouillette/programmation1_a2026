# Solutions — Le module csv (fiche « Module csv »)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
import csv
from pathlib import Path

CHEMIN_ETUDIANTS = Path(__file__).parent / "etudiants.csv"
SEUIL_REUSSITE = 60


def main():
    total = 0
    nb_etudiants = 0

    print(f"{'Nom':<13}{'Prénom':<14}{'Note':>5}")
    print("-" * 32)
    with open(CHEMIN_ETUDIANTS, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)                            # en-tête
        for champs in lecteur:
            if len(champs) == 3:
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

- Trois changements seulement : `import csv`, `newline=""` à l'ouverture, et `csv.reader` + `next()` à la place de `readline()` + `strip().split(",")`.
- La ligne `"Côté, Jr",Paul,79` donne bien 3 champs : `['Côté, Jr', 'Paul', '79']`.
- Avec l'ancienne version, `split(",")` donnait 4 champs : `['"Côté', ' Jr"', 'Paul', '79']`. Le programme affichait `"Côté` comme nom et plantait sur `int('Paul')` (`ValueError`).
- Le test `len(champs) == 3` ignore une ligne vide à la fin du fichier (le lecteur la renvoie sous forme de liste vide `[]`).

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
import csv
from pathlib import Path

CHEMIN_HORAIRE = Path(__file__).parent / "horaire.csv"

COURS = [
    ["420-116-RI", "Programmation 1, Python", "B-1234"],
    ["109-101-MQ", "Activité physique et santé", "Gymnase"],
    ["340-101-MQ", "Philosophie et rationalité", "A-2050"],
    ["601-101-MQ", "Écriture et littérature", "A-1120"],
]


def main():
    with open(CHEMIN_HORAIRE, "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["code", "titre", "local"])
        ecrivain.writerows(COURS)
    print(f"{len(COURS)} cours écrits dans {CHEMIN_HORAIRE.name}.")


main()
```

*`horaire.csv` produit :*

```text
code,titre,local
420-116-RI,"Programmation 1, Python",B-1234
109-101-MQ,Activité physique et santé,Gymnase
340-101-MQ,Philosophie et rationalité,A-2050
601-101-MQ,Écriture et littérature,A-1120
```

- Le titre `Programmation 1, Python` contient une virgule : `csv.writer` l'a **automatiquement entouré de guillemets**, pour qu'il reste un seul champ à la relecture. Les autres valeurs n'en ont pas besoin.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
import csv
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_MENU = DOSSIER / "menu.csv"
COL_CATEGORIE = 1


def charger_csv(chemin):
    """Renvoie (en_tete, rangees) : l'en-tête et la liste 2D des rangées (des chaînes)."""
    rangees = []
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier)
        en_tete = next(lecteur)
        for champs in lecteur:
            if len(champs) == len(en_tete):
                rangees.append(champs)
    return en_tete, rangees


def trouver_categories(rangees):
    categories = []
    for rangee in rangees:
        if rangee[COL_CATEGORIE] not in categories:
            categories.append(rangee[COL_CATEGORIE])
    return categories


def lire_choix(message, choix_valides):
    reponse = input(message).strip().lower()
    while reponse not in choix_valides:
        print(f"Erreur : choisissez parmi {', '.join(choix_valides)}.")
        reponse = input(message).strip().lower()
    return reponse


def main():
    en_tete, rangees = charger_csv(CHEMIN_MENU)
    categories = trouver_categories(rangees)
    print(f"Catégories : {', '.join(categories)}")
    categorie = lire_choix("Catégorie à extraire : ", categories)

    chemin_sortie = DOSSIER / f"menu_{categorie}.csv"
    nb_ecrits = 0
    with open(chemin_sortie, "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(en_tete)
        for rangee in rangees:
            if rangee[COL_CATEGORIE] == categorie:
                ecrivain.writerow(rangee)
                nb_ecrits += 1

    print(f"{nb_ecrits} produit(s) écrit(s) dans {chemin_sortie.name}.")


main()
```

- On ne convertit **pas** les prix et les stocks : on se contente de recopier les rangées, donc les chaînes suffisent.
- L'en-tête est récupéré avec `next()` et réécrit tel quel dans le nouveau fichier.
- `"Muffin, bleuets"` est relu comme un seul champ, puis réécrit avec ses guillemets : le module s'occupe de tout, dans les deux sens.
- Ici, `join()` sert seulement à **afficher** les catégories à l'écran, pas à écrire du CSV.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
import csv
from pathlib import Path

CHEMIN_INSCRIPTIONS = Path(__file__).parent / "inscriptions.csv"
EN_TETE = ["nom", "groupe", "jeu"]


def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le texte ne doit pas être vide.")
        texte = input(message).strip()
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


def ajouter_inscription(chemin, inscription):
    nouveau_fichier = not chemin.exists()          # à tester AVANT l'ouverture
    with open(chemin, "a", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        if nouveau_fichier:
            ecrivain.writerow(EN_TETE)
        ecrivain.writerow(inscription)


def compter_inscriptions(chemin):
    nb = 0
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)
        for champs in lecteur:
            if len(champs) == len(EN_TETE):
                nb += 1
    return nb


def main():
    nom = lire_texte("Nom complet : ")
    groupe = lire_entier("Groupe (1 à 4) : ", 1, 4)
    jeu = lire_texte("Jeu préféré : ")

    ajouter_inscription(CHEMIN_INSCRIPTIONS, [nom, groupe, jeu])
    total = compter_inscriptions(CHEMIN_INSCRIPTIONS)
    print(f"Inscription enregistrée! {total} inscrit(s) au total.")


main()
```

- `csv.writer` fonctionne aussi en mode `"a"` : la rangée est ajoutée à la fin du fichier.
- Si on testait `exists()` **après** `open(..., "a")`, la réponse serait toujours `True` : l'ouverture en mode `"a"` crée le fichier.
- Le nom `Tremblay, Marie` est entouré de guillemets automatiquement, sans qu'on ait besoin de refuser la virgule comme en 8.6.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
import csv
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_EXCEL = DOSSIER / "depenses_excel.csv"
CHEMIN_STANDARD = DOSSIER / "depenses.csv"
CHEMIN_POUR_EXCEL = DOSSIER / "depenses_pour_excel.csv"

COL_CATEGORIE = 1
COL_MONTANT = 3


def charger_depenses(chemin, delimiteur, encodage):
    """Renvoie (en_tete, depenses), avec le montant converti en float.

    Accepte la virgule ou le point comme séparateur décimal.
    """
    depenses = []
    with open(chemin, "r", encoding=encodage, newline="") as fichier:
        lecteur = csv.reader(fichier, delimiter=delimiteur)
        en_tete = next(lecteur)
        for champs in lecteur:
            if len(champs) == len(en_tete):
                champs[COL_MONTANT] = float(champs[COL_MONTANT].replace(",", "."))
                depenses.append(champs)
    return en_tete, depenses


def sauvegarder_depenses(chemin, en_tete, depenses, delimiteur, encodage, virgule_decimale):
    with open(chemin, "w", encoding=encodage, newline="") as fichier:
        ecrivain = csv.writer(fichier, delimiter=delimiteur)
        ecrivain.writerow(en_tete)
        for depense in depenses:
            montant = f"{depense[COL_MONTANT]:.2f}"
            if virgule_decimale:
                montant = montant.replace(".", ",")
            ecrivain.writerow([depense[0], depense[1], depense[2], montant])


def calculer_total(depenses, categorie):
    total = 0.0
    for depense in depenses:
        if categorie == "" or depense[COL_CATEGORIE] == categorie:
            total += depense[COL_MONTANT]
    return total


def exporter_pour_excel(chemin_source, chemin_destination):
    en_tete, depenses = charger_depenses(chemin_source, ",", "utf-8")
    sauvegarder_depenses(chemin_destination, en_tete, depenses, ";", "utf-8-sig", True)


def main():
    en_tete, depenses = charger_depenses(CHEMIN_EXCEL, ";", "utf-8-sig")
    sauvegarder_depenses(CHEMIN_STANDARD, en_tete, depenses, ",", "utf-8", False)
    print(f"{len(depenses)} dépenses converties dans {CHEMIN_STANDARD.name}.")
    print(f"Total : {calculer_total(depenses, ''):.2f} $")
    print(f"Épicerie : {calculer_total(depenses, 'épicerie'):.2f} $")

    exporter_pour_excel(CHEMIN_STANDARD, CHEMIN_POUR_EXCEL)
    print(f"Copie pour Excel : {CHEMIN_POUR_EXCEL.name}")


main()
```

*`depenses.csv` produit :*

```text
date,categorie,description,montant
2026-11-01,épicerie,"IGA, commande de la semaine",143.27
2026-11-03,transport,Essence,62.10
2026-11-05,loisirs,Cinéma,14.50
2026-11-08,épicerie,Marché,38.95
```

- La description est conservée **intacte**, entre guillemets : plus besoin de remplacer la virgule par un espace.
- Les mêmes fonctions de lecture et d'écriture servent dans les deux sens : seuls le délimiteur, l'encodage et le séparateur décimal changent. Ce sont des **paramètres**, comme vu au cours 7.
- `depenses_pour_excel.csv` contient les mêmes données que le fichier de départ. La seule différence possible est la signature invisible (*BOM*) ajoutée par `"utf-8-sig"` au début du fichier, qui aide Excel à reconnaître l'UTF-8.
