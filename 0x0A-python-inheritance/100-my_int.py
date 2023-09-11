#!/usr/bin/python3
"""Defining MyInt class"""


class MyInt(int):
    """a class MyInt that inherits from int"""

    def __eq__(self, other):
        """implement the equal to comparison
        operator"""
        return (type(self) == other)

    def __ne__(self, other):
        """implement the not equal comparison
        operator"""
        return (type(self) != other)
