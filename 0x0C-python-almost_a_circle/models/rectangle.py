#!/usr/bin/python3
"""
This module define a class Rectangle that inherits from Base
"""
import json
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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Return str
        """
        string = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
        string1 = string + str(self.y) + " - " + str(self.width) + "/"
        return string1 + str(self.height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dic = {"id": self.id, "width": self.__width, "height": self.__height}
        dic["x"] = self.__x
        dic["y"] = self.__y
        return dic
