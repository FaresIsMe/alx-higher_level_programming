#!/usr/bin/python3
"""
I wallahy don't know what is this
"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, 'r') as file:
        return json.loads(file.read())
