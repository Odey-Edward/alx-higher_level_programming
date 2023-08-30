#!/usr/bin/python3
''' A Square Class '''


class Square:
    ''' Defining a square class '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initializing an object attribute
        Args: size: private instance attribute
        '''
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) <= 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        ''' a getter function to retrive the position(a private attribute) '''
        return (self.__position)

    @position.setter
    def position(self, value):
        ''' setter function to set the position of a squnare instance '''

        p1, p2 = value
        if p1 < 0 or p2 < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = p1, p2

    def area(self):
        ''' return the area of a square instance '''
        return (self.__size ** 2)

    def my_print(self):
        '''prints in stdout the square with the character #'''
        
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
