# Exercices — Classes et objets, le principe (fiche 10.1)

> 📌 **À savoir** : chaque classe a une docstring, et chaque méthode aussi. Les noms de classes sont en *PascalCase* (`Livre`, `Tirelire`), les attributs et les méthodes en `snake_case`.

## 🟢 Exercice 1 : Facile

**But** : Définir une classe et créer des objets.

**Énoncé** : Écris la classe `Cours`, dont le constructeur reçoit le `code`, le `titre` et le nombre d'`heures` d'un cours. Chaque cours commence avec 0 `inscrits`.

Programme principal :

```python
prog1 = Cours("420-116-RI", "Introduction à la programmation", 90)
reseau = Cours("420-113-RI", "Introduction aux réseaux", 75)

prog1.inscrits = 32
reseau.inscrits = prog1.inscrits - 4
reseau.heures += 15

print(prog1.code, prog1.inscrits, prog1.heures)
print(reseau.code, reseau.inscrits, reseau.heures)
print(f"Total des inscrits : {prog1.inscrits + reseau.inscrits}")
```

*Sortie attendue :*

```text
420-116-RI 32 90
420-113-RI 28 90
Total des inscrits : 60
```

## 🟢 Exercice 2 : Facile

**But** : Reconnaître les erreurs fréquentes dans une classe.

**Énoncé** : Chacun de ces programmes contient **une** erreur. Pour chacun, donne le message d'erreur affiché, puis corrige-le.

```python
# Programme A
class Renard:
    def _init_(self, nom):
        self.nom = nom

roux = Renard("Roux")
```

```python
# Programme B
class Renard:
    def __init__(self, nom):
        nom = nom

roux = Renard("Roux")
print(roux.nom)
```

```python
# Programme C
class Renard:
    def __init__(self, nom):
        self.nom = nom

roux = Renard()
```

## Solutions

➡️ Les solutions se trouvent dans [Solutions 10.1 - Classes et objets, le principe](Solutions%2010.1%20-%20Classes%20et%20objets%2C%20le%20principe.md).
