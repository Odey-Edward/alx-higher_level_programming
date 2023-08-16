#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for list_ in matrix:
       squared_matrix.append(list( map((lambda x: x ** 2), list_)))
    return (squared_matrix)
