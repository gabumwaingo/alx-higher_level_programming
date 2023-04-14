#!/usr/bin/python3
"""Module for save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """Writes n object to a text file"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
