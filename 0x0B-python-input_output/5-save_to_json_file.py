#!/usr/bin/python3
"""
I wallahy don't know what is this
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding="UTF-8") as file:
        x = json.dumps(my_obj)
        file.write(x)
