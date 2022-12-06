"""Advent of code 2022 day 6 solution."""

import sys


# Difine funcdtion to read input input_file
def read_file(filename):
    """Read File Contents."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().strip()


# Solve part 1
def solve(input_str, index):
    """Solve part 1."""
    # Move on string to find 4 consecutive unrepeated characters
    for i in range(len(input_str) - index - 1):
        if len(set(input_str[i:i + index])) == index:
            return i + index


if __name__ == "__main__":
    input_file = sys.argv[1]
    data = read_file(input_file)

    # Part 1
    part1 = solve(data, 4)
    print(f'Part 1: {part1}')
    # Part 2
    part2 = solve(data, 14)
    print(f'Part 2: {part2}')
