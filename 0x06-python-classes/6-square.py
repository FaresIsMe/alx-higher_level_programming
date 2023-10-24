#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square represtnation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialze a new Square.

        Args:
            size(int): The size of the square
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """Draws a square based on size"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print(" " * self.__position[0], end='')
            print('#' * self.__size)

    @property
    def position(self):
        "Gets and sets the positions inside the square."
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            self.__position = value
        else:
            print("position must be a tuple of 2 positive integers")
