#!/usr/bin/python3
"""checks if an object is ssubclass of a class"""


def inherits_from(obj, a_class):
    """checks if an object is subclass of a given class
       Args:
           obj: the object to be checked
           a_class: the class to be mapped to
        Returns: True or falsche
    """
    cls1 = type(obj)
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
