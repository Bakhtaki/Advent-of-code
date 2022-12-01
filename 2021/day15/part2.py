"""
Advent of the code 2021.

day15 part 1,2.
"""

import heapq
import pprint as pp
from collections import defaultdict


def get_data(filename):
    """Read the data from the file."""
    data = []
    with open(filename, 'r', encoding='utf8') as file:
        raw_data = file.read().strip().split()
        data = [[int(x) for x in line] for line in raw_data]
        return data


def part2(grid):
    """Find Cost Of Shortest Path."""
    max_row = len(grid)
    max_col = len(grid[0])

    rows = max_row * 5
    cols = max_col * 5

    def extended_map(r, c):
        updated_point = (grid[r % max_row][c % max_col] +
                         r // max_row + c // max_col)
        return (updated_point - 1) % 9 + 1

    # Define Cost Dictionary
    cost = defaultdict(int)

    # Define Priority Queue:
    pq = [(0, 0, 0)]

    # Define visited
    visited = set()

    # heapfiy the queue
    heapq.heapify(pq)

    # Loop through the queue
    while len(pq) > 0:
        # Get the current node
        point_cost, current_row, current_col = heapq.heappop(pq)

        # Check in current node is visited
        if (current_row, current_col) in visited:
            continue

        # Add current node to visited
        visited.add((current_row, current_col))

        # Update cost
        cost[(current_row, current_col)] = point_cost

        # Check if we are at the end
        if current_row == rows - 1 and current_col == cols - 1:
            break

        # Get the current node's neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Get the new row and column
            rr = current_row + dr
            cc = current_col + dc
            # Check if the new row and column are valid
            if not (0 <= rr < rows and 0 <= cc < cols):
                continue
            # Add the new node to the queue
            heapq.heappush(pq, (point_cost + extended_map(rr,cc), rr, cc))

    # Print the cost
    pp.pprint(f'Cost:{cost[(rows - 1, cols - 1)]}')


def main():
    """Control the program."""
    data = get_data('day15.txt')
    # pp.pprint(data)
    part2(data)


if __name__ == '__main__':
    main()
