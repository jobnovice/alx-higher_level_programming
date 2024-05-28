#!/usr/bin/python3
"""deserialization of a json string to an object."""
import json


def from_json_string(my_str):
    """deserialization of a json string to an object.
        Args:
            my_str: a json string
        Returns: a python object
    """
    python_obj = json.loads(my_str)
    return python_obj
