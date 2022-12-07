#!/usr/bin/python
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for k in sorted(a_dictionary.keys()):
            print(k, ": ", a_dictionary[k])
