#!/usr/bin/python3
"""Defining Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """initialize and validate attributes"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of a Square"""
        return (self.__size ** 2)

    def __str__(self):
        """String representation of the Square class"""
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
