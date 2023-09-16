#!/usr/bin/python3
"""Defination of a Rectangle class"""

from base import Base


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
        self.__y = value
