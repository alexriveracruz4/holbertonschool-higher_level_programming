#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize tha class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return(self.__dict__)
        newDict = {}
        for at in attrs:
            try:
                newDict[at] = self.__dict__[at]
            except:
                pass
        return newDict
