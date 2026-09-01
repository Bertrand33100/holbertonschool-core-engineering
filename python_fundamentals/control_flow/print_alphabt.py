#!/usr/bin/env python3

alphabet = ""

for letter in range(97, 123):
    character = chr(letter)
    if character != "e" and character != "q":
        alphabet += character

print("{}".format(alphabet), end="")
