#!/usr/bin/python3
"""a function tha checks if a given object is the exact instance of class"""


def is_same_class(obj, a_class):
    """maps the object to a class
        Args:
            obj: the object to be checked
            a_class: the class to be mapped to
        Returns: True or False
    """
    return (isinstance(obj, a_class))
