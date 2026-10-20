# Exercices — Définir et appeler une fonction (fiche 7.2)

## 🟢 Exercice 1 : Facile

**But** : Distinguer la définition d'une fonction de son appel.

**Énoncé** : Sans exécuter de code, écris exactement ce qu'affiche le programme suivant. Réponds ensuite aux questions.

```python
def afficher_titre():
    print("--- Bibliothèque du cégep ---")


def afficher_heures_semaine():
    print("Lundi au jeudi : 8 h à 21 h")
    print("Vendredi : 8 h à 17 h")


def afficher_heures_fin_semaine():
    print("Samedi et dimanche : fermé")


afficher_titre()
afficher_heures_semaine()
print("Bonne session!")
afficher_titre()
```

[▶️ Vérifier dans Python Tutor](https://pythontutor.com/visualize.html#code=def%20afficher_titre%28%29%3A%0A%20%20%20%20print%28%22---%20Biblioth%C3%A8que%20du%20c%C3%A9gep%20---%22%29%0A%0A%0Adef%20afficher_heures_semaine%28%29%3A%0A%20%20%20%20print%28%22Lundi%20au%20jeudi%20%3A%208%20h%20%C3%A0%2021%20h%22%29%0A%20%20%20%20print%28%22Vendredi%20%3A%208%20h%20%C3%A0%2017%20h%22%29%0A%0A%0Adef%20afficher_heures_fin_semaine%28%29%3A%0A%20%20%20%20print%28%22Samedi%20et%20dimanche%20%3A%20ferm%C3%A9%22%29%0A%0A%0Aafficher_titre%28%29%0Aafficher_heures_semaine%28%29%0Aprint%28%22Bonne%20session%21%22%29%0Aafficher_titre%28%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

a. Combien de fois le corps de `afficher_titre()` est-il exécuté?
b. Pourquoi le texte « Samedi et dimanche : fermé » n'apparaît-il jamais?
c. Quelle ligne faudrait-il ajouter, et où, pour qu'il apparaisse juste après les heures de la semaine?

## 🟢 Exercice 2 : Facile

**But** : Repérer les erreurs fréquentes dans la définition et l'appel d'une fonction.

**Énoncé** : Le programme ci-dessous devrait afficher le menu d'une borne de prêt, puis un message d'au revoir. Il contient **cinq** erreurs. Trouve-les, explique chacune, puis écris la version corrigée.

```python
afficher_menu()

def afficher_menu()
    print("1. Emprunter un livre")
print("2. Retourner un livre")
    print("3. Quitter")

def Afficher_Au_Revoir():
    print("Merci et à bientôt!")

afficher_au_revoir
```

[▶️ Vérifier dans Python Tutor](https://pythontutor.com/visualize.html#code=afficher_menu%28%29%0A%0Adef%20afficher_menu%28%29%0A%20%20%20%20print%28%221.%20Emprunter%20un%20livre%22%29%0Aprint%28%222.%20Retourner%20un%20livre%22%29%0A%20%20%20%20print%28%223.%20Quitter%22%29%0A%0Adef%20Afficher_Au_Revoir%28%29%3A%0A%20%20%20%20print%28%22Merci%20et%20%C3%A0%20bient%C3%B4t%21%22%29%0A%0Aafficher_au_revoir&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

> 💡 L'une de ces erreurs ne provoque **aucun** message d'erreur : le programme s'exécute, mais ne fait pas ce qu'on attend.

*Sortie attendue du programme corrigé :*

```text
1. Emprunter un livre
2. Retourner un livre
3. Quitter
Merci et à bientôt!
```

## 🟢 Exercice 3 : Facile

**But** : Écrire et appeler ses premières fonctions.

**Énoncé** : Écris un programme qui affiche l'affiche des règles de la bibliothèque du cégep. Le programme contient :

- une constante `LARGEUR = 40`;
- une fonction `afficher_ligne()`, qui affiche une ligne de `LARGEUR` tirets;
- une fonction `afficher_regles()`, qui affiche les quatre règles numérotées ci-dessous.

Le programme principal appelle ces fonctions (et `print()`) pour produire exactement la sortie suivante. Le titre est centré sur `LARGEUR` caractères.

*Sortie attendue :*

```text
----------------------------------------
       RÈGLES DE LA BIBLIOTHÈQUE
----------------------------------------
1. Parler à voix basse.
2. Aucune nourriture près des ordinateurs.
3. Rapporter les livres au comptoir.
4. Réserver les salles de travail en ligne.
----------------------------------------
```

## 🟡 Exercice 4 : Moyen

**But** : Faire appeler une fonction par une autre fonction.

**Énoncé** : Le gym du cégep veut afficher son horaire à l'écran de l'accueil. Écris un programme qui contient :

- les constantes suivantes :

  ```python
  NOM_GYM = "Gym Les Diablos"
  LARGEUR = 32
  JOURS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
  HEURES = ("6 h - 22 h", "6 h - 22 h", "6 h - 22 h", "6 h - 22 h", "6 h - 20 h", "8 h - 18 h", "Fermé")
  ```

- une fonction `afficher_banniere()`, qui affiche le nom du gym centré entre deux lignes de `=`;
- une fonction `afficher_horaire()`, qui **appelle** `afficher_banniere()`, puis affiche chaque jour et ses heures d'ouverture à l'aide d'une boucle `for`. Les jours sont alignés à gauche sur 12 caractères et les heures, à droite sur 20 caractères.

Le programme principal ne contient qu'**un seul** appel : `afficher_horaire()`.

*Sortie attendue :*

```text
================================
        Gym Les Diablos
================================
Lundi                 6 h - 22 h
Mardi                 6 h - 22 h
Mercredi              6 h - 22 h
Jeudi                 6 h - 22 h
Vendredi              6 h - 20 h
Samedi                8 h - 18 h
Dimanche                   Fermé
```

> 💡 Les largeurs `12` et `20` additionnées donnent `LARGEUR`. Pour centrer le nom, utilise la largeur en constante dans le format, comme dans la fiche : `{NOM_GYM:^{LARGEUR}}`.

## 🟡 Exercice 5 : Moyen

**But** : Suivre le déroulement de l'exécution d'un programme qui contient des fonctions.

**Énoncé** : Les lignes du programme ci-dessous sont numérotées.

```python
 1  def afficher_bonjour():
 2      print("Bonjour!")
 3
 4
 5  def afficher_menu_du_jour():
 6      afficher_bonjour()
 7      print("Soupe : poulet et nouilles")
 8      afficher_dessert()
 9
10
11  def afficher_dessert():
12      print("Dessert : pouding chômeur")
13
14
15  print("Cafétéria du cégep")
16  afficher_menu_du_jour()
17  print("Bon appétit!")
```

[▶️ Vérifier dans Python Tutor](https://pythontutor.com/visualize.html#code=def%20afficher_bonjour%28%29%3A%0A%20%20%20%20print%28%22Bonjour%21%22%29%0A%0A%0Adef%20afficher_menu_du_jour%28%29%3A%0A%20%20%20%20afficher_bonjour%28%29%0A%20%20%20%20print%28%22Soupe%20%3A%20poulet%20et%20nouilles%22%29%0A%20%20%20%20afficher_dessert%28%29%0A%0A%0Adef%20afficher_dessert%28%29%3A%0A%20%20%20%20print%28%22Dessert%20%3A%20pouding%20ch%C3%B4meur%22%29%0A%0A%0Aprint%28%22Caf%C3%A9t%C3%A9ria%20du%20c%C3%A9gep%22%29%0Aafficher_menu_du_jour%28%29%0Aprint%28%22Bon%20app%C3%A9tit%21%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

a. Sans exécuter le programme, écris la liste des numéros de lignes **dans l'ordre où Python les exécute**. Compte les lignes `def` (Python les lit pour mémoriser les fonctions), mais pas les lignes vides.
b. Écris ce qu'affiche le programme.
c. `afficher_dessert()` est appelée à la ligne 8, mais n'est définie qu'à la ligne 11. Le programme provoque-t-il une erreur `NameError`? Explique.
d. Vérifie tes réponses avec le débogueur de VS Code : place un point d'arrêt (`F9`) sur la ligne 15, démarre le débogage (`F5`), puis avance avec `F11` (**Pas à pas détaillé**) en notant chaque ligne surlignée.

## Solutions

➡️ Les solutions se trouvent dans [Solutions 7.2 - Définir et appeler une fonction](Solutions%207.2%20-%20Définir%20et%20appeler%20une%20fonction.md).
