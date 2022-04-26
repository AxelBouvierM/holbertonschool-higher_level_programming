#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            a = ord(i) - 32
            x = chr(a)
        else:
            x = i
        print("{}".format(x), end="")
    print()
