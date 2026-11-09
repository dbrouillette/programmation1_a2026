# Solutions — La portée des variables (fiche 7.5)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
Points avec bonus : 15
Total du joueur : 0
Points avec bonus : 25
Total du joueur : 20
```

a. À l'intérieur de `ajouter_bonus()`, l'affectation `points = ...` crée une **nouvelle variable locale** nommée `points`. La variable globale `points` n'est jamais modifiée : elle vaut toujours `0`, puis `20` lorsque le programme principal la change lui-même.

b. **Deux** : la variable **globale** `points` (créée au premier niveau du fichier, qui existe pendant tout le programme) et la variable **locale** `points` (créée dans la fonction, qui disparaît à la fin de l'appel). Le paramètre `points_question` est une troisième variable, locale elle aussi.

c. Version corrigée :

```python
BONUS = 5


def ajouter_bonus(points_question):
    return points_question + BONUS


points = 0
points = ajouter_bonus(10)
print(f"Total du joueur : {points}")
points = ajouter_bonus(points)
print(f"Total du joueur : {points}")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=BONUS%20%3D%205%0A%0A%0Adef%20ajouter_bonus%28points_question%29%3A%0A%20%20%20%20return%20points_question%20%2B%20BONUS%0A%0A%0Apoints%20%3D%200%0Apoints%20%3D%20ajouter_bonus%2810%29%0Aprint%28f%22Total%20du%20joueur%20%3A%20%7Bpoints%7D%22%29%0Apoints%20%3D%20ajouter_bonus%28points%29%0Aprint%28f%22Total%20du%20joueur%20%3A%20%7Bpoints%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- La fonction n'affiche plus rien et ne touche à aucune variable globale : elle reçoit les points et **renvoie** le nouveau total.
- C'est le programme principal qui décide de ranger le résultat dans `points`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

a. `paie` est une variable **locale** à `calculer_paie()`. Elle est bien créée pendant l'appel, mais elle **disparaît** dès que la fonction se termine. Au moment du `print()`, elle n'existe plus.

b. `TARIF_HORAIRE` est une **constante globale**, définie au premier niveau du fichier. Une fonction peut toujours **lire** une variable globale : Python la cherche d'abord parmi les variables locales, puis parmi les globales.

c. Version corrigée :

```python
TARIF_HORAIRE = 17.50


def calculer_paie(heures):
    return round(heures * TARIF_HORAIRE, 2)


paie = calculer_paie(12)
print(f"Paie de la semaine : {paie:.2f} $")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=TARIF_HORAIRE%20%3D%2017.50%0A%0A%0Adef%20calculer_paie%28heures%29%3A%0A%20%20%20%20return%20round%28heures%20%2A%20TARIF_HORAIRE%2C%202%29%0A%0A%0Apaie%20%3D%20calculer_paie%2812%29%0Aprint%28f%22Paie%20de%20la%20semaine%20%3A%20%7Bpaie%3A.2f%7D%20%24%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- La fonction **renvoie** la paie, et le programme principal la range dans sa propre variable `paie`. Les deux noms pourraient être différents.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

a. Affichage :

```text
Dans la fonction : ['Kukum', "Bonheur d'occasion"], 1 emprunt(s)
Après l'appel : ['Kukum', "Bonheur d'occasion"], 0 emprunt(s)
```

b. Le paramètre `inventaire` et la variable `livres` désignent **la même liste** (comme un alias, fiche 6.2). `remove()` modifie le **contenu** de cette liste : le changement est donc visible à l'extérieur. À l'inverse, `nb_emprunts += 1` **réaffecte** le paramètre local `nb_emprunts`, sans aucun effet sur la variable `compteur` du programme principal.

c. Version modifiée :

```python
def emprunter(inventaire, nb_emprunts, titre):
    inventaire.remove(titre)
    return nb_emprunts + 1


livres = ["Kukum", "Agaguk", "Bonheur d'occasion"]
compteur = 0
compteur = emprunter(livres, compteur, "Agaguk")
compteur = emprunter(livres, compteur, "Kukum")
print(f"Après les appels : {livres}, {compteur} emprunt(s)")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20emprunter%28inventaire%2C%20nb_emprunts%2C%20titre%29%3A%0A%20%20%20%20inventaire.remove%28titre%29%0A%20%20%20%20return%20nb_emprunts%20%2B%201%0A%0A%0Alivres%20%3D%20%5B%22Kukum%22%2C%20%22Agaguk%22%2C%20%22Bonheur%20d%27occasion%22%5D%0Acompteur%20%3D%200%0Acompteur%20%3D%20emprunter%28livres%2C%20compteur%2C%20%22Agaguk%22%29%0Acompteur%20%3D%20emprunter%28livres%2C%20compteur%2C%20%22Kukum%22%29%0Aprint%28f%22Apr%C3%A8s%20les%20appels%20%3A%20%7Blivres%7D%2C%20%7Bcompteur%7D%20emprunt%28s%29%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- La liste est toujours modifiée directement par `remove()`.
- Le compteur, lui, est **renvoyé** puis rangé dans `compteur` par le programme principal.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

a. La fonction **lit** la variable globale `solde`, mais ne la modifie jamais : elle affiche seulement le résultat du calcul `solde - montant`. Chaque paiement part donc du même solde de 25,00 $, et le troisième achat est accepté alors qu'il ne devrait pas l'être.

b. et c. Version corrigée :

```python
SOLDE_INITIAL = 25.00
ACHATS = (8.75, 6.50, 12.25, 4.00)


def payer(solde, montant):
    if montant <= solde:
        nouveau_solde = round(solde - montant, 2)
        print(f"Paiement de {montant:.2f} $ accepté. Nouveau solde : {nouveau_solde:.2f} $")
        return nouveau_solde
    else:
        print(f"Paiement de {montant:.2f} $ refusé : solde insuffisant.")
        return solde


solde = SOLDE_INITIAL
for achat in ACHATS:
    solde = payer(solde, achat)
print(f"Solde final : {solde:.2f} $")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=SOLDE_INITIAL%20%3D%2025.00%0AACHATS%20%3D%20%288.75%2C%206.50%2C%2012.25%2C%204.00%29%0A%0A%0Adef%20payer%28solde%2C%20montant%29%3A%0A%20%20%20%20if%20montant%20%3C%3D%20solde%3A%0A%20%20%20%20%20%20%20%20nouveau_solde%20%3D%20round%28solde%20-%20montant%2C%202%29%0A%20%20%20%20%20%20%20%20print%28f%22Paiement%20de%20%7Bmontant%3A.2f%7D%20%24%20accept%C3%A9.%20Nouveau%20solde%20%3A%20%7Bnouveau_solde%3A.2f%7D%20%24%22%29%0A%20%20%20%20%20%20%20%20return%20nouveau_solde%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28f%22Paiement%20de%20%7Bmontant%3A.2f%7D%20%24%20refus%C3%A9%20%3A%20solde%20insuffisant.%22%29%0A%20%20%20%20%20%20%20%20return%20solde%0A%0A%0Asolde%20%3D%20SOLDE_INITIAL%0Afor%20achat%20in%20ACHATS%3A%0A%20%20%20%20solde%20%3D%20payer%28solde%2C%20achat%29%0Aprint%28f%22Solde%20final%20%3A%20%7Bsolde%3A.2f%7D%20%24%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- Tout ce dont la fonction a besoin entre par ses **paramètres**, et le résultat sort par **`return`** : elle ne dépend d'aucune variable globale.
- Les deux branches du `if` renvoient une valeur. Sans le `return solde` du `else`, un paiement refusé ferait passer le solde à `None`.
- Dans la boucle, `solde = payer(solde, achat)` met à jour le solde après chaque achat.

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
def retirer_absents(presences, absents):
    for absent in absents:
        if absent in presences:
            presences.remove(absent)


def filtrer_absents(presences, absents):
    presents = []
    for etudiant in presences:
        if etudiant not in absents:
            presents.append(etudiant)
    return presents


groupe = ["Léa", "Samuel", "Noah", "Zoé", "Mia"]
absents_du_jour = ["Noah", "Mia", "Félix"]

presents = filtrer_absents(groupe, absents_du_jour)
print("Après filtrer_absents()")
print(f"  Groupe : {groupe}")
print(f"  Présents : {presents}")

resultat = retirer_absents(groupe, absents_du_jour)
print("Après retirer_absents()")
print(f"  Groupe : {groupe}")
print(f"  Valeur renvoyée : {resultat}")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=def%20retirer_absents%28presences%2C%20absents%29%3A%0A%20%20%20%20for%20absent%20in%20absents%3A%0A%20%20%20%20%20%20%20%20if%20absent%20in%20presences%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20presences.remove%28absent%29%0A%0A%0Adef%20filtrer_absents%28presences%2C%20absents%29%3A%0A%20%20%20%20presents%20%3D%20%5B%5D%0A%20%20%20%20for%20etudiant%20in%20presences%3A%0A%20%20%20%20%20%20%20%20if%20etudiant%20not%20in%20absents%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20presents.append%28etudiant%29%0A%20%20%20%20return%20presents%0A%0A%0Agroupe%20%3D%20%5B%22L%C3%A9a%22%2C%20%22Samuel%22%2C%20%22Noah%22%2C%20%22Zo%C3%A9%22%2C%20%22Mia%22%5D%0Aabsents_du_jour%20%3D%20%5B%22Noah%22%2C%20%22Mia%22%2C%20%22F%C3%A9lix%22%5D%0A%0Apresents%20%3D%20filtrer_absents%28groupe%2C%20absents_du_jour%29%0Aprint%28%22Apr%C3%A8s%20filtrer_absents%28%29%22%29%0Aprint%28f%22%20%20Groupe%20%3A%20%7Bgroupe%7D%22%29%0Aprint%28f%22%20%20Pr%C3%A9sents%20%3A%20%7Bpresents%7D%22%29%0A%0Aresultat%20%3D%20retirer_absents%28groupe%2C%20absents_du_jour%29%0Aprint%28%22Apr%C3%A8s%20retirer_absents%28%29%22%29%0Aprint%28f%22%20%20Groupe%20%3A%20%7Bgroupe%7D%22%29%0Aprint%28f%22%20%20Valeur%20renvoy%C3%A9e%20%3A%20%7Bresultat%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

a. `filtrer_absents()` est la plus sûre : elle laisse la liste `groupe` **intacte** et renvoie une nouvelle liste. Après `retirer_absents()`, Noah et Mia ont disparu de `groupe` : il faudrait les rajouter le lendemain.

b. `retirer_absents()` n'a pas d'instruction `return` : comme toute fonction sans `return`, elle renvoie `None`. Son travail consiste à **modifier** la liste reçue, comme les méthodes `append()` ou `sort()`.

c. Il n'y a pas de danger ici, parce que la boucle parcourt la liste `absents`, alors que `remove()` retire des éléments de la liste `presences`. Le piège de la fiche 6.2 survient seulement quand on retire des éléments de la liste **qu'on est en train de parcourir**. La vérification `if absent in presences` évite aussi la `ValueError` pour Félix, qui n'est pas dans le groupe.
