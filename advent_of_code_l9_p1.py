"""
This Script, is solution for advent of code 2021.

Level9 part1.
"""

# import sys
# import itertools
# from collections import defaultdict, Counter
import pprint as pp


def get_data(filename):
    """Get data from file."""
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        while (line := file.readline().strip()):
            line = [int(x) for x in line]
            lines.append(list(line))
    file.close()
    return lines


def check_adjacency(point, row, column, matrix):
    """Evaluate neighbors  points of input."""
    print(point, row, column, matrix)
    if (row, column) == (0, 0):
        return (point < matrix[row + 1][column]) and (point < matrix[row][column + 1])
    elif (row, column) == (len(matrix) - 1 , len(matrix[0]) - 1):
        return (point < matrix[row][column-1]) and (point < matrix[row - 1][column -1])
    else:
        return None



def check_point(matrix):
    """
    Check each point for determine wether is lowest neighbor or not.

        input  : list of list
        output : list
    """
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    targets = []
    for row in range(len_rows):
        for column in range(len_cols):
            result = False
            point_value = matrix[row][column]
            result = check_adjacency(point_value, row, column, matrix)
            if result:
                targets.append(point_value)
    total = sum(targets)
    return total


def main():
    """Logical flow of the script."""
    data = get_data('level9.txt')
    pp.pprint(data)
    total = check_point(data)
    print(f"Total is : {total}")


if __name__ == '__main__':
    main()
