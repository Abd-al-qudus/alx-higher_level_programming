#!/usr/bin/python3

""" This module tokenize strings and print it
    in a  more specialized form..."""


def text_indentation(text):
    """this function tokenize texts and print new
        lines if any of ".?:" is encountered..."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    token = ".:?"
    i = 0
    while i < len(text):
        if text[i] in token:
            print(text[i])
            i = i + 1
            while text[i] == ' ':
                i = i + 1
            i -= 1
            print()
        else:
            print(text[i], end="")
        i = i + 1

