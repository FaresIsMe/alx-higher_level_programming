#!/usr/bin/python3
"""Define a class Rectangle

A module that defines a class rectangle

"""


class Rectangle:
    """Rectangle represtnation"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """sets the shape of the rectangle to be printed"""
        shape = ""
        
        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    shape += '#'
                if i != self.__height - 1:
                    shape += '\n'
            return shape
        else:
            return shape
