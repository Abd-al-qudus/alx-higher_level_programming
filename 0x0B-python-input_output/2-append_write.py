#!/usr/bin/python3

"""This module appends to a file and return the number of chars added"""


def append_write(filename="", text=""):
    """The append_write function"""
    with open(filename, "a+", encoding="UTF8") as fob:
        fob.write(text)
    fob.close()
    return len(text)
