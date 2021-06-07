#!/usr/bin/python3
"""Defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print representation"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width))

    @property
    def size(self):
        """Getter size of Square"""
        return(self.width)

    @size.setter
    def size(self, value):
        """Setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return(dic)
