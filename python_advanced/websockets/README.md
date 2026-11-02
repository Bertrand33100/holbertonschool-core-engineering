# Communication en temps réel avec WebSockets

## Description

Ce projet fait partie du programme **Python Advanced de Holberton School**.

Il a pour objectif de découvrir la communication en temps réel entre un client et un serveur grâce au protocole **WebSockets** et à la programmation asynchrone en Python.

Contrairement au protocole HTTP traditionnel, qui fonctionne sur un modèle requête-réponse, WebSockets établit une connexion persistante et bidirectionnelle.

Cela permet au client et au serveur d'échanger des messages à tout moment, sans avoir à recréer une connexion à chaque échange.

## Objectifs pédagogiques

À la fin de ce projet, je souhaite être capable de :

- Comprendre les différences entre HTTP et WebSockets.
- Créer un serveur WebSocket avec Python.
- Comprendre la programmation asynchrone avec `async` et `await`.
- Gérer plusieurs connexions clientes simultanément.
- Envoyer et recevoir des messages en temps réel.
- Mettre en place le routage et la validation des messages.
- Intégrer WebSockets dans une interface web.

## Technologies utilisées

- Python 3
- Bibliothèque WebSockets
- Asyncio
- Programmation asynchrone
- Git et GitHub

## Structure du projet

```text
python_advanced/
└── websockets/
    ├── README.md
    └── echo_server.py
```

## Exercices

### 0. Serveur WebSocket

**Fichier :** `echo_server.py`

Le premier exercice consiste à créer un serveur WebSocket capable de recevoir des messages et de les renvoyer à leur expéditeur.

Le serveur doit :

- Écouter sur le port `8765`.
- Accepter plusieurs connexions clientes.
- Recevoir des messages textuels.
- Renvoyer exactement le même message au client.
- Maintenir la connexion ouverte pour permettre des échanges continus.

**Comportement attendu :**

Lorsque le client envoie :

```text
Bonjour
```

Le serveur doit répondre :

```text
Bonjour
```

Le message doit être renvoyé sans aucune modification.

### Lancement du serveur

Pour démarrer le serveur, utiliser la commande :

```bash
python3 echo_server.py
```

Pour se connecter au serveur avec le client WebSocket :

```bash
websockets ws://localhost:8765/
```

## Exigences générales

- Tous les fichiers Python doivent commencer par le shebang Python 3.
- Le code doit respecter les conventions PEP 8.
- Utiliser la bibliothèque `websockets`.
- Utiliser la programmation asynchrone (`async` / `await`).
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- Respecter précisément les consignes de chaque exercice.

## Méthode d'apprentissage

Ce projet est réalisé progressivement afin de comprendre chaque notion avant de passer à la pratique.

Les étapes de travail sont :

1. Comprendre les concepts théoriques.
2. Apprendre les bases de la programmation asynchrone.
3. Développer chaque fonctionnalité étape par étape.
4. Tester le fonctionnement du programme.
5. Comprendre et corriger les erreurs.
6. Devenir progressivement autonome dans l'écriture du code.
