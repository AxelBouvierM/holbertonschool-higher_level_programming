#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    x = number % 10
else:
    i = number * -1
    t = i % 10
    x = t * -1
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif x == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif x < 6:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
