#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
============================
Define child class Rectangle
============================
"""


class Rectangle(BaseGeometry):
    """Class Representaion"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.width = width
        self.integer_validator("height", height)
        self.width = height
