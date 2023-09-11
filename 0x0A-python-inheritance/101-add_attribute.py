#!/usr/bin/python3
"""Define add_attribute function"""


def add_attribute(obj, name, value):
    """ function that adds a new attribute to an object"""

    if isinstance(obj, (str, tuple, int)):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
