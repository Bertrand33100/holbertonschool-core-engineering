# Python Fundamentals — Control Flow

## Introduction

Ce chapitre présente le **contrôle du flux d'exécution en Python** (*Control Flow*).

Jusqu'à présent, un programme pouvait principalement exécuter des instructions les unes après les autres. Avec le contrôle du flux, le programme devient capable de :

* prendre des décisions en fonction de conditions ;
* exécuter différentes instructions selon les situations ;
* répéter des instructions ;
* combiner plusieurs conditions ;
* parcourir une série de nombres.

Ce chapitre se concentre exclusivement sur :

* `if`
* `elif`
* `else`
* les opérateurs de comparaison ;
* la logique booléenne ;
* `while` ;
* `for` ;
* `range()`.

---

## Objectifs d'apprentissage

À la fin de ce chapitre, je dois être capable de :

* utiliser correctement `if`, `elif` et `else` ;
* comparer des valeurs avec les opérateurs de comparaison ;
* utiliser `and`, `or` et `not` ;
* créer des boucles avec `while` ;
* créer des boucles avec `for` ;
* utiliser `range()` pour contrôler les répétitions ;
* comprendre les limites de début et de fin d'une boucle ;
* produire une sortie exactement conforme aux exigences d'un exercice ;
* combiner des conditions et des boucles.

---

## 1. Les conditions

Les conditions permettent au programme de prendre une décision.

### `if`

`if` signifie **« si »**.

Il permet d'exécuter un bloc d'instructions lorsqu'une condition est vraie.

```text
if condition:
    instruction
```

### `elif`

`elif` signifie **« sinon si »**.

Il permet de tester une nouvelle condition lorsque la précédente est fausse.

```text
if condition_1:
    instruction
elif condition_2:
    instruction
```

### `else`

`else` signifie **« sinon »**.

Il permet d'exécuter un bloc lorsque toutes les conditions précédentes sont fausses.

```text
if condition:
    instruction
else:
    instruction
```

### Structure générale

```text
if condition_1:
    → premier cas

elif condition_2:
    → deuxième cas

else:
    → dernier cas
```

---

## 2. Les opérateurs de comparaison

Les opérateurs de comparaison permettent de comparer des valeurs.

| Opérateur | Signification       |
| --------- | ------------------- |
| `>`       | supérieur à         |
| `<`       | inférieur à         |
| `>=`      | supérieur ou égal à |
| `<=`      | inférieur ou égal à |
| `==`      | égal à              |
| `!=`      | différent de        |

### Attention à `=` et `==`

C'est une distinction fondamentale en Python.

```text
=
```

sert à **affecter** une valeur.

```text
number = 5
```

signifie :

> mettre la valeur `5` dans la variable `number`.

Alors que :

```text
==
```

sert à **comparer**.

```text
number == 5
```

signifie :

> vérifier si `number` est égal à `5`.

---

## 3. La logique booléenne

Python permet de combiner plusieurs conditions.

Les principaux opérateurs sont :

| Opérateur | Signification                             |
| --------- | ----------------------------------------- |
| `and`     | toutes les conditions doivent être vraies |
| `or`      | au moins une condition doit être vraie    |
| `not`     | inverse le résultat logique               |

### `and`

Les deux conditions doivent être vraies.

```text
condition_1 and condition_2
```

### `or`

Au moins une condition doit être vraie.

```text
condition_1 or condition_2
```

### `not`

Inverse une condition.

```text
not condition
```

---

## 4. La boucle `while`

La boucle `while` permet de répéter des instructions **tant qu'une condition est vraie**.

Logiquement :

```text
TANT QUE la condition est vraie :
    répéter les instructions
```

Le fonctionnement peut être représenté ainsi :

```text
        ┌─────────────┐
        │  Condition  │
        └──────┬──────┘
               │
          ┌────┴────┐
        vraie      fausse
          │           │
          ▼           ▼
      Exécuter       Fin
          │
          └───────────┐
                      │
                      ▼
                  Condition
```

### Point important

Il faut faire attention aux **boucles infinies**.

Si la condition d'un `while` reste toujours vraie, la boucle peut continuer indéfiniment.

Il faut donc comprendre :

```text
condition
    ↓
exécution
    ↓
modification
    ↓
nouvelle vérification
```

---

## 5. La boucle `for`

La boucle `for` permet de parcourir une série de valeurs.

Elle est particulièrement utile lorsque l'on connaît la séquence ou le nombre d'éléments à parcourir.

La logique est :

```text
POUR chaque valeur :
    exécuter les instructions
```

---

## 6. La fonction `range()`

`range()` permet de générer une suite de nombres.

### `range(stop)`

Par exemple :

```text
range(5)
```

correspond aux valeurs :

```text
0
1
2
3
4
```

**5 n'est pas inclus.**

C'est une notion importante à retenir.

### `range(start, stop)`

On peut également définir un début et une limite :

```text
range(2, 6)
```

produit :

```text
2
3
4
5
```

Là encore, la valeur `6` n'est pas incluse.

### `range(start, stop, step)`

Le troisième paramètre permet de définir le pas de progression.

```text
start → valeur de départ
stop  → limite
step  → progression
```

---

# Exercice 0 — Positive anything is better than negative nothing

## Objectif

Le premier exercice permet de mettre en pratique :

* `if` ;
* `elif` ;
* `else` ;
* les comparaisons ;
* `print()` ;
* les variables.

Le programme reçoit un nombre entier aléatoire compris entre `-10` et `10`.

La ligne suivante est imposée par le sujet :

```python
number = __import__('random').randint(-10, 10)
```

Le programme doit ensuite déterminer si le nombre est :

* positif ;
* égal à zéro ;
* négatif.

---

## Logique de l'exercice

La logique à appliquer est :

```text
SI number > 0
    → afficher "<number> is positive"

SINON SI number == 0
    → afficher "<number> is zero"

SINON
    → afficher "<number> is negative"
```

### Exemples

```text
5 is positive
```

```text
0 is zero
```

```text
-4 is negative
```

---

## Structure du projet

Le fichier doit se trouver dans :

```text
holbertonschool-core-engineering/
└── python_fundamentals/
    └── control_flow/
        └── positive_or_negative.py
```

---

## Exigences générales

Les exercices de ce projet doivent respecter les contraintes suivantes :

* environnement de correction : Ubuntu 20.04 LTS ;
* version Python : Python 3.8.x ;
* chaque fichier Python doit commencer par le shebang demandé ;
* chaque fichier doit être exécutable ;
* chaque fichier doit se terminer par une nouvelle ligne ;
* le code doit respecter PEP8 ;
* `pycodestyle` 2.7.x est utilisé pour la vérification du style ;
* aucune bibliothèque externe n'est autorisée ;
* aucune fonction ne doit être créée dans ce projet ;
* aucun import classique ne doit être utilisé ;
* la sortie doit correspondre exactement au résultat attendu.

---

## Vérification

Pour vérifier la syntaxe d'un fichier Python :

```bash
python3 -m py_compile positive_or_negative.py
```

Pour rendre le fichier exécutable :

```bash
chmod +x positive_or_negative.py
```

Pour exécuter le programme :

```bash
./positive_or_negative.py
```

---

## Ce que je dois retenir

### Conditions

```text
if
elif
else
```

permettent au programme de prendre des décisions.

### Comparaisons

```text
>
<
>=
<=
==
!=
```

permettent de comparer des valeurs.

### Logique

```text
and
or
not
```

permettent de combiner ou d'inverser des conditions.

### Boucles

```text
while
```

répète des instructions tant qu'une condition est vraie.

```text
for
```

permet de parcourir une série de valeurs.

### `range()`

`range()` permet de générer une suite de nombres et sa limite finale n'est pas incluse.

---

## Compétences acquises

À travers ce chapitre, je développe ma capacité à :

1. analyser une condition ;
2. transformer une règle en logique informatique ;
3. choisir entre `if`, `elif` et `else` ;
4. comparer correctement des valeurs ;
5. construire des répétitions ;
6. comprendre le fonctionnement d'une boucle ;
7. contrôler les limites d'une séquence ;
8. produire exactement la sortie demandée ;
9. écrire du Python conforme aux contraintes d'un projet Holberton.

---

## Ressources

* Python Documentation — Control Flow Tools
  https://docs.python.org/3/tutorial/controlflow.html

* Python Documentation — Comparisons
  https://docs.python.org/3/reference/expressions.html#comparisons
