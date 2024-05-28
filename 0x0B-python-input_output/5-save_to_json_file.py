#!/usr/bin/python3
"""serialize and save the serailized data to a file"""

import json


def save_to_json_file(my_obj, filename):
    """save the seraialized data to a file
        Args:
            my_obj: Object to be serialized and saved
            filename: the name of the file
        Returns: None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, filename)
