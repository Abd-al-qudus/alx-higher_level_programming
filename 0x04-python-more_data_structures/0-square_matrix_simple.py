#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = list(list(map(lambda el: [y**2 for y in el],
                                   (el for el in matrix))))
        return new_matrix
