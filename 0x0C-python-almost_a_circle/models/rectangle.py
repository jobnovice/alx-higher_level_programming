#!/usr/bin/python3
""" Module that defines the Rectangle class, inheriting from the Base class."""

#from base import Base


# class Rectangle(Base):
    # """A rectangle that inherits from the base class Base."""

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Instantiates a new Rectangle object.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int): The x coordinate. Defaults to 0.
#             y (int): The y coordinate. Defaults to 0.
#             id (int): The id of the object. Defaults to None.
#         """
#         super().__init__(id)  # Corrected the call to super()
#         # self.width = width
#         # self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Gets the width of the rectangle."""
#         return self.__width

#     @width.setter
#     def width(self, width):
#         """
#         Sets the width of the rectangle.

#         Args:
#             width (int): The width of the rectangle.

#         Raises:
#             ValueError: If width is less than or equal to zero.
#             TypeError: If width is not an integer.
#         """
#         if not isinstance(width, int):
#             raise TypeError("width must be an integer")
#         if width <= 0:
#             raise ValueError("width must be greater than zero")
#         self.__width = width

#     @property
#     def height(self):
#         """Gets the height of the rectangle."""
#         return self.__height

#     @height.setter
#     def height(self, height):
#         """
#         Sets the height of the rectangle.

#         Args:
#             height (int): The height of the rectangle.

#         Raises:
#             ValueError: If height is less than or equal to zero.
#             TypeError: If height is not an integer.
#         """
#         if not isinstance(height, int):
#             raise TypeError("height must be an integer")
#         if height <= 0:
#             raise ValueError("height must be greater than zero")
#         self.__height = height

#     @property
#     def x(self):
#         """Gets the x coordinate of the rectangle."""
#         return self.__x

#     @x.setter
#     def x(self, x):
#         """
#         Sets the x coordinate of the rectangle.

#         Args:
#             x (int): The x coordinate of the rectangle.

#         Raises:
#             ValueError: If x is less than zero.
#             TypeError: If x is not an integer.
#         """
#         if not isinstance(x, int):
#             raise TypeError("x must be an integer")
#         if x < 0:
#             raise ValueError("x must be greater than or equal to zero")
#         self.__x = x

#     @property
#     def y(self):
#         """Gets the y coordinate of the rectangle."""
#         return self.__y

#     @y.setter
#     def y(self, y):
#         """
#         Sets the y coordinate of the rectangle.

#         Args:
#             y (int): The y coordinate of the rectangle.

#         Raises:
#             ValueError: If y is less than zero.
#             TypeError: If y is not an integer.
#         """
#         if not isinstance(y, int):
#             raise TypeError("y must be an integer")
#         if y < 0:
#             raise ValueError("y must be greater than or equal to zero")
#         self.__y = y
