# pylint: disable=invalid-name
"""
This script is a simple solution for advent of code 2021.

day 11 part1.
"""

from __future__ import annotations
from typing import Generator
import datetime
import numpy as np


def get_data(file_name):
    """Get data from file."""
    lines = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = [[int(x) for x in line] for line in lines]
        lines = np.array(lines)
        # Print Lines
        return lines


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    """Check All Adjacent Neighbors of x,y."""
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x + x_d, y + y_d


def part1(data):
    """Solution for part1."""
    coordinates = {}
    flashes = 0  # Number of flashes

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            coordinates[x, y] = int(char)

    for _ in range(100):
        todo = []
        for key, _value in coordinates.items():
            coordinates[key] += 1
            if coordinates[key] > 9:
                todo.append(key)

        while todo:
            point = todo.pop()
            if coordinates[point] == 0:
                continue
            coordinates[point] = 0
            flashes += 1

            for other in adjacent(*point):
                if other in coordinates and coordinates[other] != 0:
                    coordinates[other] += 1
                    if coordinates[other] > 9:
                        todo.append(other)

    print("Answer for Part one : ")
    print(f'Total flashes is equal to : {flashes}')


def part2(data):
    """Solution for part 2."""
    coordinates = {}
    steps = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            coordinates[x, y] = int(char)

    totally_flashed = False
    while not totally_flashed:
        todo = []
        totally_flashed = True
        for key, _value in coordinates.items():
            coordinates[key] += 1
            if coordinates[key] > 9:
                todo.append(key)
        while todo:
            point = todo.pop()
            if coordinates[point] == 0:
                continue
            coordinates[point] = 0

            for other in adjacent(*point):
                if other in coordinates and coordinates[other] != 0:
                    coordinates[other] += 1
                    if coordinates[other] > 9:
                        todo.append(other)
        for key, _value in coordinates.items():
            if coordinates[key] != 0:
                totally_flashed = False
        steps += 1
    print(f'Total steps is equal to : {steps}')


def main():
    """Logical flow of the script."""
    start_time = datetime.datetime.now()
    data = get_data('day11.txt')
    # part1(data)
    part2(data)
    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    print(f'Total execution time is equal to: {execution_time}')


if __name__ == '__main__':
    main()
