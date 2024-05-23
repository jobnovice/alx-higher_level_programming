#!/usr/bin/python3
"""again same class with added usecase"""


class BaseGeometry:
    """base class for geometry objects"""
    def area(self):
        """returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """it validates the value of the integer
            Args:
                name: is a string that represents the name of the value
                value: is an integer value
            Returns: nothing new
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


# b1 = BaseGeometry()
# BaseGeometry.area()

# b1.integer_validator("int")
