import sys
from collections import defaultdict
import re
import math


def get_file_content(file_name):
    with open(file_name, "r") as file:
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

    current = "AAA"
    count = 0

    while current != "ZZZ":
        step = steps[count % len(steps)]
        if step == "L":
            current = children[current][0]
        else:
            current = children[current][1]
        count += 1

    print(f"Part 1 answer: {count}")


def part2(data):
    line = data.splitlines()
    steps = line[0]

    def number_of_steps(point):
        count = 0
        while point[2] != "Z":
            step = steps[count % len(steps)]
            if step == "L":
                point = children[point][0]
            else:
                point = children[point][1]
            count += 1

        return count

    children = defaultdict(str)
    for line in line[2:]:
        par, left, right = re.search(
            r"(...) = \((...), (...)\)", line).groups(0)

        children[par] = (left, right)

    current = [point for point in children if point[2] == "A"]

    ways = [number_of_steps(point) for point in current]

    answer = math.lcm(*ways)

    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
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
