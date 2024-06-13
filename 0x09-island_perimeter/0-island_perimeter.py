#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """ island perimeter """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four sides
                if r == 0 or grid[r-1][c] == 0:  # Check up
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # Check down
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Check left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # Check right
                    perimeter += 1

    return perimeter
