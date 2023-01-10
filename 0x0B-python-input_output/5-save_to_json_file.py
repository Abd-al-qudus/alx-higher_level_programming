#!/usr/bin/python3

"""This module saves file to json object"""
import json


def save_to_json_file(my_obj, filename):
    """This function serialize an object to a json file"""
    with open(filename, "w") as fob:
        json.dump(my_obj, fob)
    fob.close()
