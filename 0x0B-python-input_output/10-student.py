#!/usr/bin/python3
"""Based on the 8-my_class creating the same class"""


class Student():
    """Student class implemented with slight modification"""
    def __init__(self, first_name, last_name, age):
        """instantiating the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json represnatation based on attrs
            Args:
                attrs: optional list of attributes
            returns: a json representaion of the object
        """
        dict1 = {}
        if attrs and isinstance(attrs, list):
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    dict1[attr] = value
        else:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        return dict1
