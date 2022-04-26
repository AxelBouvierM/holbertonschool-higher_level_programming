#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        n = number % 10
        print("{}".format(n), end="")
        return (n)
    else:
        x = number * -1
        n = x % 10
        print("{}".format(n), end="")
        return n
