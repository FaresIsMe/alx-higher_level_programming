#!/usr/bin/python3
"""
Defining a write module
"""


def write_file(filename="", text=""):
    """Writes in a file"""
    with open(filename, mode='w', encoding="UTF-8") as file:
        return (file.write(text))
