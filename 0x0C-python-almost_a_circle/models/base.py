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
        if list_objs is not None:
            for i in list_objs:
                listt.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(listt))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        listt = []
        if json_string is None or len(json_string) == 0:
            return listt
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        listt = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                read = f.read()
                x = cls.from_json_string(read)
                for i in x:
                    listt.append(cls.create(**i))
        except FileNotFoundError:
            pass
        return listt
