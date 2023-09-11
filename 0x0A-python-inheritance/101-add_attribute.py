#!/usr/bin/python3
"""Define add_attribute function"""


def add_attribute(obj, name, value):
    """ function that adds a new attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
