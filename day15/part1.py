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
    """Find Cost Of Shortest Path."""
    max_row = len(map)
    max_col = len(map[0])

    # Define Cost Dictionary
    cost = defaultdict(int)

    # Define Priority Queue
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
        if current_row == max_row - 1 and current_col == max_col - 1:
            break

        # Get the current node's neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Get the new row and column
            rr = current_row + dr
            cc = current_col + dc
            # Check if the new row and column are valid
            if not (0 <= rr < max_row and 0 <= cc < max_col):
                continue
            # Add the new node to the queue
            heapq.heappush(pq, (point_cost + map[rr][cc], rr, cc))

    # Print the cost
    pp.pprint(f'Cost:{cost[(max_row - 1, max_col - 1)]}')


def main():
    """Control the program."""
    data = get_data('day15_test.txt')
    # pp.pprint(data)
    part1(data)


if __name__ == '__main__':
    main()
