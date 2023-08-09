#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            n = 32
        else:
            n = 0
        print("{:c}".format(ord(i) - n), end="")
    print()
