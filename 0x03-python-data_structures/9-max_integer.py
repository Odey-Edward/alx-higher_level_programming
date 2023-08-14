#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        max_nu = None
    else:
        max_nu = my_list[0]
        for i in my_list:
            if max_nu < i:
                max_nu = i
    return (max_nu)
