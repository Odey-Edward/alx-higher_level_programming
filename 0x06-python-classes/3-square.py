#!/usr/bin/python3
''' creating a Square class '''


class Square:
    ''' Defining a Square class '''

    def __init__(self, size=0):
        ''' Initializing a square attribute
        Args:
            size: A private attribute instance
        '''

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' return the area of the current square '''

        return (self.__size ** 2)
