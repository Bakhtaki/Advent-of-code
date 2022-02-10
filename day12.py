"""

This is script for advent of code 2021.

day 12 part 1,2.
"""

import collections
import pprint as pp


def get_data(filename):
    """Extract data fom file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
        content = [line.rstrip() for line in content]
    file.close()
    return content


def part1(data: list) -> int:
    """Part 1 day 12."""
    edges = collections.defaultdict(set)
    for line in data:
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)
    pp.pprint(edges)

    all_path = set()
    todo = [('start',)]


def main():
    """Control logic of Script."""
    data = get_data('day12_test1.txt')
    part1(data)


if __name__ == "__main__":
    main()
