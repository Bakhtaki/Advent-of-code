'''Advent of code 2022 day21 solution.'''
from functools import lru_cache
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]

    # Read the input file
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()

    # Create Dictionary
    lookup = {}

    @lru_cache(None)
    def compute(name):
        if isinstance(lookup[name], int):
            return lookup[name]
        sections = lookup[name]

        left = compute(sections[0])
        right = compute(sections[2])

        return eval(f'{left} {sections[1]} {right}')

    for line in lines:
        parts = line.split(' ')
        monkey = parts[0][:-1]

        if len(parts) == 2:
            lookup[monkey] = int(parts[1])
        else:
            lookup[monkey] = parts[1:]

    # Compute the result
    answer = int(compute('root'))

    print(f'Answer: {answer}')
