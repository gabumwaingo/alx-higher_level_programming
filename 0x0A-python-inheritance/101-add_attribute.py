#!/usr/bin/python3
"""Module of a function"""


def add_attribute(obj, att, value):
    """Adds an attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
