#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """wrtie to a file with given a text as an input
        Args:
            filename: name of the file
            text: string to write
        Returns: the number of charcters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        s = str(text)
        return (f.write(s))


nb_characters = write_file("my_first_file2.txt", "This School is not so cool!\n")
print(nb_characters)