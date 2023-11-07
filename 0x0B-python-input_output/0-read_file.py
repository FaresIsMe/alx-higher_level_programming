#!/usr/bin/python3
"""
Defining read_file module
"""


def read_file(filename=""):
    """reads the file with utf-8"""
    with open(filename, 'r',  encoding="UTF-8") as file:
        read_data = file.read()
    print(read_data, end='')
