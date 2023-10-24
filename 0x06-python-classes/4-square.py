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
        """Gets and sets the size of the square

        Returns:
            private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Square area

        Returns:
            the area.
        """
        return self.__size * self.__size
