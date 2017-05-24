#!/usr/bin/python3
"""
Module 7-rectangle
provides several methods pertainning to the size of a rectangle
"""


class Rectangle:
    """
    defines a rectangle by:
      - private instance attributes 'width' and 'height'
      - instantiation with optional 'width' and 'height'
      - public instance method 'area'
      - public instance method 'perimeter'
      - public class instance 'number_of_instances' increments
      - public class attribute 'print_symbol'
        when class is instantiated
      - print() and str() print the rectangle using #
      - repr() returns a string representation of the rectangle
        so eval() can create a new instance
      - prints "Bye rectangle..." when an instance of Rectangle is deleted
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes Rectangle with optional width and height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        if class instance is arg of print(),
        this returns rectangle ASCII using '#'
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        string = (
            ((str(self.print_symbol) * self.__width) + "\n") * self.__height
            )
        return string[:-1]

    def __repr__(self):
        """
        returns a string representation of Rectangle instance
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        prints a message when an instancer of Rectangle is deleted
        """
        self.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """
        returns the area of a rectangle instance
        """
        self.handle_width_errors(self.__width)
        self.handle_height_errors(self.__height)
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimter of a rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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
