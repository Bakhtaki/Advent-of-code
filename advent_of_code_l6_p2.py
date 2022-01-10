"""
This scripts written for advent of code 2021.

level6 part2
"""
import datetime


def read_file(file_name):
    """Import data to code."""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = list(map(int, file.readline().split(',')))
        return lines


def get_population(population, target_day):
    """Calculate number of individual at target time."""
    data = {}
    day = 0
    final_population = 0
    for key in range(9):
        data[key] = 0
    for fish in population:
        data[fish] += 1
    print(data)
    while day < target_day:
        zeroes = data[0]
        data[0] = 0
        for index in range(1, len(data)):
            data[index - 1] += data[index]
            data[index] = 0
        data[6] += zeroes
        data[8] += zeroes
        # print(data)
        day += 1
    for _key in data:
        final_population += data[key]
    return final_population


def main():
    """Logic of code."""
    start_time = datetime.datetime.now()
    print(f'The App startted at : {start_time}')
    initial_state = read_file("advent_of_code_l6.txt")
    final_population = get_population(initial_state, 256)
    print(f'Final population is :{final_population}')
    end_time = datetime.datetime.now()
    print(f'The App ended at :{end_time}')
    print(f'Total time of execution is : {end_time - start_time}')


if __name__ == "__main__":
    main()
