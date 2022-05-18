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
        self.size = size

    @property
    def size(self):
        """
        Gets the value
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Equal to the other square
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Different to the other square
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than other square
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater or equal to other square
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than the other square
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less or equal to other square
        """
        return self.area() <= other.area()
