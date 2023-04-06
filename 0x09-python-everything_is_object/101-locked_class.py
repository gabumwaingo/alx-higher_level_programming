#!/usr/bin/python3
"""class to prevent dynamic crewrion of attributes"""


class LockedClass:
    """attribute allowed"""

    __slots__ = ["first_name"]
