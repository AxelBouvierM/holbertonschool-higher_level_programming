#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Define a BaseGeometry class
    """
    def __init__(self, width, height):
        """
        Initialization the attributes of Rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return rectangle description
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
