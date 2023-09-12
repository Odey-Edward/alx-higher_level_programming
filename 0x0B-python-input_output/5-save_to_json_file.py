#!/usr/bin/python3
"""Defined save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
