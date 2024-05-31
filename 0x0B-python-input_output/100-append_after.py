#!/usr/bin/python3
"""replacing a line with another"""


def append_after(filename="", search_string="", new_string=""):
    """searching and replacing a line inside a file
        filename: the name of the file
        search_string: the string to be replaced
        new_string: the string to replace it with
        returns: None
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if line.find(search_string) == 1:
                line.append(new_string)
        f.seek(0)
        f.truncate()
        f.writelines(lines)
