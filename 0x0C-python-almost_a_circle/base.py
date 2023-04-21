#!/usr/bin/python3
"""Defines a class Base"""


import json
import unittest


class Base:
    """Base class for all other classes in the project"""
    __nb_objects = 0
    """Private attribute"""

    def __init__(self, id=None):
        """Initialises the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns json string represenytation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
