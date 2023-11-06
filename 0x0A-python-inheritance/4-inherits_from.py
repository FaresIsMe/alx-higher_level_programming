#!/usr/bin/python3
"""
=====================
Module to check class
=====================
"""


def inherits_from(obj, a_class):
    """is same class?"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
