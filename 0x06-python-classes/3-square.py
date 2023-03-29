#!/usr/bin/python3
"""define square class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialises the class
        Arg:
        size(int: the size of a side of the square
        Return: nothing
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Gets the area of the square
        Args:
        size: size of the square
        Return: the area of the square
        """
        self.__area = self.__size**2
        return self.__area
