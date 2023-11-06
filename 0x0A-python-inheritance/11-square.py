#!/usr/bin/python3
"""
===================
Square Class Module
===================
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initilize Square method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
