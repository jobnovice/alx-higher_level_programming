#!/usr/bin/python3
"""a method that lists all the available methods and attributes of an object"""


def lookup(obj):
    """returns a list of object
        Args:
            obj: object to lookup
            returns: lists of methods and attributes of the object"""
    return dir(obj)
