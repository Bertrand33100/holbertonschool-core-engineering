#!/usr/bin/env python3
"""Pour lire et afficcher le texte du fichier"""


def read_file(filename=""):
    """lire le text (utf8) et affiche la sortie"""
    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read, end="")
