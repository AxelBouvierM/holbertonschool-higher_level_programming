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

    @property
    def size(self):
        """
        Gets the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.height = value
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
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        dic = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dic
