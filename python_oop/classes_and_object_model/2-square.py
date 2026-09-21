#!/usr/bin/env python3
"""Documentation du module."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a Square with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
