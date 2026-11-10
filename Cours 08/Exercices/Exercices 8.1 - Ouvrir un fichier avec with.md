# Exercices — Ouvrir un fichier avec with (fiche 8.1)

> 📌 **À savoir** : Python Tutor ne gère pas les fichiers. Fais ces exercices dans VS Code.

## 🟢 Exercice 1 : Facile

**But** : Choisir le bon mode d'ouverture.

**Énoncé** : Pour chaque situation, donne le mode (`"r"`, `"w"` ou `"a"`) à utiliser, et dis ce qui arrive si le fichier **n'existe pas encore**.

| Situation | Mode? | Si le fichier n'existe pas? |
| --- | --- | --- |
| a. Afficher la liste des produits de `menu.txt` | | |
| b. Ajouter la vente qui vient d'être faite à la fin de `ventes.txt` | | |
| c. Réécrire `taches.txt` au complet avec la liste modifiée | | |
| d. Noter l'heure de chaque démarrage du programme dans `journal.txt` | | |
| e. Compter le nombre de lignes de `inscriptions.txt` | | |

> 🤔 **Réflexion** : un collègue ouvre `ventes.txt` en mode `"w"` pour ajouter une vente. Que perd-il?

## 🟢 Exercice 2 : Facile

**But** : Utiliser `with` correctement.

**Énoncé** : Ce programme fonctionne, mais il ne respecte pas les règles du cours. Réécris-le avec `with`, puis réponds aux questions.

```python
fichier = open("menu.txt", "r")
contenu = fichier.read()
fichier.close()
print(contenu)
print(fichier.read())
```

a. Quelles sont les **deux** améliorations à apporter à la première ligne?

b. Que se passe-t-il à la dernière ligne, et pourquoi?

c. Pourquoi `with` est-il plus sûr que `close()` si une erreur survient pendant la lecture?

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.1 - Ouvrir un fichier avec with](Solutions%208.1%20-%20Ouvrir%20un%20fichier%20avec%20with.md).
