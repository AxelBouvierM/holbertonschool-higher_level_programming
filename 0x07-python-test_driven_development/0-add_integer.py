#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Function that add_integer
    a and b are of type int or float
    Return:
        Add of a and b
    Raises:
        TypeError: If a and b is not int and float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
