#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list or search or replace:
        new_list = list(el if el != search else replace for el in my_list)
        return new_list
