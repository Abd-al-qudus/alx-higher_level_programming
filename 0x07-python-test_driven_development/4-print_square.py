#!/usr/bin/python3

"""
    This module prints # as a square matrix of value size.
"""


def print_square(size):
    """
        This function takes an argument size and
        prints a square matrix in the # pattern
    """
    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()


