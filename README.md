# Python - Environment & First Programs

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![PEP 8](https://img.shields.io/badge/code%20style-PEP8-brightgreen)
![Holberton School](https://img.shields.io/badge/Holberton%20School-Project-red)

## Description

Ce chapitre constitue une introduction à l'environnement Python et aux premiers programmes.

L'objectif est de comprendre comment Python exécute du code, aussi bien **interactivement avec l'interpréteur (REPL)** qu'à partir de **fichiers scripts**.

Le chapitre aborde également l'installation d'outils avec `pip`, les problèmes liés aux installations globales et l'utilisation des **environnements virtuels (`venv`)** pour isoler les dépendances.

---

## Objectifs d'apprentissage

À la fin de ce chapitre, je dois être capable de :

* Comprendre le fonctionnement de l'interpréteur Python.
* Faire la différence entre une **expression** et une **instruction**.
* Comprendre pourquoi certaines expressions affichent automatiquement leur résultat dans le REPL.
* Comprendre le rôle de `print()`.
* Créer et exécuter un script Python.
* Utiliser le **shebang** `#!/usr/bin/env python3`.
* Rendre un fichier Python exécutable.
* Installer un outil Python avec `pip`.
* Comprendre les problèmes liés aux installations globales.
* Comprendre le principe d'un environnement virtuel.
* Créer et utiliser un environnement avec `venv`.
* Vérifier la conformité du code avec `pycodestyle`.
* Respecter les conventions **PEP 8**.

---

# 1. L'interpréteur Python

Python peut être utilisé directement depuis un terminal grâce à son interpréteur interactif.

Pour démarrer :

```bash
python3
```

On obtient alors une invite similaire à :

```text
>>>
```

Cette interface est appelée **REPL** :

* **Read** : Python lit l'entrée.
* **Eval** : Python évalue l'expression.
* **Print** : Python affiche éventuellement le résultat.
* **Loop** : Python recommence.

Exemple :

```python
>>> 2 + 3
5
```

Le résultat est affiché automatiquement parce que `2 + 3` est une expression évaluée par l'interpréteur interactif.

---

# 2. Expressions et instructions

Une notion importante de ce chapitre est la différence entre une **expression** et une **instruction**.

## Expression

Une expression peut être évaluée pour produire une valeur.

Exemples :

```python
2 + 3
```

```python
10 > 5
```

```python
"Hello"
```

Dans le REPL, Python peut afficher automatiquement le résultat d'une expression.

Exemple :

```python
>>> 10 > 5
True
```

---

## Instruction

Une instruction demande à Python d'effectuer une action.

Par exemple, une affectation :

```python
x = 10
```

Dans le REPL :

```python
>>> x = 10
>>>
```

Python n'affiche pas automatiquement `10`.

Cependant, si on entre ensuite :

```python
>>> x
10
```

Python affiche la valeur de la variable.

---

# 3. Le rôle de `print()`

`print()` permet d'afficher explicitement une information.

Exemple :

```python
>>> x = 10
>>> print(x)
10
```

La différence essentielle est donc :

| Situation                     | Résultat                                        |
| ----------------------------- | ----------------------------------------------- |
| Expression seule dans le REPL | Résultat éventuellement affiché automatiquement |
| Affectation d'une variable    | Pas d'affichage automatique                     |
| `print()`                     | Affichage demandé explicitement                 |

Cette distinction est importante lorsque l'on passe du REPL à l'exécution de scripts.

---

# 4. Python en mode interactif vs script

Python peut principalement être utilisé de deux manières.

### Mode interactif

```bash
python3
```

Puis :

```python
>>> 2 + 2
4
```

Le code est exécuté immédiatement.

### Mode script

On écrit le code dans un fichier, par exemple :

```text
script.py
```

Puis on l'exécute :

```bash
python3 script.py
```

Dans un script, une expression seule n'est généralement pas affichée automatiquement.

Pour afficher une valeur, il faut explicitement utiliser :

```python
print()
```

---

# 5. Le shebang

Un fichier Python destiné à être exécuté directement doit commencer par :

```python
#!/usr/bin/env python3
```

Cette ligne est appelée **shebang**.

Elle indique au système quel interpréteur doit être utilisé pour exécuter le fichier.

Le projet demande que chaque fichier Python commence exactement par :

```python
#!/usr/bin/env python3
```

---

# 6. Rendre un script exécutable

Un fichier peut être rendu exécutable avec :

```bash
chmod +x nom_du_fichier.py
```

On peut ensuite l'exécuter directement :

```bash
./nom_du_fichier.py
```

Le shebang permet alors au système de savoir qu'il doit utiliser Python 3.

---

# 7. `pip`

`pip` est l'outil utilisé pour installer des paquets Python.

Exemple :

```bash
pip install pycodestyle
```

Dans certains environnements, on peut utiliser :

```bash
pip3 install pycodestyle
```

`pip` permet notamment d'installer des outils qui ne font pas partie de la bibliothèque standard Python.

---

# 8. Pourquoi éviter les installations globales ?

Installer des paquets directement dans l'environnement global peut provoquer des conflits.

Par exemple :

```text
Projet A
   └── version 1 d'une dépendance

Projet B
   └── version 2 de la même dépendance
```

Si les deux projets utilisent le même environnement Python global, une version peut entrer en conflit avec l'autre.

Cela peut rendre les projets difficiles à maintenir et à reproduire.

---

# 9. Les environnements virtuels

Python fournit le module `venv` permettant de créer des environnements virtuels.

Un environnement virtuel permet d'isoler :

* les paquets installés ;
* leurs versions ;
* les dépendances d'un projet.

Schéma :

```text
Ordinateur
│
├── Python système
│
├── Projet A
│   └── environnement virtuel
│       ├── dépendance X v1
│       └── dépendance Y v2
│
└── Projet B
    └── environnement virtuel
        ├── dépendance X v3
        └── dépendance Z v1
```

Les projets peuvent ainsi utiliser des versions différentes sans nécessairement entrer en conflit.

---

# 10. Création d'un environnement virtuel

Un environnement virtuel peut être créé avec :

```bash
python3 -m venv venv
```

Ici :

* `python3` → utilise Python 3 ;
* `-m` → demande à Python d'exécuter un module ;
* `venv` → module permettant de créer un environnement virtuel ;
* `venv` → nom du dossier créé.

---

# 11. Activation de l'environnement virtuel

Sous Linux/Ubuntu :

```bash
source venv/bin/activate
```

Lorsque l'environnement est actif, le terminal indique généralement son nom :

```text
(venv) user@computer:~$
```

Les installations effectuées avec `pip` sont alors associées à cet environnement.

---

# 12. Désactivation

Pour quitter l'environnement virtuel :

```bash
deactivate
```

On revient alors à l'environnement Python précédent.

---

# 13. `pycodestyle` et PEP 8

Le projet demande que le code respecte **PEP 8**, le guide de style officiel pour Python.

`pycodestyle` permet de vérifier certaines règles de style.

Exemple :

```bash
pycodestyle fichier.py
```

Si aucune erreur n'est retournée, le fichier respecte les règles vérifiées par l'outil.

Le projet utilise :

```text
pycodestyle 2.7.x
```

---

# 14. Exigences générales du projet

Les fichiers Python doivent respecter plusieurs règles.

### Version Python

L'environnement de correction utilise :

```text
Python 3.8.x
```

### Shebang obligatoire

Chaque fichier Python doit commencer exactement par :

```python
#!/usr/bin/env python3
```

### Fichier exécutable

Les scripts doivent être exécutables :

```bash
chmod +x fichier.py
```

### Fin de fichier

Chaque fichier doit se terminer par une nouvelle ligne.

### Style

Le code doit être conforme à **PEP 8** et vérifiable avec `pycodestyle`.

### Sortie

Les sorties demandées par les exercices doivent être reproduites exactement.

### Bibliothèques externes

Aucune bibliothèque externe ne doit être utilisée sauf lorsqu'elle est explicitement demandée.

---

# 15. Commandes importantes

| Commande                   | Utilité                           |
| -------------------------- | --------------------------------- |
| `python3`                  | Lance l'interpréteur Python       |
| `python3 fichier.py`       | Exécute un script Python          |
| `chmod +x fichier.py`      | Rend un fichier exécutable        |
| `./fichier.py`             | Exécute directement un script     |
| `pip install ...`          | Installe un paquet Python         |
| `python3 -m venv venv`     | Crée un environnement virtuel     |
| `source venv/bin/activate` | Active l'environnement virtuel    |
| `deactivate`               | Désactive l'environnement virtuel |
| `pycodestyle fichier.py`   | Vérifie le style du code          |

---

# 16. Ce que je dois retenir

## Interpréteur

```text
python3
   ↓
REPL
   ↓
lecture → évaluation → affichage éventuel → répétition
```

## Expression

Une expression produit une valeur.

```python
2 + 2
```

Résultat dans le REPL :

```text
4
```

## Affectation

Une affectation stocke une valeur dans une variable.

```python
x = 4
```

Elle ne provoque pas automatiquement l'affichage de `4`.

## `print()`

Permet de demander explicitement un affichage :

```python
print(x)
```

## Script

Un fichier `.py` contient du code Python qui peut être exécuté avec :

```bash
python3 fichier.py
```

## Shebang

```python
#!/usr/bin/env python3
```

Permet notamment d'indiquer l'interpréteur utilisé lorsqu'un script est exécuté directement.

## `pip`

Permet d'installer des paquets Python.

## `venv`

Permet de créer un environnement Python isolé pour un projet.

---

# 17. Ressources officielles

* **Python Documentation — Using the Interpreter**
  https://docs.python.org/3/tutorial/interpreter.html

* **Python Documentation — `venv`**
  https://docs.python.org/3/library/venv.html

* **pip Documentation — User Guide**
  https://pip.pypa.io/en/stable/user_guide/

* **pycodestyle Documentation**
  https://pycodestyle.pycqa.org/

---

# Conclusion

Ce chapitre pose les bases de l'utilisation professionnelle de Python.

Les notions essentielles à maîtriser sont :

```text
Python
│
├── Interpréteur / REPL
│   ├── Expressions
│   ├── Instructions
│   └── print()
│
├── Scripts Python
│   ├── .py
│   ├── shebang
│   └── exécution
│
├── Gestion des paquets
│   └── pip
│
└── Isolation des dépendances
    └── venv
```

La compréhension de ces concepts constitue la base nécessaire pour commencer à développer des programmes Python plus complexes.
