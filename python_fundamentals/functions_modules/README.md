# Python Fundamentals — Functions & Modules

## Introduction & Contexte

Lorsque les programmes deviennent plus importants, répéter plusieurs fois la même logique rend le code plus difficile à maintenir et augmente le risque d'erreurs.

Python permet de résoudre ce problème grâce notamment aux **fonctions** et aux **modules**.

Une **fonction** permet d'encapsuler une logique dans un bloc réutilisable.

Un **module** permet d'organiser du code dans différents fichiers afin de pouvoir réutiliser des fonctions et des variables dans plusieurs programmes.

Ce projet permet de comprendre progressivement :

* La définition d'une fonction.
* Les paramètres d'une fonction.
* Les valeurs de retour avec `return`.
* La différence entre `print` et `return`.
* Le fonctionnement de l'exécution d'un fichier Python.
* L'utilisation de `if __name__ == "__main__":`.
* L'importation de fonctions depuis un autre fichier.
* L'importation de variables depuis un autre fichier.
* La réutilisation du code entre plusieurs fichiers.

L'ordre des exercices est progressif : on commence par créer des fonctions simples, puis on apprend à organiser et réutiliser du code dans plusieurs fichiers.

---

## Objectifs pédagogiques

À la fin de ce projet, je dois être capable de :

* Définir une fonction avec des paramètres.
* Utiliser `return` pour retourner une valeur.
* Faire la différence entre `print()` et `return`.
* Utiliser des conditions et des boucles à l'intérieur d'une fonction.
* Comprendre comment Python exécute le code situé au niveau principal d'un fichier.
* Comprendre le rôle de `if __name__ == "__main__":`.
* Importer une fonction depuis un autre fichier.
* Importer une variable depuis un autre fichier.
* Écrire un fichier qui fonctionne correctement lorsqu'il est exécuté directement.
* Écrire un fichier qui peut également être importé sans exécuter inutilement son code principal.

---

# Fonctions en Python

## Définition d'une fonction

Une fonction est un bloc de code auquel on donne un nom afin de pouvoir l'utiliser plusieurs fois.

Structure générale :

```python
def nom_de_fonction(parametre):
    # instructions
    return resultat
```

### Les différents éléments

| Élément           | Rôle                                  |
| ----------------- | ------------------------------------- |
| `def`             | Indique que l'on définit une fonction |
| `nom_de_fonction` | Nom donné à la fonction               |
| `parametre`       | Donnée reçue par la fonction          |
| `:`               | Début du bloc de la fonction          |
| `return`          | Retourne une valeur                   |

---

# `print()` et `return`

Une notion importante de ce chapitre est de comprendre que **`print()` et `return` n'ont pas le même rôle**.

### `print()`

`print()` affiche une information à l'écran.

### `return`

`return` renvoie une valeur au programme qui a appelé la fonction.

Exemple conceptuel :

```text
Fonction
   │
   ├── print()  → affiche quelque chose
   │
   └── return   → renvoie une valeur
```

Une valeur retournée peut ensuite être stockée dans une variable ou utilisée dans une autre opération.

---

# Modules Python

Un module est simplement un fichier Python qui contient du code pouvant être réutilisé.

Par exemple :

```text
projet/
│
├── calculator.py
└── main.py
```

Une fonction définie dans `calculator.py` peut être utilisée depuis `main.py`.

Cela permet de séparer les responsabilités et d'éviter de mettre tout le programme dans un seul fichier.

---

# Importation

Python permet d'importer du code provenant d'un autre fichier.

Le principe est :

```text
main.py
   │
   │ importe
   ▼
calculator.py
   │
   └── fonction réutilisable
```

Cela permet de construire des programmes composés de plusieurs modules.

---

# `if __name__ == "__main__"`

Cette condition est particulièrement importante dans ce projet.

Lorsqu'un fichier Python est exécuté directement, Python lui attribue :

```python
__name__ = "__main__"
```

Lorsqu'un fichier est importé depuis un autre fichier, sa variable `__name__` prend généralement le nom du module.

Cela permet de distinguer deux situations :

```text
Exécution directe
       │
       ▼
python fichier.py
       │
       ▼
__name__ == "__main__"


Importation
       │
       ▼
import fichier
       │
       ▼
__name__ != "__main__"
```

La condition :

```python
if __name__ == "__main__":
```

permet donc de contrôler le code qui doit être exécuté uniquement lorsque le fichier est lancé directement.

---

# Organisation du projet

Repository GitHub :

`holbertonschool-core-engineering`

Répertoire du projet :

```text
python_fundamentals/
└── functions_modules/
```

---

# Exercice 0 — `islower`

## Objectif

Créer une fonction :

```python
def islower(c):
```

Cette fonction doit déterminer si le caractère reçu est une lettre minuscule.

Elle doit retourner :

* `True` si le caractère est une lettre minuscule.
* `False` dans les autres cas.

### Exemples

```text
islower('a') → True
islower('A') → False
islower('3') → False
```

---

## Contraintes

Pour cet exercice :

* Il ne faut pas utiliser `.islower()`.
* Il faut utiliser la logique basée sur l'ASCII.
* La fonction doit utiliser `ord()`.
* La fonction doit retourner une valeur booléenne.
* La valeur retournée doit être `True` ou `False`.

---

# Comprendre l'ASCII

Chaque caractère possède une valeur numérique dans la table ASCII.

Les lettres minuscules sont situées dans l'intervalle :

```text
a → 97
b → 98
c → 99
...
z → 122
```

Ainsi, pour savoir si un caractère est une minuscule, on peut comparer sa valeur ASCII à cet intervalle.

Conceptuellement :

```text
        lettres minuscules

97                              122
 │--------------------------------│
 a                                z
```

La fonction `ord()` permet d'obtenir la valeur numérique correspondant à un caractère.

Exemple :

```text
ord('a') → 97
```

L'exercice demande donc de raisonner avec la valeur ASCII plutôt que d'utiliser une méthode Python toute faite.

---

# Fichiers

Le premier exercice se trouve ici :

```text
holbertonschool-core-engineering/
└── python_fundamentals/
    └── functions_modules/
        └── islower.py
```

---

# Exigences générales

Les corrections sont effectuées avec :

* **Ubuntu 20.04 LTS**
* **Python 3.8.x**
* **pycodestyle 2.7.x**

Chaque fichier Python doit :

* Commencer exactement par :

```python
#!/usr/bin/env python3
```

* Être exécutable.
* Se terminer par une nouvelle ligne.
* Respecter le style **PEP8**.
* Ne pas utiliser de bibliothèque externe.
* Ne pas utiliser `sys.argv`.
* Respecter les contraintes spécifiques de chaque exercice.

---

# Vérification du code

Pour vérifier le style PEP8, le projet utilise `pycodestyle`.

Exemple :

```bash
pycodestyle islower.py
```

Il est également important de vérifier que le fichier est exécutable.

On peut vérifier les permissions avec :

```bash
ls -l islower.py
```

Le fichier doit avoir le droit d'exécution.

---

# Notions importantes à retenir

## 1. Une fonction

Une fonction permet de regrouper une logique réutilisable.

```text
Fonction
   │
   ├── reçoit éventuellement des paramètres
   │
   ├── exécute des instructions
   │
   └── peut retourner une valeur
```

## 2. `return`

`return` permet de transmettre une valeur au code qui a appelé la fonction.

## 3. `print`

`print()` sert principalement à afficher une information.

## 4. Un module

Un module est un fichier Python pouvant contenir des fonctions, variables et autres éléments réutilisables.

## 5. `import`

`import` permet d'utiliser du code provenant d'un autre module.

## 6. `__name__`

`__name__` permet notamment de savoir si un fichier Python est exécuté directement ou utilisé comme module.

## 7. `if __name__ == "__main__":`

Cette condition permet d'exécuter certaines instructions uniquement lorsque le fichier est lancé directement.

---

# Progression du chapitre

Le projet suit une progression logique :

```text
Fonctions
   │
   ▼
Paramètres
   │
   ▼
Valeurs de retour
   │
   ▼
Conditions et boucles
   │
   ▼
Exécution d'un fichier
   │
   ▼
__name__
   │
   ▼
if __name__ == "__main__"
   │
   ▼
Modules
   │
   ▼
Importation
   │
   ▼
Réutilisation du code
```

L'objectif final est de passer d'un programme contenant toute sa logique dans un seul fichier à une organisation plus propre où les différentes fonctions et responsabilités peuvent être séparées dans plusieurs modules.

---

# Ressources

* Python Documentation — **Defining Functions**
  [Python Tutorial — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html?utm_source=chatgpt.com#defining-functions)

* Python Documentation — **Modules**
  [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html?utm_source=chatgpt.com)

* Python Documentation — **`__name__` / Python Library Reference**
  [Python Documentation](https://docs.python.org/3/library/?utm_source=chatgpt.com)

* Python Enhancement Proposal — **PEP 8 Style Guide**
  [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/?utm_source=chatgpt.com)

---

# Conclusion

Ce chapitre constitue une étape importante dans l'apprentissage de Python.

Il permet de comprendre comment :

```text
écrire une fonction
       ↓
retourner une valeur
       ↓
réutiliser cette fonction
       ↓
séparer le code dans plusieurs fichiers
       ↓
importer les modules
       ↓
organiser correctement un projet Python
```

Les notions de **fonctions**, **`return`**, **modules**, **`import`** et **`if __name__ == "__main__"`** sont fondamentales pour écrire des programmes Python structurés, réutilisables et maintenables.
