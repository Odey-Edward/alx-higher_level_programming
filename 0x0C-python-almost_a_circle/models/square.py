#!/usr/bin/python3
"""A square class definition"""

from rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the string representation of the Square class"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter method for the square size"""
        return (self.width)

    @size.setter
    """setter method for the square size"""
    def size(self, value):
        self.width = value
        self.height = value
