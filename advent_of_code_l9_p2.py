"""
This Script, is solution for advent of code 2021.

Level9 part2.
"""

# import sys
# import itertools
# from collections import defaultdict, Counter
# import pprint as pp
import datetime
import numpy as np


def get_data(filename):
    """Get data from file."""
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        while (line := file.readline().strip()):
            line = [int(x) for x in line]
            lines.append(list(line))
    file.close()
    lines = np.array([np.array(line) for line in lines])
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
    coordinates = []
    for row in range(len_rows):
        for column in range(len_cols):
            result = False
            point_value = matrix[row][column]
            result = check_adjacency(point_value, row, column, matrix)
            if result:
                # print("Target Identified")
                targets.append(point_value)
                coordinates.append((row, column))
    basin_count = len(targets)
    return basin_count , coordinates


def find_basins(data):
    """Check the Matrix for find 3 most biggest basins.

    Args:
        data ([numpy array ]): [Array of coordinates to find.]
    """
    checked = np.zeros(shape=(len(data),len(data[0])))
    print(checked)


def main():
    """Logical flow of the script."""
    start_time = datetime.datetime.now()
    data = get_data('level9.txt')
    # print(data)
    basin_count , coordinates = check_point(data)
    print(f'There are {basin_count} basins , cooridnates of basins are : {coordinates}')
    find_basins(data)
    end_time = datetime.datetime.now()
    print(f"Total Execution Time: {end_time - start_time}")



if __name__ == '__main__':
    main()
