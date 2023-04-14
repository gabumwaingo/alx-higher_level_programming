#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """Appends string at the end of the text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
