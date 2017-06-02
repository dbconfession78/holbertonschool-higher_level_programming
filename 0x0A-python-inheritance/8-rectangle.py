#!/usr/bin/python3
"""
Module:  8-rectangle.py
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
      - `width` and `height` must be private
      - `width` and `height` must be positive integers validated by
        `integer_validator`
    """
    def __init__(self, width, height):
        """
        uses the superclass method, integer_validtaor() to
        confirm 'width' and 'height' are both positive integers
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
