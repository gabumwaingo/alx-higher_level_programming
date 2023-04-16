#!/usr/bin/python3
"""Module for a class student"""


class Student:
    """Defines class student
    Attributes
    first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs="none"):
        """Gets list representation of Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attribute instances of Student"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
