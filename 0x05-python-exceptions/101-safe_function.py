#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception:", ex, file=stderr)
    return None
