#!/usr/bin/python3
def max_integer(my_list=[]):
    max_nu = None
    if len(my_list) < 1:
        return (max_nu)
    max_nu = 0
    for i in my_list:
        if max_nu < i:
            max_nu = i
    return ("{:d}".format(max_nu))
