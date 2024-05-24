#!/usr/bin/python3
"""new class Square created that inheirts from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class created """
    def __init__(self, size):
        """instantiates square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square object"""
        return (self.__size * self.__size)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
