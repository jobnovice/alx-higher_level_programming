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
