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
