# Solutions — Le format JSON (fiche « Module json »)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

a. Les 4 erreurs :

| Ligne | Erreur | Correction |
| --- | --- | --- |
| `'Traditionnel',` | Guillemets simples interdits en JSON | `"Traditionnel"` |
| `True,` | Les booléens JSON sont en minuscules | `true` |
| `["MI", 1.0],` | Virgule après le dernier élément du tableau | Retirer la virgule |
| `None` | La valeur vide JSON est `null` | `null` |

Fichier corrigé :

```json
[
    "Vive le vent",
    "Traditionnel",
    120,
    true,
    [
        ["MI", 0.5],
        ["MI", 0.5],
        ["MI", 1.0]
    ],
    null
]
```

b. Valeurs et types :

| Expression | Valeur | Type |
| --- | --- | --- |
| `chanson[0]` | `'Vive le vent'` | `str` |
| `chanson[2] + 10` | `130` | `int` (aucune conversion nécessaire!) |
| `chanson[3]` | `True` | `bool` |
| `len(chanson)` | `6` | `int` |
| `chanson[4]` | `[['MI', 0.5], ['MI', 0.5], ['MI', 1.0]]` | `list` (liste 2D) |
| `len(chanson[4])` | `3` | `int` |
| `chanson[4][2]` | `['MI', 1.0]` | `list` |
| `chanson[4][2][1]` | `1.0` | `float` |
| `chanson[5]` | `None` | `NoneType` |

- Pour descendre dans des listes imbriquées, on enchaîne les index : `[4]` choisit la liste des notes, `[2]` la troisième note, puis `[1]` sa durée.
- Une liste JSON peut mélanger des valeurs de types différents, exactement comme une liste Python.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
import json
from pathlib import Path

CHEMIN_FILMS = Path(__file__).parent / "films.json"


def main():
    films = []
    film = input("Film (Entrée pour terminer) : ").strip()
    while film != "":
        films.append(film)
        film = input("Film (Entrée pour terminer) : ").strip()

    with open(CHEMIN_FILMS, "w", encoding="utf-8") as fichier:
        json.dump(films, fichier, indent=4, ensure_ascii=False)
    print(f"{len(films)} film(s) sauvegardé(s) dans {CHEMIN_FILMS.name}.\n")

    with open(CHEMIN_FILMS, "r", encoding="utf-8") as fichier:
        films_relus = json.load(fichier)

    for i in range(len(films_relus)):
        print(f"{i + 1}. {films_relus[i]}")


main()
```

- La liste relue est une copie fidèle de l'originale : une seule ligne pour sauvegarder, une seule pour relire.
- Sans `ensure_ascii=False`, le fichier contient `"Là-haut"` : l'accent est remplacé par son code Unicode. Le programme relit quand même `Là-haut` correctement, mais le fichier est moins lisible pour un humain.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
import csv
import json
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_CSV = DOSSIER / "menu.csv"
CHEMIN_JSON = DOSSIER / "menu.json"

COL_PRODUIT = 0
COL_PRIX = 2
COL_STOCK = 3


def charger_menu_csv(chemin):
    menu = []
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)
        for champs in lecteur:
            if len(champs) == 4:
                menu.append([champs[0], champs[1], float(champs[2]), int(champs[3])])
    return menu


def trouver_plus_cher(menu):
    plus_cher = menu[0]
    for produit in menu:
        if produit[COL_PRIX] > plus_cher[COL_PRIX]:
            plus_cher = produit
    return plus_cher


def calculer_valeur_stock(menu):
    valeur = 0.0
    for produit in menu:
        valeur += produit[COL_PRIX] * produit[COL_STOCK]
    return valeur


def main():
    menu = charger_menu_csv(CHEMIN_CSV)
    with open(CHEMIN_JSON, "w", encoding="utf-8") as fichier:
        json.dump(menu, fichier, indent=4, ensure_ascii=False)
    print(f"{len(menu)} produits convertis dans {CHEMIN_JSON.name}.")

    # Relecture : aucun float() ni int() nécessaire
    with open(CHEMIN_JSON, "r", encoding="utf-8") as fichier:
        menu_relu = json.load(fichier)

    produit = trouver_plus_cher(menu_relu)
    print(f"Produit le plus cher : {produit[COL_PRODUIT]} ({produit[COL_PRIX]:.2f} $)")
    print(f"Valeur du stock : {calculer_valeur_stock(menu_relu):.2f} $")


main()
```

- Les conversions `float()` et `int()` ne sont faites **qu'une fois**, au moment de lire le CSV. Le JSON conserve ensuite les types.
- Dans `menu.json`, les prix et les stocks sont écrits **sans guillemets** : ce sont de vrais nombres.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
import json
from pathlib import Path

CHEMIN_CONTACTS = Path(__file__).parent / "contacts.json"

COL_NOM = 0
COL_COURRIEL = 1
COL_TELEPHONE = 2


def charger_contacts(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Avertissement : contacts.json est invalide. Carnet vide.")
        return []


def sauvegarder_contacts(chemin, contacts):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(contacts, fichier, indent=4, ensure_ascii=False)


def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le texte ne doit pas être vide.")
        texte = input(message).strip()
    return texte


def lire_courriel(message):
    courriel = input(message).strip()
    while "@" not in courriel:
        print("Erreur : le courriel doit contenir un @.")
        courriel = input(message).strip()
    return courriel


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


def afficher_contact(contact):
    print(f"{contact[COL_NOM]:<15}| {contact[COL_COURRIEL]:<26}| {contact[COL_TELEPHONE]}")


def afficher_contacts(contacts):
    if len(contacts) == 0:
        print("(carnet vide)")
    for i in range(len(contacts)):
        print(f"{i + 1:>2}. ", end="")
        afficher_contact(contacts[i])


def rechercher(contacts, texte):
    """Renvoie la liste des contacts dont le nom contient texte (sans tenir compte des majuscules)."""
    resultats = []
    for contact in contacts:
        if texte.lower() in contact[COL_NOM].lower():
            resultats.append(contact)
    return resultats


def main():
    contacts = charger_contacts(CHEMIN_CONTACTS)
    choix = -1
    while choix != 0:
        print("\n1. Afficher  2. Ajouter  3. Rechercher  4. Supprimer  0. Quitter")
        choix = lire_entier("Choix : ", 0, 4)

        if choix == 1:
            afficher_contacts(contacts)
        elif choix == 2:
            nom = lire_texte("Nom : ")
            courriel = lire_courriel("Courriel : ")
            telephone = lire_texte("Téléphone : ")
            contacts.append([nom, courriel, telephone])
            sauvegarder_contacts(CHEMIN_CONTACTS, contacts)
        elif choix == 3:
            resultats = rechercher(contacts, lire_texte("Rechercher : "))
            if len(resultats) == 0:
                print("Aucun contact trouvé.")
            for contact in resultats:
                afficher_contact(contact)
        elif choix == 4:
            if len(contacts) == 0:
                print("Le carnet est vide.")
            else:
                afficher_contacts(contacts)
                numero = lire_entier("Numéro à supprimer : ", 1, len(contacts))
                supprime = contacts.pop(numero - 1)
                sauvegarder_contacts(CHEMIN_CONTACTS, contacts)
                print(f"{supprime[COL_NOM]} supprimé.")


main()
```

- 🤔 **Réponse à la réflexion** : avec JSON, toute la liste 2D est sauvegardée et rechargée en **une seule ligne** chacune : pas d'en-tête à sauter, pas de `split()`, et une virgule dans un nom ne pose aucun problème.
- Le téléphone est gardé comme une **chaîne** : ce n'est pas un nombre sur lequel on calcule, il contient des tirets, et un numéro qui commence par 0 perdrait ce 0 s'il était converti en entier.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
import json
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_QUIZ = DOSSIER / "quiz.json"
CHEMIN_RECORD = DOSSIER / "record.json"

Q_TEXTE = 0
Q_CHOIX = 1
Q_REPONSE = 2

R_SCORE = 0
R_PSEUDO = 1


def charger_json(chemin, valeur_par_defaut):
    """Renvoie le contenu du fichier JSON, ou valeur_par_defaut s'il est absent ou invalide."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return valeur_par_defaut
    except json.JSONDecodeError:
        print(f"Avertissement : {chemin.name} est invalide.")
        return valeur_par_defaut


def sauvegarder_json(chemin, donnees):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)


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


def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le texte ne doit pas être vide.")
        texte = input(message).strip()
    return texte


def poser_question(numero, question):
    """Pose une question et renvoie True si la réponse est bonne."""
    print(f"\n{numero}. {question[Q_TEXTE]}")
    choix = question[Q_CHOIX]
    for i in range(len(choix)):
        print(f"   {i + 1}) {choix[i]}")

    reponse = lire_entier("Ta réponse : ", 1, len(choix)) - 1
    if reponse == question[Q_REPONSE]:
        print("Bonne réponse!")
        return True
    print(f"Mauvaise réponse. C'était : {choix[question[Q_REPONSE]]}")
    return False


def main():
    questions = charger_json(CHEMIN_QUIZ, [])
    if len(questions) == 0:
        print("Impossible de charger le quiz.")
        return

    score = 0
    for i in range(len(questions)):
        if poser_question(i + 1, questions[i]):
            score += 1

    print(f"\nScore : {score} / {len(questions)}")

    record = charger_json(CHEMIN_RECORD, [0, "personne"])
    print(f"Record actuel : {record[R_SCORE]} ({record[R_PSEUDO]})")
    if score > record[R_SCORE]:
        record[R_SCORE] = score
        record[R_PSEUDO] = lire_texte("🏆 Nouveau record! Ton pseudo : ")
        sauvegarder_json(CHEMIN_RECORD, record)


main()
```

- Le programme ne contient **aucune** question : tout vient du fichier. Ajouter une question ou un choix ne demande aucune modification du code. C'est la grande force des programmes **pilotés par les données**.
- La borne de `lire_entier()` dépend du nombre de choix de **chaque** question : `len(choix)`.
- On soustrait 1 à la réponse de l'utilisateur pour la comparer à l'**index** stocké dans le fichier.
- Une même paire de fonctions `charger_json()` / `sauvegarder_json()` sert pour les deux fichiers. Le paramètre `valeur_par_defaut` permet à chaque appel de choisir quoi renvoyer si le fichier est absent.
- Les constantes `Q_...` et `R_...` évitent les index « magiques ». Au cours 9, les dictionnaires permettront d'écrire plus clairement `question["choix"]` ou `record["pseudo"]`.
