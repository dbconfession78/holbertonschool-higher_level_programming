#!/usr/bin/python3
"""
Module:  11-square.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    inherits from `Rectangle`, which inherits from BaseGeometry
    """
    def __init__(self, size):
        """
        initializes Square and makes Rectangle's public attributes accessbile
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
