#!/usr/bin/env python3
"""Documentation du module."""


class Square:
    """Represent a square."""

    def __init(self, size):
        """Initialize a Square with a Validated Size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size