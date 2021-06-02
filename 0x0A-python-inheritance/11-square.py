#!/usr/bin/python3
"""Define Rectangle Class
Define Square Subclass"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """Initialize the Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of square"""
        return(self.__size ** 2)

    def __str__(self):
        """Representation of teh print of square"""
        return("[Square] {}/{}".format(self.__size, self.__size))
