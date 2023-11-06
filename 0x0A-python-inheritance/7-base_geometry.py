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
