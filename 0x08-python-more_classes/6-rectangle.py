#!/usr/bin/python3
"""
This module define an empty class Rectangle
"""


class Rectangle:
    """
    Is an empty class of type Rectangle
    Attributes:
        None
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Inizialization the attrubutes of Rectangle
        Args:
            width (int): Is the width of a Rectangle
            height (int): Is the height of a Rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        Get the height
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

    def area(self):
        """
        Return the area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of Rectangle
        """
        width2 = self.__width * 2
        height2 = self.__height * 2
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = width2 + height2
        return result

    def __str__(self):
        """
        asdsadsa
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for x in range(self.__height):
                for i in range(self.__width):
                    string += "#"
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """
        string = "Rectangle(" + str(self.__width) + ", " + str(self.__height)
        string += ")"
        return string

    def __del__(self):
        """
        Print message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
