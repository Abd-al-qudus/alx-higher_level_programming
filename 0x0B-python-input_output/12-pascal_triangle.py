#!/usr/bin/python3

""""Pascal triangle module"""


def pascal_triangle(n):
    """pascal triangle function"""
    triangle = []
    for i in range(n):
        triangle.append(list(map(lambda x: int(x), str(11 ** i))))
    return triangle
