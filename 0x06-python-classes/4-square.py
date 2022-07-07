#!/usr/bin/python3
'''Class square'''


class square:
    '''class square '''

    def __init__(self, size=0):
        ''' well constructor
            Args:
                size (int): well it's an int
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property 
    def size(self):
        ''' do we need to documment this or should i leave it like that
            Return the deafult size
        '''
        return self.__size
    @size.setter
    def size(self, value):
        ''' yeah man 
            Args:
                value (int): the value to change the size of square with
        '''
        self.__size = value
    def area(self):
        '''Return the area of the square'''
        return (self.__size * self.__size)
