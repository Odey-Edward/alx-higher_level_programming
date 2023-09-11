#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """MyList class, subclass of the list class"""

    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
