#!/usr/bin/python3
"""Checks if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """
    Returns true if obj is an instance in a_class
    otherwise false
    """
    return (type(obj) == a_class)
