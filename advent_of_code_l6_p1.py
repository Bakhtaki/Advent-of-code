"""
This scripts written for advent of code 2021.

level6 part1
"""
import datetime


def read_file(file_name):
    """Import data to code."""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = list(map(int, file.readline().split(',')))
        return lines


def get_population(population, target_day):
    """Calculate number of individual at target time."""
    day = 0
    while day < target_day:
        temp = []
        new_born = 0
        for fish in population:
            if fish - 1 >= 0:
                temp.append(fish - 1)
            else:
                new_born += 1
                temp.append(6)
        for _i in range(new_born):
            temp.append(8)
        population = temp
        # print(population)
        day += 1
    print(f'Total Population after {target_day} is equal to {len(population)}')


def main():
    """Logic of code."""
    start_time = datetime.datetime.now()
    print(f'The App startted at : {start_time}')
    initial_state = read_file("advent_of_code_l6.txt")
    get_population(initial_state, 80)
    end_time = datetime.datetime.now()
    print(f'The App ended at :{end_time}')
    print(f'Total time of execution is : {end_time - start_time}')


if __name__ == "__main__":
    main()
