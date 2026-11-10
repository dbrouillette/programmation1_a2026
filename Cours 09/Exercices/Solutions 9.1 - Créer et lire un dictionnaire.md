# Solutions — Créer et lire un dictionnaire (fiche 9.1)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
5
1867
True
False
False
0
True
{'titre': 'Vive le vent', 'auteur': 'J. Pierpont', 'annee': 1857, 'tempo': 140}
Vive
Traceback (most recent call last):
  ...
KeyError: 'duree'
```

| Instruction | Affichage | Explication |
| --- | --- | --- |
| `len(chanson)` | `5` | 4 clés au départ, plus `favori`. Modifier `tempo` n'ajoute pas de clé. |
| `chanson["annee"] + 10` | `1867` | La valeur est un `int` : on peut calculer avec. |
| `"auteur" in chanson` | `True` | `in` vérifie les clés. |
| `"Auteur" in chanson` | `False` | Les clés sont sensibles à la casse. |
| `1857 in chanson` | `False` | `in` cherche dans les **clés**, pas dans les valeurs. |
| `chanson.get("duree", 0)` | `0` | Clé absente : `get()` renvoie la valeur par défaut, sans erreur. |
| `chanson.pop("favori")` | `True` | `pop()` supprime la paire et **renvoie** sa valeur. |
| `print(chanson)` | le dictionnaire | `favori` a disparu; `tempo` vaut 140. |
| `chanson["titre"][:4]` | `Vive` | `chanson["titre"]` est une chaîne : on peut lui appliquer le *slicing*. |
| `chanson["duree"]` | `KeyError: 'duree'` | Clé absente lue avec des crochets : erreur. |

## 🟢 Exercice 2 : Facile

### ✅ Solution 2

```python
from utilitaires import lire_entier, lire_texte

LARGEUR_LCD = 16

def creer_fiche(titre, auteur, annee):
    """Renvoie la fiche d'une chanson sous forme de dictionnaire."""
    return {"titre": titre, "auteur": auteur, "annee": annee}

def afficher_lcd(chanson):
    """Simule l'afficheur 16 x 2 : titre sur la ligne 1, auteur sur la ligne 2."""
    print("+" + "-" * LARGEUR_LCD + "+")
    print(f"|{chanson['titre'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print(f"|{chanson['auteur'][:LARGEUR_LCD]:<{LARGEUR_LCD}}|")
    print("+" + "-" * LARGEUR_LCD + "+")

def main():
    titre = lire_texte("Titre : ")
    auteur = lire_texte("Auteur : ")
    annee = lire_entier("Année : ", 1500, 2026)

    fiche = creer_fiche(titre, auteur, annee)
    print(fiche)
    afficher_lcd(fiche)

main()
```

- La fonction `creer_fiche()` renvoie directement un dictionnaire construit avec ses paramètres.
- `afficher_lcd()` ne reçoit qu'**un seul** paramètre, le dictionnaire, plutôt que trois. Si on ajoute une clé à la fiche plus tard, la signature de la fonction ne change pas.
- La largeur peut être une variable dans le format : `:<{LARGEUR_LCD}`. On peut aussi écrire `:<16` directement.
- Un afficheur réel recevrait exactement ces deux chaînes de 16 caractères.

## 🟡 Exercice 3 : Moyen

### ✅ Solution 3

```python
FREQUENCES = {
    "DO4": 262,
    "RE4": 294,
    "MI4": 330,
    "FA4": 349,
    "SOL4": 392,
    "LA4": 440,
    "SI4": 494,
    "DO5": 523,
}

def frequence_de(note):
    """Renvoie la fréquence (Hz) de la note, ou 0 (silence) si elle est inconnue."""
    return FREQUENCES.get(note.strip().upper(), 0)

def main():
    note = input("Note (Entrée pour terminer) : ").strip().upper()
    while note != "":
        frequence = frequence_de(note)
        if frequence == 0:
            print(f"{note} : note inconnue (silence)")
        else:
            print(f"{note} : {frequence} Hz")
        note = input("Note (Entrée pour terminer) : ").strip().upper()

main()
```

- `get(cle, 0)` remplace un `if note in FREQUENCES: ... else: ...` en une seule ligne.
- La normalisation (`strip()` et `upper()`) est faite dans la fonction : n'importe quel appelant en profite.

**Bonus** : on remplace l'octave 5 par l'octave 4, puis on double la fréquence.

```python
def frequence_de(note):
    """Renvoie la fréquence (Hz) de la note, ou 0 (silence) si elle est inconnue.

    Les notes de l'octave 5 absentes de la table sont calculées à partir de l'octave 4.
    """
    note = note.strip().upper()
    if note in FREQUENCES:
        return FREQUENCES[note]
    if note != "" and note[-1] == "5":
        note_octave_4 = note[:-1] + "4"
        return FREQUENCES.get(note_octave_4, 0) * 2
    return 0
```

- `RE5` → `RE4` (294 Hz) → 588 Hz. Une note inconnue comme `ZZ5` donne `0 * 2`, donc `0`.
- Le test `note != ""` évite une `IndexError` sur `note[-1]` si on reçoit une chaîne vide.
