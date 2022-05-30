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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
