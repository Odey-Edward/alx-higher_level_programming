#!/usr/bin/python3
def max_integer(my_list=[]):
    max_nu = 0
    if not my_list:
        return (None)
    for i in my_list:
        if max_nu < i:
            max_nu = i
    return (max_nu)
