# Solutions — Écrire dans un fichier texte (fiche 8.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```python
from pathlib import Path

DOSSIER = Path(__file__).parent


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


def ecrire_table(chemin, nombre):
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(f"Table de {nombre}\n")
        for i in range(1, 11):
            fichier.write(f"{i:>2} x {nombre} = {i * nombre:>2}\n")


def main():
    nombre = lire_entier("Quelle table (1 à 12)? ", 1, 12)
    nom_fichier = f"table_{nombre}.txt"
    ecrire_table(DOSSIER / nom_fichier, nombre)
    print(f"Table de {nombre} écrite dans {nom_fichier}.")


main()
```

- Chaque `write()` se termine par `\n`, sinon toute la table serait sur une seule ligne.
- Le formatage `:>2` aligne les nombres, exactement comme avec `print()`. Pour la table de 12, `:>3` serait plus joli pour le produit.
- Relancer le programme avec le même nombre **remplace** le fichier : c'est le comportement du mode `"w"`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from datetime import datetime
from pathlib import Path

CHEMIN_JOURNAL = Path(__file__).parent / "journal.txt"


def lire_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : le message ne doit pas être vide.")
        texte = input(message).strip()
    return texte


def ajouter_entree(chemin, message):
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(chemin, "a", encoding="utf-8") as fichier:
        fichier.write(f"{horodatage} | {message}\n")


def afficher_journal(chemin):
    print("\n--- Journal ---")
    with open(chemin, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")


def main():
    message = lire_texte("Message : ")
    ajouter_entree(CHEMIN_JOURNAL, message)
    afficher_journal(CHEMIN_JOURNAL)


main()
```

- Le mode `"a"` crée le fichier à la première exécution, puis ajoute à la fin aux exécutions suivantes.
- On n'a pas besoin de gérer `FileNotFoundError` à la lecture : le fichier vient tout juste d'être créé ou complété.
- `end=""` évite une ligne vide de trop : le contenu lu se termine déjà par `\n`.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

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

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
from pathlib import Path

DOSSIER = Path(__file__).parent
CHEMIN_SOURCE = DOSSIER / "poeme.txt"
CHEMIN_DESTINATION = DOSSIER / "poeme_numerote.txt"


def numeroter(chemin_source, chemin_destination):
    """Écrit une copie numérotée du fichier source. Renvoie (nb_lignes, nb_mots)."""
    nb_lignes = 0
    nb_mots = 0
    with open(chemin_source, "r", encoding="utf-8") as source, \
         open(chemin_destination, "w", encoding="utf-8") as destination:
        for ligne in source:
            texte = ligne.strip()
            if texte == "":
                destination.write("\n")
            else:
                nb_lignes += 1
                nb_mots += len(texte.split())
                destination.write(f"{nb_lignes:>3} | {texte}\n")
        destination.write(f"--- {nb_lignes} lignes, {nb_mots} mots ---\n")
    return nb_lignes, nb_mots


def main():
    try:
        nb_lignes, nb_mots = numeroter(CHEMIN_SOURCE, CHEMIN_DESTINATION)
        print(f"{CHEMIN_DESTINATION.name} créé : {nb_lignes} lignes, {nb_mots} mots.")
    except FileNotFoundError:
        print(f"Erreur : {CHEMIN_SOURCE.name} est introuvable.")


main()
```

- Les deux fichiers sont ouverts dans le même `with`; le `\` permet de continuer l'instruction sur la ligne suivante.
- `split()` **sans argument** découpe sur n'importe quel nombre d'espaces : c'est la bonne façon de compter des mots.
- La fonction renvoie un tuple, comme vu en 7.4, pour que le programme principal puisse afficher une confirmation.

## 🔴 Exercice 5 : Moyen-Difficile

### ✅ Solution 5

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
