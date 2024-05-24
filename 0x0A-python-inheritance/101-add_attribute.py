#!/usr/bin/python3
"""a method that adds attributes to a class if possible"""


def add_attribute(obj, attr_name, attr_value):
    """adds the attribute with its value to the class
        Args:
            className: the class that accepts the new attribute
            name: the name of the attribute
            value: the value of the attribute
        Returns: True or False upon sucess
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
