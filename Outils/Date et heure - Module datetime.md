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

## 4. Que contient une valeur `datetime` ?

Une valeur `datetime` contient plusieurs composantes qui décrivent un moment précis :

- `year` : l'année
- `month` : le mois, de 1 à 12
- `day` : le jour du mois
- `hour` : l'heure, de 0 à 23
- `minute` : les minutes, de 0 à 59
- `second` : les secondes, de 0 à 59
- `microsecond` : une fraction de seconde, lorsque nécessaire

```python
print(maintenant.year)
print(maintenant.month)
print(maintenant.day)
print(maintenant.hour)
print(maintenant.minute)
print(maintenant.second)
print(maintenant.microsecond)
```

### Comparaison avec Excel

Excel représente généralement une date par un nombre :

- la partie entière représente le nombre de jours écoulés depuis une date de référence;
- la partie décimale représente la fraction de la journée correspondant à l'heure.

Par exemple, `45000,5` représente un jour dont l'heure est environ 12 h, puisque `0,5` correspond à la moitié d'une journée. Excel affiche ensuite ce nombre sous forme de date ou d'heure selon le format de cellule choisi.

Dans Excel :

- `=AUJOURDHUI()` renvoie la date du jour, sans l'heure;
- `=MAINTENANT()` renvoie la date du jour avec l'heure actuelle.

Le rôle de ces fonctions est comparable à celui de Python :

```python
date_du_jour = datetime.date.today()       # comparable à =AUJOURDHUI()
maintenant = datetime.datetime.now()       # comparable à =MAINTENANT()
```

La différence est qu'Excel stocke directement la date comme un nombre séquentiel, alors que Python utilise un objet `date` ou `datetime` avec des composantes accessibles. Dans les deux cas, le format d'affichage ne change pas la valeur réelle.

## 5. Formater une date ou une heure

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

## 6. Calculer la différence entre deux dates

La soustraction de deux objets `datetime` produit un objet `timedelta`. Cet objet permet notamment d'obtenir le nombre total de jours, de secondes, de minutes ou d'heures entre deux moments.

```python
import datetime

debut = datetime.datetime(2026, 9, 15, 8, 30, 0)
fin = datetime.datetime(2026, 9, 16, 10, 45, 20)

difference = fin - debut
secondes_totales = int(difference.total_seconds())
minutes_totales = secondes_totales // 60
secondes_restantes = secondes_totales % 60

print("Différence en jours :", difference.days)
print("Différence en minutes :", minutes_totales)
print("Différence en secondes :", secondes_totales)
print(f"Durée : {difference.days} jour(s), {minutes_totales % 60} minute(s) et {secondes_restantes} seconde(s)")
```

Les minutes et les secondes sont exactes. En revanche, un mois peut avoir 28, 29, 30 ou 31 jours et une année peut avoir 365 ou 366 jours. Une conversion en mois ou en années est donc une **approximation** lorsqu'on utilise une durée :

```python
annees_approximatives = secondes_totales / (365.25 * 24 * 60 * 60)
mois_approximatifs = secondes_totales / (30.44 * 24 * 60 * 60)

print(f"Environ {annees_approximatives:.2f} année(s)")
print(f"Environ {mois_approximatifs:.2f} mois")
```

Pour un âge ou une durée exprimée en années et en mois civils exacts, il faut comparer les composantes de la date (`year`, `month`, `day`) plutôt que convertir une durée en secondes.

### Le module `calendar`

Le module `datetime` sert à créer et à manipuler une date précise. Par exemple, `datetime.date(2026, 1, 31)` représente le 31 janvier 2026. Le module `calendar`, lui, fournit des informations sur le calendrier, comme le nombre de jours dans un mois.

On peut donc utiliser `datetime` pour la date et `calendar` pour vérifier les règles du mois. La fonction `calendar.monthrange()` renvoie le jour de la semaine du premier jour et le nombre de jours du mois.

### Ajouter un mois sans gérer sa longueur

Pour ajouter des jours, utilisez `timedelta`. Python s'occupe alors automatiquement des changements de mois et d'année. Pour ajouter un mois, utilisez `calendar.monthrange()` afin d'obtenir le dernier jour réel du mois, sans mémoriser si le mois contient 28, 29, 30 ou 31 jours.

```python
import calendar
import datetime

date_depart = datetime.date(2026, 1, 31)
nouvelle_annee = date_depart.year
nouveau_mois = date_depart.month + 1
dernier_jour = calendar.monthrange(nouvelle_annee, nouveau_mois)[1]
nouveau_jour = min(date_depart.day, dernier_jour)
date_apres_un_mois = date_depart.replace(
	year=nouvelle_annee,
	month=nouveau_mois,
	day=nouveau_jour,
)
date_apres_30_jours = date_depart + datetime.timedelta(days=30)

print("Après un mois :", date_apres_un_mois)  # 2026-02-28
print("Après 30 jours :", date_apres_30_jours)  # 2026-03-02

date_limite = datetime.date.today() + datetime.timedelta(days=30)
if datetime.date.today() >= date_limite:
	print("La date limite est atteinte.")
else:
	print("La date limite n'est pas encore atteinte.")
```

Un **mois civil** et un nombre fixe de jours ne représentent pas la même durée. Utilisez `ajouter_mois()` pour une échéance mensuelle, comme une facture ou un abonnement, et `timedelta(days=...)` pour une durée exacte en jours. Cette approche est comparable à la fonction `MOIS.DECALER()` d'Excel.

### Valider une date saisie

La méthode `strptime()` déclenche une erreur `ValueError` si la chaîne ne respecte pas le format attendu ou si la date n'existe pas. Un bloc `try/except` permet d'intercepter cette erreur et de redemander une saisie valide.

```python
import datetime

date_valide = False

while not date_valide:
	date_texte = input("Entrez une date (JJ/MM/AAAA) : ")

	try:
		date_choisie = datetime.datetime.strptime(date_texte, "%d/%m/%Y")
		date_valide = True
	except ValueError:
		print("Erreur : utilisez une date réelle au format JJ/MM/AAAA.")

print("Date acceptée :", date_choisie.strftime("%d/%m/%Y"))
```

## 7. Déclencher un compteur à une date donnée

Une date entrée par l'utilisateur est une chaîne de caractères. La méthode `strptime()` permet de la convertir en objet `datetime`. On peut ensuite utiliser une boucle `while` qui attend jusqu'à la date prévue. Dans cet exemple, le programme affiche le nombre de secondes restantes et déclenche une action à l'arrivée.

```python
import datetime
import time

date_cible = None

while date_cible is None:
	date_texte = input("Date de déclenchement (JJ/MM/AAAA HH:MM:SS) : ")

	try:
		date_cible = datetime.datetime.strptime(date_texte, "%d/%m/%Y %H:%M:%S")
	except ValueError:
		print("Erreur : utilisez une date réelle au format JJ/MM/AAAA HH:MM:SS.")

while datetime.datetime.now() < date_cible:
	maintenant = datetime.datetime.now()
	secondes_restantes = int((date_cible - maintenant).total_seconds())
	print(f"Il reste {secondes_restantes} seconde(s).")
	time.sleep(1)

print("La date cible est atteinte !")
```

Pour tester rapidement le programme, entrez une date située une ou deux minutes dans le futur. La date doit respecter exactement le format `JJ/MM/AAAA HH:MM:SS`.

## 8. Exemple complet

```python
import datetime

maintenant = datetime.datetime.now()
print(f"Il est {maintenant.strftime('%H:%M')} le {maintenant.strftime('%d/%m/%Y')}")
```

## 9. Résumé

- `datetime.date.today()` donne la date seule.
- `datetime.datetime.now()` donne date et heure.
- `strftime()` permet de personnaliser l'affichage.
- `strptime()` convertit une chaîne en objet `datetime`.
- La soustraction de deux objets `datetime` produit un `timedelta`.
- Une boucle `while` peut attendre l'arrivée d'une date cible.

## 10. Exercices d'application

### Exercice 1 — Date du jour

Affichez la date du jour sous la forme complète en toutes lettres, par exemple `mardi 15 septembre 2026`.

### Exercice 2 — Heure actuelle

Affichez l'heure actuelle sous la forme `HH:MM:SS` (par exemple `14:05:09`).

### Exercice 3 — Âge approximatif

Demandez à l'utilisateur son année de naissance, puis calculez et affichez son âge approximatif (année actuelle moins année de naissance).

### Exercice 4 — Date personnalisée

Demandez à l'utilisateur une année, un mois et un jour (trois nombres entiers séparés). Créez un objet `date` à partir de ces valeurs avec `datetime.date(annee, mois, jour)`, puis affichez-le sous la forme `JJ/MM/AAAA`.

### Exercice 5 — Composantes d'une date

Créez une variable `maintenant` avec `datetime.datetime.now()`. Affichez séparément son année, son mois, son jour, son heure, ses minutes et ses secondes.

### Exercice 6 — Valider une date entrée au clavier

Demandez une date au format `JJ/MM/AAAA`. Utilisez `try/except` et `strptime()` pour redemander la date tant que la saisie n'est pas valide. Affichez ensuite la date acceptée.

### Exercice 7 — Différence entre deux dates

Demandez deux dates et heures au format `JJ/MM/AAAA HH:MM:SS`. Calculez la différence entre ces deux moments et affichez-la en jours, en minutes et en secondes.

### Exercice 8 — Ajouter un mois à une date

Créez une date correspondant au 31 janvier 2026. Utilisez `calendar.monthrange()` pour trouver le nombre de jours du mois suivant, puis affichez le dernier jour de ce mois. Le résultat attendu est le 28 février 2026.

### Exercice 9 — Compteur jusqu'à une date cible

Demandez une date cible au format `JJ/MM/AAAA HH:MM:SS`. Validez la saisie, puis utilisez une boucle `while` et `time.sleep(1)` pour afficher le nombre de secondes restantes jusqu'à l'atteinte de la date cible.

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

### Solution 5 — Composantes d'une date

```python
import datetime

maintenant = datetime.datetime.now()
print("Année :", maintenant.year)
print("Mois :", maintenant.month)
print("Jour :", maintenant.day)
print("Heure :", maintenant.hour)
print("Minutes :", maintenant.minute)
print("Secondes :", maintenant.second)
```

### Solution 6 — Valider une date entrée au clavier

```python
import datetime

date_choisie = None

while date_choisie is None:
	date_texte = input("Date (JJ/MM/AAAA) : ")

	try:
		date_choisie = datetime.datetime.strptime(date_texte, "%d/%m/%Y")
	except ValueError:
		print("Date invalide. Recommencez.")

print("Date acceptée :", date_choisie.strftime("%d/%m/%Y"))
```

### Solution 7 — Différence entre deux dates

```python
import datetime

debut_texte = input("Début (JJ/MM/AAAA HH:MM:SS) : ")
fin_texte = input("Fin (JJ/MM/AAAA HH:MM:SS) : ")

debut = datetime.datetime.strptime(debut_texte, "%d/%m/%Y %H:%M:%S")
fin = datetime.datetime.strptime(fin_texte, "%d/%m/%Y %H:%M:%S")
difference = fin - debut

print("Différence en jours :", difference.days)
print("Différence en minutes :", difference.total_seconds() / 60)
print("Différence en secondes :", difference.total_seconds())
```

### Solution 8 — Ajouter un mois à une date

```python
import calendar
import datetime

date_depart = datetime.date(2026, 1, 31)
mois_suivant = date_depart.month + 1
nombre_de_jours = calendar.monthrange(date_depart.year, mois_suivant)[1]
date_fin_du_mois = datetime.date(date_depart.year, mois_suivant, nombre_de_jours)

print("Dernier jour du mois suivant :", date_fin_du_mois)
```

### Solution 9 — Compteur jusqu'à une date cible

```python
import datetime
import time

date_cible = None

while date_cible is None:
	date_texte = input("Date cible (JJ/MM/AAAA HH:MM:SS) : ")

	try:
		date_cible = datetime.datetime.strptime(date_texte, "%d/%m/%Y %H:%M:%S")
	except ValueError:
		print("Date invalide. Recommencez.")

while datetime.datetime.now() < date_cible:
	secondes_restantes = int(
		(date_cible - datetime.datetime.now()).total_seconds()
	)
	print("Il reste", secondes_restantes, "seconde(s).")
	time.sleep(1)

print("La date cible est atteinte !")
```
