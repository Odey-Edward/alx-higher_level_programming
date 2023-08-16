#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for list_ in matrix:
       squared_matrix.append([i ** 2 for i in list_])
    return (squared_matrix)
