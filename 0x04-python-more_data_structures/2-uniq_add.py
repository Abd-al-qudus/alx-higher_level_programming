#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        sum = 0
        for el in set(my_list):
            sum += el
        return sum
    return 0
