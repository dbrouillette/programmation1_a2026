# Solutions — Ouvrir un fichier avec with (fiche 8.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Situation | Mode | Si le fichier n'existe pas |
| --- | --- | --- |
| a. Afficher les produits | `"r"` | `FileNotFoundError` |
| b. Ajouter une vente à la fin | `"a"` | Le fichier est créé |
| c. Réécrire la liste au complet | `"w"` | Le fichier est créé |
| d. Noter chaque démarrage | `"a"` | Le fichier est créé |
| e. Compter les lignes | `"r"` | `FileNotFoundError` |

- Lire : `"r"`. Ajouter sans rien effacer (journal, historique) : `"a"`. Remplacer tout le contenu (sauvegarde) : `"w"`.
- 🤔 **Réponse à la réflexion** : le mode `"w"` **efface** le fichier dès l'ouverture. Toutes les ventes précédentes sont perdues; il ne reste que la nouvelle.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
with open("menu.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()

print(contenu)
```

a. Utiliser `with` (le fichier est refermé automatiquement) et préciser `encoding="utf-8"` (fiche 8.2).

b. `ValueError: I/O operation on closed file.` : le fichier est déjà fermé. On garde ce qu'on a lu dans une variable (`contenu`) et on travaille avec elle; la dernière ligne est donc retirée.

c. Si une erreur survient entre `open()` et `close()`, la ligne `close()` n'est jamais atteinte et le fichier reste ouvert. Avec `with`, le fichier est fermé à la fin du bloc **même en cas d'erreur**.
