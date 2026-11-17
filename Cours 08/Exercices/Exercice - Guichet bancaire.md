# Exercice — Guichet bancaire (fichiers CSV)

> 📌 Les comptes doivent être conservés dans un fichier CSV, pour que les données restent disponibles même après avoir fermé le programme.

## 🟡 Énoncé

Écris un programme Python qui simule un guichet automatique. Les comptes (nom du titulaire et solde) sont enregistrés dans un fichier `comptes.csv` avec deux colonnes :

```text
nom,solde
```

Au démarrage, le programme affiche un menu avec les **5 options** suivantes :

```text
1. Ajouter un compte
2. Afficher le solde
3. Déposer
4. Retirer
5. Fermer un compte
```

> 💡 Tu peux ajouter une option `0. Quitter` pour sortir proprement du programme — elle ne compte pas parmi les 5 fonctionnalités demandées.

### Comportement attendu pour chaque option

- **Ajouter un compte** : demande le nom du titulaire et un solde de départ, puis ajoute une nouvelle ligne dans le fichier CSV. Refuse si le nom existe déjà.
- **Afficher le solde** : demande un nom et affiche le solde correspondant, ou un message d'erreur si le compte n'existe pas.
- **Déposer** : demande un nom et un montant, additionne le montant au solde du compte, puis enregistre le changement dans le fichier CSV.
- **Retirer** : demande un nom et un montant. Le retrait est refusé si le compte n'a pas assez de fonds; sinon le solde est mis à jour dans le fichier CSV.
- **Fermer un compte** : demande un nom et retire la ligne correspondante du fichier CSV (le compte n'existe plus par la suite).

### Contraintes

- Le programme doit relire le fichier CSV à chaque opération (ou garder les données synchronisées en mémoire) afin que les informations affichées soient toujours à jour.
- Prévoir les erreurs de base : nom de compte inexistant, montant négatif, fichier CSV absent au premier lancement, etc.

## Exemples d'exécution

**Exemple 1 — Création d'un compte et dépôt**

```text
=== Guichet automatique ===
1. Ajouter un compte
2. Afficher le solde
3. Déposer
4. Retirer
5. Fermer un compte
0. Quitter
Votre choix : 1
Nom du titulaire : Alice
Solde de départ : 100
Compte créé avec succès pour Alice (solde : 100.00$)

Votre choix : 3
Nom du titulaire : Alice
Montant à déposer : 50
Nouveau solde pour Alice : 150.00$

Votre choix : 2
Nom du titulaire : Alice
Le solde de Alice est de 150.00$

Votre choix : 0
Au revoir !
```

**Exemple 2 — Retrait refusé et fermeture de compte**

```text
=== Guichet automatique ===
1. Ajouter un compte
2. Afficher le solde
3. Déposer
4. Retirer
5. Fermer un compte
0. Quitter
Votre choix : 1
Nom du titulaire : Bob
Solde de départ : 20
Compte créé avec succès pour Bob (solde : 20.00$)

Votre choix : 4
Nom du titulaire : Bob
Montant à retirer : 50
Retrait refusé : solde insuffisant (solde actuel : 20.00$)

Votre choix : 4
Nom du titulaire : Bob
Montant à retirer : 20
Nouveau solde pour Bob : 0.00$

Votre choix : 5
Nom du titulaire : Bob
Le compte de Bob a été fermé.

Votre choix : 2
Nom du titulaire : Bob
Erreur : aucun compte trouvé pour Bob

Votre choix : 0
Au revoir !
```
