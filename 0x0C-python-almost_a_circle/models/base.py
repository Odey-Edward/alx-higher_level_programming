#!/usr/bin/python3
"""A custom base class definition"""


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initailization of the attribute"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
