# Solutions — Listes de dictionnaires et données imbriquées (fiche 9.3)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Expression | Valeur | Type |
| --- | --- | --- |
| `len(bibliotheque)` | `2` | `int` |
| `bibliotheque[1]` | `{'titre': 'Au clair de la lune', 'auteur': 'Traditionnel', 'notes': []}` | `dict` |
| `bibliotheque[0]["auteur"]` | `'J. Pierpont'` | `str` |
| `bibliotheque[0]["notes"][1]` | `{'note': 'SOL4', 'intensite': 100, 'duree': 600}` | `dict` |
| `bibliotheque[0]["notes"][1]["duree"] * 2` | `1200` | `int` |
| `len(bibliotheque[1]["notes"])` | `0` | `int` |
| `bibliotheque[0]["titre"][0]` | `'V'` | `str` (premier caractère du titre) |
| `bibliotheque["titre"]` | ❌ `TypeError: list indices must be integers or slices, not str` | |
| `bibliotheque[1]["notes"][0]` | ❌ `IndexError: list index out of range` | |
| `"notes" in bibliotheque[1]` | `True` | `bool` (la clé existe, même si la liste est vide) |

- `bibliotheque` est une **liste** : on y accède avec un index entier, jamais avec une clé. Il faut d'abord choisir une chanson : `bibliotheque[0]["titre"]`.
- La liste de notes d'*Au clair de la lune* est vide : elle n'a pas d'élément no 0.
- Le type de chaque niveau dicte l'accès suivant : liste → `[index]`, dictionnaire → `["clé"]`, chaîne → `[index]` d'un caractère.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
CHANSON_2D = [
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["MI4", 80, 300], ["MI4", 100, 600],
    ["MI4", 80, 300], ["SOL4", 80, 300], ["DO4", 90, 450], ["RE4", 60, 150],
    ["MI4", 100, 1200],
]


def convertir_en_dictionnaires(chanson_2d):
    """Renvoie la chanson sous forme de liste de dictionnaires {note, intensite, duree}."""
    chanson = []
    for rangee in chanson_2d:
        chanson.append({"note": rangee[0], "intensite": rangee[1], "duree": rangee[2]})
    return chanson


def calculer_duree_totale(chanson):
    total = 0
    for note in chanson:
        total += note["duree"]
    return total


def filtrer_par_intensite(chanson, intensite_min):
    """Renvoie la liste des notes dont l'intensité est au moins intensite_min."""
    resultat = []
    for note in chanson:
        if note["intensite"] >= intensite_min:
            resultat.append(note)
    return resultat


def main():
    chanson = convertir_en_dictionnaires(CHANSON_2D)
    print(chanson[0])
    print(f"{len(chanson)} notes, {calculer_duree_totale(chanson)} ms")

    fortes = filtrer_par_intensite(chanson, 90)
    print(f"Notes à 90 % ou plus ({len(fortes)}) :")
    for note in fortes:
        print(f"  {note['note']:<5}{note['intensite']:>4} %{note['duree']:>6} ms")


main()
```

- `convertir_en_dictionnaires()` crée un nouveau dictionnaire à chaque tour de boucle, directement dans `append()`.
- `note["duree"]` se lit tout seul, alors que `rangee[2]` obligeait à se souvenir de l'ordre des colonnes.
- `filtrer_par_intensite()` renvoie des dictionnaires **déjà existants** : ce ne sont pas des copies, mais les mêmes notes que dans `chanson`.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
import csv
import json
from pathlib import Path

from utilitaires import lire_texte

DOSSIER = Path(__file__).parent
CHEMIN_NOTES = DOSSIER / "notes.csv"
CHEMIN_CHANSON = DOSSIER / "chanson.json"

FREQUENCES = {
    "DO4": 262, "RE4": 294, "MI4": 330, "FA4": 349,
    "SOL4": 392, "LA4": 440, "SI4": 494, "DO5": 523,
}
SILENCE = "-"
LARGEUR_LCD = 16


def lire_notes_csv(chemin):
    """Renvoie la liste des notes valides du fichier CSV, sous forme de dictionnaires.

    Les lignes invalides sont ignorées avec un avertissement.
    """
    notes = []
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:
        numero = 1                                  # l'en-tête est la ligne 1
        for rangee in csv.DictReader(fichier):
            numero += 1
            if None in rangee.values():             # DictReader met None si une colonne manque
                print(f"Ligne {numero} ignorée : valeur manquante.")
            else:
                try:
                    note = rangee["note"].strip().upper()
                    intensite = int(rangee["intensite"])
                    duree = int(rangee["duree"])
                    if note != SILENCE and note not in FREQUENCES:
                        print(f"Ligne {numero} ignorée : note « {note} » inconnue.")
                    elif not 0 <= intensite <= 100 or not 50 <= duree <= 2000:
                        print(f"Ligne {numero} ignorée : intensité ou durée hors limites.")
                    else:
                        notes.append({"note": note, "intensite": intensite, "duree": duree})
                except ValueError:
                    print(f"Ligne {numero} ignorée : intensité ou durée non numérique.")
    return notes


def afficher_lcd(chanson):
    print("+" + "-" * LARGEUR_LCD + "+")
    print(f"|{chanson['titre'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print(f"|{chanson['auteur'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print("+" + "-" * LARGEUR_LCD + "+")


def sauvegarder_chanson(chemin, chanson):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(chanson, fichier, indent=4, ensure_ascii=False)


def main():
    notes = lire_notes_csv(CHEMIN_NOTES)
    print(f"{len(notes)} notes lues dans {CHEMIN_NOTES.name}.")

    chanson = {
        "titre": lire_texte("Titre : "),
        "auteur": lire_texte("Auteur : "),
        "notes": notes,
    }
    sauvegarder_chanson(CHEMIN_CHANSON, chanson)

    duree = 0
    for note in chanson["notes"]:
        duree += note["duree"]
    print(f"Chanson sauvegardée dans {CHEMIN_CHANSON.name} ({duree / 1000:.1f} s).")
    afficher_lcd(chanson)


main()
```

- `csv.DictReader` utilise l'en-tête `note,intensite,duree` comme clés : `rangee["duree"]` plutôt que `champs[2]`.
- Quand une ligne a moins de colonnes que l'en-tête, `DictReader` met `None` pour les colonnes manquantes. `None in rangee.values()` le détecte avant toute conversion; sinon, `int(None)` lèverait une `TypeError`.
- La note est normalisée (`strip()` et `upper()`) : `mi4` dans le fichier est accepté.
- La chanson sauvegardée contient de **vrais nombres** : le JSON n'aura plus jamais besoin de conversion.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
import csv
import json
from pathlib import Path

from utilitaires import lire_entier, lire_texte, lire_oui_non

DOSSIER = Path(__file__).parent
CHEMIN_BIBLIOTHEQUE = DOSSIER / "bibliotheque.json"
CHEMIN_NOTES = DOSSIER / "notes.csv"

FREQUENCES = {
    "DO4": 262, "RE4": 294, "MI4": 330, "FA4": 349,
    "SOL4": 392, "LA4": 440, "SI4": 494, "DO5": 523,
}
SILENCE = "-"


# lire_notes_csv(chemin) : identique à l'exercice 3


def charger_bibliotheque(chemin):
    """Renvoie la liste des chansons, ou une liste vide si le fichier est absent ou invalide."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Avertissement : bibliotheque.json est invalide. Bibliothèque vide.")
        return []


def sauvegarder_bibliotheque(chemin, bibliotheque):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(bibliotheque, fichier, indent=4, ensure_ascii=False)


def calculer_duree(chanson):
    """Renvoie la durée totale de la chanson, en millisecondes."""
    total = 0
    for note in chanson["notes"]:
        total += note["duree"]
    return total


def afficher_catalogue(bibliotheque):
    print()
    if len(bibliotheque) == 0:
        print("(bibliothèque vide)")
    for i in range(len(bibliotheque)):
        chanson = bibliotheque[i]
        print(f"{i + 1:>2}. {chanson['titre']:<22}{chanson['auteur']:<16}"
              f"{len(chanson['notes']):>4} notes{calculer_duree(chanson) / 1000:>6.1f} s")
    print()


def chercher_titre(bibliotheque, titre):
    """Renvoie l'index de la chanson qui porte ce titre (sans tenir compte de la casse), ou -1."""
    for i in range(len(bibliotheque)):
        if bibliotheque[i]["titre"].lower() == titre.lower():
            return i
    return -1


def importer_chanson(bibliotheque):
    notes = lire_notes_csv(CHEMIN_NOTES)
    if len(notes) == 0:
        print("Aucune note valide : importation annulée.")
        return
    titre = lire_texte("Titre : ")
    if chercher_titre(bibliotheque, titre) != -1:
        print(f"Une chanson s'appelle déjà « {titre} ». Importation annulée.")
        return
    auteur = lire_texte("Auteur : ")
    bibliotheque.append({"titre": titre, "auteur": auteur, "notes": notes})
    sauvegarder_bibliotheque(CHEMIN_BIBLIOTHEQUE, bibliotheque)
    print(f"« {titre} » ajoutée ({len(notes)} notes).")


def supprimer_chanson(bibliotheque):
    afficher_catalogue(bibliotheque)
    numero = lire_entier("Numéro de la chanson à supprimer : ", 1, len(bibliotheque))
    titre = bibliotheque[numero - 1]["titre"]
    if lire_oui_non(f"Supprimer « {titre} »? (o/n) : "):
        bibliotheque.pop(numero - 1)
        sauvegarder_bibliotheque(CHEMIN_BIBLIOTHEQUE, bibliotheque)
        print(f"« {titre} » supprimée.")


def main():
    bibliotheque = charger_bibliotheque(CHEMIN_BIBLIOTHEQUE)
    choix = -1
    while choix != 0:
        print("1. Catalogue  2. Importer notes.csv  3. Supprimer  0. Quitter")
        choix = lire_entier("Choix : ", 0, 3)
        if choix == 1:
            afficher_catalogue(bibliotheque)
        elif choix == 2:
            importer_chanson(bibliotheque)
        elif choix == 3:
            if len(bibliotheque) == 0:
                print("La bibliothèque est vide.")
            else:
                supprimer_chanson(bibliotheque)


main()
```

- `lire_notes_csv()` est copiée de l'exercice 3, sans modification. Dans un vrai projet, on la placerait dans un module (fiche 7.8) pour l'importer plutôt que de la recopier.
- Toute la bibliothèque (une liste de dictionnaires qui contiennent des listes de dictionnaires!) est sauvegardée et rechargée en **une seule ligne** chacune.
- `calculer_duree()` cache les détails de la structure : le catalogue reste lisible.
- `importer_chanson()` utilise des `return` pour **annuler** l'importation dès qu'un problème est détecté, sans imbriquer les `if`.
- La sauvegarde après chaque modification protège la bibliothèque si le programme est fermé brusquement.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

```python
import csv
import json
from pathlib import Path

from utilitaires import lire_entier

DOSSIER = Path(__file__).parent
CHEMIN_BIBLIOTHEQUE = DOSSIER / "bibliotheque.json"
DOSSIER_CLE = DOSSIER / "cle_usb"
COLONNES = ["note", "intensite", "duree"]


def charger_bibliotheque(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def exporter_chanson(chanson, dossier):
    """Écrit notes.csv et titre.txt dans le dossier (créé au besoin)."""
    dossier.mkdir(exist_ok=True)
    with open(dossier / "notes.csv", "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.DictWriter(fichier, fieldnames=COLONNES)
        ecrivain.writeheader()
        ecrivain.writerows(chanson["notes"])
    with open(dossier / "titre.txt", "w", encoding="utf-8") as fichier:
        fichier.write(f"{chanson['titre']}\n{chanson['auteur']}\n")


def relire_notes(chemin):
    notes = []
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:
        for rangee in csv.DictReader(fichier):
            notes.append({
                "note": rangee["note"],
                "intensite": int(rangee["intensite"]),
                "duree": int(rangee["duree"]),
            })
    return notes


def main():
    bibliotheque = charger_bibliotheque(CHEMIN_BIBLIOTHEQUE)
    if len(bibliotheque) == 0:
        print("Aucune chanson à exporter.")
        return

    for i in range(len(bibliotheque)):
        print(f"{i + 1}. {bibliotheque[i]['titre']}")
    numero = lire_entier("Chanson à exporter : ", 1, len(bibliotheque))
    chanson = bibliotheque[numero - 1]

    exporter_chanson(chanson, DOSSIER_CLE)
    print(f"« {chanson['titre']} » exportée dans le dossier {DOSSIER_CLE.name}.")

    # Vérification : on relit le fichier et on compare avec l'original
    if relire_notes(DOSSIER_CLE / "notes.csv") == chanson["notes"]:
        print(f"✅ Vérification réussie : {len(chanson['notes'])} notes identiques.")
    else:
        print("❌ Le fichier exporté ne correspond pas à la chanson!")


main()
```

- `writerows()` écrit directement la liste de dictionnaires : les clés de chaque note correspondent exactement aux `fieldnames`.
- `titre.txt` est un simple fichier texte de deux lignes (fiche 8.2) : tous les formats vus au cours 8 cohabitent.
- La vérification compare deux **listes de dictionnaires** avec `==`. Elle échouerait si on oubliait de convertir l'intensité et la durée en `int` à la relecture : `"70" == 70` est faux.
- Dans le TP3, c'est exactement ce dossier (`notes.csv` + `titre.txt`) que le Raspberry Pi lira sur la clé USB.
