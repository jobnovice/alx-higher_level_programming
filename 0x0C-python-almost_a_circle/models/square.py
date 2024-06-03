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

    @property
    def size(self):
        """Returns the size of the square which are the width and height"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square which are the width
            and height of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square with one of the argument type"""
        if len(args) >= 1:
            j = 0
            for i in range(len(args)):
                if j == 0:
                    self.id = args[0]
                    j += 1
                elif j == 1:
                    self.width = args[1]
                    self.height = args[1]
                    j += 1
                elif j == 2:
                    self.x = args[2]
                    j += 1
                elif j == 3:
                    self.y = args[3]
                    j += 1
        elif kwargs:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the object"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        }
