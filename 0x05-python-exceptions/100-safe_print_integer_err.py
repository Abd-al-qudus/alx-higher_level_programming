#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except Exception as err:
        print("Exception:", err, file=stderr)
        return False
