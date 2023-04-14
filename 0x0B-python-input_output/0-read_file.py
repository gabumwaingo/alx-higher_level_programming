#!/usr/bin/python3
"""Module of a function"""


def read_file(filename=""):
    """Reads a txt file and returns content in stdout"""
    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
