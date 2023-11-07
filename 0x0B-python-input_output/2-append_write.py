#!/usr/bin/python3
"""
Define an append module
"""


def append_write(filename="", text=""):
    """Appends on a file with UTF-8"""
    with open(filename, mode='a', encoding="UTF-8") as file:
        return file.write(text)
