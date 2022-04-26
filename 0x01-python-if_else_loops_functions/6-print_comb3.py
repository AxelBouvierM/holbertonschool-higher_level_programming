#!/usr/bin/python3

for i in range(0, 9):
    for x in range(0, 10):
        if i != x and i < x:
            if i + x == 17:
                print("89")
                break
            print("{}".format(i), end="")
            print("{}".format(x), end=", ")
