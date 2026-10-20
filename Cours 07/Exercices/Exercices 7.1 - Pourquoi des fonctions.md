# Exercices — Pourquoi des fonctions? (fiche 7.1)

> 📌 Les exercices de cette série se font **sans écrire de programme**. Ils servent à bien maîtriser le vocabulaire et le rôle des fonctions avant de commencer à en écrire. Tu peux toutefois vérifier tes réponses dans VS Code lorsque c'est possible.

## 🟢 Exercice 1 : Facile

**But** : Distinguer ce qu'on **donne** à une fonction de ce qu'elle **renvoie** ou **fait**.

**Énoncé** : Pour chacun des appels suivants, indique :

- **ce qu'on lui donne** (ses arguments, et leur type);
- si elle **renvoie** une valeur (laquelle, et de quel type) ou si elle se contente de **faire** quelque chose (afficher, modifier une liste…).

Fais d'abord l'exercice sans exécuter de code. Vérifie ensuite tes réponses dans VS Code en affichant le résultat de chaque appel avec `print()`.

```python
a.  len("bonjour")
b.  round(2.675, 1)
c.  round(18.7)
d.  print("Allo", "toi")
e.  input("Ton nom : ")          # suppose que l'utilisateur tape : Léa
f.  int("42")
g.  float("3.5")
h.  str(2026)
i.  abs(-7)
j.  max(12, 45, 8)
k.  sum([2.25, 4.50, 1.95])
l.  type(3.0)
m.  "latté".upper()
n.  "  muffin  ".strip()
o.  "café,thé,jus".split(",")
p.  epicerie.append("lait")     # epicerie vaut ["pain"] avant l'appel
q.  sorted([3, 1, 2])
r.  epicerie.sort()             # epicerie vaut ["pain", "lait"] avant l'appel
```

*Exemple de réponse attendue (pour l'appel a.) :*

| Appel | On lui donne | Elle renvoie / elle fait |
| --- | --- | --- |
| a. `len("bonjour")` | une chaîne (`str`) | renvoie `7` (`int`) |
| b. `round(2.675, 1)` | ... | ... |
| c. `...` | ... | ... |

## 🟢 Exercice 2 : Facile

**But** : Reconnaître le **nom**, les **paramètres**, les **arguments** et la **valeur de retour** d'une fonction.

**Énoncé** : Pour chacun des extraits suivants, identifie :

1. le **nom** de la fonction;
2. ses **paramètres** (dans la définition);
3. les **arguments** de chaque appel (dans l'appel);
4. la **valeur de retour** de chaque appel, s'il y en a une (sinon, écris « aucune »).

Pas besoin de comprendre chaque détail de la syntaxe : elle sera vue dans les prochaines fiches. Concentre-toi sur le vocabulaire.

### Extrait A

```python
def calculer_aire_rectangle(largeur, hauteur):
    return largeur * hauteur

aire = calculer_aire_rectangle(4, 2.5)
```

### Extrait B

```python
def afficher_bienvenue():
    print("Bienvenue à la bibliothèque du cégep!")

afficher_bienvenue()
```

### Extrait C

```python
def saluer(prenom):
    print(f"Bonjour {prenom}!")

nom_etudiant = "Samuel"
saluer(nom_etudiant)
saluer("Léa")
```

### Extrait D

```python
def convertir_en_minutes(heures, minutes):
    return heures * 60 + minutes

duree = convertir_en_minutes(2, 15)
print(convertir_en_minutes(1, 0))
```

### Extrait E

```python
def calculer_prix_taxes(prix):
    return round(prix * 1.14975, 2)

prix_livre = 24.95
total = calculer_prix_taxes(prix_livre) + calculer_prix_taxes(5.00)
```

### Extrait F

```python
def afficher_note(cours, note):
    print(f"{cours} : {note} %")

afficher_note("Programmation", 87)
afficher_note("Français", 79 + 3)
```

> 💡 Dans l'extrait C, le nom de la variable `nom_etudiant` est-il le même que celui du paramètre? Est-ce un problème?

## 🟡 Exercice 3 : Moyen

**But** : Repérer le code répété dans un programme et le remplacer, en pensée, par des fonctions.

**Énoncé** : Le programme ci-dessous calcule la moyenne de trois groupes d'un cours. Lis-le attentivement, puis :

a. Repère les **blocs de code répétés** (indique leurs numéros de lignes).  
b. Pour chacun de ces blocs, propose un **nom de fonction** significatif.  
c. Réécris le programme principal (les lignes qui appelleraient tes fonctions) comme s'il utilisait ces fonctions. Les fonctions elles-mêmes n'ont pas à être écrites.
d. Si on voulait maintenant que les notes soient acceptées entre 0 et **105** (pour un bonus), combien de modifications faudrait-il faire dans le programme actuel? Et dans ta version avec des fonctions?

```python
 1  NB_ETUDIANTS = 3
 2
 3  print("=" * 30)
 4  print("Groupe 01")
 5  print("=" * 30)
 6  total = 0
 7  for i in range(1, NB_ETUDIANTS + 1):
 8      valide = False
 9      while not valide:
10          try:
11              note = float(input(f"Note {i} : "))
12              if 0 <= note <= 100:
13                  valide = True
14              else:
15                  print("La note doit être entre 0 et 100.")
16          except ValueError:
17              print("Ce n'est pas un nombre.")
18      total += note
19  print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")
20
21  print("=" * 30)
22  print("Groupe 02")
23  print("=" * 30)
24  total = 0
25  for i in range(1, NB_ETUDIANTS + 1):
26      valide = False
27      while not valide:
28          try:
29              note = float(input(f"Note {i} : "))
30              if 0 <= note <= 100:
31                  valide = True
32              else:
33                  print("La note doit être entre 0 et 100.")
34          except ValueError:
35              print("Ce n'est pas un nombre.")
36      total += note
37  print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")
38
39  print("=" * 30)
40  print("Groupe 03")
41  print("=" * 30)
42  total = 0
43  for i in range(1, NB_ETUDIANTS + 1):
44      valide = False
45      while not valide:
46          try:
47              note = float(input(f"Note {i} : "))
48              if 0 <= note <= 100:
49                  valide = True
50              else:
51                  print("La note doit être entre 0 et 100.")
52          except ValueError:
53              print("Ce n'est pas un nombre.")
54      total += note
55  print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")
```

## 🟡 Exercice 4 : Moyen

**But** : Relier chaque avantage des fonctions à une situation concrète.

**Énoncé** : Associe chacune des situations suivantes à l'avantage des fonctions qu'elle illustre le mieux. Chaque avantage est utilisé une seule fois.

| Avantages |
| --- |
| A. Réutiliser |
| B. Découper un problème |
| C. Nommer une tâche |
| D. Maintenance facile |
| E. Faciliter les tests |

| # | Situation |
| --- | --- |
| 1 | Le taux de la TVQ change. Mia modifie une seule ligne, dans `calculer_taxes()`, et toutes les factures de son programme sont maintenant exactes. |
| 2 | Avant d'écrire son jeu de quiz, Noah fait la liste des étapes : afficher les règles, poser une question, vérifier la réponse, afficher le score. Il écrit ensuite une fonction pour chaque étape. |
| 3 | Dans son TP, Léa appelle sa fonction de saisie validée à six endroits différents, sans recopier la boucle de validation une seule fois. |
| 4 | En relisant son code un mois plus tard, Samuel comprend tout de suite ce que fait la ligne `if est_bissextile(annee):`, sans relire le calcul. |
| 5 | Avant d'intégrer `convertir_en_fahrenheit()` à son programme, Zoé l'appelle avec `0`, `100` et `-40` pour vérifier que les résultats sont bons. |

## 🔴 Exercice 5 : Difficile

**But** : Découper un problème en fonctions avant de programmer.

**Énoncé** : La Ville de Trois-Rivières veut un petit programme pour ses bornes de location de vélos. Voici ce qu'il doit faire :

> Au démarrage, la borne affiche un message de bienvenue et la liste des vélos offerts (vélo régulier, vélo électrique, vélo cargo) avec leur tarif à l'heure. L'utilisateur choisit un vélo, puis indique pour combien d'heures il veut le louer (entre 1 et 8 heures). Chaque saisie est validée. Les membres de Vélo-TR ont un rabais de 20 %. La borne calcule le coût de la location, ajoute les taxes, puis affiche un reçu détaillé. Enfin, elle demande si l'utilisateur veut louer un autre vélo; si oui, on recommence.

Propose une liste de **5 à 8 fonctions** pour ce programme. Pour chacune, donne :

- un **nom** significatif (en `snake_case`, commençant par un verbe);
- ce qu'elle **reçoit** (ses paramètres, s'il y en a);
- ce qu'elle **renvoie** ou ce qu'elle **fait**;
- une phrase qui décrit son **rôle**.

*Exemple de réponse attendue (pour une fonction) :*

```text
Nom      : afficher_bienvenue
Reçoit   : rien
Renvoie  : rien (elle affiche)
Rôle     : Affiche le message de bienvenue de la borne.
```

> 💡 Inspire-toi de la caisse du Café Le Binaire : on y trouve des fonctions qui **affichent**, des fonctions qui **lisent** une saisie validée et des fonctions qui **calculent**.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.1 - Pourquoi des fonctions](Solutions%207.1%20-%20Pourquoi%20des%20fonctions.md).
