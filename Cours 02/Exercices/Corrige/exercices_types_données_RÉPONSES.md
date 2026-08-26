# RÉPONSES - Exercices sur les types de données

|Variable|Type (réponses variables)|Nom (réponses variables)|
|---|---|---|
|1. Le salaire horaire|`float`|`salaire_horaire`|
|2. Le prénom du client|`str`|`prenom_client`|
|3. Un code postal|`str`|`code_postal`|
|4. L'âge d'une personne|`int`|`age`|
|5. Le montant total d'une facture|`float`|`total`|
|6. La date courante|`str`|`date`|
|7. Le genre de quelqu'un|`str`|`genre`|
|8. Le statut de retraité d'un travailleur|`bool`|`est_retraite`|
|9. Un nombre de billes|`int`|`nb_billes`|
|10. L'adresse de l'étudiant|`str`|`adresse_etu`|
|11. Une note au bulletin|`int`|`note_bulletin`|
|12. Le nombre d'étoiles dans l'univers|`int`|`nb_etoiles_univers`|

## 💡 Choix de types à retenir

- **Le code postal, la date et le genre** utilisent `str` plutôt qu'un type numérique spécial : Python n'a pas de type `char`, donc même un seul caractère se représente avec `str`.
- **L'âge et la note au bulletin** utilisent `int` plutôt que `byte` : Python n'a qu'un seul type entier, sans distinction de taille en mémoire.
- **Le nombre d'étoiles dans l'univers**, malgré sa très grande valeur, reste un `int` en Python (pas besoin d'un équivalent à `long`) : la taille des entiers en Python s'ajuste automatiquement, sans limite fixe.
