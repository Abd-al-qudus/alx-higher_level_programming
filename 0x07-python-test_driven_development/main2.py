#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

new = [[2.0, 3, 4.3], [1, 0.76655, 0]]
print(matrix_divided(new, 2))
print(matrix)