#!/usr/bin/python3
""" yeah automatically filled it with string documentation"""


class Square:
    """ the class with square and it's specfiction"""

    def __int__(self, size=0):
        """yeah the constructor needs to introduce us it's arguments
            Args:
                size (int): the size of the square
            Returns:
                None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size

    def area(self):
        """Returns: 
            the current area of the squaree"""
        return self.__size * self.__size
