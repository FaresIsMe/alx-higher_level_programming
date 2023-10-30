#!/usr/bin/python3
"""
Define a class Rectangle

A module that defines a class rectangle
"""


class Rectangle:
    """Rectangle representation"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width"""
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
        """Get the height"""
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
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        shape = ""

        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    shape += str(self.print_symbol)
                if i != self.__height - 1:
                    shape += '\n'
            return shape
        else:
            return shape

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor that decreases the number of instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle, or rect_1 if equals."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() >= rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with equal width and height."""
        return cls(size, size)
