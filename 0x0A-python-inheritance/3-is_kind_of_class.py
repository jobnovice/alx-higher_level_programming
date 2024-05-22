#!/usr/bin/python3
"""checks if a class isinstacnce of a class"""


def is_kind_of_class(obj, a_class):
    """is a method that checks if a class
       is of a class
       Args:
           obj: an object to that is to be checked
           a_class: a class to be mapped to
        Returns: True or falsche
    """
    return (isinstance(obj, a_class))
