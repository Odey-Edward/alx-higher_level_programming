#!/usr/bin/python3
"""Defining BaseGeometry class"""


class BaseGeometry:
    """ BaseGeometry class, this class does nothing """

    def area(self):
        """that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value according to requirement"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value == float("inf"):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
