#!/usr/bin/python3
"""Defines a class Square"""


from turtle import position


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
                print("")
    
    @property
    def position(self):
        '''getter of the position 
            Returns:
                the position of the size.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setter of the position
            Args:
                value (tuple): a tuple of size 2
            Returns:
                None'''
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if type(value[i]) is not int:
                    raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    self.__position[i] = value [i]