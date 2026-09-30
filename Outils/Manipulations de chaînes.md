# Méthodes utiles pour les chaînes de caractères (`str`) en Python

## Objectifs

- Connaître les méthodes utiles pour manipuler les chaînes de caractères.
- Savoir accéder à un caractère et extraire une sous-chaîne (« slicing »).
- Apprendre à comparer, transformer et remplacer du texte.

| Méthode/Fonction | Description | Exemple d'utilisation |
| --- | --- | --- |
| `len(s)` | Retourne la longueur de la chaîne. **Fonction native, pas une méthode!** | `len("Bonjour")` → `7` |
| `s.strip()` | Supprime les caractères invisibles (espaces, tabulations `\t`, retours de ligne `\n`) au début et à la fin de la chaîne. | `"  Salut  ".strip()` → `"Salut"` |
| `s.lower()` | Convertit tous les caractères en minuscules. | `"PYTHON".lower()` → `"python"` |
| `s.upper()` | Convertit tous les caractères en majuscules. | `"python".upper()` → `"PYTHON"` |
| `s.capitalize()` | Met le premier caractère en majuscule et **tous les autres en minuscules**. | `"bonJOUR le monde".capitalize()` → `"Bonjour le monde"` |
| `s1 == s2` | Compare deux chaînes en tenant compte de la casse. **Utiliser directement `==` pour comparer.** | `"test" == "Test"` → `False` |
| `s1.lower() == s2.lower()` | Compare deux chaînes sans tenir compte de la casse. | `"test".lower() == "Test".lower()` → `True` |
| `s[index]` | Retourne le caractère à l'index donné (commence à 0). **Accès direct par indexation avec crochets `[ ]`.** | `"abc"[1]` → `'b'` |
| `s.find(sous_chaine)` | Retourne l'index de la première occurrence de `sous_chaine` (ou `-1` si absent). | `"programmation".find("gram")` → `3` |
| | | `"programmation".find("y")` → `-1` |
| `s[debut:]` | Retourne la sous-chaîne à partir de l'index donné jusqu'à la fin. **Notation par tranche (« *slicing* »).** | `"Bonjour"[3:]` → `"jour"` |
| | Si `debut` est omis, la tranche commence au premier caractère. | `"Bonjour"[:]` → `"Bonjour"` |
| `s[debut:fin]` | Retourne la sous-chaîne entre les index `debut` (inclus) et `fin` (exclu). | `"Bonjour"[0:3]` → `"Bon"` |
| | Si `debut` est omis, la tranche commence au premier caractère. | `"Bonjour"[:3]` → `"Bon"` |
| | Si `fin` est omis, la tranche se termine à la fin de `s`. | `"Bonjour"[2:]` → `"njour"` |
| `s[debut:fin:pas]` | Retourne la sous-chaîne entre les index `debut` (inclus) et `fin` (exclu) par bonds de `pas`. | `"Bonjour"[0:3:2]` → `"Bn"` |
| | Si `debut` est omis, la tranche commence au premier caractère. | `"Bonjour"[:3:2]` → `"Bn"` |
| | Si `fin` est omis, la tranche se termine à la fin de `s`. | `"Bonjour"[1::3]` → `"oo"` |
| | Avec un `pas` **négatif**, les indices sont inversés : `debut` = fin de la chaîne, `fin` = début de la chaîne | `"Bonjour"[5:2:-1]` → `"uoj"` |
| | Si `debut` est omis, la tranche commence au **dernier** caractère. | `"Bonjour"[:2:-1]` → `"ruoj"` |
| | Si `fin` est omis, la tranche se termine **au début** de `s`. | `"Bonjour"[5::-1]` → `"uojnoB"` |
| | Cas particulier : tranche complète inversée. | `"Bonjour"[::-2]` → `"ronB"` |
| `s.replace(cible, remplacement)` | Remplace toutes les occurrences de `cible` par `remplacement` — fonctionne autant pour un seul caractère que pour une chaîne complète. | `"papa".replace("p", "m")` → `"mama"` |
| `sous_chaine in s` | Vérifie si `sous_chaine` est présente dans `s`. **Opérateur, pas une méthode!** | `"gram" in "programmation"` → `True` |
| `s.startswith(debut)` | Vérifie si la chaîne commence par `debut`. | `"Bonjour".startswith("Bon")` → `True` |
| `s.endswith(fin)` | Vérifie si la chaîne se termine par `fin`. | `"photo.jpg".endswith(".jpg")` → `True` |
| `s.count(sous_chaine)` | Retourne le nombre d'occurrences de `sous_chaine` dans `s`. | `"banane".count("a")` → `3` |
| `s.isdigit()` | Vérifie si la chaîne contient **uniquement** des chiffres (et au moins un caractère). | `"42".isdigit()` → `True` |
| | ⚠️ Le signe `-` et le point `.` ne sont pas des chiffres. | `"-5".isdigit()` → `False` |
| `s.split(separateur)` | Découpe la chaîne en morceaux selon `separateur` et retourne une **liste**. 📋 *Nécessite les listes.* | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `separateur.join(liste)` | Assemble les éléments d'une **liste** en une chaîne, séparés par `separateur`. L'inverse de `split()`. 📋 *Nécessite les listes.* | `"-".join(['a', 'b', 'c'])` → `"a-b-c"` |

> 📋 **Note :** `split()` et `join()` utilisent des **listes**, que nous verrons plus tard dans la session. Elles sont présentées ici pour que le tableau soit complet; nous y reviendrons lorsque les listes auront été vues.

## 📝 Points importants à retenir

### 1. `len()` est une fonction, pas une méthode

**On appelle `len()` avec la chaîne comme argument** (une fonction native, qui fonctionne aussi sur beaucoup d'autres types que nous verrons plus tard, comme les listes) — ce n'est pas une méthode qu'on appelle sur la chaîne elle-même.

```python
texte = "Bonjour"
print(len(texte))       # ✅ correct
print(texte.length())   # ❌ ERREUR — .length() n'existe pas en Python!
```

### 2. Accès aux caractères par indexation

On accède directement à un caractère avec des crochets `[ ]`, comme pour une liste :

```python
mot = "Python"
print(mot[0])   # 'P'
print(mot[2])   # 't'
```

### 3. Le « slicing » pour extraire une sous-chaîne

Pour extraire une partie d'une chaîne, on utilise la **notation par tranche** (« slicing ») directement avec des crochets et `:` :

```python
mot = "Bonjour"
print(mot[3:])     # "jour"   (à partir de l'index 3 jusqu'à la fin)
print(mot[0:3])    # "Bon"    (de l'index 0 à 3, exclu)
print(mot[:3])     # "Bon"    (le début peut être omis)
print(mot[-4:])    # "jour"   (les index négatifs comptent depuis la fin)
```

### 4. On utilise `==` directement pour comparer

Comme vu dans le fichier sur les opérateurs relationnels, Python compare toujours le **contenu** des chaînes avec `==`. Il n'y a donc jamais besoin d'une méthode séparée pour comparer deux chaînes.

### 5. Une seule méthode `.replace()` pour tout

**Python n'a qu'une seule méthode `.replace()`**, qui fonctionne peu importe la longueur des chaînes impliquées — que ce soit un seul caractère ou une chaîne complète.

### 6. `in` pour vérifier la présence d'un texte

Pour savoir si une chaîne en contient une autre, `in` est plus simple et plus lisible que `find()` :

```python
courriel = "etudiant@cegeptr.qc.ca"
if "@" in courriel:              # ✅ simple et clair
    print("Courriel valide")
if courriel.find("@") != -1:     # fonctionne aussi, mais moins lisible
    print("Courriel valide")
```

### 7. Valider une saisie avec `isdigit()` avant de convertir

`int(input())` plante si l'utilisateur tape autre chose qu'un nombre. On peut vérifier d'abord avec `isdigit()` :

```python
reponse = input("Entrez votre âge : ")
if reponse.isdigit():
    age = int(reponse)
else:
    print("Veuillez entrer un nombre entier positif.")
```

⚠️ **Attention :** `isdigit()` retourne `False` pour les nombres négatifs (`"-5"`) et les nombres décimaux (`"3.14"`), car `-` et `.` ne sont pas des chiffres.

## 🎥 Vidéo explicative

[![Regarder](https://img.youtube.com/vi/gPfWk2oYnR0/maxresdefault.jpg)](https://youtu.be/gPfWk2oYnR0)

*Cette vidéo présente plusieurs méthodes utiles pour manipuler des chaînes de caractères en Python, dont `split`, `join`, `strip` et `startswith`.*
