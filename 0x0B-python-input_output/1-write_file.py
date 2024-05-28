#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """wrtie to a file with given a text as an input
        Args:
            filename: name of the file
            text: string to write
        Returns: the number of charcters written
    """
    with open(filename, 'w+x', encoding='utf-8') as f:
        return f.write(text)
