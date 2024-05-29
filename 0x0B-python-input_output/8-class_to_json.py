#!/usr/bin/python3
"""returning the dictionary description for json serialization"""


def class_to_json(obj):
    """serializing a class object into json
        Args:
            obj: an instance of a class
        Returns: the dictionary description for json serialization
    """
    if hasattr(obj, '__dict__'):
        return (obj.__dict__)
