#!/usr/bin/python3
"""
student class module
"""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        """class initialziation"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation"""
        if attrs is not None:
            x = {i: self.__dict__[i] for i in self.__dict__.keys() & attrs}
            return x
        else:
            return self.__dict__
