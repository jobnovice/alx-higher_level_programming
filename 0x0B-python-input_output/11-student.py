#!/usr/bin/python3
"""
    11-student.py
"""


class Student:
    """student class revised again"""
    def __init__(self, first_name, last_name, age):
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
            res = {k: self.__dict__[k] for k  in self.__dict__.keys() & attrs}
            return res
        else:
            return self.__dict__
        
    def reload_json(self, json):
        """reloading the json represenation to"""
        for key,value in json.items():
            setattr(self,key,value)
