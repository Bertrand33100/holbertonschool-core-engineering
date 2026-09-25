# Python - Gestion des fichiers

## Introduction

Les entrées et sorties (**Input / Output ou I/O**) sont des concepts fondamentaux en programmation. Elles permettent à un programme d'interagir avec des données externes et de conserver des informations après son exécution.

En Python, la gestion des fichiers permet notamment de :

* Ouvrir un fichier
* Lire un fichier
* Écrire des données dans un fichier
* Ajouter des données à un fichier existant
* Lire un fichier ligne par ligne
* Déplacer le curseur dans un fichier
* Fermer correctement un fichier après son utilisation

Ce projet permet de découvrir les bases de la **manipulation de fichiers en Python** et notamment l'utilisation de l'instruction `with` pour gérer correctement les ressources.

Ces notions sont importantes dans les applications réelles, car les programmes doivent régulièrement enregistrer des résultats, traiter des données externes ou communiquer avec d'autres systèmes.

---

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable de comprendre et d'utiliser :

* Comment ouvrir un fichier
* Comment écrire du texte dans un fichier
* Comment lire le contenu complet d'un fichier
* Comment lire un fichier ligne par ligne
* Comment déplacer le curseur dans un fichier
* Comment s'assurer qu'un fichier est correctement fermé
* Ce qu'est l'instruction `with` et comment l'utiliser

---

## Notions importantes

### 1. Ouvrir un fichier

Python fournit la fonction intégrée `open()` pour accéder à un fichier.

Le principe général est :

```text
open(fichier, mode)
```

Les modes les plus courants sont :

| Mode | Signification               |
| ---- | --------------------------- |
| `r`  | Lire le fichier             |
| `w`  | Écrire dans le fichier      |
| `a`  | Ajouter à la fin du fichier |
| `r+` | Lire et écrire              |

---

### 2. Lire un fichier

Python propose plusieurs méthodes pour lire un fichier.

#### `read()`

La méthode `read()` permet de lire le contenu du fichier.

```text
file.read()
```

Elle peut permettre de récupérer l'ensemble du contenu.

#### `readline()`

La méthode `readline()` permet de lire une ligne.

```text
file.readline()
```

#### Lire ligne par ligne

Un fichier peut également être parcouru avec une boucle :

```text
for line in file:
    ...
```

Cette méthode permet de traiter les lignes une par une.

---

### 3. Écrire dans un fichier

La méthode `write()` permet d'écrire des données dans un fichier.

```text
file.write(...)
```

Le comportement dépend du mode utilisé avec `open()`.

Par exemple :

* `w` écrit dans le fichier et peut remplacer son contenu existant.
* `a` ajoute les nouvelles données à la fin du fichier.

---

## L'instruction `with`

L'instruction `with` est particulièrement importante lorsqu'on travaille avec des fichiers.

Elle permet à Python de gérer automatiquement la fermeture du fichier lorsque le bloc de code est terminé.

Le principe est :

```text
with open(...) as file:
    # travailler avec le fichier

# le fichier est automatiquement fermé ici
```

### Pourquoi utiliser `with` ?

Un fichier est une ressource utilisée par le système.

Si on ouvre un fichier sans correctement le fermer, on peut laisser une ressource ouverte inutilement.

Avec `with`, Python s'occupe automatiquement de la fermeture du fichier lorsque l'on sort du bloc.

Pour la tâche 0 de ce projet, l'utilisation de `with` est obligatoire.

---

## Tâche 0 — Lire un fichier

### Objectif

Créer une fonction :

```text
def read_file(filename=""):
```

Cette fonction doit :

1. Ouvrir un fichier texte encodé en UTF-8.
2. Lire son contenu.
3. Afficher son contenu sur la sortie standard (`stdout`).
4. Utiliser l'instruction `with`.
5. Ne pas importer de module.

La fonction n'a pas besoin de gérer :

* Les erreurs de permissions du fichier.
* Le cas où le fichier n'existe pas.

---

## UTF-8

Le fichier utilisé par la fonction est un fichier texte encodé en **UTF-8**.

UTF-8 est un encodage permettant de représenter de nombreux caractères, notamment les caractères accentués.

Par exemple :

```text
é
è
à
ç
```

---

## `stdout`

`stdout` signifie **standard output**, ou **sortie standard**.

Dans une utilisation normale d'un terminal, la sortie standard correspond généralement à ce qui est affiché à l'écran.

On peut représenter le fonctionnement ainsi :

```text
Programme
    ↓
 stdout
    ↓
Terminal
```

Dans notre exercice, le contenu du fichier doit être envoyé vers `stdout`.

---

## Le curseur dans un fichier

Lorsque Python lit un fichier, il garde une position appelée **curseur du fichier**.

On peut imaginer :

```text
Bonjour Python
^
curseur
```

Après avoir lu une partie du fichier :

```text
Bonjour Python
       ^
     curseur
```

Le curseur avance au fur et à mesure de la lecture.

La méthode `seek()` permet notamment de déplacer ce curseur.

---

## Exigences du projet

### Scripts Python

Les fichiers doivent respecter les règles suivantes :

* Les fichiers sont exécutés avec Python 3.8.5 sur Ubuntu 20.04 LTS.
* Tous les fichiers doivent se terminer par une nouvelle ligne.
* La première ligne de chaque fichier doit être exactement :

```text
#!/usr/bin/env python3
```

* Un fichier `README.md` est obligatoire à la racine du projet.
* Le code doit respecter `pycodestyle` version `2.7.*`.
* Tous les fichiers doivent être exécutables.
* La longueur des fichiers peut être vérifiée avec `wc`.

---

## Ressources

### À lire ou à regarder

* [7.2. Reading and Writing Files](https://intranet.hbtn.io/rltoken/1fWMxb6WgEpLGgEHSlmlXw)
* [8.7. Predefined Clean-up Actions](https://intranet.hbtn.io/rltoken/GGSxHAvz8uhyNxFPmC4AvQ)
* [Dive Into Python 3 — Chapitre 11 : Files](https://intranet.hbtn.io/rltoken/6Go6e4fJASUxr_OkiwVShg)

  * Jusqu'à **11.4 Binary Files**, inclus.
* [Learn to Program 8 — Reading / Writing Files](https://intranet.hbtn.io/rltoken/P9xajlsSkvQJWVyW2ng20Q)

---

## Structure du projet

```text
holbertonschool-core-engineering/
└── python_advanced/
    └── file_handling/
        ├── README.md
        └── read_file.py
```

---

## Dépôt

**Dépôt GitHub :**

```text
holbertonschool-core-engineering
```

**Répertoire du projet :**

```text
python_advanced/file_handling
```

**Fichier principal :**

```text
read_file.py
```

---

## À retenir

Les notions essentielles de ce projet peuvent être résumées ainsi :

```text
open()
   ↓
Ouvrir un fichier
   ↓
read() / readline() / boucle
   ↓
Lire le contenu
   ↓
with
   ↓
Gérer automatiquement le fichier
   ↓
Fichier correctement fermé
```

### Les points les plus importants

* `open()` permet d'ouvrir un fichier.
* `read()` permet de lire son contenu.
* `readline()` permet de lire une ligne.
* `write()` permet d'écrire dans un fichier.
* `seek()` permet de déplacer le curseur.
* `with` permet de gérer correctement l'ouverture et la fermeture du fichier.
* `stdout` correspond à la sortie standard du programme.
* `UTF-8` est un encodage utilisé pour les fichiers texte.

La notion centrale de ce projet est donc la **gestion correcte des fichiers en Python**, notamment grâce à l'instruction `with`.
