#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Class with method area"""
    def area(self):
        """Raise an exception when is called"""
        raise Exception("area() is not implemented")
