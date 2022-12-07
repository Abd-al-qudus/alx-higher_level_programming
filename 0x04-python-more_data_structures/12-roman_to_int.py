#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    output = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        if i+1 < len(roman_string) and\
            roman_dict[roman_string[i]]\
                < roman_dict[roman_string[i + 1]]:
            output -= roman_dict[roman_string[i]]
        else:
            output += roman_dict[roman_string[i]]
    return output
