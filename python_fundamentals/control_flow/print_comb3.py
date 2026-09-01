#!/usr/bin/env python3

for i in range(10):
    for j in range(i + 1, 10):
        last = (i == 8 and j == 9)
        print("{}{}".format(i, j), end="\n" if last else ", ")
