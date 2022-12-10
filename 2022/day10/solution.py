"""Advent of code 2022 day 10 solution."""

import sys


# Find signal strength at given time
def signal_strength(data: list) -> None:
    """Find signal strength at given time."""
    strength_history = {}
    time = 1
    value_x = 1
    strength_history[time] = value_x

    for line in data:
        if line.startswith('a'):
            temp_value = int(line.split(' ')[1])
            time += 1
            strength_history[time] = value_x
            time += 1
            value_x += temp_value
            strength_history[time] = value_x
        if line.startswith('n'):
            time += 1
            strength_history[time] = value_x

    requested_time = [20, 60, 100, 140, 180, 220]

    answer = 0
    for time in requested_time:
        answer += strength_history[time] * time

    print(f'Answer: {answer}')


# Define display_crt
def display_crt(data: list) -> None:
    """Display CRT."""

    current_x = 1
    operation = 0

    row = 0
    column = 0

    crt = [1] * 241

    for line in data:
        sections = line.split(' ')

        if sections[0].startswith('n'):
            operation += 1
            crt[operation] = current_x
        elif sections[0].startswith('a'):
            value = int(sections[1])
            crt[operation + 1] = current_x
            current_x += value
            operation += 2
            crt[operation] = current_x

    answer = [['.'] * 40 for _ in range(6)]

    for row in range(6):
        for column in range(40):
            counter = row * 40 + column + 1

            if abs(crt[counter - 1] - (column)) <= 1:
                answer[row][column] = '##'
            else:
                answer[row][column] = '  '

    for row in answer:
        print(''.join(row))


if __name__ == "__main__":
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()

    # Part 1
    signal_strength(lines)

    # Part 2.
    display_crt(lines)
