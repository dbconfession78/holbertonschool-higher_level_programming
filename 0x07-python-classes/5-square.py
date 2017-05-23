#!/usr/bin/python3
"""
Module 5-square
calcualates the area of a square
"""


class Square:
    """
    class Square: contains getter/setter properties for 'size'
    and functions to calculate area and print the square
    """
    def __init__(self, size):
        self.handle_errors(size)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.handle_errors(value)
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    def handle_errors(self, value):
        """
        checks if size is an integer and is >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
