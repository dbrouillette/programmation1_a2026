# Réponses : Expressions Arithmétiques en Python

Voici les explications et résultats pour chaque expression.

1. `x + y * z - gamma` → 14 + (6 * 3) - 2 = 30
2. `alpha // beta + gamma % z` → 10 // 4 + 2 % 3 = 2 + 2 = 4
3. `delta += epsilon * theta - omega` → 8 + (5 * 7 - 9) = 8 + 26 = 34
4. `omega //= x - y + z` → 9 // (14 - 6 + 3) = 9 // 11 = 0
5. `beta %= gamma + epsilon - theta` → 4 % (2 + 5 - 7) = 4 % 0 → Erreur (`ZeroDivisionError`, division par zéro — **le programme plante ici**; `beta` conserve donc sa dernière valeur valide (4) pour la suite de l'exercice)
6. `alpha += 1` puis `alpha + beta * gamma - delta` → alpha devient 11 → 11 + 4 * 2 - 34 = 11 + 8 - 34 = -15
7. `omega - epsilon + theta * z` (avant décrémentation) puis `omega -= 1` → omega vaut 0 (depuis l'étape 4) → 0 - 5 + 7 * 3 = -5 + 21 = 16 (omega devient ensuite -1)
8. `x *= y + z - gamma` → 14 * (6 + 3 - 2) = 14 * 7 = 98
9. `(alpha + beta) * (gamma - delta % epsilon)` → (11 + 4) * (2 - 34 % 5) = 15 * (2 - 4) = 15 * -2 = -30
10. `y -= 1` puis `x + y * z % alpha - beta // gamma` puis `x += 1` → y devient 5 → 98 + (5 * 3 % 11) - (4 // 2) = 98 + 4 - 2 = 100 (x devient ensuite 99)

## 💡 Pourquoi diviser certaines lignes en deux instructions?

Puisque Python n'a pas de `++` / `--`, chaque incrémentation/décrémentation « pré » ou « post » doit être écrite explicitement, **placée avant ou après** l'instruction qui utilise la variable :

- **Pré-incrémentation/décrémentation** (`++alpha`, `--y`) → écrire `alpha += 1` **avant** la ligne qui l'utilise.
- **Post-incrémentation/décrémentation** (`omega--`, `x++`) → écrire `omega -= 1` **après** la ligne qui l'utilise.

C'est en fait **plus explicite**, puisque l'ordre des opérations est directement visible dans le code plutôt que caché dans un symbole.
