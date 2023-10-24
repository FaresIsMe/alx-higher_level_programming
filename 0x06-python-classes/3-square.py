#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square represtnation."""

    def __init__(self, size=0):
        """Initialze a new Square.

        Args:
            size(int): The size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Square area
        Args:
            a(int): Are of the square
        """
        a = self.__size * self.__size
        return a
