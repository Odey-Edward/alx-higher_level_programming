#!/usr/bin/python3
"""
Divides all elements of a matrix, and return a new matrix

All matrix values must be integers/floats
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    if not all(isinstance(el, list) for el in matrix) or\
            any((len(el) == 0) for el in matrix):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    if not all(isinstance(i, (int, float)) for el in matrix for i in el):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if i < len(matrix) - 1:
            if not (len(matrix[i]) == len(matrix[i+1])):
                raise TypeError("Each row of the matrix\
 must have the same size")

    new = []
    for el in matrix:
        new.append(list(map(lambda i: round(i / div, 2), el)))
    return (new)
