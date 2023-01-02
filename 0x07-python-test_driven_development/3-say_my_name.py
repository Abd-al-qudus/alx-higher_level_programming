#!/usr/bin/python3

"""
    This module takes in two arguments and print
    the formatted name of the user
"""


def say_my_name(first_name, last_name=""):
    """
        this function prints the name of a full name of a user.
        Exceptions are raised on standard errors
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
