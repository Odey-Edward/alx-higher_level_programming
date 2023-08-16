#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for value in matrix:
        squared_matrix.append([x ** 2 for x in value])
    return (squared_matrix)
