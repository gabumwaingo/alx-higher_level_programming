#!/usr/bin/python3
"""defines square class"""


class Square:
    """Represents attributes of the square
    Attributes:
    __size(int): size of a side of the square
    """
    def __init__(self, size):
        """Initialises the square
        Atributes:
        size(int): size of a side of the square
        Returs: none
        """
        self.__size = size
