#!/usr/bin/python3
''' creating a square class '''

class Square:
    ''' A square class '''

    def __init__(self, size=0):
        ''' initializing size
            Args: size: private instance variable
        '''

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
