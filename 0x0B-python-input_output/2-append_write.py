#!/usr/bin/python3
"""appending to a file"""


def append_write(filename="", text=""):
    """appending to a file with a given text
        Args:
            filename: the name of the file
            text: the text to append to the file
        Returns: the numbers of the charaters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        s = str(text)
        return (f.write(s))
