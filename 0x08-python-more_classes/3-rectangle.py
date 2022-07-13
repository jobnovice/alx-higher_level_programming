#!/usr/bin/python3
"""new class defined Rectangle"""


class Rectangle:
    """new class Rectangle defined but it's empty for now"""
    def __init__(self, width=0, height=0):
        """ yeah module is documented
            Args:
                width (int): the width of the rectangle
                height (int): the height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        '''to set the value of the heigh
            Args:
                value (int): the value to be seted with'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''to set the value of the heigh
            Args:
                value (int): the value to be seted with'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the current perimeter of the rectangle'''
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
