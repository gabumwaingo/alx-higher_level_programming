#!/usr/bin/python3
"""define square class"""


class Square:
    """Represents a square
    Attributes:
    __size(Int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the class
        Arguments:
        size(int): size of a side of the square
        Returns: nothing
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
