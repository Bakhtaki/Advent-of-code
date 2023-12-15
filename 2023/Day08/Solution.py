import sys
from collections import defaultdict
import re


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):

    lines = data.splitlines()
    steps = lines[0]

    children = defaultdict(str)

    for line in lines[2:]:
        par, left, right = re.search(
            r"(...) = \((...), (...)\)", line).groups(0)
        children[par] = (left, right)

    current = 'AAA'
    count = 0

    while current != 'ZZZ':
        step = steps[count % len(steps)]
        if step == 'L':
            current = children[current][0]
        else:
            current = children[current][1]
        count += 1

    print(f"Part 1 answer: {count}")


def part2(data):
    return data


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
