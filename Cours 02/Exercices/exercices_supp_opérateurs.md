# Exercices : Expressions Arithmétiques en Python

Voici 10 expressions arithmétiques complexes en Python. Identifiez le résultat ou expliquez le fonctionnement de chaque expression.

**ATTENTION** : les résultats sont cumulatifs, alors ils doivent être faits DANS l'ORDRE proposé!

*Note : Python n'a pas de `++` / `--`. Pour simuler une pré/post-incrémentation, ce code utilise plutôt `+= 1` ou `-= 1` placé **avant** ou **après** l'expression qui utilise la variable.*

```python
x = 14
y = 6
z = 3
alpha = 10
beta = 4
gamma = 2
delta = 8
epsilon = 5
theta = 7
omega = 9

# 1
result1 = x + y * z - gamma

# 2
result2 = alpha // beta + gamma % z

# 3
delta += epsilon * theta - omega

# 4
omega //= x - y + z

# 5
beta %= gamma + epsilon - theta

# 6
alpha += 1  # équivalent de ++alpha (incrémentation AVANT utilisation)
result3 = alpha + beta * gamma - delta

# 7
result4 = omega - epsilon + theta * z  # on utilise omega avant de le décrémenter
omega -= 1  # équivalent de omega-- (décrémentation APRÈS utilisation)

# 8
x *= y + z - gamma

# 9
result5 = (alpha + beta) * (gamma - delta % epsilon)

# 10
y -= 1  # équivalent de --y (décrémentation AVANT utilisation)
result6 = x + y * z % alpha - beta // gamma
x += 1  # équivalent de x++ (incrémentation APRÈS utilisation, visible pour la suite)
```
