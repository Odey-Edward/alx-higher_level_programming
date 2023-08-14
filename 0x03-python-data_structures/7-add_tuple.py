#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple1 = tuple_a + (0, 0)
    new_tuple2 = tuple_b + (0, 0)

    result = (new_tuple1[0] + new_tuple2[0]), (new_tuple1[1] + new_tuple2[1])
    return (result)
