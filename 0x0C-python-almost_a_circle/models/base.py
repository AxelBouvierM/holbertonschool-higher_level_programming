#!/usr/bin/python3
"""
This module create a Base class
"""


class Base():
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instanitation of Base class
        Args:
            id: is a identificator 
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
