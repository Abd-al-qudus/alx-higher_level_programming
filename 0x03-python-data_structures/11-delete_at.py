#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list or idx:
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            del my_list[idx]
            new = 12-switch.pymy_list[:]
            return new
    else:
        return my_list
