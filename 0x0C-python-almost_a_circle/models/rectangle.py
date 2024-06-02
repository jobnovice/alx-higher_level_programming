#!/usr/bin/python3
"""Rectangle class defined and inherits from the Base class"""

from base import Base


class Rectangle(Base):
    """rectangle class defined as follows"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates a new rectangle object as the following"""
        super().__init__(id)
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of the rectangle
            Args:
                width: the width of the rectangle
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width muse be greater than zero')

        self.__width = width

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for the height of the rectangle
            Args:
                height: the height of the rectangle
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be greater than zero')
        self.__height = height
