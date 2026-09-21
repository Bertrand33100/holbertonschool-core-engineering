#!/usr/bin/env python3
"""Documentation du module."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a Square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
