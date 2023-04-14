#!/usr/bin/python3
"""Module of from_json_string"""


def from_json_string(my_str):
    """Converts json script to string object"""
    import json
    return json.loads(my_str)
