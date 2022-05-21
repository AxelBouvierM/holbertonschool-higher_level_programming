#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    Function that print the square print_square
    size is the size of square
    Raises:
        TypeError: If size is not int
        TypeError: If the size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
