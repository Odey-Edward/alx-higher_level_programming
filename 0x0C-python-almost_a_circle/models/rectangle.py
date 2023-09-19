#!/usr/bin/python3
"""Defination of a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for the private
        instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter method for the private
        instance attribute width"""
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter method for the private
        instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter method for the private
        instance attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter method for the private
        instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """setter method for the private
        instanceattribute x"""
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter method for the private
        instance attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """setter method for the provate
        instance attribute y"""
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print(end="\n" * self.y)
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return the string representation of the Rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the class, assigns argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        d = {}

        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y

        return (d)
