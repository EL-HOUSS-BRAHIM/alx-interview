#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0

    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the land cell
                perimeter += 4

                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
