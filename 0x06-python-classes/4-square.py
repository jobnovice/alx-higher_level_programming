#!/usr/bin/python3
"""a Class square defined in this python file ."""


class square:
    """class square that contains some methods and also setter and getters.
        Attributes:
            __size (int): a private instance variable
    """

    def __init__(self, size=0):
        """ well constructor
            Args:
                size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ do we need to documment this or should i leave it like that
            Return the deafult size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """the function to set the new size of the square
            Args:
                value (int): the value to change the size of square with
        """
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
