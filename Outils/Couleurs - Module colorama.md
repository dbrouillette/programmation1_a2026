# Couleurs dans la console avec le module `colorama`

## Objectifs

- Installer et importer des éléments du module `colorama`.
- Comprendre le rôle de `Fore`, `Back`, `Style` et `init()`.
- Colorer du texte dans la console en sortie (`print`) et en entrée (`input`).

## Référence

`colorama` est un module tiers (il ne fait pas partie de la bibliothèque standard de Python) qui simplifie l'utilisation des codes ANSI dans la console. Il fournit des constantes lisibles (`Fore.RED`, `Back.BLUE`, `Style.BRIGHT`, ...) à la place des codes numériques, et rend les codes ANSI fonctionnels sur d'anciennes versions de Windows qui ne les supportent pas nativement.

> **Documentation officielle** : Pour la liste complète des constantes et fonctions disponibles, voir la page du projet : [pypi.org/project/colorama](https://pypi.org/project/colorama/).

## 1. Installer et importer `colorama`

`colorama` n'étant pas inclus avec Python, il faut d'abord l'installer avec `pip` avant de pouvoir l'importer.

Dans un terminal, taper la commande suivante :

```bash
pip install colorama
```

Puis on peut charger et utiliser `colorama` dans nos programmes. Principalement, nous utiliserons les classes `Fore`, `Back` et `Style` ainsi que la méthode `init()`

```python
# importations "à la pièce"
# on importe seulement ces 4 éléments du module
from colorama import Fore, Back, Style, init
init(autoreset=True)
```

- La méthode `init()` active la conversion des codes ANSI, notamment sur les consoles Windows plus anciennes.
- Le paramètre `autoreset=True` remet automatiquement les couleurs par défaut après chaque `print()`, sans avoir à écrire `Style.RESET_ALL` soi-même.

## 2. Couleurs de texte avec `Fore`

La classe `Fore` fournit une constante par couleur de texte.

| Constante | Couleur |
| --- | --- |
| `Fore.BLACK` | Noir |
| `Fore.RED` | Rouge |
| `Fore.GREEN` | Vert |
| `Fore.YELLOW` | Jaune |
| `Fore.BLUE` | Bleu |
| `Fore.MAGENTA` | Magenta |
| `Fore.CYAN` | Cyan |
| `Fore.WHITE` | Blanc |
| `Fore.RESET` | Réinitialise la couleur du texte |

```python
print(Fore.RED + "Texte en rouge")
print(Fore.GREEN + "Texte en vert")
```

## 3. Couleurs de fond avec `Back`

La classe `Back` fonctionne exactement comme `Fore`, mais pour la couleur de fond.

```python
print(Back.RED + "Texte sur fond rouge")
print(Back.BLUE + "Texte sur fond bleu")
```

- Les mêmes noms de couleurs (`RED`, `GREEN`, `BLUE`, ...) sont disponibles pour `Back`.

## 4. Styles de texte avec `Style`

La classe `Style` contrôle l'intensité du texte plutôt que sa couleur.

| Constante | Effet |
| --- | --- |
| `Style.DIM` | Texte atténué |
| `Style.NORMAL` | Intensité normale (par défaut) |
| `Style.BRIGHT` | Texte en gras / plus vif |
| `Style.RESET_ALL` | Réinitialise couleur ET style |

```python
print(Style.BRIGHT + Fore.CYAN + "Texte vif en cyan")
```

## 5. Combiner `Fore`, `Back` et `Style`

Les constantes de `Fore`, `Back` et `Style` peuvent être combinées en les concaténant avant le texte.

```python
print(Style.BRIGHT + Fore.WHITE + Back.RED + "Erreur critique")
```

Avec `init(autoreset=True)`, il n'est pas nécessaire d'ajouter `Style.RESET_ALL` à la fin : la couleur redevient normale dès le `print()` suivant.

## 6. De la couleur dans les saisies (`input`)

Le message passé à `input()` est une chaîne comme une autre : on peut donc y insérer des constantes de `Fore`, `Back` ou `Style`. Mais l'endroit où le code de couleur est placé dans cette chaîne change complètement le résultat.

### Colorer l'invite au complet

Si le code de couleur est placé **au début** de la chaîne, c'est le texte de l'invite (le message affiché avant la saisie) qui est coloré.

```python
nom = input(Fore.CYAN + "Quel est votre nom ? ")
```

### Colorer ce que l'utilisateur tape

Il est aussi possible de colorer **différemment la saisie de l'utilisateur**, en laissant l'invite dans la couleur par défaut. Pour cela, on place le code de couleur de la saisie à la **fin** de la chaîne passée à `input()`, juste après le texte de l'invite : le code ANSI reste actif au moment où l'utilisateur commence à taper, donc c'est ce qu'il tape (et non l'invite) qui apparaît coloré.

```python
from colorama import Fore, Back, Style, init
init(autoreset=True)

nom = input(f"Votre nom : {Fore.GREEN}")
print(end=Style.RESET_ALL)  # on remet à zéro, sinon le print suivant est aussi coloré!
print(f"Bienvenue, {Fore.GREEN}{nom}")
```

- En pratique, contrairement à un `print()`, le message affiché par `input()` n'est **pas** remis à zéro automatiquement par `autoreset=True`.
- Il faut donc réinitialiser soi-même la couleur après le `input()` (par exemple avec `print(end=Style.RESET_ALL)`), sinon la couleur reste active pour au moins l'affichage suivant.

### Exemple : menu de difficulté coloré

En combinant `colorama` avec une structure `if` / `elif` / `else`, on peut colorer la réponse affichée selon le choix de l'utilisateur dans un menu :

```python
print("1. Facile")
print("2. Intermédiaire")
print("3. Avancé")

choix = input("Quel est votre choix ? ")

if choix == "1":
    print(Fore.GREEN + "Vous avez choisi le niveau Facile.")
elif choix == "2":
    print(Fore.YELLOW + "Vous avez choisi le niveau Intermédiaire.")
elif choix == "3":
    print(Fore.BLUE + "Vous avez choisi le niveau Avancé.")
else:
    print(Back.WHITE + Fore.RED + Style.BRIGHT + "Choix invalide!")
```

## 7. Remarques

- `colorama` doit être installé séparément (`pip install colorama`) ; ce n'est pas un module de la bibliothèque standard.
- Sans `init()`, certaines consoles Windows n'interpréteront pas correctement les couleurs.
- `autoreset=True` est recommandé pour éviter d'oublier de réinitialiser les couleurs après chaque affichage.

## 8. Exercices d'application

### Exercice 1 — Couleurs de base

Affichez le texte `Ceci est un succès` en vert, puis `Ceci est une erreur` en rouge, sur deux lignes distinctes.

### Exercice 2 — Avertissement

Affichez le message `Attention, espace disque faible !` avec un fond jaune, un texte noir, en gras (`Style.BRIGHT`).

### Exercice 3 — Invite colorée

Demandez le prénom de l'utilisateur avec une invite affichée en cyan (`Quel est votre prénom ?`), puis affichez `Bonjour, <prénom> !` en blanc.

### Exercice 4 — Colorer la saisie plutôt que l'invite

Demandez le prénom de l'utilisateur, mais cette fois l'invite doit rester dans la couleur par défaut du terminal et ce que l'utilisateur **tape** doit apparaître en magenta. N'oubliez pas de réinitialiser la couleur après la saisie.

### Exercice 5 — Mini-menu Roche-Papier-Ciseaux

Affichez un menu à trois choix :

- `1. Roche`
- `2. Papier`
- `3. Ciseaux`

Demandez à l'utilisateur son choix. Affichez le choix sélectionné dans une couleur différente pour chacun des trois choix (par exemple bleu pour Roche, blanc pour Papier, jaune pour Ciseaux), et un message d'erreur en rouge sur fond blanc si le choix n'est pas `1`, `2` ou `3`.

## 9. Résumé

- `from colorama import Fore, Back, Style, init` puis `init(autoreset=True)` pour démarrer.
- `Fore` pour la couleur du texte, `Back` pour la couleur de fond, `Style` pour l'intensité.
- `colorama` rend le code plus lisible que les codes ANSI bruts, au prix d'une dépendance externe à installer.

## RÉPONSES aux exercices d'application

### Solution 1 — Couleurs de base

```python
from colorama import Fore, init
init(autoreset=True)

print(Fore.GREEN + "Ceci est un succès")
print(Fore.RED + "Ceci est une erreur")
```

### Solution 2 — Avertissement

```python
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + "Attention, espace disque faible !")
```

### Solution 3 — Invite colorée

```python
from colorama import Fore, init
init(autoreset=True)

prenom = input(Fore.CYAN + "Quel est votre prénom ? ")
print(Fore.WHITE + f"Bonjour, {prenom} !")
```

### Solution 4 — Colorer la saisie plutôt que l'invite

```python
from colorama import Fore, Style, init
init(autoreset=True)

prenom = input(f"Quel est votre prénom ? {Fore.MAGENTA}")
print(end=Style.RESET_ALL)  # on remet à zéro, sinon le print suivant est aussi coloré!
print(f"Bonjour, {prenom} !")
```

### Solution 5 — Mini-menu Roche-Papier-Ciseaux

```python
from colorama import Fore, Back, init
init(autoreset=True)

print("1. Roche")
print("2. Papier")
print("3. Ciseaux")

choix = input("Quel est votre choix ? ")

if choix == "1":
    print(Fore.BLUE + "Vous avez choisi : Roche")
elif choix == "2":
    print(Fore.WHITE + "Vous avez choisi : Papier")
elif choix == "3":
    print(Fore.YELLOW + "Vous avez choisi : Ciseaux")
else:
    print(Back.WHITE + Fore.RED + "Choix invalide !")
```
