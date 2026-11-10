# Solutions — Sauvegarder et recharger une liste (fiche 8.5)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_NOTES = DOSSIER / "notes.txt"

print(f"Dossier du programme : {DOSSIER.name}")
print(f"Fichier cherché      : {CHEMIN_NOTES.name}")
print(f"Le fichier existe?   {CHEMIN_NOTES.exists()}")

with open(CHEMIN_NOTES, "a", encoding="utf-8") as fichier:
    fichier.write("Une ligne de plus\n")

with open(CHEMIN_NOTES, "r", encoding="utf-8") as fichier:
    nb_lignes = 0
    for ligne in fichier:
        nb_lignes += 1
print(f"notes.txt contient maintenant {nb_lignes} ligne(s).")
```

- `Path(__file__).parent` est le dossier qui contient le programme, peu importe d'où il est lancé : c'est toujours le même `notes.txt` qui est modifié.
- Avec un simple `open("notes.txt", "a", ...)`, le fichier serait créé dans le **dossier courant** : lancé depuis un autre dossier, le programme écrirait dans un autre `notes.txt`!
- Le mode `"a"` crée le fichier s'il n'existe pas encore.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
from pathlib import Path

CHEMIN_EPICERIE = Path(__file__).parent / "epicerie.txt"

def charger_epicerie(chemin):
    """Renvoie la liste des articles, ou une liste vide si le fichier n'existe pas."""
    articles = []
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                article = ligne.strip()
                if article != "":
                    articles.append(article)
    except FileNotFoundError:
        pass
    return articles

def sauvegarder_epicerie(chemin, articles):
    with open(chemin, "w", encoding="utf-8") as fichier:
        for article in articles:
            fichier.write(f"{article}\n")

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

def afficher_epicerie(articles):
    print("\nListe d'épicerie :")
    if len(articles) == 0:
        print("  (vide)")
    for i in range(len(articles)):
        print(f"  {i + 1}. {articles[i]}")
    print()

def main():
    articles = charger_epicerie(CHEMIN_EPICERIE)
    choix = -1
    while choix != 0:
        afficher_epicerie(articles)
        print("1. Ajouter  2. Retirer  0. Quitter")
        choix = lire_entier("Choix : ", 0, 2)

        if choix == 1:
            articles.append(lire_texte("Article : "))
            sauvegarder_epicerie(CHEMIN_EPICERIE, articles)
        elif choix == 2:
            if len(articles) == 0:
                print("La liste est vide : rien à retirer.")
            else:
                numero = lire_entier("Numéro de l'article à retirer : ", 1, len(articles))
                articles.pop(numero - 1)
                sauvegarder_epicerie(CHEMIN_EPICERIE, articles)

main()
```

- Le programme **travaille en mémoire** avec une liste; le fichier ne sert qu'au chargement et à la sauvegarde.
- La sauvegarde après **chaque** modification protège les données si le programme est fermé brusquement.
- La borne maximale de `lire_entier()` dépend de la taille actuelle de la liste : impossible de retirer un article qui n'existe pas.

## 🔴 Exercice 3 : Moyen-Difficile

### ✅ Solution 3

```python
from pathlib import Path

CHEMIN_SCORES = Path(__file__).parent / "meilleurs_scores.txt"
NB_SCORES_MAX = 5
SCORE_MAX = 99_999

def charger_scores(chemin):
    scores = []
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne != "":
                    scores.append(int(ligne))
    except FileNotFoundError:
        pass
    return scores

def sauvegarder_scores(chemin, scores):
    with open(chemin, "w", encoding="utf-8") as fichier:
        for score in scores:
            fichier.write(f"{score}\n")

def trouver_position(scores, nouveau):
    """Renvoie l'index où insérer nouveau pour garder la liste en ordre décroissant."""
    position = 0
    while position < len(scores) and scores[position] >= nouveau:
        position += 1
    return position

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

def afficher_palmares(scores):
    print("\n--- Palmarès ---")
    for i in range(len(scores)):
        print(f"{i + 1}. {scores[i]:>5}")

def main():
    scores = charger_scores(CHEMIN_SCORES)
    nouveau = lire_entier("Ton score : ", 0, SCORE_MAX)

    position = trouver_position(scores, nouveau)
    if position < NB_SCORES_MAX:
        scores.insert(position, nouveau)
        scores = scores[:NB_SCORES_MAX]
        sauvegarder_scores(CHEMIN_SCORES, scores)
        if position == 0:
            print("Nouveau record!")
        else:
            print(f"Tu entres au palmarès en position {position + 1}!")
    else:
        print("Pas assez pour le palmarès. Réessaie!")

    afficher_palmares(scores)

main()
```

- `trouver_position()` avance tant que les scores existants sont plus grands ou égaux. En cas d'égalité, le nouveau score se place donc **après** l'ancien : premier arrivé, premier servi.
- La condition `position < len(scores)` doit être testée **en premier** : si elle est fausse, Python n'évalue pas `scores[position]`, ce qui évite une `IndexError`.
- Si la position est 5 ou plus, le score ne fait pas partie du palmarès et le fichier n'est pas modifié.
- Fichier absent ou incomplet : la liste a moins de 5 scores, donc n'importe quel score y entre.
