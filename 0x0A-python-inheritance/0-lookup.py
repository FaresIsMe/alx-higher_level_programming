#!/usr/bin/python3
def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return sorted(dir(obj))
