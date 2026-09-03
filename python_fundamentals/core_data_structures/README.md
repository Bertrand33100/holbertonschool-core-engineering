# Python - Core Data Structures

## Description

Ce chapitre introduit les principales structures de données disponibles en Python et leur utilisation.

Une structure de données permet de **stocker, organiser, parcourir et manipuler plusieurs valeurs** dans un programme.

Les principales structures étudiées sont :

* **Lists** : listes ordonnées et modifiables
* **Tuples** : séquences ordonnées et non modifiables
* **Sets** : collections de valeurs uniques
* **Dictionaries** : collections de données sous forme `clé: valeur`

Ce chapitre permet également de travailler avec :

* les fonctions ;
* les boucles `for` ;
* le parcours de listes ;
* l'affichage des données ;
* le formatage des valeurs ;
* les méthodes propres aux différentes structures de données.

---

## Objectifs

À la fin de ce chapitre, je dois être capable de :

* créer et utiliser une liste ;
* accéder aux éléments d'une liste ;
* parcourir une liste avec une boucle `for` ;
* créer une fonction qui manipule une liste ;
* afficher les éléments d'une liste ;
* comprendre la différence entre une liste, un tuple, un set et un dictionnaire ;
* choisir une structure de données adaptée à un problème ;
* utiliser correctement les méthodes associées aux structures de données ;
* comprendre la différence entre données **modifiables** et **non modifiables**.

---

# 0. Print a list of integers

## Objectif

Écrire une fonction permettant d'afficher tous les entiers contenus dans une liste.

### Prototype

```python
def print_list_integer(my_list=[]):
```

Chaque entier doit être affiché sur une ligne différente.

### Exemple

Pour :

```python
my_list = [1, 2, 3, 4, 5]
```

le résultat attendu est :

```text
1
2
3
4
5
```

---

## Solution

```python
#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))
```

---

## Explication

### La fonction

```python
def print_list_integer(my_list=[]):
```

`def` permet de créer une fonction.

`my_list` représente la liste reçue en argument.

```python
my_list = [1, 2, 3]
```

La fonction reçoit donc :

```text
[1, 2, 3]
```

---

### La boucle `for`

```python
for number in my_list:
```

La boucle parcourt chaque élément de la liste.

Pour :

```text
[1, 2, 3]
```

Python effectue :

```text
number = 1
number = 2
number = 3
```

À chaque passage dans la boucle, `number` contient l'élément actuel.

---

### Le formatage `:d`

```python
print("{:d}".format(number))
```

`:d` indique que la valeur doit être formatée comme un **entier décimal**.

C'est une exigence particulière du checker de cet exercice.

Même si :

```python
print(number)
```

produit visuellement le même résultat, il faut utiliser explicitement `:d`.

---

# Notions importantes à retenir

## 1. Liste

Une liste permet de stocker plusieurs valeurs dans un ordre précis.

```python
my_list = [10, 20, 30]
```

Les éléments possèdent des positions appelées **indices**.

```text
        10    20    30
index    0     1     2
```

Par exemple :

```python
my_list[0]
```

renvoie :

```text
10
```

---

## 2. Parcourir une liste

La méthode classique consiste à utiliser `for`.

```python
for element in my_list:
    ...
```

Cela signifie :

> Pour chaque élément présent dans `my_list`, effectuer les instructions suivantes.

---

## 3. Fonction

Une fonction regroupe des instructions permettant d'effectuer une tâche.

Structure générale :

```python
def nom_fonction(parametre):
    instruction
```

Exemple :

```python
def print_list_integer(my_list=[]):
    ...
```

La fonction peut ensuite être appelée avec :

```python
print_list_integer([1, 2, 3])
```

---

# Les quatre structures principales

## List

```python
my_list = [1, 2, 3]
```

Caractéristiques :

* ordonnée ;
* modifiable ;
* accepte les doublons ;
* accessible par index.

---

## Tuple

```python
my_tuple = (1, 2, 3)
```

Caractéristiques :

* ordonné ;
* non modifiable ;
* accepte les doublons ;
* accessible par index.

---

## Set

```python
my_set = {1, 2, 3}
```

Caractéristiques :

* valeurs uniques ;
* pas d'accès classique par index ;
* modifiable ;
* utile notamment pour éliminer les doublons.

---

## Dictionary

```python
person = {
    "name": "Bertrand",
    "age": 30
}
```

Le dictionnaire fonctionne avec des associations :

```text
clé → valeur
```

Ici :

```text
"name" → "Bertrand"
"age"  → 30
```

---

# Tableau récapitulatif

| Structure  | Ordonnée    | Modifiable | Doublons     | Accès par index |
| ---------- | ----------- | ---------- | ------------ | --------------- |
| List       | Oui         | Oui        | Oui          | Oui             |
| Tuple      | Oui         | Non        | Oui          | Oui             |
| Set        | Non garanti | Oui        | Non          | Non             |
| Dictionary | Oui*        | Oui        | Clés uniques | Par clé         |

* Les dictionnaires conservent l'ordre d'insertion dans les versions modernes de Python.

---

# Ce que je dois savoir faire

À la fin du chapitre, je dois notamment savoir :

```text
Créer une liste
      ↓
Ajouter / supprimer des éléments
      ↓
Accéder à un élément
      ↓
Parcourir la liste
      ↓
Modifier les éléments
      ↓
Utiliser une fonction avec une liste
      ↓
Choisir la bonne structure de données
```

---

# Points essentiels à mémoriser

### Liste

```python
my_list = [1, 2, 3]
```

### Premier élément

```python
my_list[0]
```

### Dernier élément

```python
my_list[-1]
```

### Parcourir

```python
for element in my_list:
```

### Fonction

```python
def my_function(my_list):
```

### Afficher un entier avec le format demandé

```python
print("{:d}".format(number))
```

---

# Exercice 0 - Checklist

Avant de valider l'exercice, vérifier :

* [ ] Le fichier s'appelle `print_list_integer.py`
* [ ] La fonction s'appelle `print_list_integer`
* [ ] Le prototype est respecté
* [ ] Une boucle `for` parcourt la liste
* [ ] Chaque entier est affiché sur une ligne
* [ ] Le format `:d` est utilisé
* [ ] Le fichier contient le shebang demandé
* [ ] Le fichier est exécutable
* [ ] Le résultat correspond exactement à celui attendu

---

# Commandes Git

Après avoir terminé l'exercice :

```bash
git status
```

Ajouter le fichier :

```bash
git add print_list_integer.py
```

Créer le commit :

```bash
git commit -m "0. Print a list of integers"
```

Envoyer vers GitHub :

```bash
git push
```

---

# Conclusion

L'objectif principal de ce chapitre est de comprendre que Python fournit plusieurs structures permettant de **stocker et manipuler des collections de données**.

Pour l'exercice 0, les trois notions essentielles sont :

```text
FONCTION
   ↓
BOUCLE FOR
   ↓
LISTE
```

La logique à retenir est :

> Je reçois une liste → je parcours chaque élément → j'affiche chaque entier avec le format demandé.
