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
