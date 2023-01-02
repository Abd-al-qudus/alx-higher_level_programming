#!/usr/bin/python3

"""This module takes in a matrix and an integer or float
    divisor, divides the matrix with the divisor and return
    the divided matrix. standard exceptions are raised on errors..."""


def matrix_divided(matrix, div):
    """This module takes in two arguments,a matrix and an int,
    divides and return the resulting matrix"""

    check = False
    icheck = False
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for el in matrix:
        for i in range(len(el)):
            if not isinstance(el[i], (float, int)) or \
                    el[i] == float('nan'):
                check = True
        if not isinstance(el, list):
            icheck = True
    if icheck:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    lengths = [len(el) for el in matrix]
    if max(lengths) > min(lengths):
        raise TypeError("Each row of the matrix must have the same size")
    if check:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)) or div == 0:
        if not isinstance(div, (float, int)):
            raise TypeError('div must be a number')
        else:
            raise ZeroDivisionError("division by zero")
    new_matrix = list(list(map(lambda x: list(map(lambda j: round(j/div, 2), x)), matrix)))
    return new_matrix

