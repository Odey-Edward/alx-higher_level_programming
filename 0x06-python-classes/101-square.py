#!/usr/bin/python3
''' A Square Class '''


class Square:
    ''' Defining a square class '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initializing an object attribute
        Args:
            size (int): private instance attribute
            position (tuple): tuple of 2 positive integers
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
        ''' setter function to set the size of a squnare instance
        Args:
            value (int): positive integer'''

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
        ''' setter function to set the position of a squnare instance
        Args:
            value (tuple): tuple of 2 positive integers
        '''

        p1, p2 = value
        self.__position = p1, p2

    def area(self):
        ''' return the area of a square instance '''
        return (self.__size ** 2)

    def my_print(self):
        '''prints in stdout the square with the character'''

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print(end=self.__position[1] * "\n")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        '''define the string representation of the object when printed'''

        value = []
        if self.__size == 0:
            value.append("")
        else:
            if self.__position[1] > 0:
                value.append((self.__position[1] - 1) * "\n")
            for i in range(self.__size):
                s1 = " " * self.__position[0]
                s2 = "#" * self.__size
                value.append(s1 + s2)
        return("\n".join(value))
