#!/usr/bin/python3
"""A custom base class definition"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or len(list_dictionaries) == 0:
            return ([])
        return (json.dumps(list_dictionaries))
