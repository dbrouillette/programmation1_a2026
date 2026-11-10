# Solutions — L'encodage des caractères (fiche 8.2)

## 🟢 Exercice 1 : Facile

### ✅ Solution 1

```text
65 97 233
4 4
4 5
b'\xc3\xa9'
```

- `ord()` donne le numéro du caractère : 65 pour `A` et 97 pour `a`, comme dans la table ASCII; 233 pour `é`, qui n'est pas dans ASCII.
- `"Noël"` a 4 **caractères**, comme `"Noel"`.
- En UTF-8, `"Noel"` prend 4 octets, mais `"Noël"` en prend 5 : le `ë` utilise **2** octets.
- `b'\xc3\xa9'` : les deux octets du `é` en UTF-8 (195 et 169), écrits en hexadécimal.

## 🟡 Exercice 2 : Moyen

### ✅ Solution 2

```python
from pathlib import Path

CHEMIN = Path(__file__).parent / "menu_cafe.txt"

with open(CHEMIN, "w", encoding="utf-8") as fichier:
    fichier.write("Café crème\n")
    fichier.write("Thé à la menthe\n")

with open(CHEMIN, "r", encoding="cp1252") as fichier:
    print("Relu en cp1252 :", fichier.read().strip().replace("\n", " | "))

with open(CHEMIN, "r", encoding="utf-8") as fichier:
    print("Relu en UTF-8  :", fichier.read().strip().replace("\n", " | "))
```

a. En UTF-8, chaque lettre accentuée est écrite avec **2 octets**. La table cp1252 traduit chaque octet séparément : 2 octets donnent 2 caractères (`Ã` et `©` pour le `é`).

b. Non : ses octets sont intacts. Seule la **lecture** a utilisé la mauvaise table; relu en UTF-8, tout redevient correct.

c. VS Code affiche le même charabia (`CafÃ© crÃ¨me`) : il relit les mêmes octets avec la table cp1252. On revient en arrière avec *Reopen with Encoding* → `UTF-8`.
