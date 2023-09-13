#!/usr/bin/python3
"""Pascal_triangle fuction module"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    pascal = []
    prev = []
    present = []

    if n <= 0:
        return (pascal)

    for i in range(n):
        if len(pascal) == 0:
            prev.append(1)
            pascal.append(prev[:])
        else:
            if len(prev) == 1:
                prev.append(1)
                pascal.append(prev[:])
            else:
                present.append(1)
                for j in range(len(prev)):
                    if j == len(prev) - 1:
                        present.append(1)
                    else:
                        present.append(prev[j] + prev[j+1])

                pascal.append(present)
                prev = present[:]
                present = []
    return (pascal)
