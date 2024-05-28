#!/usr/bin/python3
"""reading and deserailzing from a JSon file"""

import json


def load_from_json_file(filename):
    """Load the json file the deserailzing it
        Args:
            filename: the name of the file
        Returns: nada
    """
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        return data
