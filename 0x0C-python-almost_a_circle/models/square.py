#!/usr/bin/python3
"""new class named square implemented with inheritance"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class defined by extending from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instatiating a Square object with the follwing attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation of the object"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width))
