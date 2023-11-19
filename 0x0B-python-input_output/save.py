#!/usr/bin/python3
"""Defined save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)


save_to_json_file({1:'a', 2:'b', 3:'c'}, "eddy.json")
