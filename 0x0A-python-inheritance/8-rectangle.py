#!/usr/bin/python3
"""
=========================
Define class BaseGeometry
=========================
"""


class BaseGeometry(object):
    """Class representaion"""
    pass

    def area(self):
        """Method raises and exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value"""
        if type(value) is int:
            if value > 0:
                pass
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


"""
============================
Define child class Rectangle
============================
"""


class Rectangle(BaseGeometry):
    """Class Representaion"""

    def __init__(self, width, height):
        """Intitilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
