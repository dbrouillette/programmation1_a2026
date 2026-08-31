# 🐱 Exercices ludiques : La Chatterie du Ronron Doré

> **Fiches associées** : [2.4 - Opérateurs arithmétiques](../2.4%20-%20Opérateurs%20arithmétiques.md) et [2.5 - Opérateurs d'assignation](../2.5%20-%20Opérateurs%20d'assignation.md)

Bienvenue à la **Chatterie du Ronron Doré**! Vous êtes le nouvel employé chargé de gérer les croquettes, les siestes et les boules de poils. Malheureusement, tout se calcule en Python...

**Consigne générale** : répondez **sans exécuter le code**. Écrivez vos calculs à la main, puis vérifiez ensuite dans Python.

---

## Partie 1 — Le partage des croquettes 🍽️

```python
chats = 17
croquettes = 100
```

Donnez la valeur **et le type** (`int` ou `float`) de chaque expression :

1. `croquettes / chats`
2. `croquettes // chats`
3. `croquettes % chats`
4. `chats ** 2`
5. `chats % 2`

> 💡 La question 5 répond à : « le nombre de chats est-il pair ou impair? »

---

## Partie 2 — La journée de Mme Moustache 🧶

**ATTENTION** : les lignes sont **cumulatives**, faites-les **dans l'ordre**! Donnez la valeur des variables après chaque ligne.

```python
croquettes = 240
chats = 6

croquettes -= 40      # 1. les souris ont pillé le sac pendant la nuit
croquettes //= chats  # 2. on partage également entre les chats
chats += 2            # 3. deux chatons errants s'invitent
croquettes *= chats   # 4. le patron rachète le même montant pour chaque chat
croquettes %= 10      # 5. on garde seulement les croquettes en trop du dernier paquet de 10
croquettes /= 2       # 6. on en donne la moitié au chat du voisin
```

6. Après la ligne 6, quelle est la valeur **et le type** de `croquettes`? ⚠️ Attention, il y a un piège!
7. Quelle ligne aurait-il fallu écrire à la place de la ligne 6 pour garder un `int`?

---

## Partie 3 — Priorité aux chats (et aux opérateurs) 🥇

```python
siestes = 12
souris = 5
boules_de_poils = 3
```

Évaluez chaque expression en respectant la **priorité des opérations** (les variables ne changent jamais de valeur ici) :

1. `siestes + souris * boules_de_poils`
2. `(siestes + souris) * boules_de_poils`
3. `siestes // souris ** 2`
4. `siestes % souris * boules_de_poils`
5. `-siestes // souris` ⚠️ (piège!)

---

## Partie 4 — La roue des corvées 🔁

Trois colocataires se relaient pour nourrir le chat, un jour chacun :

| Reste de `jour % 3` | Responsable |
|:---:|---|
| `0` | Alice |
| `1` | Bob |
| `2` | Chloé |

Qui nourrit le chat...

1. le jour `7`?
2. le jour `11`?
3. le jour `30`?
4. le jour `365`?

---

## Partie 5 — 🏆 Défi : le distributeur automatique

Écrivez un petit programme qui, à partir de ces valeurs, affiche les 4 informations demandées :

```python
GRAMMES_PAR_CHAT = 45   # ration quotidienne d'un chat
nb_chats = 7
sac_grammes = 2000
```

Le programme doit afficher (avec des f-strings) :

1. la quantité de croquettes nécessaire **par jour** pour toute la chatterie;
2. le nombre de **jours complets** que le sac permet de nourrir tout le monde;
3. le nombre de **grammes restants** dans le sac le dernier jour;
4. le nombre de **chats** qui pourront quand même manger leur ration complète avec ce reste.

*Exemple de sortie attendue :*

```
Ration quotidienne de la chatterie : ... g
Jours complets : ...
Restant dans le sac : ... g
Chats nourris avec le reste : ...
```

---

## Partie 6 — Vrai ou faux? 🤔

1. `10 / 2` donne `5` (un `int`).
2. `chats++` ajoute 1 au nombre de chats.
3. `croquettes //= 3` peut transformer un `int` en `float`.
4. `7 % 2` vaut `1`, donc `7` est impair.
5. `2 ** 3 ** 2` vaut `64`.
