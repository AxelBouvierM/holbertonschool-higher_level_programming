#!/usr/bin/python3
"""
This module define a MyList class
"""


class MyList(list):
    """
    Define class of type MyList
    """
    def print_sorted(self):
        """
        Function that sorted list
        """
        print(sorted(self))
