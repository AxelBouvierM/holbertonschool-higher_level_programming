#!/usr/bin/python3
"""
This function returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    Args:
        obj: Object is object
    """
    return dir(obj)
