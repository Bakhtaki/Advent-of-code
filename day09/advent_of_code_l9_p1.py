# pylint: disable=too-many-return-statements
"""
This Script, is solution for advent of code 2021.

Level9 part1.
"""

# import sys
# import itertools
# from collections import defaultdict, Counter
# import pprint as pp
import datetime


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
    flag = False
    # print(row, column)
    if (row, column) == (0, 0):
        # print("Top,Left")
        flag = ((point < matrix[row + 1][column]) and
                (point < matrix[row][column + 1]))
    elif (row, column) == (len(matrix) - 1, len(matrix[0]) - 1):
        # print("Buttom,Right")
        flag = ((point < matrix[row][column-1]) and
                (point < matrix[row - 1][column - 1]))
    elif (row, column) == (0, len(matrix[0]) - 1):
        # print("Top,Right")
        flag = ((point < matrix[row][column - 1] and
                point < matrix[row + 1][column]))
    elif (row, column) == (len(matrix) - 1, 0):
        # print("Buttom,Left")
        flag = ((point < matrix[row][column + 1]) and
                (point < matrix[row - 1][column]))
    elif row == 0:
        # print("First Line")
        flag = ((point < matrix[row][column - 1]) and
                (point < matrix[row][column + 1]) and
                point < matrix[row + 1][column])
    elif row == len(matrix) - 1:
        # print("last line")
        flag = ((point < matrix[row][column - 1]) and
                (point < matrix[row][column + 1]) and
                point < matrix[row - 1][column])
    elif column == 0:
        # print("First Column")
        flag = ((point < matrix[row][column + 1]) and
                point < matrix[row + 1][column] and
                point < matrix[row - 1][column])
    elif column == len(matrix[0]) - 1:
        # print("Last Column")
        flag = ((point < matrix[row][column - 1]) and
                point < matrix[row + 1][column] and
                point < matrix[row - 1][column])
    else:
        # print("Middle Of table")
        flag = ((point < matrix[row][column - 1]) and
                (point < matrix[row][column + 1]) and
                (point < matrix[row - 1][column]) and
                (point < matrix[row + 1][column]))
    return flag


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
                # print("Target Identified")
                targets.append(point_value)
    total = sum(targets) + len(targets)
    return total


def main():
    """Logical flow of the script."""
    start_time = datetime.datetime.now()
    data = get_data('advent_of_code_l9.txt')
    # pp.pprint(data)
    total = check_point(data)
    end_time = datetime.datetime.now()
    print(f"Total Execution Time: {end_time - start_time}")
    print(f"Total is : {total}")


if __name__ == '__main__':
    main()
