# pylint: disable=too-many-locals
"""
THis is  solution for day 14 of the Advent of Code 2021.

day14:
    Part1.
"""
from collections import Counter


def get_data(filename):
    """Read the data from the file and returns a list of integers."""
    with open(filename, 'r', encoding='utf-8') as file:
        template, instruction = file.read().split("\n\n")
    return template, instruction


def part1(template, instruction):
    """Part 1 of the puzzle."""
    formula = {}
    for line in instruction.split("\n"):
        if line == "":
            continue
        key, value = line.split("->")
        key = key.strip()
        value = value.strip()
        formula[key] = value
    print(f"Formula: {formula}")

    for _i in range(10):
        new_template = ''
        for _j in range(len(template) - 1):
            last_char = template[-1]
            checking = template[_j] + template[_j + 1]
            checking = checking[:-1] + formula[checking]
            new_template = new_template + checking
        new_template = new_template + last_char
        template = new_template

    chars = list(set(template))
    max_char = 0
    min_char = len(template)
    for element in chars:
        char_count = template.count(element)
        max_char = char_count if char_count > max_char else max_char
        min_char = min(min_char, char_count)

    print(f'result  of part 1 is equal to:{max_char - min_char}')


def part2(template, instruction):
    """Part 2 of the puzzle."""
    # print(f"Template: {template}")
    # print(f"Instruction: {instruction}")

    patterns = {}
    for line in instruction.split("\n"):
        if line == "":
            continue
        key, value = line.split(" -> ")
        patterns[key] = value
    # print(f"Patterns: {patterns}")

    pair_count = Counter()
    for i in range(0, len(template) - 1):
        pair_count[template[i:i+2]] += 1
    # print(f"Pair Count: {pair_count}")

    for _ in range(40):

        new_pair_count = Counter()
        char_count = Counter()

        for key, value in pair_count.items():
            new_pair_count[f'{key[0]}{patterns[key]}'] += value
            new_pair_count[f'{patterns[key]}{key[1]}'] += value
            # print(f'New Pair Count: {new_pair_count}')

            char_count[key[0]] += value
            char_count[patterns[key]] += value
        pair_count = new_pair_count
        # print(f'pair_count: {pair_count}')
    char_count[template[-1]] += 1

    values = sorted(char_count.values())
    result = values[-1] - values[0]
    print("Part 2:", result)


def main():
    """Flow Control of script."""
    template, instruction = get_data('day14.txt')
    print(f"Template: {template}")
    part1(template, instruction)
    part2(template, instruction)


if __name__ == '__main__':
    main()
    print("Done")
