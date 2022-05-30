#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
