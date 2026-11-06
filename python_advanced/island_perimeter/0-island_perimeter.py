#!/usr/bin/python3
"""Calculate the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island represented by ``grid``.

    Each land cell contributes four sides. Every shared side between two
    adjacent land cells removes two sides from the perimeter.
    """
    perimeter = 0

    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if cell != 1:
                continue

            perimeter += 4

            if column_index + 1 < len(row) and row[column_index + 1] == 1:
                perimeter -= 2
            if (row_index + 1 < len(grid) and
                    grid[row_index + 1][column_index] == 1):
                perimeter -= 2

    return perimeter
