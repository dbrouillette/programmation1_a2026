# Exercices — Les conditions imbriquées (fiche 4.3)

## 🟢 Exercice 1 : Facile

**But** : Reproduire une imbrication à 2 niveaux.

**Énoncé** : Écris un programme qui demande l'âge de l'utilisateur et s'il possède un permis de conduire (`True`/`False`).

- Si l'âge est de 18 ans ou plus :
  - Si l'utilisateur a un permis, affiche : *"Vous pouvez conduire"*.
  - Sinon, affiche : *"Vous ne pouvez pas conduire sans permis"*.
- Sinon (moins de 18 ans), affiche : *"Vous êtes mineur"*.

## 🟡 Exercice 2 : Moyen

**But** : Imbriquer une condition qui ne s'applique que dans un cas précis.

**Énoncé** : Écris un programme qui demande l'âge d'un visiteur pour l'entrée d'un parc d'attractions.

- Si l'âge est inférieur à 12 ans :
  - Demande si le visiteur est accompagné d'un adulte (`True`/`False`).
  - Si oui, affiche : *"Entrée autorisée"*.
  - Si non, affiche : *"Entrée refusée : accompagnement requis"*.
- Sinon (12 ans et plus), affiche directement : *"Entrée autorisée"* (sans poser la question de l'accompagnement).

## 🟡 Exercice 3 : Moyen

**But** : Valider deux critères imbriqués avec des messages distincts à chaque niveau.

**Énoncé** : Pour valider la réussite d'un cours, écris un programme qui demande le taux de présence (en %) et la note finale (sur 100).

- Si le taux de présence est d'au moins 80% :
  - Si la note est d'au moins 60, affiche : *"Cours réussi"*.
  - Sinon, affiche : *"Cours échoué : note insuffisante"*.
- Sinon, affiche : *"Cours échoué : présence insuffisante"*.

## 🔴 Exercice 4 : Moyen-Difficile

**But** : Imbriquer la vérification de deux règles indépendantes sur un mot de passe.

**Énoncé** : Écris un programme qui demande un mot de passe et vérifie, de façon imbriquée :

- D'abord, si le mot de passe contient au moins 8 caractères. Si non, affiche : *"Mot de passe trop court"* (et arrête là).
- Sinon, vérifie s'il contient au moins un chiffre (indice : parcourir les caractères et utiliser `.isdigit()`, ou `any(c.isdigit() for c in mot_de_passe)`).
  - Si oui, affiche : *"Mot de passe valide"*.
  - Sinon, affiche : *"Le mot de passe doit contenir au moins un chiffre"*.

## 🔴 Exercice 5 : Difficile

**But** : Simuler un système de connexion à 2 niveaux de vérification, avec un message distinct pour chaque échec possible.

**Énoncé** : Écris un programme qui demande un identifiant et un mot de passe, puis les compare aux valeurs attendues (`identifiant_attendu = "prof2026"`, `mot_de_passe_attendu = "python!"`).

- Si l'identifiant est correct :
  - Si le mot de passe est également correct, affiche : *"Connexion réussie"*.
  - Sinon, affiche : *"Mot de passe incorrect"*.
- Sinon, affiche : *"Identifiant incorrect"* (sans même vérifier le mot de passe).
