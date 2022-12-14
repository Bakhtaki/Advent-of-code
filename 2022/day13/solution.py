"""Advent of code 2022 day 13."""
import sys
from functools import cmp_to_key


def compare(first, second):
    """Compare two lists."""
    if isinstance(first, list) and isinstance(second, int):
        second = [second]

    if isinstance(first, int) and isinstance(second, list):
        first = [first]

    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        if first == second:
            return 0
        return -1
    if isinstance(first, list) and isinstance(second, list):
        i = 0
        while i < len(first) and i < len(second):
            temp = compare(first[i], second[i])
            if temp == 1:
                return 1
            if temp == -1:
                return -1
            i += 1

        if i == len(first):
            if len(first) == len(second):
                return 0
            return 1
        return -1


# Part 1
def part1(parts):
    """Part 1."""
    answer = 0

    for i, part in enumerate(parts):
        left, right = map(eval, part.split("\n"))
        if compare(left, right) == 1:
            answer += i + 1
    print(f"Answer: {answer}")


# Part 2.
def part2(file_name):
    """Part 2."""
    with open(file_name, 'r', encoding='utf-8') as file:
        parts = file.read().strip().replace('\n\n', '\n').split('\n')

        lists = list(map(eval, parts))
        lists.append([[2]])
        lists.append([[6]])

        lists = sorted(lists, key=cmp_to_key(compare), reverse=True)

        for i, part in enumerate(lists):
            if part == [[2]]:
                first = i + 1
            if part == [[6]]:
                second = i + 1

    # Print first * second for part 2.
    print(f"Answer: {first * second}")


# Main
if __name__ == '__main__':
    input_file = sys.argv[1]
    with open(input_file, encoding='utf-8') as file:
        pairs = file.read().strip().split('\n\n')

    # Part 1
    part1(pairs)

    # Part 2.
    part2(input_file)
