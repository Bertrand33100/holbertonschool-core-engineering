# Python - Classes & Object Model

## 1. Introduction

En Python, **tout est un objet**.

Un objet possède principalement :

* une **identité** ;
* un **type** ;
* des **données** ;
* des **méthodes** permettant de réaliser des actions.

Exemples :

```python
number = 42
text = "hello"
numbers = [1, 2, 3]
```

Ces trois variables contiennent des objets appartenant à des classes différentes :

```python
type(number)   # int
type(text)     # str
type(numbers)  # list
```

L'objectif de ce chapitre est d'apprendre à créer nos propres classes et nos propres objets.

---

# 2. Classe et instance

## Classe

Une **classe** est un modèle permettant de créer des objets.

```python
class Person:
    """Représente une personne."""
```

La classe décrit ce que les objets pourront contenir et faire.

## Instance

Une **instance** est un objet créé à partir d'une classe.

```python
person = Person()
```

Ici :

* `Person` → classe
* `person` → instance

On peut créer plusieurs instances à partir de la même classe :

```python
person1 = Person()
person2 = Person()
```

`person1` et `person2` sont deux objets différents créés à partir du même modèle.

### À retenir

> **Classe = modèle**
> **Instance = objet créé à partir du modèle**

---

# 3. Créer une classe

Syntaxe :

```python
class Dog:
    """Représente un chien."""
```

Le mot-clé `class` permet de créer une classe.

Par convention, le nom d'une classe commence par une majuscule :

```python
class User:
    pass
```

Puis :

```python
user = User()
```

---

# 4. La méthode `__init__`

`__init__` est appelée automatiquement lors de la création d'une instance.

Elle permet notamment d'initialiser les attributs de l'objet.

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name, age):
        """Initialise un utilisateur."""
        self.name = name
        self.age = age
```

Création d'un objet :

```python
user = User("Bertrand", 30)
```

L'objet possède maintenant :

```python
user.name
user.age
```

---

# 5. `self`

`self` représente **l'instance actuelle**.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name):
        """Initialise l'utilisateur."""
        self.name = name
```

Lorsque l'on fait :

```python
user1 = User("Alice")
user2 = User("Bob")
```

Python associe :

```text
user1 → self
user2 → self
```

Ainsi :

```python
user1.name
```

contient :

```text
Alice
```

et :

```python
user2.name
```

contient :

```text
Bob
```

### À retenir

> `self` permet à une méthode d'accéder aux données de l'instance actuelle.

---

# 6. Les attributs

Un **attribut** est une donnée appartenant à un objet.

Exemple :

```python
class Car:
    """Représente une voiture."""

    def __init__(self, brand, color):
        """Initialise la voiture."""
        self.brand = brand
        self.color = color
```

Création :

```python
car = Car("Toyota", "blue")
```

Attributs :

```python
car.brand
car.color
```

Résultat :

```text
Toyota
blue
```

On peut donc représenter l'objet ainsi :

```text
Car
│
├── brand = "Toyota"
└── color = "blue"
```

---

# 7. Les méthodes

Une **méthode** est une fonction définie à l'intérieur d'une classe.

Elle permet de définir le comportement d'un objet.

```python
class Dog:
    """Représente un chien."""

    def bark(self):
        """Fait aboyer le chien."""
        print("Woof!")
```

Utilisation :

```python
dog = Dog()
dog.bark()
```

Résultat :

```text
Woof!
```

### Différence

```text
Attribut → ce que l'objet possède
Méthode  → ce que l'objet peut faire
```

Exemple :

```text
Voiture
│
├── couleur      → attribut
├── marque       → attribut
│
├── démarrer()   → méthode
└── arrêter()    → méthode
```

---

# 8. `type()`

`type()` permet de connaître la classe d'un objet.

```python
number = 42
text = "hello"
numbers = [1, 2, 3]

type(number)
type(text)
type(numbers)
```

Résultat :

```text
<class 'int'>
<class 'str'>
<class 'list'>
```

Donc :

```text
42          → int
"hello"     → str
[1, 2, 3]   → list
```

Pour une classe personnelle :

```python
class User:
    """Représente un utilisateur."""

user = User()

type(user)
```

Résultat :

```text
<class '__main__.User'>
```

---

# 9. `id()`

`id()` permet d'obtenir l'identité d'un objet.

```python
number = 42

id(number)
```

Python retourne un identifiant entier correspondant à l'identité de cet objet pendant son existence.

Deux objets peuvent avoir le même contenu tout en étant deux objets différents.

Exemple :

```python
list_a = [1, 2]
list_b = [1, 2]
```

Les contenus sont identiques :

```python
list_a == list_b
```

Résultat :

```text
True
```

Mais ce sont deux objets distincts :

```python
list_a is list_b
```

Résultat :

```text
False
```

### À retenir

> `==` compare les valeurs.
> `is` vérifie l'identité des objets.

---

# 10. `dir()`

`dir()` permet d'obtenir les noms des attributs et méthodes accessibles sur un objet.

Exemple :

```python
text = "hello"

dir(text)
```

On peut ensuite utiliser certaines méthodes :

```python
text.upper()
```

Résultat :

```text
HELLO
```

Ou :

```python
text.replace("h", "H")
```

Résultat :

```text
Hello
```

---

# 11. Encapsulation

L'encapsulation consiste à contrôler la manière dont les données d'un objet sont utilisées.

En Python, on peut utiliser la convention `_attribut` pour signaler qu'un attribut est destiné à un usage interne.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name):
        """Initialise l'utilisateur."""
        self._name = name
```

Le `_` indique généralement :

> « Cet attribut est destiné à être utilisé en interne. »

Python ne rend cependant pas automatiquement cet attribut réellement privé.

---

# 12. Validation des données

Une classe peut vérifier les données reçues lors de la création d'un objet.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, age):
        """Initialise et valide l'âge."""
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self.age = age
```

Ainsi :

```python
user = User(25)
```

fonctionne.

Mais :

```python
user = User(-5)
```

provoque une `ValueError`.

### Principe

```text
Donnée reçue
     ↓
Validation
     ↓
Valide ? ── Oui ──→ création de l'objet
     │
     Non
     ↓
Exception
```

---

# 13. Getter et Setter

Les getters et setters permettent de contrôler l'accès aux données.

## Getter

Un getter permet de **lire** une donnée.

## Setter

Un setter permet de **modifier** une donnée, éventuellement après validation.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, age):
        """Initialise l'utilisateur."""
        self._age = age

    def get_age(self):
        """Retourne l'âge."""
        return self._age

    def set_age(self, age):
        """Modifie l'âge après validation."""
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self._age = age
```

Utilisation :

```python
user = User(25)

user.get_age()
```

Puis :

```python
user.set_age(30)
```

---

# 14. Méthodes spéciales

Python possède des méthodes spéciales reconnaissables par leur double underscore :

```text
__init__
__str__
__repr__
```

Elles permettent de définir certains comportements particuliers des objets.

---

# 15. `__init__`

`__init__` initialise l'objet après sa création.

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name):
        """Initialise l'utilisateur."""
        self.name = name
```

Puis :

```python
user = User("Alice")
```

Python appelle automatiquement `__init__`.

---

# 16. `__str__`

`__str__` définit une représentation lisible de l'objet lorsqu'on utilise `print()`.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name):
        """Initialise l'utilisateur."""
        self.name = name

    def __str__(self):
        """Retourne une représentation lisible."""
        return self.name
```

Puis :

```python
user = User("Alice")
print(user)
```

Résultat :

```text
Alice
```

---

# 17. `__repr__`

`__repr__` permet de définir une représentation destinée notamment à être utile pour identifier l'objet lors du développement et du débogage.

Exemple :

```python
class User:
    """Représente un utilisateur."""

    def __init__(self, name):
        """Initialise l'utilisateur."""
        self.name = name

    def __repr__(self):
        """Retourne une représentation de l'objet."""
        return "User({!r})".format(self.name)
```

---

# 18. Résumé des fonctions importantes

| Fonction / méthode | Utilité                                                        |
| ------------------ | -------------------------------------------------------------- |
| `class`            | Créer une classe                                               |
| `__init__`         | Initialiser une instance                                       |
| `self`             | Référence vers l'instance actuelle                             |
| `type()`           | Connaître le type/classe d'un objet                            |
| `id()`             | Obtenir l'identité d'un objet                                  |
| `dir()`            | Explorer les attributs et méthodes disponibles                 |
| `__str__`          | Définir une représentation lisible                             |
| `__repr__`         | Définir une représentation destinée notamment au développement |
| `raise`            | Déclencher une exception                                       |

---

# 19. Vocabulaire essentiel

| Terme         | Définition                                      |
| ------------- | ----------------------------------------------- |
| Classe        | Modèle permettant de créer des objets           |
| Instance      | Objet créé à partir d'une classe                |
| Objet         | Entité manipulée par Python                     |
| Attribut      | Donnée associée à un objet                      |
| Méthode       | Fonction définie dans une classe                |
| `self`        | Instance actuelle                               |
| `__init__`    | Méthode d'initialisation                        |
| Encapsulation | Organisation et contrôle de l'accès aux données |
| Getter        | Méthode permettant de lire une donnée           |
| Setter        | Méthode permettant de modifier une donnée       |
| `__str__`     | Représentation lisible de l'objet               |
| `__repr__`    | Représentation utile au développement           |

---

# 20. Exemple complet

```python
#!/usr/bin/env python3

class User:
    """Représente un utilisateur."""

    def __init__(self, name, age):
        """Initialise un utilisateur."""
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")

        self.name = name
        self._age = age

    def get_age(self):
        """Retourne l'âge de l'utilisateur."""
        return self._age

    def set_age(self, age):
        """Modifie l'âge après validation."""
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self._age = age

    def __str__(self):
        """Retourne une représentation lisible."""
        return "{} ({})".format(self.name, self._age)
```

Utilisation :

```python
user = User("Alice", 25)

print(user.name)
print(user.get_age())

user.set_age(30)

print(user)
```

Résultat :

```text
Alice
25
Alice (30)
```

---

# 21. Schéma mental à retenir

```text
                    CLASSE
                      │
             ┌────────┴────────┐
             │                 │
         Attributs          Méthodes
             │                 │
             └────────┬────────┘
                      │
                      ↓
                  INSTANCE
                      │
             ┌────────┴────────┐
             │                 │
           Données         Comportement
```

Exemple :

```text
                    User
                     │
        ┌────────────┴────────────┐
        │                         │
     name / age             get_age()
        │                     set_age()
        │                     __str__()
        ↓
      user
```

---

# 22. Les erreurs à éviter

### Confondre classe et instance

Incorrect :

```text
Classe = objet
```

Correct :

```text
Classe → modèle
Instance → objet créé depuis le modèle
```

### Oublier `self`

Incorrect :

```python
def __init__(name):
    name = name
```

Correct :

```python
def __init__(self, name):
    self.name = name
```

### Confondre attribut et méthode

```text
user.name     → attribut
user.get_age() → méthode
```

### Utiliser `==` pour vérifier l'identité

```python
a == b
```

compare les valeurs.

```python
a is b
```

vérifie si les deux références désignent le même objet.

---

# 23. Questions de révision

Avant de considérer le chapitre comme maîtrisé, il faut pouvoir répondre sans regarder le cours :

1. Qu'est-ce qu'une classe ?
2. Qu'est-ce qu'une instance ?
3. Quelle est la différence entre une classe et un objet ?
4. À quoi sert `__init__` ?
5. Que représente `self` ?
6. Qu'est-ce qu'un attribut ?
7. Qu'est-ce qu'une méthode ?
8. À quoi sert `type()` ?
9. À quoi sert `id()` ?
10. À quoi sert `dir()` ?
11. Quelle différence entre `==` et `is` ?
12. À quoi sert l'encapsulation ?
13. Qu'est-ce qu'un getter ?
14. Qu'est-ce qu'un setter ?
15. À quoi sert `__str__` ?
16. À quoi sert `__repr__` ?
17. Pourquoi peut-on utiliser `raise ValueError(...)` dans `__init__` ?

---

# 24. À retenir absolument

```text
CLASS
= modèle

INSTANCE
= objet créé à partir d'une classe

ATTRIBUTE
= donnée de l'objet

METHOD
= comportement de l'objet

self
= instance actuelle

__init__
= initialise l'instance

type()
= donne le type d'un objet

id()
= donne son identité

dir()
= montre ce que l'objet peut utiliser

__str__
= représentation lisible

__repr__
= représentation utile au développement

GETTER
= lire

SETTER
= modifier / valider
```

## La phrase clé

> **Une classe définit le modèle, une instance est un objet créé à partir de ce modèle, les attributs représentent son état et les méthodes définissent son comportement.**
