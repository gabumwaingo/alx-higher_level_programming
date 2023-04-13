#!/usr/bin/python3
"""Base geometry class and subclass of rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle"""
    def __init__(self, width, height):
        """Instantation of rectagle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Prints the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
