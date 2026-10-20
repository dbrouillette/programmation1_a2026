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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=SEUIL_REUSSITE%20%3D%2060%0A%0A%0Adef%20calculer_moyenne%28notes%29%3A%0A%20%20%20%20total%20%3D%200%0A%20%20%20%20for%20note%20in%20notes%3A%0A%20%20%20%20%20%20%20%20total%20%2B%3D%20note%0A%20%20%20%20return%20total%20%2F%20len%28notes%29%0A%0A%0Anotes_groupe%20%3D%20%5B78%2C%2054%2C%2091%2C%2066%2C%2083%5D%0Amoyenne%20%3D%20calculer_moyenne%28notes_groupe%29%0Aprint%28f%22Moyenne%20du%20groupe%20%3A%20%7Bmoyenne%3A.1f%7D%22%29%0Aif%20moyenne%20%3E%3D%20SEUIL_REUSSITE%3A%0A%20%20%20%20print%28%22Le%20groupe%20r%C3%A9ussit%20en%20moyenne.%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=TEMP_MIN%20%3D%20-90%0ATEMP_MAX%20%3D%2060%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20convertir_en_fahrenheit%28celsius%29%3A%0A%20%20%20%20return%20celsius%20%2A%209%20%2F%205%20%2B%2032%0A%0A%0Adef%20convertir_en_celsius%28fahrenheit%29%3A%0A%20%20%20%20return%20%28fahrenheit%20-%2032%29%20%2A%205%20%2F%209%0A%0A%0Acelsius%20%3D%20valider_nombre%28%22Temp%C3%A9rature%20%28%C2%B0C%29%20%3A%20%22%2C%20TEMP_MIN%2C%20TEMP_MAX%29%0Afahrenheit%20%3D%20convertir_en_fahrenheit%28celsius%29%0Aretour%20%3D%20convertir_en_celsius%28fahrenheit%29%0A%0Aprint%28f%22%7Bcelsius%3A.1f%7D%20%C2%B0C%20%3D%20%7Bfahrenheit%3A.1f%7D%20%C2%B0F%22%29%0Aprint%28f%22%7Bfahrenheit%3A.1f%7D%20%C2%B0F%20%3D%20%7Bretour%3A.1f%7D%20%C2%B0C%22%29%0Aprint%28f%22V%C3%A9rification%20%3A%20%7Bconvertir_en_celsius%28convertir_en_fahrenheit%28-40%29%29%3A.1f%7D%20%C2%B0C%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=PSEUDO_MIN%20%3D%203%0APSEUDO_MAX%20%3D%2012%0AVILLE_MIN%20%3D%202%0AVILLE_MAX%20%3D%2040%0A%0A%0Adef%20valider_texte%28msg_saisie%2C%20longueur_min%2C%20longueur_max%29%3A%0A%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20while%20not%20longueur_min%20%3C%3D%20len%28texte%29%20%3C%3D%20longueur_max%3A%0A%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20entre%20%7Blongueur_min%7D%20et%20%7Blongueur_max%7D%20caract%C3%A8res.%22%29%0A%20%20%20%20%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20return%20texte%0A%0A%0Apseudo%20%3D%20valider_texte%28%22Pseudo%20%283%20%C3%A0%2012%20caract%C3%A8res%29%20%3A%20%22%2C%20PSEUDO_MIN%2C%20PSEUDO_MAX%29%0Aville%20%3D%20valider_texte%28%22Ville%20%3A%20%22%2C%20VILLE_MIN%2C%20VILLE_MAX%29%0Aprint%28f%22%5CnBienvenue%20au%20club%20d%27%C3%A9checs%2C%20%7Bpseudo%7D%20de%20%7Bville%7D%21%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=TEMP_MIN%20%3D%20-50%0ATEMP_MAX%20%3D%200%0AVENT_MIN%20%3D%205%0AVENT_MAX%20%3D%20100%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20calculer_refroidissement%28temperature%2C%20vitesse_vent%29%3A%0A%20%20%20%20facteur_vent%20%3D%20vitesse_vent%20%2A%2A%200.16%0A%20%20%20%20indice%20%3D%2013.12%20%2B%200.6215%20%2A%20temperature%20-%2011.37%20%2A%20facteur_vent%20%2B%200.3965%20%2A%20temperature%20%2A%20facteur_vent%0A%20%20%20%20return%20round%28indice%29%0A%0A%0Adef%20classer_risque%28indice%29%3A%0A%20%20%20%20if%20indice%20%3E%3D%20-9%3A%0A%20%20%20%20%20%20%20%20return%20%22faible%22%0A%20%20%20%20elif%20indice%20%3E%3D%20-27%3A%0A%20%20%20%20%20%20%20%20return%20%22mod%C3%A9r%C3%A9%22%0A%20%20%20%20elif%20indice%20%3E%3D%20-39%3A%0A%20%20%20%20%20%20%20%20return%20%22%C3%A9lev%C3%A9%22%0A%20%20%20%20elif%20indice%20%3E%3D%20-47%3A%0A%20%20%20%20%20%20%20%20return%20%22tr%C3%A8s%20%C3%A9lev%C3%A9%22%0A%20%20%20%20elif%20indice%20%3E%3D%20-54%3A%0A%20%20%20%20%20%20%20%20return%20%22grave%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20%22extr%C3%AAme%22%0A%0A%0Atemperature%20%3D%20valider_nombre%28%22Temp%C3%A9rature%20%28%C2%B0C%29%20%3A%20%22%2C%20TEMP_MIN%2C%20TEMP_MAX%29%0Avitesse_vent%20%3D%20valider_nombre%28%22Vitesse%20du%20vent%20%28km%2Fh%29%20%3A%20%22%2C%20VENT_MIN%2C%20VENT_MAX%29%0Aindice%20%3D%20calculer_refroidissement%28temperature%2C%20vitesse_vent%29%0Aprint%28f%22%5CnRefroidissement%20%C3%A9olien%20%3A%20%7Bindice%7D%22%29%0Aprint%28f%22Risque%20de%20gelures%20%3A%20%7Bclasser_risque%28indice%29%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=ANNEE_MIN%20%3D%201583%0AANNEE_MAX%20%3D%209999%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20est_bissextile%28annee%29%3A%0A%20%20%20%20return%20%28annee%20%25%204%20%3D%3D%200%20and%20annee%20%25%20100%20%21%3D%200%29%20or%20annee%20%25%20400%20%3D%3D%200%0A%0A%0Aannee%20%3D%20valider_entier%28%22Ann%C3%A9e%20%3A%20%22%2C%20ANNEE_MIN%2C%20ANNEE_MAX%29%0Aif%20est_bissextile%28annee%29%3A%0A%20%20%20%20print%28f%22%7Bannee%7D%20est%20bissextile%20%3A%20f%C3%A9vrier%20compte%2029%20jours.%22%29%0Aelse%3A%0A%20%20%20%20print%28f%22%7Bannee%7D%20n%27est%20pas%20bissextile%20%3A%20f%C3%A9vrier%20compte%2028%20jours.%22%29%0A%0Anb_bissextiles%20%3D%200%0Afor%20a%20in%20range%282000%2C%202101%29%3A%0A%20%20%20%20if%20est_bissextile%28a%29%3A%0A%20%20%20%20%20%20%20%20nb_bissextiles%20%2B%3D%201%0Aprint%28f%22De%202000%20%C3%A0%202100%2C%20il%20y%20a%20%7Bnb_bissextiles%7D%20ann%C3%A9es%20bissextiles.%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=JOURS%20%3D%20%28%22Lundi%22%2C%20%22Mardi%22%2C%20%22Mercredi%22%2C%20%22Jeudi%22%2C%20%22Vendredi%22%2C%20%22Samedi%22%2C%20%22Dimanche%22%29%0ATEMPERATURES%20%3D%20%28-4.5%2C%20-11.0%2C%20-8.2%2C%201.3%2C%203.8%2C%20-2.1%2C%20-15.6%29%0A%0A%0Adef%20trouver_min_max%28valeurs%29%3A%0A%20%20%20%20minimum%20%3D%20valeurs%5B0%5D%0A%20%20%20%20maximum%20%3D%20valeurs%5B0%5D%0A%20%20%20%20for%20valeur%20in%20valeurs%3A%0A%20%20%20%20%20%20%20%20if%20valeur%20%3C%20minimum%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20minimum%20%3D%20valeur%0A%20%20%20%20%20%20%20%20if%20valeur%20%3E%20maximum%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20maximum%20%3D%20valeur%0A%20%20%20%20return%20minimum%2C%20maximum%0A%0A%0Atemp_min%2C%20temp_max%20%3D%20trouver_min_max%28TEMPERATURES%29%0Aprint%28f%22Temp%C3%A9rature%20la%20plus%20basse%20%3A%20%7Btemp_min%3A.1f%7D%20%C2%B0C%20%28%7BJOURS%5BTEMPERATURES.index%28temp_min%29%5D%7D%29%22%29%0Aprint%28f%22Temp%C3%A9rature%20la%20plus%20haute%20%3A%20%7Btemp_max%3A.1f%7D%20%C2%B0C%20%28%7BJOURS%5BTEMPERATURES.index%28temp_max%29%5D%7D%29%22%29%0Aprint%28f%22%C3%89cart%20de%20la%20semaine%20%3A%20%7Btemp_max%20-%20temp_min%3A.1f%7D%20%C2%B0C%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

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

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=VOYELLES%20%3D%20%22aeiouy%C3%A0%C3%A2%C3%A4%C3%A9%C3%A8%C3%AA%C3%AB%C3%AE%C3%AF%C3%B4%C3%B6%C3%B9%C3%BB%C3%BC%22%0APHRASE_MIN%20%3D%201%0APHRASE_MAX%20%3D%20100%0A%0A%0Adef%20valider_texte%28msg_saisie%2C%20longueur_min%2C%20longueur_max%29%3A%0A%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20while%20not%20longueur_min%20%3C%3D%20len%28texte%29%20%3C%3D%20longueur_max%3A%0A%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20entre%20%7Blongueur_min%7D%20et%20%7Blongueur_max%7D%20caract%C3%A8res.%22%29%0A%20%20%20%20%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20return%20texte%0A%0A%0Adef%20compter_voyelles_consonnes%28phrase%29%3A%0A%20%20%20%20nb_voyelles%20%3D%200%0A%20%20%20%20nb_consonnes%20%3D%200%0A%20%20%20%20for%20caractere%20in%20phrase.lower%28%29%3A%0A%20%20%20%20%20%20%20%20if%20caractere%20in%20VOYELLES%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nb_voyelles%20%2B%3D%201%0A%20%20%20%20%20%20%20%20elif%20caractere.isalpha%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nb_consonnes%20%2B%3D%201%0A%20%20%20%20return%20nb_voyelles%2C%20nb_consonnes%0A%0A%0Adef%20est_palindrome%28mot%29%3A%0A%20%20%20%20mot%20%3D%20mot.lower%28%29%0A%20%20%20%20for%20i%20in%20range%28len%28mot%29%20%2F%2F%202%29%3A%0A%20%20%20%20%20%20%20%20if%20mot%5Bi%5D%20%21%3D%20mot%5B-1%20-%20i%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20return%20True%0A%0A%0Aphrase%20%3D%20valider_texte%28%22Phrase%20%3A%20%22%2C%20PHRASE_MIN%2C%20PHRASE_MAX%29%0Anb_voyelles%2C%20nb_consonnes%20%3D%20compter_voyelles_consonnes%28phrase%29%0Aprint%28f%22%5Cn%7Bnb_voyelles%7D%20voyelles%20et%20%7Bnb_consonnes%7D%20consonnes%22%29%0A%0Aprint%28%22Palindromes%20%3A%22%2C%20end%3D%22%20%22%29%0Anb_palindromes%20%3D%200%0Afor%20mot%20in%20phrase.split%28%29%3A%0A%20%20%20%20if%20len%28mot%29%20%3E%201%20and%20est_palindrome%28mot%29%3A%0A%20%20%20%20%20%20%20%20print%28mot%2C%20end%3D%22%20%22%29%0A%20%20%20%20%20%20%20%20nb_palindromes%20%2B%3D%201%0Aif%20nb_palindromes%20%3D%3D%200%3A%0A%20%20%20%20print%28%22aucun%22%2C%20end%3D%22%22%29%0Aprint%28%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">exécution...</a></sub></p>

- `compter_voyelles_consonnes()` renvoie deux compteurs dans un tuple, déballé par le programme principal.
- Dans `est_palindrome()`, la boucle ne fait que `len(mot) // 2` tours : chaque tour compare une lettre de gauche (`mot[i]`) avec sa jumelle de droite (`mot[-1 - i]`). Dès qu'une paire diffère, `return False` **termine la fonction**, sans finir la boucle.
- Le `return True` est placé **après** la boucle : on ne l'atteint que si aucune paire n'a différé.
- La réaffectation `mot = mot.lower()` ne modifie que le paramètre local : la phrase du programme principal reste intacte (voir la fiche 7.5).
- `valider_texte()` est réutilisée telle quelle, sans modification : c'est l'avantage d'une fonction générale.
