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
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return ([])
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        cls_list = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for instance in list_objs:
                cls_list.append(cls.to_dictionary(instance))

        with open(filename, "w", encoding="UTF-8") as f:
            f.write(str(cls.to_json_string(cls_list)))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string:
            return (json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            new = cls(1, 1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        value = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
        except FileNotFoundError:
            return (value)

        for inst in instances:
            value.append(cls.create(**inst))

        return (value)
