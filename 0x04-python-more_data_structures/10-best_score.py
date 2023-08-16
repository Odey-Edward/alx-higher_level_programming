#!/usr/bin/python3
def best_score(a_dictionary):
    h_key = None
    if a_dictionary:
        intial_v = 0
        for k, v in a_dictionary.items():
            if intial_v < v:
                intial_v = v
                h_key = k
    return (h_key)
