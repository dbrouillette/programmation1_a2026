# Exercices Python - Cours 03

Les exercices sont regroupés selon les fiches du cours et se font dans l'ordre. Il est recommandé de séparer chaque exercice dans des fichiers différents.

**Légende des niveaux de difficulté :** 🟢 Facile · 🟡 Moyen · 🔴 Avancé · 🟣 Synthèse

| Fiche | Sujet | Exercices | 🟢 | 🟡 | 🔴 |
| --- | --- | :---: | :---: | :---: | :---: |
| 3.1 | Entrées en console | 1 à 6 | 3 | 2 | 1 |
| 3.2 | Sorties en console | 7 à 12 | 4 | 1 | 1 |
| 3.3 | Sorties en console - formatage avancé | 13 à 18 | 2 | 3 | 1 |
| 3.4 | Opérateurs relationnels et logiques | 19 à 26 | 4 | 2 | 2 |
| — | **Exercice synthèse** 🟣 | 27 | | | |

---

## 3.1 - Entrées en console

### Exercice 1 — 🟢 Facile

Demande à l'utilisateur son prénom et affiche : `Bonjour <prénom> !`.

Résultat:  
![Exercice 1](../../images/cours03/exercice-01.png)

### Exercice 2 — 🟢 Facile

Demande à l'utilisateur deux nombres et affiche leur somme.

Résultat:  
![Exercice 2](../../images/cours03/exercice-02.png)

### Exercice 3 — 🟢 Facile

Demande l'âge de l'utilisateur et affiche `Tu as X ans. Tu es né(e) en AAAA`.

*Remarque* : il est possible que l'année de naissance réelle diffère de 1 par rapport à votre affichage, si l'anniversaire de l'utilisateur n'est pas encore atteint dans l'année courante.

Résultat:  
![Exercice 3](../../images/cours03/exercice-03.png)

### Exercice 4 — 🟡 Moyen

Demande un prix unitaire (nombre décimal) et une quantité (nombre entier), puis affiche le total à payer.

Résultat:  
![Exercice 4](../../images/cours03/exercice-04.png)

### Exercice 5 — 🟡 Moyen

Demande trois notes et affiche leur moyenne.

Résultat:  
![Exercice 5](../../images/cours03/exercice-05.png)

### Exercice 6 — 🔴 Avancé

Demande une température en degrés Celsius et affiche sa conversion en degrés Fahrenheit.  
*Indice : la formule de conversion est `F = C × 9/5 + 32`.*

Exemples de valeurs

|Celsius|Fahrenheit|
|:---|---:|
|`20`|`68.0`|
|`30.5`|`86.9`|
|`-40`|`-40.0`|

Résultat:  
![Exercice 6](../../images/cours03/exercice-06.png)

> *REMARQUE* : Pour taper le caractère `°`, maintenir la touche `ALT` (à gauche de la barre d'espacement) enfoncée, faire la combinaison `0176` sur le clavier numérique, puis relâcher `ALT`. Vous pouvez vous amuser à essayer d'autres combinaisons à 4 chiffres...

---

## 3.2 - Sorties en console

### Exercice 7 — 🟢 Facile

Écris un programme qui affiche ton prénom et ton nom sur deux lignes **en un seul appel à `print()`** (indice : le caractère `\n` permet d'afficher un retour de ligne). **BONUS** : trouve une deuxième façon équivalente de le faire.

Résultat:  
![Exercice 7](../../images/cours03/exercice-07.png)

### Exercice 8 — 🟢 Facile

Affiche la phrase : `Bonjour, je m'appelle Alice et j'ai 20 ans.` à l'aide d'une f-string.

Résultat:  
![Exercice 8](../../images/cours03/exercice-08.png)

### Exercice 9 — 🟢 Facile

Affiche un carré formé d'étoiles `*` (4x4).

Résultat:  
![Exercice 9](../../images/cours03/exercice-09.png)

### Exercice 10 — 🟢 Facile

Affiche les nombres de 1 à 5, chacun sur une ligne.

Résultat:  
![Exercice 10](../../images/cours03/exercice-10.png)

### Exercice 11 — 🟡 Moyen

Affiche un triangle d'étoiles croissant, de 1 à 5 étoiles (une ligne par `print()`).

Résultat:  
![Exercice 11](../../images/cours03/exercice-11.png)

### Exercice 12 — 🔴 Avancé

Affiche les 5 premières lignes de la table de multiplication de 5, **en un seul appel à `print()`** (indice : construis une seule chaîne de caractères contenant des `\n`).

Résultat:  
![Exercice 12](../../images/cours03/exercice-12.png)

---

## 3.3 - Sorties en console - formatage avancé

### Exercice 13 — 🟢 Facile

Affiche le nombre `42` aligné à droite dans un champ de 6 caractères, encadré par des barres `|`.

Résultat:  
![Exercice 13](../../images/cours03/exercice-13.png)

### Exercice 14 — 🟢 Facile

Affiche le mot `Python` aligné à gauche dans un champ de 12 caractères, entre crochets `[ ]`.

Résultat:  
![Exercice 14](../../images/cours03/exercice-14.png)

### Exercice 15 — 🟡 Moyen

Affiche le message `Bienvenue dans le cours de Python !` centré dans un tableau d'étoiles de 10 lignes.  
Utilise le spécificateur de centrage `^` d'une f-string pour positionner le message.

Résultat:  
![Exercice 15](../../images/cours03/exercice-15.png)

### Exercice 16 — 🟡 Moyen

Affiche un prix de `19.9` formaté avec exactement 2 décimales, précédé du symbole `$`.

Résultat:  
![Exercice 16](../../images/cours03/exercice-16.png)

### Exercice 17 — 🟡 Moyen

Affiche l'identifiant `42` sur 5 chiffres, complété par des zéros devant (`00042`).

Résultat:  
![Exercice 17](../../images/cours03/exercice-17.png)

### Exercice 18 — 🔴 Avancé

Affiche un petit reçu pour 3 produits (Pomme à 1,25 $, Banane à 0,75 $, Orange à 2,50 $), avec les noms alignés à gauche et les prix alignés à droite avec 2 décimales.

Résultat:  
![Exercice 18](../../images/cours03/exercice-18.png)

---

## 3.4 - Opérateurs relationnels et logiques

### Exercice 19 — 🟢 Facile

Demande deux nombres et affiche `True` ou `False` si (a > b) et (b > a).

Résultat:  
![Exercice 19](../../images/cours03/exercice-19.png)

### Exercice 20 — 🟢 Facile

Demande un nombre et affiche `True` ou `False` si le nombre est positif.

Résultat:  
![Exercice 20](../../images/cours03/exercice-20.png)

### Exercice 21 — 🟢 Facile

Demande un nombre et affiche `True` ou `False` si un nombre est pair ou impair.

Résultat:  
![Exercice 21](../../images/cours03/exercice-21.png)

### Exercice 22 — 🟢 Facile

Demande l'âge et affiche `True` ou `False` si la personne est majeure (>=18).

Résultat:  
![Exercice 22](../../images/cours03/exercice-22.png)

### Exercice 23 — 🟡 Moyen

Demande un nombre et affiche `True` ou `False` s'il est compris entre 10 et 20.

Résultat:  
![Exercice 23](../../images/cours03/exercice-23.png)

### Exercice 24 — 🔴 Avancé [Niveau expert]

Demande un caractère et vérifie s'il s'agit d'une voyelle (a, e, i, o, u).

Résultat:  
![Exercice 24](../../images/cours03/exercice-24.png)

### Exercice 25 — 🟡 Moyen

Demande un nombre et vérifie s'il est multiple de 3 ou de 5.

Résultat:  
![Exercice 25](../../images/cours03/exercice-25.png)

### Exercice 26 — 🔴 Avancé

Vérifie si une année entrée est bissextile.

Résultat:  
![Exercice 26](../../images/cours03/exercice-26.png)

---

## Exercice synthèse — 🟣 Générateur de carte de personnage RPG

### Exercice 27

Tu développes un petit outil pour un jeu de rôle : un générateur de **carte de personnage**. Ce programme doit combiner tout ce qui a été vu dans le Cours 03 — entrées, sorties, formatage et opérateurs logiques.

Le programme doit :

1. Demander à l'utilisateur, via `input()` :
   - le nom du personnage ;
   - sa classe (`Guerrier`, `Mage` ou `Voleur`) ;
   - son niveau ;
   - ses points de vie (PV) ;
   - ses points de mana (PM).
2. Calculer, à l'aide d'opérateurs relationnels et logiques :
   - s'il est **en vie** (`PV > 0`) ;
   - s'il **peut lancer un sort** (c'est un `Mage` **et** il a au moins 10 PM) ;
   - s'il est considéré comme **puissant** (niveau ≥ 10 **ou** PV ≥ 100).
3. Afficher une carte de personnage bien mise en forme à l'aide de f-strings : bordures faites d'étoiles ou de `=`, titre centré, et informations alignées à gauche/à droite dans des champs de largeur fixe — comme une vraie carte de jeu.

Résultat:  
![Exercice 27](../../images/cours03/exercice-27.png)
