#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializa a square.

        Args:
        size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrive size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return(self.__size * self.__size)
