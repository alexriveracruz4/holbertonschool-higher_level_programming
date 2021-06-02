#!/usr/bin/python3
"""Define BaseGeometry Class
Define Rectangle Subclass"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""
    def __init__(self, width, height):
        """Initialize the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return(self.__width * self.__height)

    def __str__(self):
        """Return print representation"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
