#!/usr/bin/env python3
"""Defines the Square class."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a specialized rectangle."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        super().__init__(size, size)
