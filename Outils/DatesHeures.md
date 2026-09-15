# Dates et heures en Python

## Objectifs

- Utiliser le module `datetime`.
- Obtenir la date et l'heure actuelles.
- Formater une date et une heure.

## Référence

Le module `datetime` fait partie de la bibliothèque standard de Python. Il fournit des classes pour manipuler des dates (`date`), des heures (`time`) et des combinaisons des deux (`datetime`), ainsi que pour faire des calculs sur des durées (`timedelta`).

> **Documentation officielle** : Pour la liste complète des classes et méthodes disponibles, voir la documentation officielle : [docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html).

## 1. Importer `datetime`

```python
import datetime
```

## 2. Date du jour

La classe `date` du module `datetime` représente une date civile (année, mois, jour), sans notion d'heure. La méthode `today()` renvoie la date actuelle fournie par l'horloge du système.

```python
date_du_jour = datetime.date.today()
print(date_du_jour)
print(date_du_jour.year)
print(date_du_jour.month)
print(date_du_jour.day)
```

## 3. Date et heure actuelles

La classe `datetime` (incluse dans le module du même nom) combine une date et une heure en un seul objet. La méthode `now()` renvoie l'instant présent, avec un accès aux heures, minutes et secondes.

```python
maintenant = datetime.datetime.now()
print(maintenant)
print(maintenant.hour)
print(maintenant.minute)
print(maintenant.second)
```

## 4. Formater une date ou une heure

Par défaut, un objet `date` ou `datetime` s'affiche dans un format fixe qui n'est pas toujours celui souhaité. La méthode `strftime()` (« string format time ») convertit un objet date/heure en chaîne de caractères, selon un gabarit composé de codes de format.

```python
print(date_du_jour)
print(maintenant)
print(maintenant.strftime("%d/%m/%Y %H:%M:%S"))
print(date_du_jour.strftime("%A %d %B %Y"))
```

### Codes de format utiles

Voici les principaux codes de format les plus couramment utilisés :

- `%Y` : année sur 4 chiffres
- `%m` : mois sur 2 chiffres
- `%B` : mois complet en lettres
- `%d` : jour du mois
- `%H` : heure (00-23)
- `%M` : minute
- `%S` : seconde
- `%B` : mois en toutes lettres
- `%A` : jour de la semaine en lettres

> Consulter la [**liste complète** des codes de format](https://docs.python.org/fr/3.14/library/datetime.html#strftime-and-strptime-format-codes) de date Python pour plus de détails.

## 5. Exemple complet

```python
import datetime

maintenant = datetime.datetime.now()
print(f"Il est {maintenant.strftime('%H:%M')} le {maintenant.strftime('%d/%m/%Y')}")
```

## 6. Résumé

- `datetime.date.today()` donne la date seule.
- `datetime.datetime.now()` donne date et heure.
- `strftime()` permet de personnaliser l'affichage.

## 7. Exercices d'application

### Exercice 1 — Date du jour

Affichez la date du jour sous la forme complète en toutes lettres, par exemple `mardi 15 septembre 2026`.

### Exercice 2 — Heure actuelle

Affichez l'heure actuelle sous la forme `HH:MM:SS` (par exemple `14:05:09`).

### Exercice 3 — Âge approximatif

Demandez à l'utilisateur son année de naissance, puis calculez et affichez son âge approximatif (année actuelle moins année de naissance).

### Exercice 4 — Date personnalisée

Demandez à l'utilisateur une année, un mois et un jour (trois nombres entiers séparés). Créez un objet `date` à partir de ces valeurs avec `datetime.date(annee, mois, jour)`, puis affichez-le sous la forme `JJ/MM/AAAA`.

## 🎥 Vidéo explicative

[![Regarder](https://img.youtube.com/vi/GzhG26cvmNg/maxresdefault.jpg)](https://youtu.be/GzhG26cvmNg)

*Cette vidéo explique comment gérer les dates et les heures en Python avec le module `datetime`.*

## RÉPONSES aux exercices d'application

### Solution 1 — Date du jour

```python
import datetime

date_du_jour = datetime.date.today()
print(date_du_jour.strftime("%A %d %B %Y"))
```

### Solution 2 — Heure actuelle

```python
import datetime

maintenant = datetime.datetime.now()
print(maintenant.strftime("%H:%M:%S"))
```

### Solution 3 — Âge approximatif

```python
import datetime

annee_naissance = int(input("Entrez votre année de naissance : "))
annee_actuelle = datetime.date.today().year
age = annee_actuelle - annee_naissance
print("Vous avez environ", age, "ans.")
```

### Solution 4 — Date personnalisée

```python
import datetime

annee = int(input("Année : "))
mois = int(input("Mois : "))
jour = int(input("Jour : "))

date_choisie = datetime.date(annee, mois, jour)
print(date_choisie.strftime("%d/%m/%Y"))
```
