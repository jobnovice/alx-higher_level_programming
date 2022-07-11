#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=0):
        """initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            value (int): the size of a size of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        '''getter of the positio
        Returns:
                the position of the size.'''
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''Prints the size of the squarein an
        array form
            Returns:
                none
        '''
        if self.__size is 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                [print(" ", end="") for l in range(0, self.__position[0])]
                print("")
