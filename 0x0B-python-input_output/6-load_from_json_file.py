#!/usr/bin/python3
"""Defined load_from_json_file function"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, encoding='UTF-8') as f:
        return (json.load(f))
