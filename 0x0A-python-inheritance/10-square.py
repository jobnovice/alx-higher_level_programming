#!/usr/bin/python3
"""new class Square created that inheirts from Rectangle"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square:
    """square class created """
    def __init__(self, size):
        """instantiates square class"""
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """returns the area of the square object"""
        return (self.__size * self.__size)
