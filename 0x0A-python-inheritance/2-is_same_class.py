#!/usr/bin/python3

"""This function checks whether a var
    is an instance of another var"""


def is_same_class(obj, a_class):
    """returns true if obj is an instance of a_class
    """

    if type(obj) != a_class:
        return False
    return True
