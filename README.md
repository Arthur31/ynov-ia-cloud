# ynov-ia-cloud

## Projet disponible à l'adresse suivante

[https://ynov-ia-cloud.herokuapp.com](https://ynov-ia-cloud.herokuapp.com)

## Pour utiliser l'API :

Vous devez imperativement créer un compte, le site vous redirigera sur la page en question.

Les url de la documentation sont soumises au login, il faut donc etre connecté, mais les points d'api ne le sont pas pour permettre d'utiliser simplement postman,
de même la vérification CSRF a été désactivé.


## La documentation:

Chaque point explique comment utiliser le service concerné, ainsi qu'un formulaire d'exemple.

Les differents point marchent sauf OCR où nous avons un problème avec l'exploitation du modèle, il marche dans jupiter mais nous n'arrivons pas à l'exploiter en production.

De même l'api de reconaissance vocale avec Google Cloud Platform ne marche pas, mais le service de Text To Speech marche en partie avec Google.