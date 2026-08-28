# RÉPONSES - Exercices supplémentaires : Expressions Arithmétiques en Python (2)

|Exercice|Variable à évaluer|Résultat|
|---|---|:---:|
|1|`resultat`|`20`|
|2|`x`|`12`|
|3|`resultat`|`5`|
|4|`y`|`36`|
|5|`resultat`|`2.75`|
|6|`p`|`24`|
|7|`resultat`|`16`|
|8|`r`|`6`|
|9|`resultat`|`0`|
|10|`resultat`|`31.0`|

## Détail des calculs

**Exercice 1** : `b * 2` = `10`, `c // 2` = `2` → `12 + 10 - 2` = `20`

**Exercice 2** : `(4 + 2) * 3` = `18` → `30 - 18` = `12`

**Exercice 3** : `17 // 4` = `4`, `17 % 4` = `1` → `4 + 1` = `5`

**Exercice 4** : `y - (2 + 3)` utilise la valeur de `y` **avant** l'affectation, donc `9 - 5` = `4` → `y *= 4` → `9 * 4` = `36`

**Exercice 5** : `15 / 4` = `3.75` (division réelle, donne un `float`) → `3.75 - 1` = `2.75`

**Exercice 6** : `p += q * 2` → `6 + 6` = `12` ; puis `p *= q - 1` → `12 * 2` = `24`

**Exercice 7** : `23 // 5` = `4`, `23 % 5` = `3` → `(4 + 3) * 3 - 5` = `21 - 5` = `16`

**Exercice 8** : `(s + t) * 2 - s` = `(7 + 3) * 2 - 7` = `13` → `58 % 13` = `6`

**Exercice 9** : `-17 // 5` = `-4` (arrondi vers le bas, pas vers zéro) ; `-17 % 5` = `3` → `-4 + (3 * 2) - (5 - 3)` = `-4 + 6 - 2` = `0`

**Exercice 10** : `k -= l * 2` → `40 - 12` = `28` ; `k /= 4` → `7.0` ; `k *= (l - 2)` → `7.0 * 4` = `28.0` ; puis `resultat = 28.0 + (6 // 2) - (6 % 2)` = `28.0 + 3 - 0` = `31.0`

## 💡 Points à retenir

- **Exercice 1 et 7** : la précédence habituelle s'applique — `*`, `/`, `//`, `%` avant `+` et `-` — même combinés à trois ou quatre variables.
- **Exercice 4** : dans une affectation augmentée comme `y *= y - (2 + 3)`, le membre de droite est évalué **au complet avec l'ancienne valeur de `y`** avant que le résultat ne soit réaffecté à `y`. C'est le même principe qu'une ligne `y = y * (y - (2 + 3))`.
- **Exercice 5 et 10** : `/` retourne toujours un `float`, même quand le résultat semble "rond" (`7.0`, pas `7`). Une fois qu'une variable devient un `float`, elle le reste pour les opérations suivantes.
- **Exercice 9** : `//` et `%` avec des nombres négatifs arrondissent **vers le bas** (vers `-∞`), pas vers zéro : `-17 // 5` vaut `-4` et non `-3`. C'est cohérent avec l'identité `(a // b) * b + (a % b) == a`.
- **Exercice 6 et 10** : quand plusieurs instructions modifient la même variable en séquence, chaque ligne part du résultat de la précédente — il faut recalculer étape par étape, pas relire l'expression finale seule.
