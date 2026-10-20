# Exercices — Paramètres et arguments (fiche 7.3)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande. Pour les nombres, utilise les fonctions fournies ci-dessous.

## 🧰 Fonctions fournies

Les deux fonctions suivantes sont **prêtes à utiliser**. Copie-les en haut de ton fichier, sous tes constantes, puis appelle-les dans tes programmes chaque fois que tu dois lire un nombre au clavier.

```python
def valider_nombre(msg_saisie, val_min, val_max):
    valide = False
    while not valide:
        try:
            nombre = float(input(msg_saisie))
            if val_min <= nombre <= val_max:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {val_min} et {val_max}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre valide.")
    return nombre


def valider_entier(msg_saisie, val_min, val_max):
    valide = False
    while not valide:
        try:
            nombre = int(input(msg_saisie))
            if val_min <= nombre <= val_max:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {val_min} et {val_max}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return nombre
```

| Fonction | Paramètres | Ce qu'elle fait |
| --- | --- | --- |
| `valider_nombre(msg_saisie, val_min, val_max)` | le message à afficher, la plus petite et la plus grande valeur acceptées | Redemande la saisie jusqu'à obtenir un **nombre réel** entre `val_min` et `val_max`, puis le renvoie (`float`). |
| `valider_entier(msg_saisie, val_min, val_max)` | les mêmes | Même chose, pour un **nombre entier** (`int`). |

On les utilise exactement comme `input()`, en rangeant le résultat dans une variable :

```python
note = valider_nombre("Note sur 100 : ", 0, 100)
nb_billets = valider_entier("Nombre de billets : ", 1, 10)
```

> 💡 Tu reconnais sans doute la recette de validation de la fiche 5.3. La seule nouveauté est la dernière ligne, `return nombre`, qui **renvoie** la valeur validée au code qui a fait l'appel. On verra en détail comment écrire ce genre de fonction dans la fiche [7.4 - Renvoyer une valeur](../7.4%20-%20Renvoyer%20une%20valeur.md). Pour l'instant, il suffit de savoir **l'appeler**.

## 🟢 Exercice 1 : Facile

**But** : Comprendre comment les arguments sont transmis aux paramètres.

**Énoncé** : Sans exécuter de code, écris exactement ce qu'affiche le programme suivant. Pour chaque appel, indique aussi la valeur que reçoivent les paramètres `titre` et `jours`.

```python
def afficher_emprunt(titre, jours):
    print(f"« {titre} » : à rapporter dans {jours} jours")


livre = "Kukum"
duree = 21

afficher_emprunt(livre, duree)
afficher_emprunt("Le Petit Prince", 14)
afficher_emprunt(livre, duree - 7)

titre = "Bonheur d'occasion"
afficher_emprunt(titre, duree * 2)
afficher_emprunt("Agaguk", len("Agaguk"))
```

## 🟢 Exercice 2 : Facile

**But** : Reconnaître les appels corrects, les appels qui donnent un résultat faux et les appels qui provoquent une erreur.

**Énoncé** : Voici une fonction qui confirme l'inscription d'un étudiant à un cours :

```python
def afficher_inscription(nom, cours, groupe):
    print(f"{nom} est inscrit(e) au cours {cours}, groupe {groupe}.")
```

Pour chacun des appels ci-dessous, indique s'il :

- ✅ **fonctionne correctement** : écris alors ce qu'il affiche;
- ⚠️ **s'exécute, mais affiche un résultat faux** : écris ce qu'il affiche et explique le problème;
- ❌ **provoque une erreur** : nomme le type d'erreur (`TypeError`, `NameError`, etc.) et explique sa cause.

Chaque appel est indépendant des autres.

```python
a.  afficher_inscription("Léa", "Programmation", 2)

b.  afficher_inscription("Programmation", "Léa", 2)

c.  afficher_inscription("Samuel", "Réseaux")

d.  afficher_inscription("Noah", "Bases de données", 3, "A26")

e.  etudiant = "Zoé"
    afficher_inscription(etudiant, "Web " + "1", 1 + 1)

f.  afficher_inscription(nom, "Programmation", 2)
```

Vérifie ensuite tes réponses dans VS Code.

## 🟢 Exercice 3 : Facile

**But** : Écrire une fonction qui reçoit un paramètre.

**Énoncé** : Écris une fonction `afficher_cadre(texte)` qui affiche le texte reçu, entouré d'un cadre d'astérisques. Le cadre s'ajuste à la longueur du texte : il y a toujours un astérisque et une espace de chaque côté du texte.

Utilise ensuite cette fonction pour afficher les trois titres suivants : `Bienvenue!`, `Menu principal` et `Merci de votre visite`.

*Sortie attendue :*

```text
**************
* Bienvenue! *
**************
******************
* Menu principal *
******************
*************************
* Merci de votre visite *
*************************
```

> 💡 La fonction `len()` donne la longueur du texte. De combien de caractères le cadre est-il plus large que le texte?

## 🟡 Exercice 4 : Moyen

**But** : Passer en argument une valeur saisie et validée.

**Énoncé** : Écris une fonction `afficher_conversion(celsius)` qui affiche une température en degrés Celsius et son équivalent en degrés Fahrenheit, chacune avec une décimale. La formule est : °F = °C × 9 / 5 + 32.

Le programme principal :

1. affiche la conversion de quatre températures repères, rangées dans une constante `REPERES = (-40, 0, 37, 100)`, à l'aide d'une boucle;
2. demande ensuite une température à l'utilisateur, entre -90 °C et 60 °C (les records sur Terre), avec `valider_nombre()`;
3. affiche la conversion de cette température.

*Exemple d'exécution :*

```text
Températures repères :
-40.0 °C = -40.0 °F
0.0 °C = 32.0 °F
37.0 °C = 98.6 °F
100.0 °C = 212.0 °F

Température à convertir (°C) : chaud
Erreur : ce n'est pas un nombre valide.
Température à convertir (°C) : 75
Erreur : entrez un nombre entre -90 et 60.
Température à convertir (°C) : -17.5
-17.5 °C = 0.5 °F
```

## 🟡 Exercice 5 : Moyen

**But** : Écrire une fonction à plusieurs paramètres et l'appeler dans une boucle.

**Énoncé** : Sur le bulletin du cégep, chaque cours est accompagné de la moyenne du groupe. Écris une fonction `afficher_ligne_releve(cours, note, moyenne_groupe)` qui affiche une ligne du relevé : le nom du cours (aligné à gauche sur 16 caractères), la note et la moyenne du groupe (alignées à droite sur 8 caractères, une décimale), puis la mention `↑` si la note est supérieure ou égale à la moyenne du groupe, ou `↓` sinon.

Le programme utilise les constantes suivantes :

```python
COURS = ("Programmation", "Mathématiques", "Français", "Philosophie")
MOYENNES_GROUPE = (74.5, 68.0, 77.2, 71.8)
```

Le programme principal :

1. demande la note de chacun des cours (entre 0 et 100) avec `valider_nombre()` et les range dans une liste;
2. affiche l'en-tête du relevé;
3. affiche une ligne par cours à l'aide de `afficher_ligne_releve()`;
4. affiche la moyenne de l'étudiant.

*Exemple d'exécution :*

```text
Note en Programmation : 87
Note en Mathématiques : 64.5
Note en Français : cent
Erreur : ce n'est pas un nombre valide.
Note en Français : 81
Note en Philosophie : 72

Cours               Note  Groupe
--------------------------------------
Programmation       87.0    74.5  ↑
Mathématiques       64.5    68.0  ↓
Français            81.0    77.2  ↑
Philosophie         72.0    71.8  ↑
--------------------------------------
Moyenne de l'étudiant : 76.1
```

## 🟡 Exercice 6 : Moyen

**But** : Écrire une fonction dont les paramètres contrôlent une boucle.

**Énoncé** : Écris une fonction `afficher_table(nombre, limite)` qui affiche la table de multiplication de `nombre`, de 1 jusqu'à `limite` inclusivement. Les colonnes sont alignées à droite.

Le programme principal demande le nombre (entre 1 et 12) et la limite (entre 1 et 20) avec `valider_entier()`, puis appelle la fonction.

*Exemple d'exécution :*

```text
Table de : 7
Jusqu'à : 25
Erreur : entrez un nombre entre 1 et 20.
Jusqu'à : 10

Table de 7
 7 x  1 =   7
 7 x  2 =  14
 7 x  3 =  21
 7 x  4 =  28
 7 x  5 =  35
 7 x  6 =  42
 7 x  7 =  49
 7 x  8 =  56
 7 x  9 =  63
 7 x 10 =  70
```

## 🟡 Exercice 7 : Moyen

**But** : Passer une liste en argument et réutiliser une même fonction avec des listes différentes.

**Énoncé** : Écris une fonction `afficher_liste_numerotee(elements)` qui affiche chaque élément de la liste reçue, numéroté à partir de 1, puis le nombre total d'éléments.

Le programme principal :

1. demande des articles d'épicerie à l'utilisateur jusqu'à ce qu'il appuie sur `Entrée` sans rien écrire, et les range dans une liste;
2. si la liste est vide, affiche « Aucun article. »; sinon :
   - affiche la liste dans l'ordre de saisie avec `afficher_liste_numerotee()`;
   - affiche la liste en ordre alphabétique avec **la même fonction**, sans modifier la liste originale.

*Exemple d'exécution :*

```text
Article (Entrée pour terminer) : pommes
Article (Entrée pour terminer) : lait
Article (Entrée pour terminer) : fromage
Article (Entrée pour terminer) : beurre
Article (Entrée pour terminer) :

Dans l'ordre de saisie :
1. pommes
2. lait
3. fromage
4. beurre
(4 articles)

En ordre alphabétique :
1. beurre
2. fromage
3. lait
4. pommes
(4 articles)
```

## 🔴 Exercice 8 : Moyen-Difficile

**But** : Écrire une fonction générale qui reçoit deux listes associées, puis la réutiliser avec des données différentes.

**Énoncé** : Écris une fonction `afficher_histogramme(etiquettes, valeurs, echelle)` qui affiche un histogramme horizontal. Pour chaque élément :

- l'étiquette est alignée à gauche sur 10 caractères;
- la barre contient un `#` par tranche complète de `echelle` (par exemple, avec une échelle de 10, une valeur de 74 donne 7 `#`);
- la valeur est affichée entre parenthèses après la barre.

Utilise ensuite la même fonction pour afficher les deux histogrammes ci-dessous, à partir de ces constantes :

```python
MOIS = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin")
PRECIPITATIONS_MM = (74, 58, 69, 81, 93, 102)

JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi")
VISITEURS_GYM = (240, 185, 210, 160, 95)
```

*Sortie attendue :*

```text
Précipitations (1 # = 10 mm)
Janvier   ####### (74)
Février   ##### (58)
Mars      ###### (69)
Avril     ######## (81)
Mai       ######### (93)
Juin      ########## (102)

Visiteurs au gym (1 # = 20 visiteurs)
Lundi     ############ (240)
Mardi     ######### (185)
Mercredi  ########## (210)
Jeudi     ######## (160)
Vendredi  #### (95)
```

> 💡 Comme la fonction reçoit l'échelle en paramètre, elle peut afficher n'importe quelles données, peu importe leur ordre de grandeur. Pense à utiliser des constantes pour les deux échelles.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.3 - Paramètres et arguments](Solutions%207.3%20-%20Paramètres%20et%20arguments.md).
