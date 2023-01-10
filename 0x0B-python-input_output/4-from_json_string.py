#!/usr/bin/python3

"""This module deserialize a json string to pyDataStructure"""
import json


def from_json_string(my_obj):
    """This function deserialize my_obj to pyDataStructure"""
    return json.loads(my_obj)
