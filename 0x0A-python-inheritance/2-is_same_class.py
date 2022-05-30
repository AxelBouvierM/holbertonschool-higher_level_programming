#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance or False
    Args:
        obj: Is an object
        a_class: Is a type
    """
    if type(obj) == a_class:
        return True
    return False
