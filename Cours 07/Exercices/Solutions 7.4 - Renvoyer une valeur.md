# Solutions — Renvoyer une valeur (fiche 7.4)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
11.50 $
11.5 None
39.49
132.20 $
4.60 $
None
```

| Ligne du programme | Affichage | Explication |
| --- | --- | --- |
| `a = calculer_prix_taxes(10)` | *(rien)* | La fonction renvoie `11.5`, qui est rangé dans `a`. Rien n'est affiché. |
| `b = afficher_prix_taxes(10)` | `11.50 $` | La fonction **affiche** le prix taxé, puis renvoie `None`, rangé dans `b`. |
| `print(a, b)` | `11.5 None` | `a` contient la valeur renvoyée; `b` contient `None`. |
| `print(calculer_prix_taxes(30) + 5)` | `39.49` | L'appel est remplacé par `34.49`, auquel on ajoute `5`. |
| `afficher_prix_taxes(calculer_prix_taxes(100))` | `132.20 $` | Le prix est taxé **deux fois** : `calculer_prix_taxes(100)` renvoie `114.98`, puis `afficher_prix_taxes()` le taxe encore. Le montant n'a pas de sens. |
| `print(afficher_prix_taxes(4))` | `4.60 $` puis `None` | La fonction affiche d'abord `4.60 $`, puis `print()` affiche la valeur qu'elle a renvoyée : `None`. |
| `calculer_prix_taxes(50)` | *(rien)* | La valeur renvoyée (`57.49`) n'est ni affichée ni rangée dans une variable : elle est perdue. |

- Une fonction qui **renvoie** n'affiche rien; c'est au code qui l'appelle de décider quoi faire de la valeur.
- Une fonction qui **affiche** renvoie `None` : son résultat ne peut pas servir dans un calcul.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

a. La fonction n'a pas d'instruction `return` : elle **affiche** la moyenne, puis renvoie `None`. La variable `moyenne` reçoit donc `None`, et la comparaison `None >= 60` provoque l'erreur `TypeError`. Le mot `NoneType` dans le message est l'indice : on utilise le résultat d'une fonction qui ne renvoie rien.

b. Version corrigée :

```python
SEUIL_REUSSITE = 60


def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total += note
    return total / len(notes)


notes_groupe = [78, 54, 91, 66, 83]
moyenne = calculer_moyenne(notes_groupe)
print(f"Moyenne du groupe : {moyenne:.1f}")
if moyenne >= SEUIL_REUSSITE:
    print("Le groupe réussit en moyenne.")
```

- Le `print()` de la fonction est remplacé par `return`.
- L'affichage est maintenant fait par le programme principal, qui peut choisir le format (`:.1f`).

## 🟢 Exercice 3 : Facile

### ✅ Solution 3

```python
TEMP_MIN = -90
TEMP_MAX = 60

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def convertir_en_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convertir_en_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius = valider_nombre("Température (°C) : ", TEMP_MIN, TEMP_MAX)
fahrenheit = convertir_en_fahrenheit(celsius)
retour = convertir_en_celsius(fahrenheit)

print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")
print(f"{fahrenheit:.1f} °F = {retour:.1f} °C")
print(f"Vérification : {convertir_en_celsius(convertir_en_fahrenheit(-40)):.1f} °C")
```

- Les deux fonctions renvoient un nombre et n'affichent rien : on peut donc enchaîner leurs appels, comme dans la dernière ligne.
- Dans `convertir_en_celsius(convertir_en_fahrenheit(-40))`, Python exécute d'abord l'appel le plus intérieur, qui renvoie `-40.0`, puis passe ce résultat à l'autre fonction.
- Avec certaines valeurs, le résultat de l'aller-retour peut contenir une minuscule erreur d'arrondi, propre aux nombres réels (`float`). Le format `:.1f` la rend invisible.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
PSEUDO_MIN = 3
PSEUDO_MAX = 12
VILLE_MIN = 2
VILLE_MAX = 40


def valider_texte(msg_saisie, longueur_min, longueur_max):
    texte = input(msg_saisie).strip()
    while not longueur_min <= len(texte) <= longueur_max:
        print(f"Erreur : entrez entre {longueur_min} et {longueur_max} caractères.")
        texte = input(msg_saisie).strip()
    return texte


pseudo = valider_texte("Pseudo (3 à 12 caractères) : ", PSEUDO_MIN, PSEUDO_MAX)
ville = valider_texte("Ville : ", VILLE_MIN, VILLE_MAX)
print(f"\nBienvenue au club d'échecs, {pseudo} de {ville}!")
```

- La condition `longueur_min <= len(texte) <= longueur_max` remplace la condition `texte == ""` de la recette 4 de la fiche 5.3 : une chaîne vide a une longueur de `0`, elle est donc refusée elle aussi.
- Pas besoin de `try`/`except` : un texte ne provoque jamais d'exception à la saisie.
- `strip()` est appliqué **avant** la vérification : `"  JeanFrançoisXYZ  "` devient `"JeanFrançoisXYZ"` (15 caractères), qui est refusé.

## 🟡 Exercice 5 : Moyen

### ✅ Solution 5

```python
TEMP_MIN = -50
TEMP_MAX = 0
VENT_MIN = 5
VENT_MAX = 100

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def calculer_refroidissement(temperature, vitesse_vent):
    facteur_vent = vitesse_vent ** 0.16
    indice = 13.12 + 0.6215 * temperature - 11.37 * facteur_vent + 0.3965 * temperature * facteur_vent
    return round(indice)


def classer_risque(indice):
    if indice >= -9:
        return "faible"
    elif indice >= -27:
        return "modéré"
    elif indice >= -39:
        return "élevé"
    elif indice >= -47:
        return "très élevé"
    elif indice >= -54:
        return "grave"
    else:
        return "extrême"


temperature = valider_nombre("Température (°C) : ", TEMP_MIN, TEMP_MAX)
vitesse_vent = valider_nombre("Vitesse du vent (km/h) : ", VENT_MIN, VENT_MAX)
indice = calculer_refroidissement(temperature, vitesse_vent)
print(f"\nRefroidissement éolien : {indice}")
print(f"Risque de gelures : {classer_risque(indice)}")
```

- `vitesse_vent ** 0.16` est calculé une seule fois et rangé dans une variable locale, puisqu'il apparaît deux fois dans la formule.
- Dans `classer_risque()`, chaque branche se termine par un `return` : dès qu'une condition est vraie, la fonction se termine. Les `elif` vérifient les bornes du haut vers le bas, de sorte qu'une seule comparaison suffit par niveau de risque.
- La température est validée entre -50 et 0 °C, parce qu'Environnement Canada ne publie l'indice que lorsque la température est sous le point de congélation et que le vent atteint au moins 5 km/h.

## 🟡 Exercice 6 : Moyen

### ✅ Solution 6

```python
ANNEE_MIN = 1583
ANNEE_MAX = 9999

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0


annee = valider_entier("Année : ", ANNEE_MIN, ANNEE_MAX)
if est_bissextile(annee):
    print(f"{annee} est bissextile : février compte 29 jours.")
else:
    print(f"{annee} n'est pas bissextile : février compte 28 jours.")

nb_bissextiles = 0
for a in range(2000, 2101):
    if est_bissextile(a):
        nb_bissextiles += 1
print(f"De 2000 à 2100, il y a {nb_bissextiles} années bissextiles.")
```

- L'expression `(annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0` vaut déjà `True` ou `False` : on la renvoie directement, sans `if`.
- Une version avec `if`/`else` et deux `return` est aussi correcte :

  ```python
  def est_bissextile(annee):
      if annee % 400 == 0:
          return True
      elif annee % 100 == 0:
          return False
      else:
          return annee % 4 == 0
  ```

- La même fonction sert dans une condition **et** dans une boucle : c'est une fonction réutilisable.

## 🟡 Exercice 7 : Moyen

### ✅ Solution 7

```python
JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
TEMPERATURES = (-4.5, -11.0, -8.2, 1.3, 3.8, -2.1, -15.6)


def trouver_min_max(valeurs):
    minimum = valeurs[0]
    maximum = valeurs[0]
    for valeur in valeurs:
        if valeur < minimum:
            minimum = valeur
        if valeur > maximum:
            maximum = valeur
    return minimum, maximum


temp_min, temp_max = trouver_min_max(TEMPERATURES)
print(f"Température la plus basse : {temp_min:.1f} °C ({JOURS[TEMPERATURES.index(temp_min)]})")
print(f"Température la plus haute : {temp_max:.1f} °C ({JOURS[TEMPERATURES.index(temp_max)]})")
print(f"Écart de la semaine : {temp_max - temp_min:.1f} °C")
```

- On initialise le minimum **et** le maximum avec le premier élément, comme dans la fiche 6.1.
- `return minimum, maximum` crée un tuple de deux valeurs.
- `temp_min, temp_max = trouver_min_max(TEMPERATURES)` **déballe** ce tuple dans deux variables. Il faut exactement deux variables à gauche du `=`.

## 🔴 Exercice 8 : Moyen-Difficile

### ✅ Solution 8

```python
VOYELLES = "aeiouyàâäéèêëîïôöùûü"
PHRASE_MIN = 1
PHRASE_MAX = 100


def valider_texte(msg_saisie, longueur_min, longueur_max):
    texte = input(msg_saisie).strip()
    while not longueur_min <= len(texte) <= longueur_max:
        print(f"Erreur : entrez entre {longueur_min} et {longueur_max} caractères.")
        texte = input(msg_saisie).strip()
    return texte


def compter_voyelles_consonnes(phrase):
    nb_voyelles = 0
    nb_consonnes = 0
    for caractere in phrase.lower():
        if caractere in VOYELLES:
            nb_voyelles += 1
        elif caractere.isalpha():
            nb_consonnes += 1
    return nb_voyelles, nb_consonnes


def est_palindrome(mot):
    mot = mot.lower()
    for i in range(len(mot) // 2):
        if mot[i] != mot[-1 - i]:
            return False
    return True


phrase = valider_texte("Phrase : ", PHRASE_MIN, PHRASE_MAX)
nb_voyelles, nb_consonnes = compter_voyelles_consonnes(phrase)
print(f"\n{nb_voyelles} voyelles et {nb_consonnes} consonnes")

print("Palindromes :", end=" ")
nb_palindromes = 0
for mot in phrase.split():
    if len(mot) > 1 and est_palindrome(mot):
        print(mot, end=" ")
        nb_palindromes += 1
if nb_palindromes == 0:
    print("aucun", end="")
print()
```

- `compter_voyelles_consonnes()` renvoie deux compteurs dans un tuple, déballé par le programme principal.
- Dans `est_palindrome()`, la boucle ne fait que `len(mot) // 2` tours : chaque tour compare une lettre de gauche (`mot[i]`) avec sa jumelle de droite (`mot[-1 - i]`). Dès qu'une paire diffère, `return False` **termine la fonction**, sans finir la boucle.
- Le `return True` est placé **après** la boucle : on ne l'atteint que si aucune paire n'a différé.
- La réaffectation `mot = mot.lower()` ne modifie que le paramètre local : la phrase du programme principal reste intacte (voir la fiche 7.5).
- `valider_texte()` est réutilisée telle quelle, sans modification : c'est l'avantage d'une fonction générale.
