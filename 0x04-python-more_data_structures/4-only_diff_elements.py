#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        diff_A = {el for el in set_2 if el not in set_1}
        diff_B = {el for el in set_1 if el not in set_2}
        return diff_A ^ diff_B
