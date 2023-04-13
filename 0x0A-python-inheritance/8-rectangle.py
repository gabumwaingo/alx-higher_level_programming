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
