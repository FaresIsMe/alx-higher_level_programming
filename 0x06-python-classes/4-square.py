#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square represtnation."""

    def __init__(self, size=0):
        """Initialze a new Square.

        Args:
            size(int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square
        
        Returns: private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """

        if not isinstance(value, int):
            raise TypeError("size must be integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Square area
        Args:
            a(int): Are of the square
        """
        a = self.__size * self.__size
        return a
