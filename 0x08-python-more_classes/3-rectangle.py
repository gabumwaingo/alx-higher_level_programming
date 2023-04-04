#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents attributes of the rectange"""
    def __init__(self, width=0, height=0):
        """initialises the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area of the rwctangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Gets the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        """Prints the rectangle"""
        string = ""
        if self.__height != 0 and self.__width != 0:
            print()
        else:
            string += "\n".join(
                    "#" * self.__width for j in range(self.__height))
        return string
