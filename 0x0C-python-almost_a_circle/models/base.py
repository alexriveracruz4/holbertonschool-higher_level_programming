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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return([])
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        li = []
        try:
            with open(filename, "r") as f:
                li = cls.from_json_string(f.read())
            for i, v in enumerate(li):
                li[i] = cls.create(**li[i])
        except:
            pass
        return(li)
