# Exercices supplémentaires — Écrire des fonctions (Cours 07)

> 📌 Ces exercices servent à pratiquer la **rédaction** de fonctions, du plus simple au plus complet. Ils couvrent les fiches 7.1 à 7.4.
>
> **Validation obligatoire** : dans l'exercice 2, chaque saisie doit être **validée** (type et valeur). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande.

## 🟢 Exercice 1 : Facile

**But** : Traduire en code une fonction décrite en mots.

**Énoncé** : Écris les 10 fonctions décrites ci-dessous, dans un même fichier. Pour chacune, on te donne :

- son **nom** et ses **paramètres**, à respecter exactement;
- ce qu'elle doit **faire** ou **renvoyer**;
- des **exemples d'appels** avec le résultat attendu.

Une fois chaque fonction écrite, ajoute ses exemples d'appels au bas du fichier et vérifie que tu obtiens les mêmes résultats.

> 💡 Avant d'écrire chaque fonction, pose-toi deux questions :
>
> 1. **Que reçoit-elle?** → ce sont ses paramètres.
> 2. **Doit-elle afficher, ou renvoyer?** → si la description dit « renvoie », la fonction se termine par `return` et ne contient **aucun** `print()`.

### a. `afficher_ligne_etoiles()`

Affiche une ligne de 20 astérisques. Elle ne reçoit rien et ne renvoie rien. Le nombre d'astérisques est une constante.

| Appel | Résultat |
| --- | --- |
| `afficher_ligne_etoiles()` | affiche `********************` |

### b. `afficher_bonjour(prenom)`

Affiche une salutation pour le prénom reçu. Elle ne renvoie rien.

| Appel | Résultat |
| --- | --- |
| `afficher_bonjour("Léa")` | affiche `Bonjour, Léa!` |
| `afficher_bonjour("Samuel")` | affiche `Bonjour, Samuel!` |

### c. `calculer_aire_cercle(rayon)`

Renvoie l'aire d'un cercle (π × rayon²). Utilise `math.pi`.

| Appel | Résultat |
| --- | --- |
| `print(f"{calculer_aire_cercle(2):.2f}")` | affiche `12.57` |
| `print(f"{calculer_aire_cercle(0.5):.2f}")` | affiche `0.79` |

### d. `convertir_km_en_miles(km)`

Renvoie la distance en miles (1 km = 0,621371 mille). Le facteur de conversion est une constante.

| Appel | Résultat |
| --- | --- |
| `print(f"{convertir_km_en_miles(10):.1f}")` | affiche `6.2` |
| `print(f"{convertir_km_en_miles(42.195):.1f}")` | affiche `26.2` (un marathon) |

### e. `est_pair(nombre)`

Renvoie `True` si le nombre entier reçu est pair, `False` sinon.

| Appel | Résultat |
| --- | --- |
| `est_pair(8)` | renvoie `True` |
| `est_pair(7)` | renvoie `False` |
| `est_pair(0)` | renvoie `True` |

### f. `calculer_prix_rabais(prix, pourcentage)`

Renvoie le prix après un rabais exprimé en pourcentage (par exemple, `25` pour 25 %), arrondi à 2 décimales.

| Appel | Résultat |
| --- | --- |
| `calculer_prix_rabais(80, 25)` | renvoie `60.0` |
| `calculer_prix_rabais(19.99, 10)` | renvoie `17.99` |

### g. `obtenir_initiales(prenom, nom)`

Renvoie les initiales du prénom et du nom, en majuscules, chacune suivie d'un point.

| Appel | Résultat |
| --- | --- |
| `obtenir_initiales("léa", "tremblay")` | renvoie `'L.T.'` |
| `obtenir_initiales("Samuel", "Côté")` | renvoie `'S.C.'` |

### h. `compter_lettre(texte, lettre)`

Renvoie le nombre de fois que `lettre` apparaît dans `texte`. Utilise une boucle `for` (pas la méthode `count()`). Les majuscules et les minuscules sont considérées comme différentes.

| Appel | Résultat |
| --- | --- |
| `compter_lettre("programmation", "m")` | renvoie `2` |
| `compter_lettre("Bonjour", "z")` | renvoie `0` |
| `compter_lettre("Anna", "a")` | renvoie `1` |

### i. `calculer_moyenne(valeurs)`

Reçoit une liste de nombres (jamais vide) et renvoie leur moyenne. Utilise une boucle `for` (pas la fonction `sum()`).

| Appel | Résultat |
| --- | --- |
| `calculer_moyenne([78, 92, 65])` | renvoie `78.33333333333333` |
| `calculer_moyenne([7.5])` | renvoie `7.5` |

### j. `trouver_mot_plus_long(mots)`

Reçoit une liste de mots (jamais vide) et renvoie le plus long. En cas d'égalité, c'est le premier trouvé qui est renvoyé.

| Appel | Résultat |
| --- | --- |
| `trouver_mot_plus_long(["chat", "éléphant", "souris"])` | renvoie `'éléphant'` |
| `trouver_mot_plus_long(["un", "deux", "six"])` | renvoie `'deux'` |

> 💡 Pour voir ce qu'une fonction **renvoie**, il faut l'afficher : `print(est_pair(8))`. Un appel seul, comme `est_pair(8)`, calcule le résultat… puis le perd.

## 🟡 Exercice 2 : Moyen

**But** : Construire un programme complet à partir d'une liste de fonctions imposées, dont une qui remplit une liste dans une boucle.

**Remise** : un seul fichier nommé `citrouilles.py`, avec l'en-tête habituel (`Auteur`, `Date`, `Sujet`).

### Mise en situation

Au concours de citrouilles géantes de la Fête des récoltes, un juge pèse chaque citrouille inscrite. Après la pesée, une citrouille est parfois disqualifiée (fissure, tige manquante…). On établit ensuite le classement et le podium.

### Fonctions imposées

Ton programme doit contenir **exactement** les fonctions suivantes, avec ces noms et ces paramètres. Les deux premières sont celles fournies dans la série [Exercices 7.3](Exercices%207.3%20-%20Paramètres%20et%20arguments.md#-fonctions-fournies) : copie-les telles quelles.

| Fonction | Ce qu'elle fait | Renvoie |
| --- | --- | --- |
| `valider_entier(msg_saisie, val_min, val_max)` | Fournie : demande un entier entre `val_min` et `val_max` jusqu'à ce que la saisie soit valide. | l'entier (`int`) |
| `valider_nombre(msg_saisie, val_min, val_max)` | Fournie : même chose pour un nombre réel. | le nombre (`float`) |
| `saisir_poids(nb_citrouilles)` | Crée une liste vide, puis, dans une boucle `for`, demande le poids de chaque citrouille (numérotées à partir de 1) avec `valider_nombre()` et l'ajoute à la liste. | la liste des poids (`list`) |
| `retirer_citrouille(poids, numero)` | Retire de la liste la citrouille dont le **numéro** (à partir de 1) est reçu. | le poids retiré (`float`) |
| `calculer_moyenne(valeurs)` | Ta fonction de l'exercice 1 i. | la moyenne (`float`) |
| `afficher_podium(classement)` | Reçoit la liste déjà classée du plus lourd au plus léger, et affiche les 3 premières places. | rien |

### Énoncé

Le programme principal, placé après les fonctions :

1. demande le **nombre de citrouilles** inscrites, un entier entre **5 et 12**;
2. demande le **poids** (en kg) de chaque citrouille, entre **1 et 1500 kg**, à l'aide de `saisir_poids()`;
3. affiche la liste des poids, telle que saisie;
4. demande le **numéro de la citrouille disqualifiée** (entre 1 et le nombre de citrouilles), la retire avec `retirer_citrouille()`, puis affiche son poids et la liste des citrouilles admissibles;
5. avec les citrouilles admissibles, affiche le poids total, le poids moyen (avec `calculer_moyenne()`) et le poids de la plus lourde, avec 1 décimale;
6. trie la liste en ordre croissant et l'affiche, puis la **renverse** et l'affiche : c'est le classement;
7. affiche le podium avec `afficher_podium()`.

Toutes les bornes (5, 12, 1, 1500 et le nombre de places du podium) sont des **constantes**.

> ⚠️ La citrouille numéro 3 n'est **pas** à l'index 3 de la liste!

### Exemple d'exécution

```text
Nombre de citrouilles (5 à 12) : 3
Erreur : entrez un nombre entre 5 et 12.
Nombre de citrouilles (5 à 12) : cinq
Erreur : ce n'est pas un nombre entier.
Nombre de citrouilles (5 à 12) : 6
Poids de la citrouille 1 (kg) : 412.5
Poids de la citrouille 2 (kg) : 655
Poids de la citrouille 3 (kg) : 380.2
Poids de la citrouille 4 (kg) : lourd
Erreur : ce n'est pas un nombre valide.
Poids de la citrouille 4 (kg) : 901.4
Poids de la citrouille 5 (kg) : 2000
Erreur : entrez un nombre entre 1 et 1500.
Poids de la citrouille 5 (kg) : 515
Poids de la citrouille 6 (kg) : 732.8

Poids saisis : [412.5, 655.0, 380.2, 901.4, 515.0, 732.8]
Numéro de la citrouille disqualifiée (1 à 6) : 9
Erreur : entrez un nombre entre 1 et 6.
Numéro de la citrouille disqualifiée (1 à 6) : 3
Citrouille 3 disqualifiée : 380.2 kg
Citrouilles admissibles : [412.5, 655.0, 901.4, 515.0, 732.8]
Poids total : 3216.7 kg
Poids moyen : 643.3 kg
Plus lourde : 901.4 kg
Triées : [412.5, 515.0, 655.0, 732.8, 901.4]
Classement : [901.4, 732.8, 655.0, 515.0, 412.5]

Podium
1re place : 901.4 kg
2e place : 732.8 kg
3e place : 655.0 kg
```

> 💡 **Démarche suggérée** : écris et teste **une fonction à la fois**, en l'appelant avec des valeurs connues, avant d'écrire le programme principal. Par exemple, `print(retirer_citrouille([10.0, 20.0, 30.0], 2))` doit afficher `20.0`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions supplémentaires - Écrire des fonctions](Solutions%20supplémentaires%20-%20Écrire%20des%20fonctions.md).
