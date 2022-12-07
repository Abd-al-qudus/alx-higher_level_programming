#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        common = {el for el in set_1 if el in set_2}
        return common
