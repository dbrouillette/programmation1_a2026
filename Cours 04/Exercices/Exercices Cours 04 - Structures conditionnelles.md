# Exercices sur les structures conditionnelles

## Exercice 1

Vérifier si un nombre est pair ou impair. Utiliser l'opérateur ternaire dans votre programme.

## Exercice 2

Afficher si un caractère saisi est une voyelle ou une consonne. Ne pas considérer les caractères accentués comme des voyelles, mais la casse doit être gérée

| Entrée | Sortie |
| :---: | --- |
| `A` | Voyelle |
| `a` | Voyelle |
| `é` | Consonne |
| `8` | Consonne |
| `+` | Consonne |

## Exercice 3

Déterminer la catégorie d'une personne en fonction de son âge :

- Enfant : moins de 12 ans
- Adolescent : 12 à 17 ans
- Adulte : 18 à 64 ans
- Senior : 65 ans et plus

| Entrée | Sortie |
| :---: | --- |
| `-3` | Entrée invalide |
| `0` | Enfant |
| `12` | Adolescent |
| `64` | Adulte |
| `2000` | Senior |

## Exercice 4

Écrire un programme qui demande deux nombres réels à l'utilisateur et l'informe ensuite si leur produit est négatif, positif ou nul.  
**Attention** : votre programme ne peut pas calculer le produit des deux nombres.

| Entrée | Sortie |
| :---: | --- |
| `3` et `2.2` | Le produit est positif |
| `0` et `-5.3` | Le produit est nul |
| `-3` et `-9,45` | Le produit est positif |
| `0,42` et `-2000` | Le produit est négatif |
| `-8.9` et `0,0001` | Le produit est négatif |

## Exercice 5

Affichez le plus grand nombre parmi 3 nombres que l'usager saisit.

| Nombre 1 | Nombre 2 | Nombre 3 | Sortie |
| :---: | :---: | :---: | --- |
| `0` | `-1` | `8` | Le max est `8` |
| `5` | `2` | `5` | Le max est `5` |
| `-2` | `-1` | `-3` | Le max est `-1` |
| `0` | `0` | `0` | Le max est `0` |

## Exercice 6

L'usager saisi les 3 nombres dans un ordre quelconque. Le programme affiche les 3 nombres en ordre croissant.

| Nombre 1 | Nombre 2 | Nombre 3 | Sortie |
| :---: | :---: | :---: | --- |
| `0` | `-1` | `8` | Ordre croissant : `-1, 0, 8` |
| `5` | `2` | `5` | Ordre croissant : `2, 5, 5` |
| `-2` | `-1` | `-3` | Ordre croissant : `-3, -2, -1` |
| `0` | `0` | `0` | Ordre croissant : `0, 0, 0` |

## Exercice 7

Écrire un programme qui demande à l'utilisateur de saisir une année et qui indique si l'année est bissextile. Une année est bissextile si elle est divisible par 400 ou si elle est divisible par 4 mais pas divisible par 100.

| Année | Sortie |
| :---: | --- |
| `2025` | Non bissextile |
| `2024` | Bissextile |
| `2000` | Bissextile |
| `1900` | Non bissextile |
