#!/usr/bin/python3
"""
prints a square with the character #
size must be an integer and greater then or equal to 0
otherwise raise a TypeError exception
"""


def print_square(size):
    """prints a square with the character #"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
