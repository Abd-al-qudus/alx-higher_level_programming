#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        new = [True if my_list[i] % 2 == 0 else False
               for i in range(len(my_list))]
        return new
