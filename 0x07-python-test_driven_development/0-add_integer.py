#!/usr/bin/python3

"""This module contains the add_integer function,
    which takes in two integers and return the sum.

    it works fine on numbers (integers and floats)
    and raises exception on invalid inputs....."""


def add_integer(a, b=98):
    """This function takes in two positional arguments,
     a and b are cast to integers before addition
     and standard exceptions are raised on error"""

    types_tuple = (float, int)
    if type(a) or type(b) not in types_tuple:
        if type(a) not in types_tuple:
            raise TypeError("a must be an integer")
        if type(b) not in types_tuple:
            raise TypeError("b must be an integer")
        a, b = int(a), int(b)
        return a + b
