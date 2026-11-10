# Exercices — Lire un fichier texte (fiche 8.3)

> 📌 **À savoir** : Python Tutor ne gère pas les fichiers. Fais ces exercices dans VS Code, et crée chaque fichier texte demandé **dans le même dossier** que ton programme. Les solutions construisent les chemins avec `Path(__file__).parent`, expliqué en [8.5](../8.5%20-%20Sauvegarder%20et%20recharger%20une%20liste.md). Chaque saisie au clavier doit être validée, comme dans les séries précédentes.

## 🟢 Exercice 1 : Facile

**But** : Repérer les erreurs fréquentes lors de la lecture d'un fichier.

**Énoncé** : Le fichier `villes.txt` contient :

```text
Trois-Rivières
Shawinigan
Québec
```

Chacun des programmes suivants contient **une** erreur. Pour chacun, explique ce qui se passe à l'exécution, puis corrige-le.

```python
# Programme A
with open("villes.txt", "w", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())
```

```python
# Programme B
with open("villes.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne.strip())
```

```python
# Programme C
with open("villes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(f"[{ligne}]")
```

```python
# Programme D
with open("villes.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
for ligne in fichier:
    print(ligne.strip())
```

> 💡 Un des programmes cause une perte de données. Lequel? Un autre ne pose problème que sur certains ordinateurs. Lequel?

## 🟢 Exercice 2 : Facile

**But** : Lire un fichier ligne par ligne et numéroter les lignes.

**Énoncé** : Crée le fichier `citations.txt` :

```text
La simplicité est la sophistication suprême.
Le code est lu bien plus souvent qu'il n'est écrit.
Un bon programme est un programme qui fonctionne.

D'abord, résous le problème. Ensuite, écris le code.
```

Écris un programme qui affiche chaque citation, numérotée, puis le nombre total de citations. Les lignes vides ne sont **pas** des citations.

*Sortie attendue :*

```text
1. La simplicité est la sophistication suprême.
2. Le code est lu bien plus souvent qu'il n'est écrit.
3. Un bon programme est un programme qui fonctionne.
4. D'abord, résous le problème. Ensuite, écris le code.

4 citations.
```

## 🟡 Exercice 3 : Moyen

**But** : Lire des nombres dans un fichier et les traiter dans une liste.

**Énoncé** : Le fichier `temperatures.txt` contient les températures maximales (en °C) d'une semaine de novembre à Trois-Rivières :

```text
4.5
2.0
-1.5

6.0
3.5
-3.0
1.0
```

Écris :

- une fonction `lire_nombres(chemin)` qui **renvoie** la liste des nombres réels du fichier, en ignorant les lignes vides;
- une fonction `calculer_moyenne(nombres)` qui **renvoie** la moyenne d'une liste.

Le programme principal affiche le nombre de valeurs, le minimum, le maximum et la moyenne (1 décimale). Les fonctions `min()` et `max()` sont permises.

*Sortie attendue :*

```text
7 températures lues
Minimum : -3.0 °C
Maximum : 6.0 °C
Moyenne : 1.8 °C
```

## 🟡 Exercice 4 : Moyen

**But** : Charger un fichier dans une liste, puis y faire des recherches.

**Énoncé** : Crée le fichier `mots_interdits.txt` (un mot par ligne) :

```text
motdepasse
123456
qwerty
azerty
soleil
bonjour
```

Écris une fonction `charger_mots(chemin)` qui **renvoie** la liste des mots du fichier **en minuscules**. Si le fichier est introuvable, elle affiche un avertissement et renvoie une liste vide.

Le programme demande ensuite des mots de passe jusqu'à ce que l'utilisateur appuie sur Entrée sans rien écrire. Pour chacun, il indique s'il fait partie de la liste des mots de passe interdits, sans tenir compte des majuscules.

*Exemple d'exécution :*

```text
Mot de passe à vérifier (Entrée pour quitter) : Soleil
❌ Mot de passe interdit!
Mot de passe à vérifier (Entrée pour quitter) : Cegep2026!
✅ Ce mot de passe n'est pas dans la liste.
Mot de passe à vérifier (Entrée pour quitter) :
```

Teste aussi ton programme en renommant temporairement le fichier, pour vérifier qu'il ne plante pas.

## 🔴 Exercice 5 : Moyen-Difficile

**But** : Lire un fichier qui contient des données invalides, sans planter.

**Énoncé** : Le fichier `notes.txt` contient les notes d'un examen, une par ligne. Malheureusement, il a été rempli à la main et contient des erreurs :

```text
78
85.5
abc
92

105
61
-4
70
```

Écris une fonction `lire_notes(chemin)` qui **renvoie** la liste des notes valides (réels entre 0 et 100 inclusivement). Pour chaque ligne invalide (non numérique ou hors de l'intervalle), elle affiche un avertissement qui indique le **numéro de la ligne** dans le fichier. Les lignes vides sont ignorées silencieusement.

Le programme principal affiche ensuite le nombre de notes valides et la moyenne.

*Sortie attendue :*

```text
Ligne 3 ignorée : « abc » n'est pas un nombre.
Ligne 6 ignorée : 105.0 n'est pas entre 0 et 100.
Ligne 8 ignorée : -4.0 n'est pas entre 0 et 100.

5 notes valides, moyenne : 77.3
```

> 💡 Il faut compter les lignes toi-même avec un compteur, **y compris** les lignes vides.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.3 - Lire un fichier texte](Solutions%208.3%20-%20Lire%20un%20fichier%20texte.md).
