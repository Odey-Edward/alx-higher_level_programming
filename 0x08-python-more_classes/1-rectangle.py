#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializing the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter method for the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height to value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
