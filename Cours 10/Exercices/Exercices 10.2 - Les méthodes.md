# Exercices — Les méthodes (fiche 10.2)

> 📌 **À savoir** : chaque classe a une docstring, et chaque méthode aussi. Les noms de classes sont en *PascalCase* (`Livre`, `Tirelire`), les attributs et les méthodes en `snake_case`.

## 🟢 Exercice 1 : Facile

**But** : Suivre l'état de deux objets.

**Énoncé** : Voici la classe `Renard` de la fiche 10.2 (avec `chasser()` et `courir()`). Sans exécuter le code, donne ce qu'affiche chaque `print()`.

```python
a = Renard("Roux", "roux", 3)
b = Renard("Flocon", "arctique", 2)
a.chasser("mulot")
b.chasser("lemming")
b.chasser("lemming")
b.chasser("campagnol")
print(a.energie, b.energie)
print(len(b.proies), b.proies[-1])
print(a.courir(8))
print(a.courir(7), a.energie)
b.age = b.age + 1
print(b.age, a.age)
c = a
c.nom = "Goupil"
print(a.nom)
```

> 🤔 **Réflexion** : pourquoi la dernière ligne n'affiche-t-elle pas `Roux`? Combien de renards existent-ils réellement?

## 🟢 Exercice 2 : Facile

**But** : Écrire sa première classe.

**Énoncé** : Écris la classe `Livre`, qui représente un livre en cours de lecture :

- le constructeur reçoit le `titre`, l'`auteur` et le nombre de pages (`nb_pages`); la `page_actuelle` commence à 0;
- `lire(pages)` avance de `pages` pages, **sans dépasser** la fin du livre;
- `pourcentage()` **renvoie** le pourcentage du livre déjà lu;
- `est_termine()` **renvoie** `True` si la dernière page est atteinte;
- `__str__()` renvoie le titre, l'auteur et le pourcentage lu (sans décimale).

Teste ta classe avec ce programme principal :

```python
roman = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
bd = Livre("Astérix le Gaulois", "Goscinny et Uderzo", 48)

roman.lire(30)
roman.lire(18)
bd.lire(60)

print(roman)
print(bd)
print(f"Roman terminé? {roman.est_termine()}")
print(f"BD terminée? {bd.est_termine()}")
```

*Sortie attendue :*

```text
« Le Petit Prince » de Antoine de Saint-Exupéry (50 % lu)
« Astérix le Gaulois » de Goscinny et Uderzo (100 % lu)
Roman terminé? False
BD terminée? True
```

## 🟡 Exercice 3 : Moyen

**But** : Ajouter des méthodes à une classe existante et piloter un objet avec un menu.

**Énoncé** : Reprends la classe `Renard` de la fiche 10.2 et ajoute-lui :

- `dormir(heures)` : +15 d'énergie par heure, sans dépasser `ENERGIE_MAX`;
- `est_affame()` : **renvoie** `True` si l'énergie est sous `SEUIL_FAIM` (30);
- `__str__()` : le nom, l'énergie et le nombre de proies, suivis de `(affamé!)` si le renard est affamé.

Écris ensuite un programme qui crée le renard *Roux* et le fait vivre avec un menu, jusqu'au choix 0. Chaque saisie est validée : la distance va de 1 à 10 km, le sommeil de 1 à 12 heures. Une course refusée affiche un message.

*Exemple d'exécution :*

```text
Roux : énergie 50, 0 proie(s)
1. Chasser  2. Courir  3. Dormir  0. Quitter : 2
Distance (1 à 10 km) : 3
Roux : énergie 20, 0 proie(s) (affamé!)
1. Chasser  2. Courir  3. Dormir  0. Quitter : 2
Distance (1 à 10 km) : 6
Roux est trop fatigué pour courir 6 km.
Roux : énergie 20, 0 proie(s) (affamé!)
1. Chasser  2. Courir  3. Dormir  0. Quitter : 3
Heures de sommeil (1 à 12) : 2
Roux : énergie 50, 0 proie(s)
1. Chasser  2. Courir  3. Dormir  0. Quitter : 1
Proie : mulot
Roux : énergie 70, 1 proie(s)
1. Chasser  2. Courir  3. Dormir  0. Quitter : 0
Bonne nuit, Roux!
```

## 🔴 Exercice 4 : Moyen-Difficile

**But** : Protéger les données d'un objet avec des méthodes qui valident.

**Énoncé** : Écris la classe `Tirelire` :

- le constructeur reçoit le nom du `proprietaire`; le `solde` commence à 0 et l'`historique` est une liste vide;
- `deposer(montant)` : refuse un montant nul ou négatif; **renvoie** `True` si l'opération est acceptée, `False` sinon;
- `retirer(montant)` : refuse un montant nul, négatif, ou plus grand que le solde; **renvoie** `True` ou `False`;
- chaque opération, **acceptée ou refusée**, ajoute une ligne à l'historique;
- `afficher_historique()` affiche les opérations numérotées, puis le solde;
- `__str__()` renvoie le propriétaire et le solde.

Programme principal :

```python
abby = Tirelire("Abby")
zoe = Tirelire("Zoé")
abby.deposer(20)
abby.deposer(-5)
abby.retirer(7.50)
abby.retirer(50)
zoe.deposer(10)

print(abby)
print(zoe)
print()
abby.afficher_historique()
```

*Sortie attendue :*

```text
Tirelire de Abby : 12.50 $
Tirelire de Zoé : 10.00 $

Tirelire de Abby
  1. Dépôt de 20.00 $
  2. Dépôt refusé : -5.00 $
  3. Retrait de 7.50 $
  4. Retrait refusé : 50.00 $
Solde : 12.50 $
```

> 💡 Les deux tirelires ont chacune **leur propre** historique : c'est pourquoi la liste doit être créée dans `__init__()`, avec `self.historique = []`.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.2 - Les méthodes](Solutions%2010.2%20-%20Les%20m%C3%A9thodes.md).
