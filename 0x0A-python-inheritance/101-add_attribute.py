#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, att, value):
    """Defines a function that adds attributes to objects."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
