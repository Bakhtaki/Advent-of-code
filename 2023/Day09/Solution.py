import sys


def get_file_content(file_name):
    """
    Reads the content of a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    with open(file_name, "r") as file:
        file_content = file.read()
    return file_content


def diff(line):
    """
    Calculates the difference between each consecutive element in the
    given list.

    Args:
        line (List[int]): A list of integers.

    Returns:
        List[int]: A list containing the difference between each
            consecutive element in the input list.
    """
    return [line[i + 1] - line[i] for i in range(len(line) - 1)]


def extrapolate(hist):
    """
    Extrapolates a histogram by extending its values until reaching a
    final value of 0.

    Parameters:
        hist (List[int]): A list of integer values representing the
        histogram.

    Returns:
        int: The extrapolated value of the histogram.
    """
    layers = [hist]

    while not all([x == 0 for x in layers[-1]]):
        layers.append(diff(layers[-1]))

    layers[-1].append(0)
    for i in range(len(layers) - 2, -1, -1):
        layers[i].append(layers[i + 1][-1] + layers[i][-1])

    return layers[0][-1]


def part1(data):
    answers = []
    for line in data.splitlines():
        line = list(map(int, line.split()))
        answers.append(extrapolate(line))

    print("Part 1:", sum(answers))


def part2(data):
    answer = []
    for line in data.splitlines():
        line = list(map(int, line.split()[::-1]))
        answer.append(extrapolate(line))

    print("Part 2:", sum(answer))


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
