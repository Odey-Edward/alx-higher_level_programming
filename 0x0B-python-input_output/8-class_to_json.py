#!/usr/bin/python3
"""defined class_to_json function"""

def class_to_json(obj):
    """ returns the dictionary description with simple
    data structure for JSON serialization of an object"""
    return (vars(obj))
