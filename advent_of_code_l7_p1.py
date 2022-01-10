"""
 This script looks for solution of advent of code 2021.

Level7 part1.
"""


def get_data(file_name):
    """Load data from source file to script."""
    with open(file_name, 'r', encoding='utf8') as file:
        lines = list(map(int, file.readline().split(',')))
        file.close()
        return lines


def calculate_cost(status):
    """Cost of optimum movement."""
    log = {}
    for point in status:
        log[point] = 0
    for index in status:
        target = index
        total_movement = 0
        for current in status:
            movement = abs(target - current)
            total_movement += movement
        log[index] = total_movement
    lowest_cost = min(log.values())
    return lowest_cost


def main():
    """Logic of this script."""
    first_state = get_data('advent_of_code_l7.txt')
    lowest_cost = calculate_cost(first_state)
    print(f'lowest cost for status is : {lowest_cost}')


if __name__ == '__main__':
    main()
