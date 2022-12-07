#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = list(a_dictionary.values())[0]
        names = list(a_dictionary.keys())
        for val in list(a_dictionary.values()):
            if max_score < val:
                max_score = val
        max_score_name = names[list(a_dictionary.values()).index(max_score)]
        return max_score_name
