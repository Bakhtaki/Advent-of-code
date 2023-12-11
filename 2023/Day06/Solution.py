import sys
import re


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):

    answers = []
    count = 1

    def cont_possible(t, d):
        possible = 0
        for i in range(t):
            if (t - i) * i > d:
                possible += 1
        return possible

    times = re.findall(r'\d+', data.split('\n')[0])
    times = [int(i) for i in times]

    distance = re.findall(r'\d+', data.split('\n')[1])
    distance = [int(i) for i in distance]

    for t, d in zip(times, distance):
        answers.append(cont_possible(t, d))

    for each in answers:
        count *= each

    print(f"Part 1: {count}")


def part2(data):
    def cont_possible(t, d):
        possible = 0
        for i in range(t):
            if (t - i) * i > d:
                possible += 1
        return possible

    times = re.findall(r'\d+', data.split('\n')[0])
    times = [int(i) for i in times]

    distance = re.findall(r'\d+', data.split('\n')[1])
    distance = [int(i) for i in distance]

    time = int(''.join([str(i) for i in times]))
    dist = int(''.join([str(i) for i in distance]))

    answer = cont_possible(time, dist)

    print(f"Part 2: {answer}")


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
