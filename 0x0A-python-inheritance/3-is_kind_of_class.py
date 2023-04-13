#!/usr/bin/python3
"""
Checks if object is an instance of a class that inherited from
the class
"""


def is_kind_of_class(obj, a_class):
    """
    Return true if it is an instance of the child or parent
    Otherwise false
    """
    return (isinstance(obj, a_class))
