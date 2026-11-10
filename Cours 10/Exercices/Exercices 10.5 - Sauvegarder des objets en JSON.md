# Exercices — Sauvegarder des objets en JSON (fiche 10.5)

> 📌 **À savoir** : applique le patron des fiches 10.5 et 10.6 : une méthode `vers_dict()` dans la classe, une fonction `..._depuis_dict()` pour le chemin inverse, une fonction de chargement qui **valide** les données lues et une fonction de sauvegarde. Le programme doit **toujours démarrer**, même si le fichier est absent ou invalide.

## 🟢 Exercice 1 : Facile

**But** : Traduire un objet en dictionnaire, et inversement.

**Énoncé** : Ajoute à la classe `Renard` (fiche 10.3) une méthode `vers_dict()` qui renvoie **tous** ses attributs : `nom`, `couleur`, `age`, `energie` et `proies`. Écris ensuite la fonction `renard_depuis_dict(donnees)`, qui recrée un objet `Renard` à partir d'un tel dictionnaire.

Programme principal : Roux attrape un mulot et un lièvre. Affiche son dictionnaire, recrée une copie avec `renard_depuis_dict()`, et vérifie que la copie a le même contenu.

*Sortie attendue :*

```text
{'nom': 'Roux', 'couleur': 'roux', 'age': 3, 'energie': 90, 'proies': ['mulot', 'lièvre']}
Roux, renard roux de 3 ans
Énergie : 90, proies : ['mulot', 'lièvre']
Même contenu? True
Même objet? False
```

> 💡 Le constructeur de `Renard` ne reçoit pas l'énergie ni les proies : il faut les remettre **après** avoir créé l'objet. `copie is roux` (fiche 10.3) vérifie s'il s'agit du **même** objet.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.5 - Sauvegarder des objets en JSON](Solutions%2010.5%20-%20Sauvegarder%20des%20objets%20en%20JSON.md).
