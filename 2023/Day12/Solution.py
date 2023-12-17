import sys


def get_file_content(file_name):
    """
    Reads the content of a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """

    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def count_possibilities(stat, nums):
    if stat == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if '#' in stat else 1

    result = 0
    if stat[0] in '.?':
        result += count_possibilities(stat[1:], nums)

    if stat[0] in '#?':
        if (nums[0] <= len(stat) and "." not in stat[:nums[0]] and
                (nums[0] == len(stat) or stat[nums[0]] != '#')):
            result += count_possibilities(stat[nums[0]+1:], nums[1:])

    return result


def part1(data):
    answer = 0
    for line in data.splitlines():
        stat, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        answer += count_possibilities(stat, nums)

    print("Part 1 answer: ", answer)


cache = {}


def count_possibilities_unfolded(stat, nums):
    if stat == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if '#' in stat else 1

    key = (stat, nums)
    if key in cache:
        return cache[key]

    result = 0

    if stat[0] in '.?':
        result += count_possibilities_unfolded(stat[1:], nums)

    if stat[0] in '#?':
        if (nums[0] <= len(stat) and "." not in stat[:nums[0]] and
                (nums[0] == len(stat) or stat[nums[0]] != '#')):
            result += count_possibilities_unfolded(stat[nums[0]+1:], nums[1:])

    cache[key] = result
    return result


def part2(data):
    answer = 0
    for line in data.splitlines():
        stat, nums = line.split()
        nums = tuple(map(int, nums.split(',')))

        stat = "?".join([stat] * 5)
        nums *= 5
        answer += count_possibilities(stat, nums)
    print("Part 2 answer: ", answer)


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
