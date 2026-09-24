#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Make the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Display the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Make the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """Display the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish."""

    def fly(self):
        """Make the flying fish soar."""
        print("The flying fish is soaring!")

    def swim(self):
        """Make the flying fish swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Display the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")


flying_fish = FlyingFish()

flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print(FlyingFish.mro())
