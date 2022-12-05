#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx > length:
        return None
    if not my_list[idx]:
        return None
    else:
        print("Element at index {0} is {1:d}".format(idx, my_list[idx]))
