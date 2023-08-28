#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        count += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            print()
            return (i)
    print()
    return (count)
