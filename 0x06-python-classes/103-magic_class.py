#!/usr/bin/python3
"""
Magic Class
"""

import math


class MagicClass:
    """
    Define a Magaic Class
    Attributes:
    None
    """

    def __init__(self, radius=0):
        """
        Initialization of Magic Class
        Args:
            radius (int): The radius of a Magic
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Return the current magic area
        """

        return self.__radius**2*math.pi

    def circumference(self):
        """
        Return the circumference of magic
        """
        return 2*math.pi*self.__radius
