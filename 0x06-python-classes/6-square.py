#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializa a square.

        Args:
        size (int): The size of the square.
        position (tuple):
        """
        self.size = size
        self.position = position

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
            self.__size = value

    @property
    def position(self):
        """Retrive position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Set position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:

            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print("".join([" " for k in range(self.__position[0])]),
                      end="")
                print("".join(["#" for l in range(self.__size)]))
