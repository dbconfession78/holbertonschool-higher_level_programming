#!/usr/bin/python3
"""
Module 1-rectangle
provides several methods pertainning to the size of a rectangle
"""


class Rectangle:
    """
    defines a rectangle by:
      - private instance attributes 'width' and 'height'
      - Instantiation with optional 'width' and 'height'
    """

    def __init__(self, width=0, height=0):
        """
        initializes Rectangle with optional width and height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self.handle_width_errors(value)
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self.handle_height_errors(value)
        self.__height = value

    def handle_width_errors(self, width):
        """
        raises an error if width isn't a positive integer
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def handle_height_errors(self, height):
        """
        raises an error if height isn't a positive integer
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
