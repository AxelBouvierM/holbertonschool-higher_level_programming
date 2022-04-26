#!/usr/bin/python3

for a in reversed(range(97, 123)):
    if a % 2 == 0:
        x = a
    elif a % 2 == 1:
        x = a - 32
    print("{}".format(chr(x)), end="")
