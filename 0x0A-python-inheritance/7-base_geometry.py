#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Area public attribute"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
