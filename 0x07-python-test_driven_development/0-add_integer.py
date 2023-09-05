#!/usr/bin/python3
"""
This is a '0-add_integer' module

adds 2 integers and return the result
"""


def add_integer(a, b=98):
    """return the result of the addition a and b.
    raise a TypeError if a or b are neither float or integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
