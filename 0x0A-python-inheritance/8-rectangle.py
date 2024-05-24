#!/usr/bin/python3
"""a rectangle class that inherits from the baseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class created by inheriting some properties from
    base geometry class"""
    def __init__(self, width, height):
        """instantiates a rectangle
            Args:
                width: width of the rectangle
                height: height of the rectangle
            Returns: None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
