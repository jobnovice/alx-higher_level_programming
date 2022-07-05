#!/usr/bin/python3
""" another square class.
"""


class Square:
    """ the real class """
    def __init__(self, size=0):
        """
        the constructor accepts the size paramter
        Args:
            size: nothing but a number
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size