#!/usr/bin/python3
"""
This module define a MyList class
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
