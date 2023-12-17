import sys
from collections import deque


def get_file_content(file_name):
    """
    Reads the content of a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """

    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def get_neighbors(i, j, lines):
    result = []
    for di, dj in list(get_direct_neighbors(i, j, lines)):
        ii, jj = i + di, j + dj

        if not (0 <= ii < len(lines) and 0 <= jj < len(lines[0])):
            continue
        result.append((ii, jj))
    return result


def get_direct_neighbors(i, j, lines):
    result = []
    if lines[i][j] == 'S':
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj

            if not (0 <= ii < len(lines) and 0 <= jj < len(lines[0])):
                continue
            if (i, j) in list(get_neighbors(ii, jj, lines)):
                result.append((di, dj))
        return result

    else:
        result = {
            '|': [(1, 0), (-1, 0)],
            '-': [(0, 1), (0, -1)],
            'L': [(0, 1), (1, 0)],
            'J': [(-1, 0), (0, -1)],
            'F': [(1, 0), (0, 1)],
            '7': [(1, 0), (0, -1)],
            '.': []
        }[lines[i][j]]
        return result


def part1(data):
    lines = data.splitlines()

    # Find Start Position
    si, sj = None, None
    for i, line in enumerate(lines):
        if 'S' in line:
            si, sj = i, line.index('S')
            break

    # BFS to find shortest path
    visited = set()
    destinations = {}

    q = deque([((si, sj), 0), ])

    while len(q) > 0:
        top, dist = q.popleft()
        if top in visited:
            continue
        visited.add(top)
        destinations[top] = dist

        for nbr in list(get_neighbors(*top, lines)):
            if nbr in visited:
                continue
            q.append((nbr, dist + 1))

    answer = max(destinations.values())
    print(f'Part 1: {answer}')


def part2(data):
    return data


if __name__ == '__main__':
    file_name = sys.argv[1]

    data = get_file_content(file_name)
    print("Which part do you want to run?")
    input = int(input("Enter 0 for both, 1 for part 1 and 2 for part 2: "))
    if input == 0:
        part1(data)
        part2(data)

    elif input == 1:
        part1(data)

    elif input == 2:
        part2(data)
    else:
        print("Invalid input")
