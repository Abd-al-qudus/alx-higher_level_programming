#!/usr/bin/python3

"""This function checks whether a class
    is a subclass of another"""


def inherits_from(obj, a_class):
    """returns true if obj is subclass of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
