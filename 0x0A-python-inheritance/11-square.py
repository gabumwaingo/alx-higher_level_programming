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


class Square(Rectangle):
    """Square subclass to rectangle subclass"""
    def __init__(self, size):
        """Initializer for square subclass"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
