# 🐱 Corrigé : La Chatterie du Ronron Doré

> Corrigé de [exercices_chats_opérateurs.md](../exercices_chats_opérateurs.md)

---

## Partie 1 — Le partage des croquettes 🍽️

Avec `chats = 17` et `croquettes = 100` :

| # | Expression | Résultat | Type | Explication |
| :---: | --- | --- | :---: | --- |
| 1 | `croquettes / chats` | `5.882352941176471` | `float` | La division `/` retourne **toujours** un `float`, même entre deux `int`. |
| 2 | `croquettes // chats` | `5` | `int` | Division entière : 17 × 5 = 85 ≤ 100, la partie décimale est tronquée. |
| 3 | `croquettes % chats` | `15` | `int` | Reste : 100 − 85 = 15 croquettes en trop. |
| 4 | `chats ** 2` | `289` | `int` | 17² = 289. |
| 5 | `chats % 2` | `1` | `int` | Reste de 1 → **17 est impair**. |

> 💡 Les questions 2 et 3 vont toujours ensemble : `//` donne « combien chacun en reçoit », `%` donne « combien il en reste ».

---

## Partie 2 — La journée de Mme Moustache 🧶

| Ligne | Instruction | Équivalence | Résultat |
| :---: | --- | --- | --- |
| 1 | `croquettes -= 40` | `croquettes = 240 - 40` | `croquettes = 200` |
| 2 | `croquettes //= chats` | `croquettes = 200 // 6` | `croquettes = 33` (et non 33.33!) |
| 3 | `chats += 2` | `chats = 6 + 2` | `chats = 8` |
| 4 | `croquettes *= chats` | `croquettes = 33 * 8` | `croquettes = 264` |
| 5 | `croquettes %= 10` | `croquettes = 264 % 10` | `croquettes = 4` |
| 6 | `croquettes /= 2` | `croquettes = 4 / 2` | `croquettes = 2.0` |

**6.** `croquettes` vaut **`2.0`**, de type **`float`**. ⚠️ C'est le piège de la fiche 2.5 : `/=` fait une division **réelle**, donc le résultat devient un `float` même si la division « tombe juste ».

**7.** Il fallait écrire `croquettes //= 2`, qui donne `2` (un `int`).

---

## Partie 3 — Priorité aux chats (et aux opérateurs) 🥇

Avec `siestes = 12`, `souris = 5`, `boules_de_poils = 3` :

1. `siestes + souris * boules_de_poils` → `12 + (5 * 3)` = `12 + 15` = **`27`**
   *(le `*` est prioritaire sur le `+`)*
2. `(siestes + souris) * boules_de_poils` → `(12 + 5) * 3` = `17 * 3` = **`51`**
   *(les parenthèses passent avant tout)*
3. `siestes // souris ** 2` → `12 // (5 ** 2)` = `12 // 25` = **`0`**
   *(la puissance `**` est prioritaire sur `//`)*
4. `siestes % souris * boules_de_poils` → `(12 % 5) * 3` = `2 * 3` = **`6`**
   *(`%` et `*` ont la **même** priorité → évaluation de gauche à droite)*
5. `-siestes // souris` → `-12 // 5` = **`-3`** ⚠️
   *(la division entière tronque vers le **bas** (−∞) : −2.4 devient −3, et non −2!)*

---

## Partie 4 — La roue des corvées 🔁

| Jour | Calcul | Reste | Responsable |
| :---: | --- | :---: | --- |
| 7 | `7 % 3` (6 + 1) | `1` | **Bob** |
| 11 | `11 % 3` (9 + 2) | `2` | **Chloé** |
| 30 | `30 % 3` (30 + 0) | `0` | **Alice** |
| 365 | `365 % 3` (363 + 2) | `2` | **Chloé** |

> 💡 C'est exactement la même astuce que dans le Roche-Papier-Ciseaux de la fiche 2.4 : le modulo sert à « faire tourner » un compteur en boucle.

---

## Partie 5 — 🏆 Défi : le distributeur automatique

```python
GRAMMES_PAR_CHAT = 45   # ration quotidienne d'un chat
nb_chats = 7
sac_grammes = 2000

ration_quotidienne = GRAMMES_PAR_CHAT * nb_chats   # 315
jours_complets = sac_grammes // ration_quotidienne  # 6
restant = sac_grammes % ration_quotidienne          # 110
chats_avec_reste = restant // GRAMMES_PAR_CHAT      # 2

print(f"Ration quotidienne de la chatterie : {ration_quotidienne} g")
print(f"Jours complets : {jours_complets}")
print(f"Restant dans le sac : {restant} g")
print(f"Chats nourris avec le reste : {chats_avec_reste}")
```

**Sortie :**

```text
Ration quotidienne de la chatterie : 315 g
Jours complets : 6
Restant dans le sac : 110 g
Chats nourris avec le reste : 2
```

**Détail des calculs :**

- `45 * 7 = 315` g par jour;
- `2000 // 315 = 6` jours complets (6 × 315 = 1890 g);
- `2000 % 315 = 110` g restants;
- `110 // 45 = 2` chats (il resterait encore 20 g, insuffisants pour un 3ᵉ chat).

> ⚠️ Utiliser `/` au lieu de `//` donnerait `6.349...` jours, ce qui n'a aucun sens ici : on ne peut pas nourrir un chat pendant 0.349 jour!

---

## Partie 6 — Vrai ou faux? 🤔

| # | Affirmation | Réponse | Explication |
| :---: | --- | :---: | --- |
| 1 | `10 / 2` donne `5` (un `int`) | ❌ **Faux** | `/` retourne toujours un `float` : le résultat est `5.0`. |
| 2 | `chats++` ajoute 1 | ❌ **Faux** | Python n'a **pas** de `++` ni de `--` → `SyntaxError`. Il faut écrire `chats += 1`. |
| 3 | `croquettes //= 3` peut donner un `float` | ❌ **Faux** | `//` entre deux `int` donne un `int`. *(Ce serait vrai si un des deux opérandes était un `float` : `7.0 // 3` → `2.0`.)* |
| 4 | `7 % 2` vaut `1`, donc `7` est impair | ✅ **Vrai** | Le test de parité classique : reste de `0` = pair, reste de `1` = impair. |
| 5 | `2 ** 3 ** 2` vaut `64` | ❌ **Faux** | `**` s'évalue **de droite à gauche** : `2 ** (3 ** 2)` = `2 ** 9` = **`512`**. |

---

## 🎯 À retenir

- `/` → toujours un `float`; `//` → division entière tronquée vers le bas; `%` → le reste.
- `//` et `%` sont les deux moitiés d'un même partage : « chacun sa part » + « ce qui reste ».
- `%` sert aussi à tester la **parité** et à créer des **cycles** (roue des corvées, RPC).
- `x /= 2` change le type de `x` en `float`; `x //= 2` le garde en `int`.
- Pas de `++` ni `--` en Python : `x += 1` et `x -= 1`.
