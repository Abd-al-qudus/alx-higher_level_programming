#!/usr/bin/python3

"""This function checks whether a class is an
    instance of another or inherits from another"""


def is_kind_of_class(obj, a_class):
    """returns True when obj is an instance
        or subclass of a_class"""

    if not isinstance(obj, a_class):
        return False
    return True
