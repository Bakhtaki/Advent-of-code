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


# Process the Columns of grid
def process_columns(j, n, m, lines) -> int:
    i = 0
    ans = 0

    while i < n:
        while i < n and lines[i][j] == '#':
            i += 1
        count = 0
        start = i
        while i < n and lines[i][j] != '#':
            if lines[i][j] == 'O':
                count += 1
            i += 1
        for k in range(start, start + count):
            ans += m - k
    return ans


def part1(data):
    lines = data.strip().split('\n')
    n, m = len(lines), len(lines[0])

    answers = 0

    for j in range(m):
        answers += process_columns(j, n, m, lines)
    print(f'Part 1: {answers}')


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
