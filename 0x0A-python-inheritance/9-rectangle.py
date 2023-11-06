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
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to get Rectangles area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
