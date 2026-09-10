# Python - Exception Handling

## Description

Ce chapitre présente la **gestion des erreurs et des exceptions en Python**.

Lorsqu'un programme rencontre un problème, Python peut générer une **exception**. Au lieu de laisser le programme s'arrêter brutalement, on peut utiliser `try` et `except` pour gérer cette situation.

La gestion des exceptions permet notamment de :

* éviter qu'un programme plante ;
* gérer les erreurs de manière contrôlée ;
* continuer l'exécution du programme lorsque c'est possible ;
* détecter certains problèmes pendant l'exécution ;
* créer ses propres erreurs avec `raise`.

---

# 1. Qu'est-ce qu'une erreur ?

Une erreur est un problème qui empêche Python d'exécuter correctement une instruction.

Par exemple :

```python
print("Hello"
```

Il manque une parenthèse.

Python renvoie une erreur de syntaxe :

```text
SyntaxError
```

Il existe plusieurs types d'erreurs.

---

# 2. Les erreurs les plus courantes

## SyntaxError

Erreur dans la syntaxe du programme.

```python
if x == 5
    print(x)
```

Résultat :

```text
SyntaxError
```

Il manque `:`.

---

## NameError

On utilise une variable qui n'existe pas.

```python
print(name)
```

Si `name` n'a jamais été créée :

```text
NameError
```

---

## TypeError

On utilise un type incompatible avec une opération.

```python
"hello" + 5
```

Python ne peut pas additionner directement une chaîne de caractères et un entier.

Résultat :

```text
TypeError
```

---

## ValueError

Le type est correct mais la valeur n'est pas valide.

```python
int("hello")
```

Python sait convertir une chaîne en entier, mais `"hello"` n'est pas un nombre.

Résultat :

```text
ValueError
```

---

## IndexError

On essaie d'accéder à un index qui n'existe pas.

```python
my_list = [1, 2, 3]

print(my_list[5])
```

La liste possède les index :

```text
0  1  2
1  2  3
```

L'index `5` n'existe pas.

Résultat :

```text
IndexError
```

---

## KeyError

On demande une clé qui n'existe pas dans un dictionnaire.

```python
person = {
    "name": "Bertrand"
}

print(person["age"])
```

La clé `"age"` n'existe pas.

Résultat :

```text
KeyError
```

---

# 3. Qu'est-ce qu'une exception ?

Une exception est un événement qui se produit pendant l'exécution du programme et qui interrompt normalement son déroulement.

Exemple :

```python
number = 10
result = number / 0
```

Python ne peut pas diviser par zéro.

Il génère :

```text
ZeroDivisionError
```

Sans gestion d'exception, le programme s'arrête.

---

# 4. `try`

Le mot-clé `try` permet de dire :

> "Essaie d'exécuter ce code."

Exemple :

```python
try:
    number = int("10")
```

Python essaie d'exécuter :

```python
number = int("10")
```

Cela fonctionne.

---

# 5. `except`

`except` permet de gérer une exception.

```python
try:
    number = int("hello")
except ValueError:
    print("La conversion est impossible")
```

Python essaie :

```python
int("hello")
```

Une `ValueError` apparaît.

Python passe alors dans :

```python
except ValueError:
```

Résultat :

```text
La conversion est impossible
```

Le programme ne s'arrête donc pas à cause de cette exception.

---

# 6. Structure générale

La structure de base est :

```python
try:
    # code qui peut provoquer une erreur
except:
    # code exécuté si une erreur apparaît
```

Il est préférable de préciser le type d'exception :

```python
try:
    # code
except ValueError:
    # gestion de ValueError
```

---

# 7. Plusieurs `except`

On peut gérer plusieurs types d'erreurs.

```python
try:
    number = int(input("Nombre : "))
    result = 10 / number

except ValueError:
    print("Vous devez entrer un nombre")

except ZeroDivisionError:
    print("Division par zéro impossible")
```

Chaque `except` correspond à une erreur différente.

---

# 8. `else`

On peut utiliser `else` après `try/except`.

`else` est exécuté **seulement si aucune exception ne s'est produite**.

```python
try:
    number = int("10")

except ValueError:
    print("Erreur")

else:
    print("Conversion réussie")
```

Résultat :

```text
Conversion réussie
```

Structure :

```python
try:
    # essayer
except:
    # erreur
else:
    # aucune erreur
```

---

# 9. `finally`

`finally` est exécuté **dans tous les cas**.

```python
try:
    number = int("10")

except ValueError:
    print("Erreur")

finally:
    print("Fin du programme")
```

Même si une erreur apparaît, `finally` sera exécuté.

Structure :

```python
try:
    # essayer
except:
    # erreur
else:
    # aucune erreur
finally:
    # toujours exécuté
```

---

# 10. `raise`

`raise` permet de provoquer volontairement une exception.

Exemple :

```python
age = -5

if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")
```

Python génère volontairement :

```text
ValueError
```

`raise` signifie donc :

> "Je veux déclencher cette exception."

---

# 11. Exemple avec une fonction

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro")

    return a / b
```

Utilisation :

```python
print(divide(10, 2))
```

Résultat :

```text
5.0
```

Mais :

```python
print(divide(10, 0))
```

provoque :

```text
ZeroDivisionError
```

---

# 12. `try/except` dans une fonction

On peut également gérer l'erreur directement dans une fonction.

```python
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return None
```

Maintenant :

```python
print(divide(10, 0))
```

renvoie :

```text
None
```

Le programme ne plante pas.

---

# 13. L'exercice `safe_print_list`

Prototype :

```python
def safe_print_list(my_list=[], x=0):
```

Objectif :

Afficher `x` éléments d'une liste.

Contraintes :

* la liste peut contenir n'importe quel type ;
* tous les éléments doivent être affichés sur la même ligne ;
* `x` représente le nombre d'éléments à afficher ;
* `x` peut être supérieur à la taille de la liste ;
* retourner le nombre réel d'éléments affichés ;
* utiliser `try / except` ;
* ne pas utiliser `len()` ;
* ne pas importer de module.

Solution :

```python
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            break

    print()
    return nb_print
```

### Pourquoi `try / except` ?

Supposons :

```python
my_list = [1, 2]
x = 5
```

La boucle essaie :

```python
my_list[0]
my_list[1]
my_list[2]
```

Mais `my_list[2]` n'existe pas.

Python provoque :

```text
IndexError
```

Le `except` intercepte cette erreur :

```python
except IndexError:
    break
```

La boucle s'arrête.

---

# 14. `break`

`break` permet de sortir immédiatement d'une boucle.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Résultat :

```text
0
1
2
3
4
```

Lorsque `i` vaut `5`, `break` arrête la boucle.

Dans `safe_print_list`, on utilise :

```python
except IndexError:
    break
```

pour arrêter la boucle lorsqu'il n'y a plus d'élément.

---

# 15. `end=""`

Normalement :

```python
print(1)
print(2)
print(3)
```

donne :

```text
1
2
3
```

`print()` ajoute automatiquement un retour à la ligne.

Avec :

```python
print(1, end="")
print(2, end="")
print(3, end="")
```

on obtient :

```text
123
```

C'est utile lorsque plusieurs éléments doivent être affichés sur la même ligne.

---

# 16. Compter les éléments affichés

Dans l'exercice :

```python
nb_print = 0
```

initialise le compteur.

Puis :

```python
nb_print += 1
```

équivaut à :

```python
nb_print = nb_print + 1
```

Chaque élément affiché augmente le compteur.

Enfin :

```python
return nb_print
```

retourne le nombre réel d'éléments affichés.

---

# 17. Différence entre `print` et `return`

C'est une notion importante.

## `print`

Affiche quelque chose à l'écran.

```python
print("Hello")
```

## `return`

Renvoie une valeur depuis une fonction.

```python
def add(a, b):
    return a + b
```

Puis :

```python
result = add(2, 3)
print(result)
```

Résultat :

```text
5
```

Dans `safe_print_list` :

```python
print(my_list[i], end="")
```

affiche l'élément.

Alors que :

```python
return nb_print
```

renvoie le nombre d'éléments affichés.

---

# 18. Schéma mental à retenir

Pour comprendre `try / except`, pense :

```text
              TRY
               |
               v
       J'essaie le code
               |
        +------+------+
        |             |
     Réussite       Erreur
        |             |
        v             v
    continuer       EXCEPT
                      |
                      v
               gérer l'erreur
```

---

# 19. Exemple complet

```python
def get_number(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        return None
```

Utilisation :

```python
numbers = [10, 20, 30]

print(get_number(numbers, 1))
print(get_number(numbers, 10))
```

Résultat :

```text
20
None
```

Le premier accès fonctionne.

Le deuxième provoque `IndexError`, qui est interceptée par `except`.

---

# 20. Les notions à connaître pour ce chapitre

## Indispensable

Tu dois savoir comprendre et utiliser :

```python
try:
```

```python
except:
```

```python
raise
```

```python
break
```

```python
return
```

et connaître :

```text
IndexError
ValueError
TypeError
NameError
KeyError
ZeroDivisionError
SyntaxError
```

---

# 21. Les questions à se poser devant une erreur

Quand Python affiche une erreur, regarde toujours :

### 1. Quel type d'erreur ?

Exemple :

```text
IndexError
```

### 2. Où est-elle apparue ?

Python indique généralement le fichier et la ligne.

### 3. Pourquoi ?

Exemple :

```python
my_list[10]
```

alors que la liste ne possède pas cet index.

### 4. Est-ce que je dois gérer cette erreur ?

Si oui :

```python
try:
    ...
except IndexError:
    ...
```

---

# 22. Erreurs à ne pas faire

## Éviter `except:` sans précision

On peut écrire :

```python
try:
    ...
except:
    ...
```

mais cela attrape pratiquement toutes les exceptions.

Il est généralement préférable d'indiquer l'erreur attendue :

```python
except IndexError:
```

ou :

```python
except ValueError:
```

---

# 23. Résumé

### `try`

> Essaie d'exécuter ce code.

```python
try:
    code
```

### `except`

> Si cette erreur apparaît, fais ceci.

```python
except ValueError:
    ...
```

### `else`

> Si aucune erreur n'est apparue, fais ceci.

```python
else:
    ...
```

### `finally`

> Fais ceci dans tous les cas.

```python
finally:
    ...
```

### `raise`

> Déclenche volontairement une exception.

```python
raise ValueError("Message")
```

### `break`

> Arrête la boucle.

```python
break
```

### `return`

> Renvoie une valeur depuis une fonction.

```python
return value
```

---

# 24. Ce qu'il faut retenir pour Holberton

Le point principal de ce chapitre est de comprendre que **toutes les erreurs ne doivent pas forcément faire planter le programme**.

On peut anticiper certaines erreurs :

```python
try:
    # opération risquée
except TypeOfError:
    # comportement prévu
```

Pour l'exercice `safe_print_list`, le raisonnement est :

```text
Je veux afficher x éléments
        ↓
Je parcours les x positions
        ↓
J'essaie d'accéder à my_list[i]
        ↓
L'élément existe ?
   ↓             ↓
 OUI            NON
   ↓             ↓
print()       IndexError
   ↓             ↓
compteur++      break
        \       /
         \     /
          ↓   ↓
       print()
          ↓
    return compteur
```

La compétence importante n'est donc pas seulement de connaître la syntaxe de `try/except`, mais de savoir **quelle opération peut provoquer quelle exception et comment réagir correctement à cette exception**.
