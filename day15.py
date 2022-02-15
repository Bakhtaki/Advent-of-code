"""
Advent of the code 2021.

day15 part 1,2.
"""


import pprint as pp

"""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

# excepted output: 40


def get_data(filename):
    """Read the data from the file."""
    data = []
    with open(filename, 'r', encoding='utf8') as file:
        while (line := file.readline().strip()):
            line = [int(x) for x in line]
            data.append(line)
    return data


def main():
    """Control the program."""
    data = get_data('day15_test.txt')
    pp.pprint(data)



if __name__ == '__main__':
    main()
