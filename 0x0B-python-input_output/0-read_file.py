#!/usr/bin/python3

"""This function reads from a file and print to standard output."""


def read_file(filename=""):
    """opens a file and print to stdout"""
    with open(filename, encoding="utf-8") as fob:
        file = fob.read()
        print(file)
    fob.close()
