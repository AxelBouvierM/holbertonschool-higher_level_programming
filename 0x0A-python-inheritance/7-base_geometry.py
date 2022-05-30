#!/usr/bin/python3
"""
This module define a class BaseGeometry
"""


class BaseGeometry():
    """
    Empty class BaseGeometry
    """
    def area(self):
        """
        Method that print exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
