#!/usr/bin/python3
"""function find_peak"""


def find_peak(list_of_integers):
    """find peak in a list of unsorted integers"""
    if not list_of_integers:
        return

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    return recursive(0, len(list_of_integers) - 1, list_of_integers)


def recursive(start, end, list_items):
    """healper function to find_peak"""
    if start >= end:
        return 0

    _len = end / 2

    value1 = recursive(start, _len, list_items)
    value2 = recursive(_len, end, list_items)

    if value1 > value2:
        return value1

    return value2
