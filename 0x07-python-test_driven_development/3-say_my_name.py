#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Fucnction that print say_my_name
    fisrt_name is the first name
    last_name is the last name
    Raises:
        TypeError: If first_name is not str or last_name is not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
