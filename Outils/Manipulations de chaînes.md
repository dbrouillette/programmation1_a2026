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

## 🎥 Vidéo explicative

[![Regarder](https://img.youtube.com/vi/gPfWk2oYnR0/maxresdefault.jpg)](https://youtu.be/gPfWk2oYnR0)

*Cette vidéo présente plusieurs méthodes utiles pour manipuler des chaînes de caractères en Python, dont `split`, `join`, `strip` et `startswith`.*
