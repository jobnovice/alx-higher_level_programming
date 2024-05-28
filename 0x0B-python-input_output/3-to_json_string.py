#!/usr/bin/python3
"""serialization for python object"""
import json


def to_json_string(my_obj):
    """serailzing a python object to json
        Args:
            my_obj: a python object
        Returns: json string represenation of the python object
        """
    json_string = json.dumps(my_obj)
    return json_string
