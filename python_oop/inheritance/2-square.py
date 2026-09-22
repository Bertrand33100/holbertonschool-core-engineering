#!/usr/bin/env python3
"""Defines the Square class."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a specialized rectangle."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a readable string representation of the square."""
        rect_str = super().__str__()
        return rect_str.replace("Rectangle", "Square", 1)
