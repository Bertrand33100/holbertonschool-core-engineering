#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)
