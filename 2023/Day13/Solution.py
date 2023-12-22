import sys
from copy import deepcopy


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


def check_pattern(grid):
    """
    Checks if the pattern whether reflected Vertically, Horizontally

    Args:
        grid (list): The grid to check.
    output:
        Int
    """
    sum = 0
    n, m = len(grid), len(grid[0])

    # Horizontal
    horizontal = -1
    for i in range(n-1):
        if check_horizontal(grid, i):
            horizontal = i
            break

    # Vertical
    vertical = -1
    transposed = transpose(grid)

    for i in range(m-1):
        if check_horizontal(transposed, i):
            vertical = i
            break

    assert horizontal == -1 or vertical == -1
    sum = vertical + 1 + 100 * (horizontal + 1)

    return sum


def check_horizontal(grid, i):

    n, m = len(grid), len(grid[0])

    for j in range(m):
        for k1 in range(n):
            k2 = i * 2+1 - k1
            if not (0 <= k2 < n):
                continue
            if grid[k1][j] != grid[k2][j]:
                return False
    return True


def transpose(grid):
    """
    Transposes a grid.

    Args:
        grid (list): The grid to transpose.

    Returns:
        list: The transposed grid.
    """

    return list(zip(*grid))


def find_reflection(grid, ignore=(-1, -1)):
    n, m = len(grid), len(grid[0])

    # Horizontal
    horizontal = -1
    for i in range(n-1):
        if i != ignore[0] and check_horizontal(grid, i):
            horizontal = i
            break

    # Vertical
    vertical = -1
    transposed = transpose(grid)
    for j in range(m-1):
        if j != ignore[1] and check_horizontal(transposed, j):
            vertical = j
            break

    return (horizontal, vertical)


def fix_reflection(grid):
    """
    Fixes the reflection of a grid.

    Args:
        grid (list): The grid to fix.

    Returns:
        list: The fixed grid.
    """

    n, m = len(grid), len(grid[0])

    original_reflection = find_reflection(grid)
    print(original_reflection)

    for i in range(n):
        for j in range(m):
            grid_copy = deepcopy(grid)
            grid_copy[i][j] = '.' if grid_copy[i][j] == '#' else '#'

            new_reflection = find_reflection(grid_copy, original_reflection)

            if new_reflection not in [original_reflection, (-1, -1)]:
                if new_reflection[0] != -1:
                    answer = (new_reflection[0] + 1) * 100
                else:
                    assert new_reflection[1] != -1
                    answer = (new_reflection[1]) + 1

                return answer


def part1(data):
    pattern = [line.split() for line in data.split('\n\n')]
    answer = 0

    for grid in pattern:
        result = check_pattern(grid)
        answer += result

    print(f'Answer: {answer}')


def part2(data):
    pattern = [[line.split() for line in grid.split('\n')]
               for grid in data.split('\n\n')]
    answer = 0

    for grid in pattern:
        result = fix_reflection(grid)
        answer += result

    print(f'Answer: {answer}')


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
