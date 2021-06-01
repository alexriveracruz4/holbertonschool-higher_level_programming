#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Class with area and integer validator public method"""
    def area(self):
        """Raise an exception when is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
