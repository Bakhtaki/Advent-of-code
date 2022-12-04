"""Solution for day 3 advent of code 2022."""

import sys
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
            'w': 23, 'x': 24, 'y': 25, 'z': 26, "A": 27, "B": 28, "C": 29,
            "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
            "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43,
            "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50,
            "Y": 51, "Z": 52}


# Define function to read input file
def read_input(input_file):
    """Read input file."""
    with open(input_file, "r", encoding='utf-8') as file:
        output_data = file.read().splitlines()
    return output_data


# Define function to part 1
def part1(input_data):
    """Part 1."""
    common_elements = []
    answer = 0
    for line in input_data:
        lenght = len(line)
        first_half = (line[:lenght//2])
        second_half = set(line[lenght//2:])

        # find the common elements
        common = set(first_half).intersection(second_half)
        # Convert Common to string
        common = ''.join(common)
        common_elements.append(common)

    for element in common_elements:
        answer += alphabet[element]

    return answer


# Define function to part 2
def part2(input_data):
    """Part2."""
    sticker_sum = 0
    # split data 3 lines at a times
    for i in range(0, len(input_data), 3):
        group = (input_data[i:i+3])

        # find the common elements in all groups
        common = set(group[0]).intersection(group[1], group[2])

        # Convert Common to string
        common = ''.join(common)

        # add the sum of the common common_elements
        sticker_sum += alphabet[common]

    return sticker_sum


if __name__ == "__main__":
    # Read file name from arguments
    filename = sys.argv[1]
    data = read_input(filename)

    # Part 1
    print(f'Part 1: {part1(data)}')

    # Part 2
    print(f'Part 2: {part2(data)}')
