#!/usr/bin/python3
"""
This module define a class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instanitation of Rectangle class
        Args:
            width: Is a width of rectangle
            height: Is a height of rectangle
            x: Is..
            y: Is..
            id: Is a identificator
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x
        """
        self.__x = value

    @property
    def y(self):
        """
        Gets the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y
        """
        self.__y = value
