#!/usr/bin/python3
"""Defines Base Class"""


class Base:
    """Represent a Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
