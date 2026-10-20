# Exercices — Renvoyer une valeur (fiche 7.4)

> 📌 **Validation obligatoire** : dans tous les exercices, chaque saisie doit être **validée** (type et valeur). Tant que la valeur entrée est invalide, le programme affiche un message d'erreur et la redemande. Pour les nombres, réutilise les fonctions fournies `valider_nombre()` et `valider_entier()` de la série [Exercices 7.3](Exercices%207.3%20-%20Paramètres%20et%20arguments.md#-fonctions-fournies).

## 🟢 Exercice 1 : Facile

**But** : Distinguer une fonction qui **renvoie** une valeur d'une fonction qui **affiche**.

**Énoncé** : Sans exécuter de code, écris exactement ce qu'affiche le programme suivant. Explique ensuite chacune des lignes affichées.

```python
TAUX_TAXES = 0.14975


def calculer_prix_taxes(prix):
    return round(prix * (1 + TAUX_TAXES), 2)


def afficher_prix_taxes(prix):
    print(f"{prix * (1 + TAUX_TAXES):.2f} $")


a = calculer_prix_taxes(10)
b = afficher_prix_taxes(10)
print(a, b)
print(calculer_prix_taxes(30) + 5)
afficher_prix_taxes(calculer_prix_taxes(100))
print(afficher_prix_taxes(4))
calculer_prix_taxes(50)
```

> 💡 Une ligne du programme n'affiche rien du tout. Laquelle, et pourquoi? Une autre affiche un montant qui n'a pas de sens. Laquelle?

## 🟢 Exercice 2 : Facile

**But** : Corriger une fonction qui affiche son résultat au lieu de le renvoyer.

**Énoncé** : Le programme suivant devrait afficher la moyenne d'un groupe, puis indiquer si le groupe réussit en moyenne. Il affiche bien un nombre… puis plante.

```python
SEUIL_REUSSITE = 60


def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total += note
    print(total / len(notes))


notes_groupe = [78, 54, 91, 66, 83]
moyenne = calculer_moyenne(notes_groupe)
if moyenne >= SEUIL_REUSSITE:
    print("Le groupe réussit en moyenne.")
```

```text
74.4
Traceback (most recent call last):
  ...
TypeError: '>=' not supported between instances of 'NoneType' and 'int'
```

a. Explique pourquoi la variable `moyenne` contient `None`.
b. Corrige la fonction. Le programme principal doit ensuite afficher lui-même la moyenne (1 décimale), puis le message.

*Sortie attendue après correction :*

```text
Moyenne du groupe : 74.4
Le groupe réussit en moyenne.
```

## 🟢 Exercice 3 : Facile

**But** : Écrire des fonctions de calcul qui renvoient leur résultat.

**Énoncé** : Écris deux fonctions :

- `convertir_en_fahrenheit(celsius)`, qui **renvoie** la température en °F (°F = °C × 9 / 5 + 32);
- `convertir_en_celsius(fahrenheit)`, qui **renvoie** la température en °C (°C = (°F − 32) × 5 / 9).

Aucune des deux fonctions n'affiche quoi que ce soit.

Le programme principal demande une température en °C (entre -90 et 60), la convertit en °F, puis reconvertit ce résultat en °C pour vérifier qu'on retrouve la valeur de départ. Il termine en vérifiant, **en une seule ligne**, que l'aller-retour de -40 °C donne bien -40 °C.

*Exemple d'exécution :*

```text
Température (°C) : 21
21.0 °C = 69.8 °F
69.8 °F = 21.0 °C
Vérification : -40.0 °C
```

> 💡 La vérification en une ligne demande de passer le résultat d'une fonction **directement en argument** à l'autre.

## 🟡 Exercice 4 : Moyen

**But** : Écrire une fonction de saisie validée qui renvoie la valeur obtenue.

**Énoncé** : Maintenant que tu sais comment fonctionne `return`, tu peux écrire tes propres fonctions de validation, sur le modèle de `valider_nombre()`.

Écris une fonction `valider_texte(msg_saisie, longueur_min, longueur_max)` qui demande un texte jusqu'à ce que sa longueur soit comprise entre `longueur_min` et `longueur_max` (inclusivement), puis le **renvoie**. Les espaces au début et à la fin de la saisie sont retirées avant la vérification.

Utilise-la pour l'inscription au club d'échecs du cégep : le programme demande un pseudo (3 à 12 caractères) et une ville (2 à 40 caractères), puis affiche un message de bienvenue.

*Exemple d'exécution :*

```text
Pseudo (3 à 12 caractères) : Mo
Erreur : entrez entre 3 et 12 caractères.
Pseudo (3 à 12 caractères) :   JeanFrançoisXYZ
Erreur : entrez entre 3 et 12 caractères.
Pseudo (3 à 12 caractères) : LeRoi
Ville :
Erreur : entrez entre 2 et 40 caractères.
Ville : Trois-Rivières

Bienvenue au club d'échecs, LeRoi de Trois-Rivières!
```

> 💡 Garde précieusement cette fonction : tu la réutiliseras dans l'exercice 8 et dans les prochaines séries.

## 🟡 Exercice 5 : Moyen

**But** : Combiner une fonction qui calcule et une fonction qui renvoie un résultat selon plusieurs cas.

**Énoncé** : En hiver, Environnement Canada publie l'indice de **refroidissement éolien**, qui combine la température et la vitesse du vent. Il se calcule ainsi, où *T* est la température (°C) et *V* la vitesse du vent (km/h) :

> indice = 13,12 + 0,6215 × *T* − 11,37 × *V*<sup>0,16</sup> + 0,3965 × *T* × *V*<sup>0,16</sup>

Écris deux fonctions :

- `calculer_refroidissement(temperature, vitesse_vent)`, qui **renvoie** l'indice arrondi à l'entier (`round()`);
- `classer_risque(indice)`, qui **renvoie** le niveau de risque de gelures selon le tableau ci-dessous. Utilise un `return` dans chaque branche.

| Indice | Risque |
| --- | --- |
| 0 à -9 | faible |
| -10 à -27 | modéré |
| -28 à -39 | élevé |
| -40 à -47 | très élevé |
| -48 à -54 | grave |
| -55 et moins | extrême |

Le programme principal demande la température (entre -50 et 0 °C) et la vitesse du vent (entre 5 et 100 km/h), puis affiche l'indice et le risque.

*Exemples d'exécution :*

```text
Température (°C) : -20
Vitesse du vent (km/h) : 30

Refroidissement éolien : -33
Risque de gelures : élevé
```

```text
Température (°C) : 5
Erreur : entrez un nombre entre -50 et 0.
Température (°C) : -35
Vitesse du vent (km/h) : 2
Erreur : entrez un nombre entre 5 et 100.
Vitesse du vent (km/h) : 40

Refroidissement éolien : -54
Risque de gelures : grave
```

> 💡 En Python, la puissance s'écrit `**` : *V*<sup>0,16</sup> s'écrit `vitesse_vent ** 0.16`.

## 🟡 Exercice 6 : Moyen

**But** : Écrire une fonction qui renvoie un booléen et l'utiliser dans une condition.

**Énoncé** : Une année est **bissextile** si elle est divisible par 4, sauf si elle est divisible par 100… à moins qu'elle soit aussi divisible par 400. Ainsi, 2024 et 2000 sont bissextiles, mais 1900 et 2100 ne le sont pas.

Écris une fonction `est_bissextile(annee)` qui **renvoie** `True` ou `False`. Elle ne contient aucun `print()`.

Le programme principal :

1. demande une année (entre 1583, première année complète du calendrier grégorien, et 9999), puis indique si elle est bissextile et combien de jours compte son mois de février;
2. compte et affiche le nombre d'années bissextiles de 2000 à 2100 inclusivement, en appelant `est_bissextile()` dans une boucle.

*Exemple d'exécution :*

```text
Année : 1900
1900 n'est pas bissextile : février compte 28 jours.
De 2000 à 2100, il y a 25 années bissextiles.
```

> 💡 Puisque la fonction renvoie un booléen, on peut écrire directement `if est_bissextile(annee):`, sans `== True`.

## 🟡 Exercice 7 : Moyen

**But** : Renvoyer plusieurs valeurs à l'aide d'un tuple.

**Énoncé** : Écris une fonction `trouver_min_max(valeurs)` qui **renvoie** à la fois la plus petite et la plus grande valeur d'une liste ou d'un tuple, sous la forme d'un tuple `(minimum, maximum)`.

Contrainte : n'utilise **ni** `min()` **ni** `max()`.

Le programme principal utilise les températures d'une semaine de décembre, récupère les deux valeurs en **déballant** le tuple, puis affiche les deux extrêmes (avec le jour correspondant) et l'écart de la semaine.

```python
JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
TEMPERATURES = (-4.5, -11.0, -8.2, 1.3, 3.8, -2.1, -15.6)
```

*Sortie attendue :*

```text
Température la plus basse : -15.6 °C (Dimanche)
Température la plus haute : 3.8 °C (Vendredi)
Écart de la semaine : 19.4 °C
```

> 💡 Pour retrouver le jour, la méthode `index()` (fiche 6.2) donne la position d'une valeur dans un tuple.

## 🔴 Exercice 8 : Moyen-Difficile

**But** : Combiner plusieurs fonctions qui renvoient des valeurs, dont une qui utilise une sortie anticipée.

**Énoncé** : Écris deux fonctions :

- `compter_voyelles_consonnes(phrase)`, qui **renvoie** un tuple contenant le nombre de voyelles et le nombre de consonnes de la phrase. Les voyelles accentuées comptent comme des voyelles (`VOYELLES = "aeiouyàâäéèêëîïôöùûü"`); les espaces et la ponctuation ne comptent pas;
- `est_palindrome(mot)`, qui **renvoie** `True` si le mot se lit de la même façon dans les deux sens, sans tenir compte des majuscules. Elle compare les lettres deux à deux, de l'extérieur vers l'intérieur, et **renvoie `False` dès** qu'une paire diffère.

Le programme principal demande une phrase (1 à 100 caractères) avec ta fonction `valider_texte()` de l'exercice 4, affiche le nombre de voyelles et de consonnes, puis la liste des mots de plus d'une lettre qui sont des palindromes (ou « aucun »).

*Exemples d'exécution :*

```text
Phrase :
Erreur : entrez entre 1 et 100 caractères.
Phrase : Elle a été à Laval en kayak

12 voyelles et 9 consonnes
Palindromes : Elle été Laval kayak
```

```text
Phrase : Bonjour tout le monde

8 voyelles et 10 consonnes
Palindromes : aucun
```

> 💡 La méthode `isalpha()` renvoie `True` si un caractère est une lettre. Pour obtenir les mots d'une phrase, utilise `split()` (fiche 6.2). Interdiction d'utiliser le *slicing* `[::-1]` dans `est_palindrome()` : le but est de pratiquer la sortie anticipée avec `return`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.4 - Renvoyer une valeur](Solutions%207.4%20-%20Renvoyer%20une%20valeur.md).
