'''Advent of code 2022 day21 solution.'''
from functools import lru_cache
import sys
from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr


if __name__ == "__main__":
    file_name = sys.argv[1]

    # Read the input file
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()

    # Create Dictionary
    lookup = {}

    humn = symbols('humn')

    @lru_cache(None)
    def compute(name):
        """_summary_

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        if name == 'humn':
            return humn

        if isinstance(lookup[name], int):
            return lookup[name]
        sections = lookup[name]

        left = compute(sections[0])
        right = compute(sections[2])

        return parse_expr(f'({left}) {sections[1]} ({right})')

    for line in lines:
        parts = line.split(' ')
        monkey = parts[0][:-1]

        if len(parts) == 2:
            lookup[monkey] = int(parts[1])
        else:
            lookup[monkey] = parts[1:]

    # Compute the result
    left = compute(lookup['root'][0])
    right = compute(lookup['root'][2])

    answer = solve_linear(left, right)[1]
    print(f'Answer: {answer}')
