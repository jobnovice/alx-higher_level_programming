#!/usr/bin/python3
"""creating another class that inherits from the base class"""

Base = __import__('base').Base


class Rectangle(Base):
    """A rectangle that inherits from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of the rectangle
            width: the width of the rectangle
        """
        if width < 0:
            raise ValueError("width must be greater than zero")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of the rectangle"""
        if height < 0:
            raise ValueError("height musst be greater than zero")
        if type(height) is not int:
            raise TypeError("height muse be an integer")

        self.__height = height
