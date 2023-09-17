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
    def size(self, value):
        """setter method for the square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class, assigns argument to each attribute"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
