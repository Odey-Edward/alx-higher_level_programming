#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        return (result)
    except (ZeroDivisionError, IndexError, TypeError, NameError) as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return (None)
