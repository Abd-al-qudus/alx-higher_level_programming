#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a or tuple_b:
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
        answer = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return answer
    else:
        return 0, 0
