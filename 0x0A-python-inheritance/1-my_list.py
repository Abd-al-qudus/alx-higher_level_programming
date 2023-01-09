#!/usr/bin/python3

"""This function inherit from built-in list
    """


class MyList(list):
    """My list class
    """

    def __init__(self):
        """initialize the class attributes"""
        super().__init__()

    def print_sorted(self):
        """print the list elements in sorted order
        """
        print(sorted(self))
