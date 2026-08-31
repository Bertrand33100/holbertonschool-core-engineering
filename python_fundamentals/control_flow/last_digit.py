#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

last_digit = abs(number) % 10

if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print("last_digit of", number, "and is greater than 5")
elif last_digit == 0: 
    print("Last digit of", number, "is", last_digit, "and is 0") 
else: 
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
