#!/usr/bin/python3
"""
Module that defines the Rectangle class, inheriting from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """A rectangle that inherits from the base class Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate. Defaults to 0.
            y (int): The y coordinate. Defaults to 0.
            id (int): The id of the object. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            ValueError: If width is less than or equal to zero.
            TypeError: If width is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            ValueError: If height is less than or equal to zero.
            TypeError: If height is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x coordinate of the rectangle.

        Args:
            value (int): The x coordinate of the rectangle.

        Raises:
            ValueError: If x is less than zero.
            TypeError: If x is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y coordinate of the rectangle.

        Args:
            value (int): The y coordinate of the rectangle.

        Raises:
            ValueError: If y is less than zero.
            TypeError: If y is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """displys to the stdout the rectangle instance"""

        {print() for x in range(self.y)}
        for i in range(self.__height):
            {print(" ", end="") for x in range(self.x)}
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns the string representation of the object"""
        return ("[{}] ({}) {}/{} - {}/{}").format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to an attribute"""

        if len(args) >= 1:
            j = 0
            for i in range(len(args)):
                if j == 0:
                    self.id = args[0]
                    j += 1
                elif j == 1:
                    self.width = args[1]
                    j += 1
                elif j == 2:
                    self.height = args[2]
                    j += 1
                elif j == 3:
                    self.x = args[3]
                    j += 1
                elif j == 4:
                    self.y = args[4]
        elif kwargs:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the object"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
