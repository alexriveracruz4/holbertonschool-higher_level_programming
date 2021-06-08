#!/usr/bin/python3
"""Defines Base Class"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            file = csv.writer(f)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    file.writerow([obj.id, obj.width, obj.height, obj.x,
                                   obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    file.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        listOb = []
        try:
            with open(filename, "r") as f:
                bdata = csv.reader(f)
                for data in bdata:
                    if cls.__name__ is "Rectangle":
                        dic = {"id": int(data[0]), "width": int(data[1]),
                               "height": int(data[2]), "x": int(data[3]),
                               "y": int(data[4])}
                    elif cls.__name__ is "Square":
                        dic = {"id": int(data[0]), "size": int(data[1]),
                               "x": int(data[2]), "y": int(data[3])}
                    obj = cls.create(**dic)
                    listOb.append(obj)
        except:
            pass
        return(listOb)
