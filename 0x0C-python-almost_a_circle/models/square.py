#!/usr/bin/python3
"""
This class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instanitation of Square class
        Args:
            size: Is size of square
            x: Coordinates
            y: Coordinates
            id: Is a identificator
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        print message
        """
        string = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        string1 = string + str(self.y) + " - " + str(self.width)
        return string1
