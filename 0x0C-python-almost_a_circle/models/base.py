#!/usr/bin/python3
"""Defines Base Class"""
import json


class Base:
    """Represent a Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        fil = cls.__name__ + ".json"
        listDic = []
        if list_objs is not None:
            for ob in list_objs:
                listDic.append(cls.to_dictionary(ob))
        with open(fil, "w") as f:
            f.write(cls.to_json_string(listDic))
