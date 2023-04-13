#!/usr/bin/python3
"""Illustrating inheritance in classes"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """Initialises subclass"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
