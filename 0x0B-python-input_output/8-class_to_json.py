#!/usr/bin/python3

"""This module converts pyObject to Json"""


def class_to_json(obj):
    """returns the json equivalence of the PyObject"""
    json_data = {}
    for key in obj.__dict__:
        val = getattr(obj, key)
        if isinstance(val, (list, int, dict, str, bool)):
            json_data[key] = val
    return json_data
