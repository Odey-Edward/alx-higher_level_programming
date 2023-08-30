#!/usr/bin/python3
''' A Square Class '''


class Square:
    ''' Defining a square class '''

    def __init__(self, size=0):
        ''' Initializing an object attribute
        Args: size: private instance attribute
        '''
        self.__size = size

    @property
    def size(self):
        ''' a getter function to retrive a size(a private attribute) '''
        return (self.__size)

    @size.setter
    def size(self, value):
        ''' setter function to set the size of a squnare instance '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' return the area of a square instance '''
        return (self.__size ** 2)
