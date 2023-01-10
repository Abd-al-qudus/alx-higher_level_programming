#!/usr/bin/python3

"""This module writes to a file and return the character count"""


def write_file(filename="", text=""):
    """opens a file/ create if it doesn't exit and return the char count"""
    with open(filename, "w", encoding="UTF8") as fob:
        file = fob.write(text)
    fob.close()
    return len(text)
