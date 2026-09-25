# Exercice — La distributrice à café

**Thèmes couverts :** variables et constantes, opérateurs `//` et `%` (Cours 02),
entrées/sorties et formatage (Cours 03), structures conditionnelles (Cours 04),
boucle `while`, gestion des erreurs et validation (Cours 05).

> ⚠️ À réaliser **sans liste, sans boucle `for` et sans fonction** :
> uniquement avec ce qui a été vu jusqu'au Cours 05.

---

## Mise en situation

La machine ne vend qu'un seul produit : **un café à 1 $, plus taxes**.

Le fichier `distributrice_depart.py` le fait déjà… une seule fois, et seulement si
l'utilisateur ne se trompe jamais. Essayez-le et trouvez ses défauts :

- tapez `abc` comme montant → le programme plante (`ValueError`) ;
- le stock et la caisse ne bougent qu'une fois : après un café, la machine reste
  figée à 4 gobelets et 11.15 $, pour toujours ;
- payez `0.50 $` un café à `1.15 $` → la distributrice vous rend `-0.65 $` de monnaie ;
- payez `1.13 $` → la machine accepte, alors qu'**aucune combinaison de pièces canadiennes
  ne donne 1.13 $** (la pièce de 1 cent n'existe plus depuis 2013!) ;
- et surtout : pour servir un deuxième café, il faut relancer le programme.

Votre mandat : en faire une vraie distributrice, qui tourne en boucle, qui n'accepte que
de vraies pièces, qui rend la monnaie en pièces, et dont les réserves et les revenus
**évoluent au fil des transactions**.

---

## Règle d'or : on travaille en CENTS

Les nombres réels sont imprécis en informatique. Essayez ceci dans la console :

```python
>>> 0.05 + 0.05 + 0.05
0.15000000000000002
```

Avec des `float`, une machine qui compare `montant >= prix` peut donc se tromper.
**Solution : tous les montants du programme sont des entiers, en cents**, et on divise
par 100 **uniquement au moment de l'affichage** :

```python
PRIX_AVANT_TAXES = 100                       # 1.00 $
print(f"{PRIX_AVANT_TAXES / 100:.2f} $")     # affiche 1.00 $
```

---

## Partie 1 — Les constantes et les variables d'état

Recopiez d'abord ce bloc de constantes. Le prix du café, taxes comprises, vaut
`114.975` cents… un montant que personne ne peut payer avec de vraies pièces! On
**arrondit donc au 5 cents le plus près**, comme les commerçants canadiens doivent le
faire depuis le retrait de la pièce de 1 cent :

```python
PRIX_AVANT_TAXES = 100  # en cents
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

PRIX_EXACT = PRIX_AVANT_TAXES * (1 + TAUX_TPS + TAUX_TVQ)
PRIX_CAFE = round(PRIX_EXACT / 5) * 5  # 115 cents, soit 1.15 $

PIECE_TOONIE = 200   # 2.00 $
PIECE_LOONIE = 100   # 1.00 $
PIECE_QUART = 25     # 0.25 $
PIECE_DIX = 10       # 0.10 $
PIECE_CINQ = 5       # 0.05 $

GOBELETS_DEPART = 5
CAISSE_DEPART = 1000   # fonds de caisse du matin : 10.00 $
```

> 💡 **Comprenez l'arrondi** : on divise par 5 (`22.995`), on arrondit à l'entier (`23`),
> puis on remultiplie par 5 (`115`). Même truc que pour arrondir à la dizaine, mais avec 5.

Initialisez ensuite les **variables d'état**. Ce sont elles qui évoluent d'une
transaction à l'autre. Le programme de départ les déclare déjà et les met à jour
**une seule fois** : observez bien le patron, votre travail consiste à le répéter
en boucle.

| Variable | Valeur de départ | Rôle |
| --- | --- | --- |
| `gobelets` | `GOBELETS_DEPART` | diminue de 1 à chaque café servi |
| `caisse` | `CAISSE_DEPART` | augmente du prix de chaque café vendu (en cents) |
| `nb_cafes` | `0` | compteur de cafés vendus |
| `monnaie_totale` | `0` | total de la monnaie rendue (en cents) |

> 💡 **Pourquoi un fonds de caisse ?** Une machine vide ne pourrait rendre aucune
> monnaie au premier client! Le 10 $ du matin sert exactement à ça. Attention :
> cet argent n'est **pas** une vente, il faudra en tenir compte au rapport.

---

## Partie 2 — Le menu et la boucle principale

Affichez ce menu, en boucle, tant que l'utilisateur ne choisit pas `0` :

```text
============== DISTRIBUTRICE ===========
1 - Acheter un café ..... 1.15 $
2 - Rapport des ventes
0 - Quitter
========================================
```

**Validation du choix :** ce doit être un **entier** faisant partie de `(0, 1, 2)`.
Utilisez le patron `valide`/`while not valide` avec `try`/`except ValueError` du Cours 05.
Un `abc`, un `2.5` ou un `9` doivent produire un message d'erreur clair et **redemander**
le choix, sans jamais faire planter le programme.

---

## Partie 3 — Acheter un café (choix 1)

1. **Vérifier le stock** : s'il ne reste plus de gobelet (`gobelets == 0`), affichez
   `Désolé, la distributrice n'a plus de gobelets.` et retournez au menu.

2. **Encaisser les pièces une à la fois.** Tant que le montant inséré n'atteint pas le prix
   (`while insere < PRIX_CAFE:`), rappelez au client combien il manque, puis demandez une pièce :

   ```text
   Il manque 1.15 $.
     1 = 2.00 $   2 = 1.00 $   3 = 0.25 $   4 = 0.10 $   5 = 0.05 $
   Insérez une pièce :
   ```

   - La saisie doit être un **entier** appartenant à `(1, 2, 3, 4, 5)` → `try`/`except` + validation par ensemble. Tout le reste (une pièce de 1 cent, un billet, `abc`) est **refusé** et redemandé.
   - Convertissez le numéro de la pièce en valeur avec un `if`/`elif`/`else`, puis ajoutez-la au montant inséré.

3. **Mettre à jour l'état** : calculez `a_rendre = insere - PRIX_CAFE`, ajoutez le prix à `caisse`, la monnaie à `monnaie_totale`, incrémentez `nb_cafes` et enlevez un gobelet.

---

## Partie 4 — Rendre la monnaie avec `//` et `%`

C'est le cœur de l'exercice. Il faut rendre le montant `a_rendre` avec **le moins de pièces
possible**, en partant de la plus grosse. Le truc : la **division entière** `//` donne le
nombre de pièces, et le **modulo** `%` donne ce qu'il reste à rendre.

```python
reste = a_rendre
nb_toonies = reste // PIECE_TOONIE   # combien de pièces de 2.00 $
reste = reste % PIECE_TOONIE         # ce qu'il reste à rendre après les 2.00 $
nb_loonies = reste // PIECE_LOONIE
reste = reste % PIECE_LOONIE
# ... et ainsi de suite jusqu'à la pièce de 5 cents
```

Répétez le patron pour le 25 ¢, le 10 ¢ et le 5 ¢, puis affichez le résultat :

```text
Monnaie rendue : 0.85 $
  0 x 2.00 $   0 x 1.00 $   3 x 0.25 $   1 x 0.10 $   0 x 0.05 $
```

Si `a_rendre` vaut `0`, affichez plutôt `Aucune monnaie à rendre. Merci d'avoir fait l'appoint!`

> 💡 **Pourquoi ça tombe toujours juste ?** Le prix (115) et toutes les pièces sont des
> multiples de 5. Le montant à rendre est donc lui aussi un multiple de 5, et le dernier
> `reste` vaut forcément `0` : **aucune pièce de 1 cent n'est jamais nécessaire.**
> Vérifiez-le : après la dernière ligne, `reste % PIECE_CINQ` doit valoir `0`.
> C'est exactement pour cette raison qu'il fallait arrondir le prix à la Partie 1.

---

## Exemple d'exécution (option 1)

```text
Votre choix : abc
Erreur - Votre choix doit être un nombre entier!
Votre choix : 9
Erreur - Votre choix doit être entre 0 et 2!
Votre choix : 1

Un café coûte 1.15 $, taxes incluses.
Il manque 1.15 $.
  1 = 2.00 $   2 = 1.00 $   3 = 0.25 $   4 = 0.10 $   5 = 0.05 $
Insérez une pièce : 7
Erreur - Cette pièce n'est pas acceptée par la machine!
Insérez une pièce : 2
  (pièce de 1.00 $ acceptée, total inséré : 1.00 $)
Il manque 0.15 $.
  1 = 2.00 $   2 = 1.00 $   3 = 0.25 $   4 = 0.10 $   5 = 0.05 $
Insérez une pièce : 3
  (pièce de 0.25 $ acceptée, total inséré : 1.25 $)

Voici votre café. Il reste 4 gobelet(s).
Monnaie rendue : 0.10 $
  0 x 2.00 $   0 x 1.00 $   0 x 0.25 $   1 x 0.10 $   0 x 0.05 $
```

## Partie 5 — Le rapport des ventes (choix 2) et la sortie (choix 0)

Affichez un rapport aligné (largeur 50, avec les alignements `<` et `>` des f-strings) :

- le nombre de cafés vendus ;
- les **ventes avant taxes** : `nb_cafes * PRIX_AVANT_TAXES` ;
- les **ventes taxes incluses** : `nb_cafes * PRIX_CAFE` ;
- les **taxes perçues** : la différence entre les deux
  *(l'arrondi au 5 cents est ainsi inclus dans les taxes)* ;
- le **fonds de caisse du matin** et l'**argent en caisse maintenant** ;
- la monnaie totale rendue aux clients ;
- les gobelets restants.

> ⚠️ **Piège à éviter** : ne calculez pas les taxes à partir de `caisse`! La caisse
> contient aussi le fonds de départ, qui n'a jamais été taxé. Partez toujours de
> `nb_cafes`.

Le choix `0` affiche ce même rapport une dernière fois, puis un message d'au revoir.

> 💡 Pour éviter d'écrire le rapport en double, placez-le dans un seul bloc
> `if choix == 2 or choix == 0:` à la fin de la boucle.

**Exemple de rapport** après deux cafés (le premier payé avec 1.25 $, le second avec
une pièce de 2.00 $) :

```text
Votre choix : 2

*************** RAPPORT DES VENTES ***************
Cafés vendus                    :        2
Ventes avant taxes              :     2.00 $
Taxes perçues                   :     0.30 $
Ventes taxes incluses           :     2.30 $
--------------------------------------------------
Fonds de caisse du matin        :    10.00 $
Argent en caisse maintenant     :    12.30 $
Monnaie rendue aux clients      :     0.95 $
Gobelets restants               :        3 sur 5
**************************************************
```

> 💡 Vérifiez vos chiffres : `10.00 $ + 2.30 $ = 12.30 $` en caisse, et
> `0.10 $ + 0.85 $ = 0.95 $` de monnaie rendue.

Avec le choix `0`, le même rapport s'affiche, suivi de :

```text
Merci d'avoir utilisé la distributrice. Bonne journée!
```

---

## Défis supplémentaires (optionnels)

1. **N'affichez que les pièces utiles** : cachez les `0 x ...` en construisant la ligne
   petit à petit avec des `if` et l'opérateur `+` sur les chaînes.
2. **Annuler** : ajoutez le choix `0` pendant le paiement pour rembourser le client.
   Il vous faudra un booléen `annule` dans la condition : `while insere < PRIX_CAFE and not annule:`.
3. **Recharger la machine** : ajoutez un choix au menu pour remettre des gobelets,
   en validant que l'on ne dépasse pas la capacité.
4. **Le 5e café gratuit** : utilisez `%` sur `nb_cafes`.
