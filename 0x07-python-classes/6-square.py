#!/usr/bin/python3
"""
Module 6-square
provides several methods pertaining to the size of a square
"""


class Square:
    """
    class Square: contains getter/setter properties for 'size'
    and functions to calculate area and print the square
    """
    def __init__(self, size, position=(0, 0)):
        """
        initializes Square with 'size' and 'position'
        """
        self.handle_size_errors(size)
        self.handle_position_errors(position)
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """
        position getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter
        """
        handle_position_errors(position)
        self.__position = position

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.handle_size_errors(value)
        self.__size = value

    def area(self):
        """
        returns the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints square based on 'size' and 'position'
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(' ', end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def handle_size_errors(self, value):
        """
        checks if size is an integer and is >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def handle_position_errors(self, value):
        """
        checks if position is tuple of two positive integers
        """
        error = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(error)
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(error)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(error)
