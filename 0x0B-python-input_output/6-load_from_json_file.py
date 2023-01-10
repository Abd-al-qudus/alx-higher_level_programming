#!/usr/bin/python3

"""This module load json object to PyObject"""
import json


def load_from_json_file(filename):
    """This function deserialize a json object to a PyObject"""
    with open(filename) as fob:
        file = json.load(fob)
    return file
