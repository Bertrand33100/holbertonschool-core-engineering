#!/usr/bin/env python3
"""Defines the VerboseList class."""


class VerboseList(list):
    """A list that displays messages when modified."""

    def append(self, item):
        """Add an item and display a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and display the number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and display a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item with a message."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
