#!/usr/bin/python3
''' creating a square class '''

class Square:
    ''' A square class '''

    def __init__(self, size=0):
        if size < 0:
            raise ValueError("
        if isinstance(size, int):
            self.__size = size
