#!/usr/bin/python3
"""class Square extends frrom Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new class square based on the Rectangle"""
    def __init__(self, size):
        """instantiate new square
            Args:
                size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """returns the string representaion of class"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
