# Récapitulatif du cours 8 : les fichiers

Tout le cours 8 sur une page. Pour les détails et les exemples, retourne aux fiches : [8.1 - Ouvrir un fichier avec `with`](8.1%20-%20Ouvrir%20un%20fichier%20avec%20with.md), [8.2 - L'encodage des caractères](8.2%20-%20L'encodage%20des%20caractères.md), [8.3 - Lire un fichier texte](8.3%20-%20Lire%20un%20fichier%20texte.md), [8.4 - Écrire dans un fichier texte](8.4%20-%20Écrire%20dans%20un%20fichier%20texte.md), [8.5 - Sauvegarder et recharger une liste](8.5%20-%20Sauvegarder%20et%20recharger%20une%20liste.md) et [8.6 - Les fichiers CSV à la main](8.6%20-%20Les%20fichiers%20CSV%20à%20la%20main.md).

## 1. La recette de base

Peu importe ce qu'on fait, on ouvre **toujours** un fichier de la même façon :

```python
with open(chemin, mode, encoding="utf-8") as fichier:
    ...   # tout le travail sur le fichier se fait ici
# ici, le fichier est déjà fermé
```

| Morceau | À retenir |
| --- | --- |
| `with` | Ferme le fichier automatiquement à la fin du bloc, même en cas d'erreur |
| `chemin` | `"menu.txt"` : cherché dans le dossier **courant**. Plus fiable : `Path(__file__).parent / "menu.txt"` |
| `mode` | `"r"` lire, `"w"` réécrire, `"a"` ajouter (voir la section 2) |
| `encoding="utf-8"` | **Toujours** le mettre. Des `Ã©` à l'écran = mauvais encodage |

## 2. Les trois modes

| Mode | Je veux… | Si le fichier n'existe pas | Si le fichier existe |
| --- | --- | --- | --- |
| `"r"` | **Lire** | ❌ `FileNotFoundError` | On lit son contenu |
| `"w"` | **Réécrire** au complet (sauvegarde) | Il est créé | ⚠️ Son contenu est **effacé** |
| `"a"` | **Ajouter** à la fin (historique) | Il est créé | On écrit à la suite |

## 3. Lire et écrire : texte et CSV

| Je veux… | Fichier texte (8.3, 8.4) | Fichier CSV (8.6) |
| --- | --- | --- |
| **Lire tout d'un coup** | `contenu = fichier.read()` (une seule chaîne) | — |
| **Lire ligne par ligne** | `for ligne in fichier:` | `for ligne in fichier:` |
| **Nettoyer la ligne** | `ligne.strip()` | `ligne.strip()` |
| **Découper en colonnes** | — | `champs = ligne.strip().split(",")` |
| **Sauter l'en-tête** | — | `fichier.readline()` avant la boucle |
| **On obtient** | Une chaîne par ligne | Une liste de chaînes par ligne → une **liste 2D** |
| **Écrire une ligne** | `fichier.write(f"{valeur}\n")` | `fichier.write(f"{nom},{prix:.2f},{stock}\n")` |

> 📌 **À retenir** : tout ce qu'on lit dans un fichier est une **chaîne**, comme avec `input()`. Pour calculer, on convertit avec `int()` ou `float()`.

## 4. Les petites méthodes qui reviennent partout

| Méthode | Fait… | Exemple |
| --- | --- | --- |
| `strip()` | Enlève les espaces et le `\n` au début et à la fin | `"Latté\n".strip()` → `"Latté"` |
| `split(",")` | Découpe une chaîne en liste | `"a,b,c".split(",")` → `["a", "b", "c"]` |
| `",".join(liste)` | Assemble une liste de **chaînes** en une chaîne | `",".join(["a", "b"])` → `"a,b"` |
| `readline()` | Lit **une seule** ligne | Pour sauter l'en-tête d'un CSV |
| `write(chaine)` | Écrit **exactement** la chaîne, sans `\n` | `fichier.write("Latté\n")` |
| `print(..., file=fichier)` | Écrit dans le fichier, avec le `\n` | `print("Latté", file=fichier)` |

## 5. Le patron à suivre : charger / sauvegarder

```python
def charger_taches():
    taches = []
    try:
        with open(CHEMIN, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                tache = ligne.strip()
                if tache != "":
                    taches.append(tache)
    except FileNotFoundError:
        pass                     # première exécution : pas encore de fichier
    return taches


def sauvegarder_taches(taches):
    with open(CHEMIN, "w", encoding="utf-8") as fichier:
        for tache in taches:
            fichier.write(f"{tache}\n")
```

On **charge** au démarrage, on travaille avec des **listes** en mémoire, puis on **sauvegarde** à la fin.

## 6. Les erreurs fréquentes

| Erreur ou symptôme | Cause | Solution |
| --- | --- | --- |
| `FileNotFoundError` | Le fichier n'existe pas, ou Python le cherche dans le mauvais dossier | `try` / `except`, et `Path(__file__).parent / "fichier"` |
| `Ã©`, `Ã¨` au lieu des accents | Fichier UTF-8 relu avec le mauvais encodage | `encoding="utf-8"` |
| `UnicodeDecodeError` | Le fichier n'est pas en UTF-8 (souvent cp1252, venant d'Excel) | Le rouvrir dans VS Code en Windows 1252, puis l'enregistrer en UTF-8 |
| Une ligne vide entre chaque ligne affichée | Le `\n` de la ligne + celui de `print()` | `ligne.strip()` |
| Tout est écrit sur une seule ligne | `write()` n'ajoute pas de `\n` | Terminer chaque chaîne par `\n` |
| `TypeError` avec `write()` ou `join()` | On leur a donné un nombre | Convertir : `f"{nombre}"` ou `str(nombre)` |
| `ValueError` en lisant un CSV | On essaie de convertir l'en-tête (`float("prix")`) | Sauter l'en-tête |
| Le fichier est vide après l'exécution! | Ouvert en `"w"`, ce qui l'efface aussitôt | `"r"` pour lire, `"a"` pour ajouter |
| `ValueError: I/O operation on closed file` | On utilise le fichier après le bloc `with` | Faire tout le travail dans le bloc |
| Une valeur coupée en deux dans un CSV | La valeur contient une virgule (`Muffin, bleuets`) | Éviter les virgules dans les valeurs, ou utiliser le module `csv` |

> 💡 **CSV d'Excel en français?** Le séparateur est le point-virgule et la virgule sert de point décimal : `split(";")`, puis `float(texte.replace(",", "."))`.

## 7. Pour aller plus loin : les outils

Deux fiches des [outils](../Outils/) font le même travail plus rapidement :

| Fiche | Ce qu'elle apporte | Ce qui change |
| --- | --- | --- |
| [Module csv](../Outils/Fichiers%20CSV%20-%20Module%20csv.md) | Gère les virgules et les guillemets dans les valeurs | `csv.reader(fichier)` remplace `strip()` + `split()`; ouvrir avec `newline=""` |
| [Module json](../Outils/Fichiers%20JSON%20-%20Module%20json.md) | Relit une liste **avec ses types** : plus de conversion | `json.dump(donnees, fichier)` pour sauvegarder, `json.load(fichier)` pour relire |
