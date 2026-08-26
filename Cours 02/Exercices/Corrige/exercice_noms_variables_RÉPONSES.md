# Réponses : Validité des noms de variables Python

1. `taux_de_reussite` — Valide ✅ : nom descriptif, commence par une lettre, respecte le `snake_case`.
2. `$montant_total` — Invalide ❌ : le symbole `$` n'est **jamais** autorisé dans un nom de variable Python, peu importe sa position.
3. `@valeur` — Invalide ❌ : commence par un caractère spécial non autorisé.
4. `class` — Invalide ❌ : `class` est un mot réservé du langage Python.
5. `nom étudiant` — Invalide ❌ : contient un espace, ce qui est interdit. Les accents sont à proscrire aussi.
6. `_compteur` — Valide ✅ : commence par un underscore, ce qui est autorisé.
7. `nombre_etudiants` — Valide ✅ : commence par une lettre et respecte la convention `snake_case` (et non `camelCase`).
8. `1er_etudiant` — Invalide ❌ : commence par un chiffre, ce qui est interdit.
9. `taux-de-reussite` — Invalide ❌ : contient des tirets, qui ne sont pas autorisés (le tiret est interprété comme l'opérateur de soustraction).
10. `valeur1` — Valide ✅ : combinaison de lettres et chiffres, commence par une lettre. Mais n'est pas 100% significatif...
