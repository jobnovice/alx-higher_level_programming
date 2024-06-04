#!/usr/bin/python3
"""created the base class"""
import json


class Base:
    """Base class for the project defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string representation of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list of dictionaries to a file"""
        filename = "{}.json".format(cls.__name__)
        dicts = cls.to_json_string(i.to_dictionary() for i in list_objs)
        with open(filename, 'w') as f:
            f.write(dicts)
