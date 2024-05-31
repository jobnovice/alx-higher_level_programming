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
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)
