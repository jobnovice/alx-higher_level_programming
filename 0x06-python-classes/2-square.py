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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
