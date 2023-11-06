#!/usr/bin/python3
"""
Module with the method lookpu
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return sorted(dir(obj))
