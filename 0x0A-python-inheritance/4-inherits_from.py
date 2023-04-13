#!/usr/bin/python3
"""
Checks if obj is an instancr of a class that inherited
directly or indeirectly from a_class
"""


def inherits_from(obj, a_class):
    """Returns true if obj is from a_class and false if not"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
