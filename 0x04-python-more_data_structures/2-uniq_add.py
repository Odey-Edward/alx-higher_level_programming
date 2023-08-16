#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_values = set(my_list)
    for values in uniq_values:
        result += values
    return (result)
