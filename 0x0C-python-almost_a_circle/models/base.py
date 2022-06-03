#!/usr/bin/python3
"""
This module create a Base class
"""
import json


class Base():
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instanitation of Base class
        Args:
            id: is a identificator
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs
        """
        filename = cls.__name__ + ".json"
        listt = []
        for i in list_objs:
            listt.append(i.to_dictionary())
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            f.write(Base.to_json_string(listt))
