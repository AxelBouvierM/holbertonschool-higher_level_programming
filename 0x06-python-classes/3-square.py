#!/usr/bin/python3
"""
Defines a square by: (based on 0-square.py)
"""


class Square:
    """
    Define a Square class
    Attributes:
        None
    """
    def __init__(self, size=0):
        """
        Initialization the attributes of Square
        Args:
            size (int): The size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the current square area
        """
        return (self.__size * self.__size)
