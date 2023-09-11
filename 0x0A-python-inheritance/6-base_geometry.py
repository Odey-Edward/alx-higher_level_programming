#!/usr/bin/python3
"""Defining BaseGeometry class"""


class BaseGeometry:
    """ BaseGeometry class, this class does nothing """

    def area(self):
        """that raises an Exception"""
        raise Exception("area() is not implemented")
