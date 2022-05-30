#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Define a Square class
    """
    def __init__(self, size):
        """
        Initialization the attributes of Square
        args:
            size: Size of Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the area of square
        """
        return self.__size * self.__size
