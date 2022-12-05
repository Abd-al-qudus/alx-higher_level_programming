#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in range(len(i)):
                print("{:d}".format(i[j]), end=" " if j != i[-1] else "")
            print()
