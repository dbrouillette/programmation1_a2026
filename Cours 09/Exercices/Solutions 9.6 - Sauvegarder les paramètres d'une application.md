# Solutions — Sauvegarder les paramètres d'une application (fiche 9.6)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

a. `jeu.json` :

```json
{
    "nom": "Abby",
    "couleur": "vert",
    "largeur": 640,
    "hauteur": 480,
    "plein_ecran": false,
    "volume": 7,
    "musique": true
}
```

- `largeur`, `hauteur` et `volume` deviennent des **nombres** (pas de guillemets).
- `oui` / `non` deviennent des **booléens** `true` / `false`.
- Le commentaire disparaît : JSON n'en permet pas.

b. Dictionnaire Python :

```python
PARAMETRES_DEFAUT = {
    "nom": "",
    "couleur": "vert",
    "largeur": 800,
    "hauteur": 600,
    "plein_ecran": False,
    "volume": 5,
    "musique": True,
}
```

c. La fonction `charger_parametres()` de la fiche 9.6 compare le type de chaque valeur lue avec le type de la valeur par défaut. Avec `"5"` (une chaîne) comme valeur par défaut, un `"volume": 7` correct dans le fichier serait **refusé** (un `int` n'est pas une `str`), alors qu'un `"volume": "fort"` serait **accepté**. Le programme devrait en plus convertir le volume avec `int()` à chaque utilisation. Le type de la valeur par défaut sert de **référence** : il doit être le bon.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
import json
from datetime import datetime
from pathlib import Path

CHEMIN_STATISTIQUES = Path(__file__).parent / "statistiques.json"

STATISTIQUES_DEFAUT = {
    "nb_executions": 0,
    "derniere_execution": "",
}

def charger_statistiques():
    lus = {}
    try:
        with open(CHEMIN_STATISTIQUES, "r", encoding="utf-8") as fichier:
            lus = json.load(fichier)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Avertissement : statistiques.json invalide, remise à zéro.")

    statistiques = {}
    for cle in STATISTIQUES_DEFAUT:
        defaut = STATISTIQUES_DEFAUT[cle]
        valeur = lus.get(cle, defaut)
        if type(valeur) == type(defaut):
            statistiques[cle] = valeur
        else:
            statistiques[cle] = defaut
    return statistiques

def sauvegarder_statistiques(statistiques):
    with open(CHEMIN_STATISTIQUES, "w", encoding="utf-8") as fichier:
        json.dump(statistiques, fichier, indent=4, ensure_ascii=False)

def main():
    statistiques = charger_statistiques()

    if statistiques["derniere_execution"] == "":
        print("Première utilisation! Bienvenue.")
    else:
        print(f"Tu as utilisé ce programme {statistiques['nb_executions']} fois.")
        print(f"Dernière utilisation : {statistiques['derniere_execution']}")

    statistiques["nb_executions"] += 1
    statistiques["derniere_execution"] = datetime.now().strftime("%Y-%m-%d à %H:%M")
    sauvegarder_statistiques(statistiques)

main()
```

- Avec `{"nb_executions": "beaucoup"}`, la valeur n'est pas un `int` : elle est remplacée par `0`. La clé `derniere_execution` est absente : elle prend la valeur par défaut `""`. Le programme affiche donc « Première utilisation! », puis réécrit un fichier valide. **Il ne plante pas.**
- La date est sauvegardée sous forme de **chaîne** : JSON n'a pas de type « date ».

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

Voici les parties modifiées de `parametres_app.py`. Le reste du programme est inchangé.

```python
PARAMETRES_DEFAUT = {
    "nom_utilisateur": "",
    "theme": "clair",
    "volume": 5,
    "sons_actifs": True,
    "langue": "fr",                     # nouveau paramètre
}

THEMES = ("clair", "sombre", "contraste")
LANGUES = ("fr", "en")
```

Dans `charger_parametres()`, avec les autres validations :

```python
    if parametres["langue"] not in LANGUES:
        parametres["langue"] = PARAMETRES_DEFAUT["langue"]
```

Deux petites fonctions pour les messages :

```python
def saluer(parametres):
    if parametres["langue"] == "en":
        print(f"Hello {parametres['nom_utilisateur']}!")
    else:
        print(f"Bonjour {parametres['nom_utilisateur']}!")

def dire_au_revoir(parametres):
    if parametres["langue"] == "en":
        print(f"See you soon, {parametres['nom_utilisateur']}!")
    else:
        print(f"À bientôt, {parametres['nom_utilisateur']}!")
```

Dans `main()` :

```python
    saluer(parametres)                   # remplace le print("Bonjour ...")

    choix = -1
    while choix != 0:
        afficher_parametres(parametres)
        print("1. Changer de nom")
        print("2. Changer de thème")
        print("3. Changer le volume")
        print("4. Activer / désactiver les sons")
        print("5. Réinitialiser les paramètres")
        print("6. Changer de langue")
        print("0. Quitter")
        choix = lire_entier("Votre choix : ", 0, 6)

        # ... choix 1 à 5 inchangés ...
        elif choix == 6:
            for i in range(len(LANGUES)):
                print(f"  {i + 1}. {LANGUES[i]}")
            numero = lire_entier("Langue : ", 1, len(LANGUES))
            parametres["langue"] = LANGUES[numero - 1]

        if choix != 0:
            sauvegarder_parametres(parametres)

    dire_au_revoir(parametres)           # remplace le print("À bientôt ...")
```

Sans oublier une ligne dans `afficher_parametres()` :

```python
    print(f"  Langue      : {parametres['langue']}")
```

- **Pourquoi l'ancien fichier fonctionne** : `charger_parametres()` parcourt les clés de `PARAMETRES_DEFAUT`, pas celles du fichier. Pour `langue`, absente du fichier, `lus.get("langue", "fr")` renvoie la valeur par défaut.
- **À la première sauvegarde**, le dictionnaire complet (incluant `langue`) est écrit : le fichier est mis à jour automatiquement vers la nouvelle version. Aucune conversion manuelle n'est nécessaire.

## 🔴 Exercice 4 : Moyen-Difficile

### ✅ Solution 4

```python
import json
from pathlib import Path

CHEMIN_PARAMETRES = Path(__file__).parent / "parametres.json"

PARAMETRES_DEFAUT = {
    "fichiers_recents": [],
    "nb_recents_max": 5,
}
NB_RECENTS_MIN = 1
NB_RECENTS_LIMITE = 20

def charger_parametres():
    lus = {}
    try:
        with open(CHEMIN_PARAMETRES, "r", encoding="utf-8") as fichier:
            lus = json.load(fichier)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Avertissement : parametres.json invalide, valeurs par défaut utilisées.")
    if type(lus) != dict:
        lus = {}

    parametres = {}
    for cle in PARAMETRES_DEFAUT:
        defaut = PARAMETRES_DEFAUT[cle]
        valeur = lus.get(cle, defaut)
        if type(valeur) == type(defaut):
            parametres[cle] = valeur
        else:
            parametres[cle] = defaut

    # Validation de l'intervalle
    if not NB_RECENTS_MIN <= parametres["nb_recents_max"] <= NB_RECENTS_LIMITE:
        parametres["nb_recents_max"] = PARAMETRES_DEFAUT["nb_recents_max"]

    # Validation du contenu de la liste : seulement des chaînes non vides, sans doublon
    recents_valides = []
    for element in parametres["fichiers_recents"]:
        if type(element) == str and element.strip() != "" and element not in recents_valides:
            recents_valides.append(element)
    parametres["fichiers_recents"] = recents_valides[:parametres["nb_recents_max"]]

    return parametres

def sauvegarder_parametres(parametres):
    with open(CHEMIN_PARAMETRES, "w", encoding="utf-8") as fichier:
        json.dump(parametres, fichier, indent=4, ensure_ascii=False)

def ajouter_fichier_recent(parametres, nom_fichier):
    """Place nom_fichier en tête de la liste des récents, sans doublon, en respectant le maximum."""
    recents = parametres["fichiers_recents"]
    if nom_fichier in recents:
        recents.remove(nom_fichier)
    recents.insert(0, nom_fichier)
    while len(recents) > parametres["nb_recents_max"]:
        recents.pop()

def afficher_recents(parametres):
    print("\nFichiers récents :")
    recents = parametres["fichiers_recents"]
    if len(recents) == 0:
        print("  (aucun)")
    for i in range(len(recents)):
        print(f"  {i + 1}. {recents[i]}")
    print()

def main():
    parametres = charger_parametres()

    afficher_recents(parametres)
    nom = input("Fichier à ouvrir (Entrée pour quitter) : ").strip()
    while nom != "":
        print(f"Ouverture de {nom}...")
        ajouter_fichier_recent(parametres, nom)
        sauvegarder_parametres(parametres)

        afficher_recents(parametres)
        nom = input("Fichier à ouvrir (Entrée pour quitter) : ").strip()

main()
```

- `ajouter_fichier_recent()` **modifie** la liste reçue (comme vu en 7.3 : une liste passée en argument peut être modifiée par la fonction). Elle n'a donc rien à renvoyer.
- Retirer puis réinsérer en tête règle d'un coup le cas du doublon et du déplacement.
- Une boucle `while` plutôt qu'un simple `if` pour le maximum : si l'utilisateur a réduit `nb_recents_max` à la main dans le fichier, plusieurs éléments peuvent devoir être retirés. (La validation au chargement s'en occupe déjà, mais la fonction reste correcte en toutes circonstances.)
- La validation de la liste montre qu'un paramètre de type `list` doit aussi être vérifié **élément par élément** : le type de la liste ne garantit rien sur son contenu.
