# Exercices — La portée des variables (fiche 7.5)

## 🟢 Exercice 1 : Facile

**But** : Distinguer une variable locale d'une variable globale qui porte le même nom.

**Énoncé** : Dans un jeu-questionnaire, chaque bonne réponse donne des points, plus un bonus. Sans exécuter de code, écris exactement ce qu'affiche le programme suivant. Réponds ensuite aux questions.

```python
points = 0


def ajouter_bonus(points_question):
    points = points_question + 5
    print(f"Points avec bonus : {points}")


ajouter_bonus(10)
print(f"Total du joueur : {points}")
points = 20
ajouter_bonus(points)
print(f"Total du joueur : {points}")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=points%20%3D%200%0A%0A%0Adef%20ajouter_bonus%28points_question%29%3A%0A%20%20%20%20points%20%3D%20points_question%20%2B%205%0A%20%20%20%20print%28f%22Points%20avec%20bonus%20%3A%20%7Bpoints%7D%22%29%0A%0A%0Aajouter_bonus%2810%29%0Aprint%28f%22Total%20du%20joueur%20%3A%20%7Bpoints%7D%22%29%0Apoints%20%3D%2020%0Aajouter_bonus%28points%29%0Aprint%28f%22Total%20du%20joueur%20%3A%20%7Bpoints%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

a. Pourquoi le total du joueur n'augmente-t-il jamais après l'appel de `ajouter_bonus()`?
b. Combien de variables nommées `points` existent pendant l'exécution de `ajouter_bonus(10)`? Où chacune existe-t-elle?
c. Réécris le programme pour que `ajouter_bonus()` **renvoie** le nouveau total (avec une constante `BONUS = 5`) et que le programme principal mette à jour `points` après chaque appel.

*Sortie attendue de la version corrigée :*

```text
Total du joueur : 15
Total du joueur : 20
```

## 🟢 Exercice 2 : Facile

**But** : Comprendre qu'une variable locale disparaît à la fin de l'appel.

**Énoncé** : Le programme suivant calcule la paie hebdomadaire d'un emploi étudiant. Il provoque une erreur.

```python
TARIF_HORAIRE = 17.50


def calculer_paie(heures):
    paie = round(heures * TARIF_HORAIRE, 2)


calculer_paie(12)
print(f"Paie de la semaine : {paie} $")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=TARIF_HORAIRE%20%3D%2017.50%0A%0A%0Adef%20calculer_paie%28heures%29%3A%0A%20%20%20%20paie%20%3D%20round%28heures%20%2A%20TARIF_HORAIRE%2C%202%29%0A%0A%0Acalculer_paie%2812%29%0Aprint%28f%22Paie%20de%20la%20semaine%20%3A%20%7Bpaie%7D%20%24%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

```text
NameError: name 'paie' is not defined
```

a. Explique pourquoi `paie` n'est « pas définie », alors que la ligne `paie = ...` a bien été exécutée.
b. La fonction utilise `TARIF_HORAIRE` sans l'avoir reçu en paramètre. Pourquoi est-ce permis?
c. Corrige le programme sans déplacer le `print()` dans la fonction.

*Sortie attendue après correction :*

```text
Paie de la semaine : 210.00 $
```

## 🟡 Exercice 3 : Moyen

**But** : Prévoir l'effet d'une fonction sur une liste et sur une variable simple reçues en paramètres.

**Énoncé** : La bibliothèque du cégep tient à jour la liste des livres disponibles et le nombre d'emprunts de la journée.

```python
def emprunter(inventaire, nb_emprunts, titre):
    inventaire.remove(titre)
    nb_emprunts += 1
    print(f"Dans la fonction : {inventaire}, {nb_emprunts} emprunt(s)")


livres = ["Kukum", "Agaguk", "Bonheur d'occasion"]
compteur = 0
emprunter(livres, compteur, "Agaguk")
print(f"Après l'appel : {livres}, {compteur} emprunt(s)")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20emprunter%28inventaire%2C%20nb_emprunts%2C%20titre%29%3A%0A%20%20%20%20inventaire.remove%28titre%29%0A%20%20%20%20nb_emprunts%20%2B%3D%201%0A%20%20%20%20print%28f%22Dans%20la%20fonction%20%3A%20%7Binventaire%7D%2C%20%7Bnb_emprunts%7D%20emprunt%28s%29%22%29%0A%0A%0Alivres%20%3D%20%5B%22Kukum%22%2C%20%22Agaguk%22%2C%20%22Bonheur%20d%27occasion%22%5D%0Acompteur%20%3D%200%0Aemprunter%28livres%2C%20compteur%2C%20%22Agaguk%22%29%0Aprint%28f%22Apr%C3%A8s%20l%27appel%20%3A%20%7Blivres%7D%2C%20%7Bcompteur%7D%20emprunt%28s%29%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

a. Sans exécuter de code, écris ce qu'affiche le programme.
b. Explique pourquoi la liste `livres` a changé après l'appel, mais pas la variable `compteur`.
c. Modifie `emprunter()` pour qu'elle **renvoie** le nouveau nombre d'emprunts (et qu'elle n'affiche plus rien). Le programme principal emprunte ensuite « Agaguk », puis « Kukum », et affiche le résultat.

*Sortie attendue de la version modifiée :*

```text
Après les appels : ["Bonheur d'occasion"], 2 emprunt(s)
```

## 🟡 Exercice 4 : Moyen

**But** : Remplacer une dépendance à une variable globale par des paramètres et une valeur de retour.

**Énoncé** : Ce programme gère la carte prépayée de la cafétéria. Il ne fonctionne pas comme prévu : le solde ne diminue jamais.

```python
solde = 25.00    # solde de la carte de cafétéria


def payer(montant):
    if montant <= solde:
        print(f"Paiement de {montant:.2f} $ accepté. Nouveau solde : {solde - montant:.2f} $")
    else:
        print(f"Paiement de {montant:.2f} $ refusé : solde insuffisant.")


payer(8.75)
payer(6.50)
payer(12.25)
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=solde%20%3D%2025.00%20%20%20%20%23%20solde%20de%20la%20carte%20de%20caf%C3%A9t%C3%A9ria%0A%0A%0Adef%20payer%28montant%29%3A%0A%20%20%20%20if%20montant%20%3C%3D%20solde%3A%0A%20%20%20%20%20%20%20%20print%28f%22Paiement%20de%20%7Bmontant%3A.2f%7D%20%24%20accept%C3%A9.%20Nouveau%20solde%20%3A%20%7Bsolde%20-%20montant%3A.2f%7D%20%24%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28f%22Paiement%20de%20%7Bmontant%3A.2f%7D%20%24%20refus%C3%A9%20%3A%20solde%20insuffisant.%22%29%0A%0A%0Apayer%288.75%29%0Apayer%286.50%29%0Apayer%2812.25%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

```text
Paiement de 8.75 $ accepté. Nouveau solde : 16.25 $
Paiement de 6.50 $ accepté. Nouveau solde : 18.50 $
Paiement de 12.25 $ accepté. Nouveau solde : 12.75 $
```

a. Explique pourquoi le solde affiché ne tient jamais compte des paiements précédents.
b. Réécris la fonction sous la forme `payer(solde, montant)` : elle reçoit le solde actuel, affiche le message, puis **renvoie** le nouveau solde (inchangé si le paiement est refusé). La fonction ne doit utiliser **aucune** variable globale.
c. Le programme principal part d'une constante `SOLDE_INITIAL = 25.00` et traite, dans une boucle, les achats de la constante `ACHATS = (8.75, 6.50, 12.25, 4.00)`.

*Sortie attendue :*

```text
Paiement de 8.75 $ accepté. Nouveau solde : 16.25 $
Paiement de 6.50 $ accepté. Nouveau solde : 9.75 $
Paiement de 12.25 $ refusé : solde insuffisant.
Paiement de 4.00 $ accepté. Nouveau solde : 5.75 $
Solde final : 5.75 $
```

> 💡 Tenter de modifier la variable globale `solde` directement dans la fonction (`solde = solde - montant`) provoque une erreur : Python considère alors `solde` comme une variable **locale**, utilisée avant d'avoir reçu une valeur. La bonne solution passe par les paramètres et `return`.

## 🔴 Exercice 5 : Difficile

**But** : Comparer une fonction qui modifie une liste reçue et une fonction qui renvoie une nouvelle liste.

**Énoncé** : Écris deux fonctions qui retirent les absents d'une liste de présences :

- `retirer_absents(presences, absents)` **modifie** directement la liste `presences` et ne renvoie rien;
- `filtrer_absents(presences, absents)` ne modifie **pas** `presences` : elle **renvoie** une nouvelle liste qui contient seulement les présents.

Un nom de la liste `absents` qui n'est pas dans `presences` doit simplement être ignoré (sans erreur).

Le programme principal utilise les listes suivantes. Il appelle d'abord `filtrer_absents()`, puis `retirer_absents()`, et affiche chaque fois le contenu de `groupe` et la valeur renvoyée.

```python
groupe = ["Léa", "Samuel", "Noah", "Zoé", "Mia"]
absents_du_jour = ["Noah", "Mia", "Félix"]
```

*Sortie attendue :*

```text
Après filtrer_absents()
  Groupe : ['Léa', 'Samuel', 'Noah', 'Zoé', 'Mia']
  Présents : ['Léa', 'Samuel', 'Zoé']
Après retirer_absents()
  Groupe : ['Léa', 'Samuel', 'Zoé']
  Valeur renvoyée : None
```

Réponds ensuite aux questions :

a. Laquelle des deux fonctions est la plus sûre si on veut conserver la liste complète du groupe pour le lendemain? Pourquoi?
b. Pourquoi `retirer_absents()` renvoie-t-elle `None`?
c. Dans `retirer_absents()`, est-il dangereux de faire `remove()` dans la boucle? Explique en pensant au piège de la fiche 6.2 (*Ne pas ajouter ou retirer d'éléments pendant qu'on parcourt la liste*).

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.5 - La portée des variables](Solutions%207.5%20-%20La%20portée%20des%20variables.md).
