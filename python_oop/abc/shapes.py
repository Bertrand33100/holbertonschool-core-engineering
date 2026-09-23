#!/usr/bin/env python

from abc import ABC, abstractclassmethod
import math


class Shape(ABC):
    """Abstarct class repreenting a Shape;"""

    @abstractclassmethod
    def area(self):
        """Calculate the area."""
        pass
    @abstractclassmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())