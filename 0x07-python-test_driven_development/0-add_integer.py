#!/usr/bin/python3
"""
0-add_integer module

Define function add_integer(a, b=89)
"""


def add_integer(a, b=98):
    """
    Returns addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
