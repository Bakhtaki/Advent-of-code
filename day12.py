"""

This is script for advent of code 2021.

day 12 part 1,2.
"""

import collections


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

    all_path = set()
    todo = [('start',)]

    while todo:
        path = todo.pop()

        if path[-1] == 'end':
            all_path.add(path)
            continue

        for node in edges[path[-1]]:
            if not node.islower() or node not in path:
                todo.append(path + (node,))

    print('Part 1 answer is equal to : ', len(all_path))


def part2(data: list) -> int:
    """Provide Solution for part 2 of day 12."""
    edges = collections.defaultdict(set)

    for line in data:
        src, dest = line.split('-')
        edges[src].add(dest)
        edges[dest].add(src)

    all_path = set()
    todo = [(('start', ), False)]

    while todo:
        path, visited = todo.pop()

        if path[-1] == 'end':
            all_path.add(path)
            continue

        for node in edges[path[-1]]:
            if node == 'start':
                continue

            if node.isupper() or node not in path:
                todo.append(((path + (node,)), visited))
            elif not visited and path.count(node) == 1:
                todo.append(((path + (node,)), True))

    print("Part 2 Answer is equal to : ", len(all_path))


def main():
    """Control logic of Script."""

    part1(get_data('day12.txt'))  # real
    part2(get_data('day12.txt'))  # real


if __name__ == "__main__":
    main()
