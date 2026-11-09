# Solutions — Valeurs par défaut et arguments nommés (fiche 7.6)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

| Appel | `article` | `quantite` | `emballage_cadeau` |
| --- | --- | --- | --- |
| `afficher_commande("Agenda")` | `"Agenda"` | `1` (défaut) | `False` (défaut) |
| `afficher_commande("Agenda", 3)` | `"Agenda"` | `3` | `False` (défaut) |
| `afficher_commande("Agenda", emballage_cadeau=True)` | `"Agenda"` | `1` (défaut) | `True` |
| `afficher_commande("Agenda", 2, True)` | `"Agenda"` | `2` | `True` |
| `afficher_commande(quantite=4, article="Stylo")` | `"Stylo"` | `4` | `False` (défaut) |
| `afficher_commande("Stylo", True)` | `"Stylo"` | **`True`** | `False` (défaut) |

```text
1 x Agenda
3 x Agenda
1 x Agenda (emballage cadeau)
2 x Agenda (emballage cadeau)
4 x Stylo
True x Stylo
```

- Le 3e appel saute `quantite` grâce à l'argument nommé : `quantite` garde sa valeur par défaut.
- Le 5e appel nomme tous ses arguments : leur ordre n'a donc plus d'importance.
- Le **6e appel** est le piège : sans nom, `True` est associé **par position** au 2e paramètre, `quantite`. Python ne voit aucun problème, mais l'affichage `True x Stylo` est absurde. Il fallait écrire `afficher_commande("Stylo", emballage_cadeau=True)`.

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

| Ligne | Résultat | Explication |
| --- | --- | --- |
| a. | ❌ `SyntaxError` : `parameter without a default follows parameter with a default` | Un paramètre obligatoire (`duree`) ne peut pas suivre un paramètre optionnel (`salle`). |
| b. | ❌ `SyntaxError` (même message) | `salle`, obligatoire, suit `duree`, optionnel. |
| c. | ✅ `Salle B-204, 60 minutes, projecteur : True` | `duree` garde sa valeur par défaut; `projecteur` est nommé. |
| d. | ❌ `SyntaxError` : `positional argument follows keyword argument` | Un argument positionnel (`"B-204"`) ne peut pas suivre un argument nommé. |
| e. | ❌ `TypeError` : `reserver() got multiple values for argument 'duree'` | `90` est déjà associé à `duree` par position; on lui donne ensuite une deuxième valeur par son nom. |
| f. | ❌ `TypeError` : `reserver() missing 1 required positional argument: 'salle'` | `salle` est obligatoire : il n'a pas de valeur par défaut. |
| g. | ✅ `Salle B-204, 90 minutes, projecteur : True` | Trois arguments positionnels, dans l'ordre. |

- Les erreurs **a**, **b** et **d** sont des erreurs de **syntaxe** : Python les détecte avant même d'exécuter le programme.
- Les erreurs **e** et **f** sont des erreurs d'**exécution** : la syntaxe est correcte, mais l'appel ne correspond pas aux paramètres.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
PRIX_REGULIER = 14.00
PRIX_ENFANT = 9.50
PRIX_AINE = 10.50
PRIX_ETUDIANT = 11.00
RABAIS_MARDI = 4.00
AGE_ENFANT_MAX = 12
AGE_AINE_MIN = 65


def calculer_prix_billet(age, est_etudiant=False, jour="semaine"):
    if age <= AGE_ENFANT_MAX:
        prix = PRIX_ENFANT
    elif age >= AGE_AINE_MIN:
        prix = PRIX_AINE
    elif est_etudiant:
        prix = PRIX_ETUDIANT
    else:
        prix = PRIX_REGULIER

    if jour == "mardi":
        prix -= RABAIS_MARDI
    return prix


prix_adulte = calculer_prix_billet(30)
prix_etudiant = calculer_prix_billet(19, est_etudiant=True)
prix_enfant_mardi = calculer_prix_billet(8, jour="mardi")
prix_etudiant_mardi = calculer_prix_billet(22, True, "mardi")

print(f"Adulte de 30 ans, en semaine : {prix_adulte:.2f} $")
print(f"Étudiant de 19 ans, en semaine : {prix_etudiant:.2f} $")
print(f"Enfant de 8 ans, le mardi : {prix_enfant_mardi:.2f} $")
print(f"Étudiant de 22 ans, le mardi : {prix_etudiant_mardi:.2f} $")
total = prix_adulte + prix_etudiant + prix_enfant_mardi + prix_etudiant_mardi
print(f"Total : {total:.2f} $")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=PRIX_REGULIER%20%3D%2014.00%0APRIX_ENFANT%20%3D%209.50%0APRIX_AINE%20%3D%2010.50%0APRIX_ETUDIANT%20%3D%2011.00%0ARABAIS_MARDI%20%3D%204.00%0AAGE_ENFANT_MAX%20%3D%2012%0AAGE_AINE_MIN%20%3D%2065%0A%0A%0Adef%20calculer_prix_billet%28age%2C%20est_etudiant%3DFalse%2C%20jour%3D%22semaine%22%29%3A%0A%20%20%20%20if%20age%20%3C%3D%20AGE_ENFANT_MAX%3A%0A%20%20%20%20%20%20%20%20prix%20%3D%20PRIX_ENFANT%0A%20%20%20%20elif%20age%20%3E%3D%20AGE_AINE_MIN%3A%0A%20%20%20%20%20%20%20%20prix%20%3D%20PRIX_AINE%0A%20%20%20%20elif%20est_etudiant%3A%0A%20%20%20%20%20%20%20%20prix%20%3D%20PRIX_ETUDIANT%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20prix%20%3D%20PRIX_REGULIER%0A%0A%20%20%20%20if%20jour%20%3D%3D%20%22mardi%22%3A%0A%20%20%20%20%20%20%20%20prix%20-%3D%20RABAIS_MARDI%0A%20%20%20%20return%20prix%0A%0A%0Aprix_adulte%20%3D%20calculer_prix_billet%2830%29%0Aprix_etudiant%20%3D%20calculer_prix_billet%2819%2C%20est_etudiant%3DTrue%29%0Aprix_enfant_mardi%20%3D%20calculer_prix_billet%288%2C%20jour%3D%22mardi%22%29%0Aprix_etudiant_mardi%20%3D%20calculer_prix_billet%2822%2C%20True%2C%20%22mardi%22%29%0A%0Aprint%28f%22Adulte%20de%2030%20ans%2C%20en%20semaine%20%3A%20%7Bprix_adulte%3A.2f%7D%20%24%22%29%0Aprint%28f%22%C3%89tudiant%20de%2019%20ans%2C%20en%20semaine%20%3A%20%7Bprix_etudiant%3A.2f%7D%20%24%22%29%0Aprint%28f%22Enfant%20de%208%20ans%2C%20le%20mardi%20%3A%20%7Bprix_enfant_mardi%3A.2f%7D%20%24%22%29%0Aprint%28f%22%C3%89tudiant%20de%2022%20ans%2C%20le%20mardi%20%3A%20%7Bprix_etudiant_mardi%3A.2f%7D%20%24%22%29%0Atotal%20%3D%20prix_adulte%20%2B%20prix_etudiant%20%2B%20prix_enfant_mardi%20%2B%20prix_etudiant_mardi%0Aprint%28f%22Total%20%3A%20%7Btotal%3A.2f%7D%20%24%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- L'ordre des conditions compte : l'âge est vérifié **avant** la carte étudiante, puisqu'un enfant ou un aîné paie son tarif, carte ou pas.
- `calculer_prix_billet(8, jour="mardi")` est l'appel le plus court pour l'enfant du mardi : `est_etudiant` garde sa valeur par défaut, et `jour` est nommé.
- Le dernier appel, `calculer_prix_billet(22, True, "mardi")`, est valide, mais moins lisible que `calculer_prix_billet(22, est_etudiant=True, jour="mardi")`.

## 🟡 Exercice 4 : Moyen

### ✅ Solution 4

```python
PSEUDO_MIN = 3
PSEUDO_MAX = 12
DEVISE_MAX = 40


def valider_texte(msg_saisie, longueur_min=1, longueur_max=100):
    texte = input(msg_saisie).strip()
    while not longueur_min <= len(texte) <= longueur_max:
        print(f"Erreur : entrez entre {longueur_min} et {longueur_max} caractères.")
        texte = input(msg_saisie).strip()
    return texte


def afficher_cadre(texte, symbole="*"):
    largeur = len(texte) + 4
    print(symbole * largeur)
    print(f"{symbole} {texte} {symbole}")
    print(symbole * largeur)


prenom = valider_texte("Prénom : ")
pseudo = valider_texte("Pseudo (3 à 12 caractères) : ", PSEUDO_MIN, PSEUDO_MAX)
devise = valider_texte("Devise (40 caractères max.) : ", longueur_max=DEVISE_MAX)

print()
afficher_cadre(prenom)
afficher_cadre(pseudo, "#")
afficher_cadre(devise, symbole="~")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=PSEUDO_MIN%20%3D%203%0APSEUDO_MAX%20%3D%2012%0ADEVISE_MAX%20%3D%2040%0A%0A%0Adef%20valider_texte%28msg_saisie%2C%20longueur_min%3D1%2C%20longueur_max%3D100%29%3A%0A%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20while%20not%20longueur_min%20%3C%3D%20len%28texte%29%20%3C%3D%20longueur_max%3A%0A%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20entre%20%7Blongueur_min%7D%20et%20%7Blongueur_max%7D%20caract%C3%A8res.%22%29%0A%20%20%20%20%20%20%20%20texte%20%3D%20input%28msg_saisie%29.strip%28%29%0A%20%20%20%20return%20texte%0A%0A%0Adef%20afficher_cadre%28texte%2C%20symbole%3D%22%2A%22%29%3A%0A%20%20%20%20largeur%20%3D%20len%28texte%29%20%2B%204%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%20%20%20%20print%28f%22%7Bsymbole%7D%20%7Btexte%7D%20%7Bsymbole%7D%22%29%0A%20%20%20%20print%28symbole%20%2A%20largeur%29%0A%0A%0Aprenom%20%3D%20valider_texte%28%22Pr%C3%A9nom%20%3A%20%22%29%0Apseudo%20%3D%20valider_texte%28%22Pseudo%20%283%20%C3%A0%2012%20caract%C3%A8res%29%20%3A%20%22%2C%20PSEUDO_MIN%2C%20PSEUDO_MAX%29%0Adevise%20%3D%20valider_texte%28%22Devise%20%2840%20caract%C3%A8res%20max.%29%20%3A%20%22%2C%20longueur_max%3DDEVISE_MAX%29%0A%0Aprint%28%29%0Aafficher_cadre%28prenom%29%0Aafficher_cadre%28pseudo%2C%20%22%23%22%29%0Aafficher_cadre%28devise%2C%20symbole%3D%22~%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- `valider_texte("Prénom : ")` utilise les deux valeurs par défaut.
- `valider_texte("Devise ... : ", longueur_max=DEVISE_MAX)` ne précise que le maximum : le minimum garde sa valeur par défaut, `1`.
- Les appels écrits pour les exercices 7.3 et 7.4 fonctionnent toujours **sans modification** : ajouter un paramètre optionnel ne brise pas les appels existants.

## 🔴 Exercice 5 : Difficile

### ✅ Solution 5

```python
NB_COUREURS = 3
TEMPS_MIN = 1
TEMPS_MAX = 86399      # 23 h 59 min 59 s
SECONDES_PAR_MINUTE = 60
SECONDES_PAR_HEURE = 3600

# (copier ici les fonctions fournies valider_nombre() et valider_entier())


def formater_duree(secondes, afficher_heures=True, separateur=":"):
    if afficher_heures:
        heures = secondes // SECONDES_PAR_HEURE
        minutes = secondes % SECONDES_PAR_HEURE // SECONDES_PAR_MINUTE
        reste = secondes % SECONDES_PAR_MINUTE
        return f"{heures}{separateur}{minutes:0>2}{separateur}{reste:0>2}"
    else:
        minutes = secondes // SECONDES_PAR_MINUTE
        reste = secondes % SECONDES_PAR_MINUTE
        return f"{minutes}{separateur}{reste:0>2}"


temps = []
for i in range(1, NB_COUREURS + 1):
    temps.append(valider_entier(f"Temps du coureur {i} (en secondes) : ", TEMPS_MIN, TEMPS_MAX))

print(f"\n{'Coureur':<10}{'h:mm:ss':>10}{'min:ss':>10}{'h.mm.ss':>10}")
for i in range(len(temps)):
    print(f"{i + 1:<10}"
          f"{formater_duree(temps[i]):>10}"
          f"{formater_duree(temps[i], afficher_heures=False):>10}"
          f"{formater_duree(temps[i], separateur='.'):>10}")
```

<p align="right"><sub><a href="https://pythontutor.com/visualize.html#code=NB_COUREURS%20%3D%203%0ATEMPS_MIN%20%3D%201%0ATEMPS_MAX%20%3D%2086399%20%20%20%20%20%20%23%2023%20h%2059%20min%2059%20s%0ASECONDES_PAR_MINUTE%20%3D%2060%0ASECONDES_PAR_HEURE%20%3D%203600%0A%0Adef%20valider_nombre%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20float%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20valide.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20valider_entier%28msg_saisie%2C%20val_min%2C%20val_max%29%3A%0A%20%20%20%20valide%20%3D%20False%0A%20%20%20%20while%20not%20valide%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nombre%20%3D%20int%28input%28msg_saisie%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val_min%20%3C%3D%20nombre%20%3C%3D%20val_max%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20valide%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Erreur%20%3A%20entrez%20un%20nombre%20entre%20%7Bval_min%7D%20et%20%7Bval_max%7D.%22%29%0A%20%20%20%20%20%20%20%20except%20ValueError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Erreur%20%3A%20ce%20n%27est%20pas%20un%20nombre%20entier.%22%29%0A%20%20%20%20return%20nombre%0A%0A%0Adef%20formater_duree%28secondes%2C%20afficher_heures%3DTrue%2C%20separateur%3D%22%3A%22%29%3A%0A%20%20%20%20if%20afficher_heures%3A%0A%20%20%20%20%20%20%20%20heures%20%3D%20secondes%20%2F%2F%20SECONDES_PAR_HEURE%0A%20%20%20%20%20%20%20%20minutes%20%3D%20secondes%20%25%20SECONDES_PAR_HEURE%20%2F%2F%20SECONDES_PAR_MINUTE%0A%20%20%20%20%20%20%20%20reste%20%3D%20secondes%20%25%20SECONDES_PAR_MINUTE%0A%20%20%20%20%20%20%20%20return%20f%22%7Bheures%7D%7Bseparateur%7D%7Bminutes%3A0%3E2%7D%7Bseparateur%7D%7Breste%3A0%3E2%7D%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20minutes%20%3D%20secondes%20%2F%2F%20SECONDES_PAR_MINUTE%0A%20%20%20%20%20%20%20%20reste%20%3D%20secondes%20%25%20SECONDES_PAR_MINUTE%0A%20%20%20%20%20%20%20%20return%20f%22%7Bminutes%7D%7Bseparateur%7D%7Breste%3A0%3E2%7D%22%0A%0A%0Atemps%20%3D%20%5B%5D%0Afor%20i%20in%20range%281%2C%20NB_COUREURS%20%2B%201%29%3A%0A%20%20%20%20temps.append%28valider_entier%28f%22Temps%20du%20coureur%20%7Bi%7D%20%28en%20secondes%29%20%3A%20%22%2C%20TEMPS_MIN%2C%20TEMPS_MAX%29%29%0A%0Aprint%28f%22%5Cn%7B%27Coureur%27%3A%3C10%7D%7B%27h%3Amm%3Ass%27%3A%3E10%7D%7B%27min%3Ass%27%3A%3E10%7D%7B%27h.mm.ss%27%3A%3E10%7D%22%29%0Afor%20i%20in%20range%28len%28temps%29%29%3A%0A%20%20%20%20print%28f%22%7Bi%20%2B%201%3A%3C10%7D%22%0A%20%20%20%20%20%20%20%20%20%20f%22%7Bformater_duree%28temps%5Bi%5D%29%3A%3E10%7D%22%0A%20%20%20%20%20%20%20%20%20%20f%22%7Bformater_duree%28temps%5Bi%5D%2C%20afficher_heures%3DFalse%29%3A%3E10%7D%22%0A%20%20%20%20%20%20%20%20%20%20f%22%7Bformater_duree%28temps%5Bi%5D%2C%20separateur%3D%27.%27%29%3A%3E10%7D%22%29&cumulative=false&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Exécution...</a></sub></p>

- `secondes // SECONDES_PAR_HEURE` donne les heures complètes. `secondes % SECONDES_PAR_HEURE` donne ce qui reste après les heures, et `// SECONDES_PAR_MINUTE` en tire les minutes.
- La fonction **renvoie** une chaîne au lieu de l'afficher : on peut donc l'utiliser directement dans un f-string, avec un alignement (`:>10`).
- Dans `formater_duree(temps[i], separateur='.')`, on utilise des apostrophes autour du point pour ne pas fermer les guillemets du f-string.
- Les appels nommés permettent de changer **une seule** option en laissant l'autre à sa valeur par défaut.
