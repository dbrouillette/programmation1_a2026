# Exercices — Les conditions enchaînées (fiche 4.2)

## 🟢 Exercice 1 : Facile

**But** : Enchaîner trois cas avec `elif`.

**Énoncé** : Écris un programme qui demande un nombre à l'utilisateur et affiche :

- *"Négatif"* si le nombre est inférieur à 0,
- *"Nul"* si le nombre est égal à 0,
- *"Positif"* si le nombre est supérieur à 0.

## 🟢 Exercice 2 : Facile-Moyen

**But** : Catégoriser une valeur selon des paliers.

**Énoncé** : Écris un programme qui demande l'âge de l'utilisateur et affiche sa catégorie :

- Enfant : moins de 13 ans
- Adolescent : 13 à 17 ans
- Adulte : 18 à 64 ans
- Senior : 65 ans et plus

| Entrée | Sortie |
| :---: | --- |
| `10` | Enfant |
| `15` | Adolescent |
| `40` | Adulte |
| `70` | Senior |

## 🟡 Exercice 3 : Moyen

**But** : Ordonner correctement une chaîne de conditions qui se chevauchent.

**Énoncé** : Écris un programme qui demande une note sur 100 et affiche la mention correspondante :

- 90 et plus : *"Excellent"*
- 75 à 89 : *"Très bien"*
- 60 à 74 : *"Bien"*
- 50 à 59 : *"Passable"*
- Moins de 50 : *"Échec"*
- En dehors de 0 à 100 : *"Note invalide"*

⚠️ Attention à l'ordre de tes conditions (voir fiche 4.2, section 3).

## 🟡 Exercice 4 : Moyen

**But** : Associer un numéro à un nom, avec gestion d'un cas invalide.

**Énoncé** :
Écris un programme qui demande un numéro de jour (1 à 7) et affiche le nom du jour correspondant (1 = Lundi, ..., 7 = Dimanche). Si le numéro n'est pas entre 1 et 7, affiche *"Numéro de jour invalide"*.

## 🔴 Exercice 5 : Difficile

**But** : Classer une valeur calculée selon plusieurs paliers, avec un piège d'ordre similaire à l'exercice 3.

**Énoncé** : L'indice de masse corporelle (IMC) se calcule ainsi : `imc = poids / (taille ** 2)` (poids en kg, taille en mètres). Écris un programme qui demande le poids et la taille, calcule l'IMC, puis affiche :

- *"Insuffisance pondérale"* si `imc < 18.5`
- *"Poids normal"* si `18.5 <= imc < 25`
- *"Surpoids"* si `25 <= imc < 30`
- *"Obésité"* si `imc >= 30`

| Poids | Taille | Sortie |
| :---: | :---: | --- |
| `50` | `1.70` | Insuffisance pondérale |
| `65` | `1.70` | Poids normal |
| `80` | `1.70` | Surpoids |
| `95` | `1.70` | Obésité |

## 🟢 Exercice 6 : Facile

**But** : Réécrire une chaîne `elif` en `match`/`case`.

**Énoncé** : Reprends l'exercice 4 (numéro de jour), mais cette fois à l'aide d'un `match`/`case` plutôt que d'une chaîne `elif`. Si le numéro n'est pas entre 1 et 7, affiche *"Numéro de jour invalide"* avec le cas `_`.

## 🟡 Exercice 7 : Moyen

**But** : Regrouper plusieurs valeurs dans un même `case` avec `|`.

**Énoncé** : Écris un programme qui demande un numéro de mois (1 à 12) et affiche la saison correspondante à l'aide d'un `match`/`case`, en regroupant les mois de chaque saison avec `|` :

- Hiver : décembre, janvier, février
- Printemps : mars, avril, mai
- Été : juin, juillet, août
- Automne : septembre, octobre, novembre

| Entrée | Sortie |
| :---: | --- |
| `1` | Hiver |
| `4` | Printemps |
| `7` | Été |
| `10` | Automne |
| `13` | Mois invalide |
