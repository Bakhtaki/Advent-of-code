"""Advent of code 2022 day 8."""

import sys
import numpy as np


# Define Functions
def visible_trees(grid, x, y):
    """Count visible_trees in the grid."""
    visible_trees = 0

    # Check all directions
    for i in range(x):
        for j in range(y):
            value = grid[i, j]
            if j == 0 or np.amax(grid[i, :j]) < value:
                visible_trees += 1
            elif j == y - 1 or np.amax(grid[i, j + 1:]) < value:
                visible_trees += 1
            elif i == 0 or np.amax(grid[:i, j]) < value:
                visible_trees += 1
            elif i == x - 1 or np.amax(grid[i + 1:, j]) < value:
                visible_trees += 1
    return visible_trees


# Function for part2
def view_score(grid, n, m):
    """Return Maximum score of the view  base on question rules."""
    # Get Maximum view_score
    answer = 0
    dd = [[0, 1], [0 , -1], [1, 0], [-1, 0]]

    for i in range(n):
        for j in range(m):
            value = grid[i, j]
            score = 1
            # Check all directions
            for di, dj in dd:
                x, y = i, j
                distance = 0
                x += di
                y += dj

                while (0 <= x < n and 0 <= y < m) and grid[x, y] < value:
                    distance += 1
                    x += di
                    y += dj

                    if (0 <= x < n and 0 <= y < m) and grid[x, y] > value:
                        distance += 1
                score *= distance
            answer = max(answer, score)
    return answer


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        data = file.read().strip().split()


    grid = [list(map(int, list(line))) for line in data]
    n = len(grid)
    m = len(grid[0])
    grid = np.array(grid)

    # Part 1
    visible = visible_trees(grid, n, m)
    print(f'Part 1: {visible}')

    # Part 2.
    score = view_score(grid, n, m)
    print(f'Part 2: {score}')


