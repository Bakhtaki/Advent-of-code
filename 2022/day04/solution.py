"""Solution for advent of code 2022 day 4."""

import sys


# Function for read file:
def read_file(filename):
    """Read input file."""
    with open(filename, 'r', encoding='utf-8') as file:
        output = file.read().splitlines()
    return output


# Function for part 1:
def part1(input_data):
    """Part 1."""
    count = 0

    for line in input_data:
        # Split line to 2 parts:
        sec1, sec2 = line.split(',')

        # Split sec1 to 2 parts:
        sec1_1, sec1_2 = sec1.split('-')

        # Split sec2 to 2 parts:
        sec2_1, sec2_2 = sec2.split('-')

        # Check if section 1 fully covered by section 2:
        if int(sec1_1) >= int(sec2_1) and int(sec1_2) <= int(sec2_2):
            count += 1

        # check if section 2 fully covered by section 1:
        elif int(sec2_1) >= int(sec1_1) and int(sec2_2) <= int(sec1_2):
            count += 1

    return count


# Function for part 2:
def part2(input_data):
    """Solutoin for part2."""
    count = 0

    for line in input_data:
        sec1, sec2 = line.split(',')
        sec1_1, sec1_2 = sec1.split('-')
        sec2_1, sec2_2 = sec2.split('-')

        if set(range(int(sec1_1), int(sec1_2) + 1)).intersection(
                set(range(int(sec2_1), int(sec2_2) + 1))):
            count += 1

    return count


if __name__ == '__main__':

    filename = sys.argv[1]
    data = read_file(filename)

    # Part 1
    print(f'Part 1: {part1(data)}')

    # Part 2
    print(f'Part 2: {part2(data)}')
