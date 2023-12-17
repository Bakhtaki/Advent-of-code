import sys
from itertools import combinations


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


def part2(data):
    return data


def calculate_distance(p1, p2, ex=None, ey=None):
    """
    Calculate the Manhattan distance between two points in a grid.

    Args:
        p1 (tuple): The coordinates of the first point (x1, y1).
        p2 (tuple): The coordinates of the second point (x2, y2).
        ex (list, optional): List of empty rows. Defaults to None.
        ey (list, optional): List of empty columns. Defaults to None.

    Returns:
        int: The Manhattan distance between the two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    empty_rows = ex
    empty_cols = ey

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    distance = 0
    for i in range(x1, x2):
        distance += 1
        if i in empty_rows:
            distance += 1
    for j in range(y1, y2):
        distance += 1
        if j in empty_cols:
            distance += 1
    return distance


def part1(data):
    lines = data.splitlines()
    n, m = len(lines), len(lines[0])

    # Find Position occupied with '#'
    occupied = []
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            if col == '#':
                occupied.append((i, j))

    # Find Empty rows
    empty_rows = []
    for i in range(n):
        for j in range(m):
            if lines[i][j] == '#':
                break
        else:
            empty_rows.append(i)

    # Find Empty columns
    empty_cols = []
    for j in range(m):
        for i in range(n):
            if lines[i][j] == '#':
                break
        else:
            empty_cols.append(j)

    sum = 0
    all_pairs = list(combinations(occupied, 2))

    for each in all_pairs:
        p1 = each[0]
        p2 = each[1]
        distance = calculate_distance(p1, p2, empty_rows, empty_cols)
        sum += distance
    print(f'Part 1: {sum}')


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
