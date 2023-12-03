"""Solution to Day 18 of Advent of Code 2022."""

import sys
import numpy as np


if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()

    # Part 1
    filled = set()

    for line in lines:
        x, y, z = map(int, line.split(','))
        filled.add((x, y, z))

    answer = 0
    for x, y, z in filled:
        covered = 0
        position = np.array((x, y, z))

        for coordinate in range(3):
            d_position = np.array([0, 0, 0])
            d_position[coordinate] = 1

            d_negative = np.array([0, 0, 0])
            d_negative[coordinate] = -1

            covered += tuple(position + d_position) in filled
            covered += tuple(position + d_negative) in filled
        answer += 6 - covered

    print(f"Part 1: {answer}")
