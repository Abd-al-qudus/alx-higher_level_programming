#!/usr/bin/python3

"""This module serialize a pyDataStructure to json string"""
import json


def to_json_string(my_obj):
    """This function serialize my_obj to json string"""
    return json.dumps(my_obj)
