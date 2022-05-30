#!/usr/bin/python3
"""
function that returns True if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance or false
    Args:
        obj: Is a object
        a_class: Is a type
    """
    if isinstance(obj, a_class) is True:
        return True
    return False
