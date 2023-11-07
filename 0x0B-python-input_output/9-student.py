#!/usr/bin/python3
"""
student class module
"""


class Studen():
    """Student"""

    def __init__(self, first_name, last_name, age):
        """class initialziation"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation"""
        return self.__dict__
