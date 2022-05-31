#!/usr/bin/python3
"""
This module create a Student class
"""


class Student():
    """
    class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    if i in self.__dict__:
                        dic[i] = self.__dict__[i]
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
