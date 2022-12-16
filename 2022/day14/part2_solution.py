"""Advent of code 2022 day 14 soltion."""

import sys


# Simluate the snad fall.
def simulate_sand():
    """Simulate the sand fall."""
    # Globalize the variables.
    global filled

    x, y = 500, 0

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        break

    return x, y


if __name__ == '__main__':
    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()

    entry_point = (500, 0)

    # Filled Points
    filled = set()

    # Fill the points from the input_file
    for line in lines:
        coordinates = []
        for coordinate in line.split(' -> '):
            x, y = map(int, coordinate.split(','))
            coordinates.append((x, y))

        for i in range(1, len(coordinates)):
            current_x, current_y = coordinates[i]
            previous_x, previous_y = coordinates[i - 1]

            if current_y != previous_y:
                assert current_x == previous_x
                for y in range(min(current_y, previous_y),
                               max(current_y, previous_y) + 1):
                    filled.add((current_x, y))
            if current_x != previous_x:
                assert current_y == previous_y
                for x in range(min(current_x, previous_x),
                               max(current_x, previous_x) + 1):
                    filled.add((x, current_y))

    max_y = max([coordinate[1] for coordinate in filled])

    # Part 1.
    part_2 = 0

    while True:
        x, y = simulate_sand()
        filled.add((x, y))
        part_2 += 1

        if (x, y) == entry_point:
            break

    print(f'Part 2: {part_2}')
