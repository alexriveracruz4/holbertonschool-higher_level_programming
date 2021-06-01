#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """Return true if obj is instance of a class that inherited from
    a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
