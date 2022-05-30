#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    Args:
        obj: Is a object
        a_class: Is a type
    """
    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return True
    return False
