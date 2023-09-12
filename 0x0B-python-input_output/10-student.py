#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """Initializing a Student instance variable"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all(type(el) == str for el in attrs):
            atr_dict = {}
            for a in attrs:
                if hasattr(self, a):
                    atr_dict[a] = getattr(self, a)
            return (atr_dict)
        else:
            return (vars(self))
