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
        if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return res
        else:
            return self.__dict__
