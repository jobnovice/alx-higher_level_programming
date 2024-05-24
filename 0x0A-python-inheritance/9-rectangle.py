#!/usr/bin/python3
"""Rectangle class implemented using basegeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherited from basegeometry"""
    def __init__(self, width, height):
        """instantiate a rectangle by valdiating the input
            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the string representation of the rectangle class"""
        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)
