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


def part1(map):
    """Find the shortest path with Dijkstra algorithm.

    Args:
        map (list): 2 dimension list of Cost
    """
    row_max = len(map)
    col_max = len(map[0])

    # Define Cost Dictionary
    cost = defaultdict(int)

    # Create heapq
    pq = [(0, 0, 0)]

    # Convert pq to heapq
    heapq.heapify(pq)

    # Define Visited set
    visited = set()

    # Define the result
    while len(pq) > 0:
        point_cost, current_row, current_col = heapq.heappop(pq)

        # Check if the point is visited
        if (current_row, current_col) in visited:
            continue
        # add the point to the visited set
        visited.add((current_row, current_col))

        # Update cost of the point
        cost[(current_row, current_col)] = point_cost

        # Check if the point is the goal
        if current_row == row_max - 1 and current_col == col_max - 1:
            break

        # Check if the point is valid
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr = current_row + dr
            dc = current_col + dc
            if not (0 <= rr < row_max and 0 <= dc < col_max):
                continue
            heapq.heappush(pq, (point_cost + map[rr][dc], rr, dc))

    # Print the result
    pp.pprint(f'Cost to Target is equal to:{cost[(row_max - 1, col_max - 1)]}')


def main():
    """Control the program."""
    data = get_data('day15.txt')
    # pp.pprint(data)
    part1(data)


if __name__ == '__main__':
    main()
