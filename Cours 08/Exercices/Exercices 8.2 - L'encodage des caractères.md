# Exercices — L'encodage des caractères (fiche 8.2)

> 📌 **À savoir** : Python Tutor ne gère pas les fichiers. Fais ces exercices dans VS Code.

## 🟢 Exercice 1 : Facile

**But** : Voir les octets derrière les caractères.

**Énoncé** : Sans exécuter le code, prévois ce qu'affiche chaque ligne. Vérifie ensuite dans VS Code.

```python
print(ord("A"), ord("a"), ord("é"))
print(len("Noel"), len("Noël"))
print(len("Noel".encode("utf-8")), len("Noël".encode("utf-8")))
print("é".encode("utf-8"))
```

> 💡 `len()` compte les **caractères** d'une chaîne, mais les **octets** d'un résultat de `encode()`.

## 🟡 Exercice 2 : Moyen

**But** : Provoquer un problème d'encodage pour le reconnaître.

**Énoncé** : Écris un programme qui :

1. écrit les deux lignes `Café crème` et `Thé à la menthe` dans `menu_cafe.txt`, en **UTF-8**;
2. relit le fichier en **cp1252** et affiche son contenu sur une ligne;
3. relit le fichier en **UTF-8** et affiche son contenu sur une ligne.

*Sortie attendue :*

```text
Relu en cp1252 : CafÃ© crÃ¨me | ThÃ© Ã  la menthe
Relu en UTF-8  : Café crème | Thé à la menthe
```

Réponds ensuite aux questions :

a. Pourquoi chaque lettre accentuée devient-elle **deux** caractères à la deuxième ligne?

b. Le fichier `menu_cafe.txt` est-il abîmé?

c. Dans VS Code, ouvre `menu_cafe.txt` et rouvre-le avec l'encodage `Western (Windows 1252)`. Que vois-tu?

## Solutions

➡️ Les solutions se trouvent dans [Solutions 8.2 - L'encodage des caractères](Solutions%208.2%20-%20L%27encodage%20des%20caract%C3%A8res.md).
