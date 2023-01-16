#!/usr/bin/python3
"""This module is the base of the project"""


class Base:
    """This is the base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
