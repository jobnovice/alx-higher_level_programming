#!/usr/bin/python3
"""reading file contents"""


def read_file(filename=""):
    """reads file content in a utf-8 format
        Args:
            filename: string representing filename
        Returns: nothing
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
