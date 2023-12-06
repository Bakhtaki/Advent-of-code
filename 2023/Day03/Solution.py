import sys


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):

    grid = data.strip().split('\n')

    n = len(grid)
    m = len(grid[0])

    def is_symbol(i, j):
        if not (0 <= i < n and 0 <= j < m):
            return False
        return grid[i][j] != '.' and not grid[i][j].isdigit()

    answer = 0

    for r, row in enumerate(grid):
        start = 0

        c = 0

        while c < m:
            start = c
            num = ''
            while c < m and row[c].isdigit():
                num += row[c]
                c += 1

            if num == '':
                c += 1
                continue

            num = int(num)

            # Numbers are found, check for the symbol in adjacent cells
            if is_symbol(r, start-1) or is_symbol(r, c):
                answer += num
                continue
            # Check for the symbol in the row above and below digonal cells
            for k in range(start-1, c+1):
                if is_symbol(r-1, k) or is_symbol(r+1, k):
                    answer += num
                    break
    print(f'Part 1: {answer}')


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
