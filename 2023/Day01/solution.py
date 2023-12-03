import sys

letters = ("one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine", "zero")


def get_file_content(file_nmae):
    with open(file_nmae, 'r') as file:
        file_content = file.read()
    return file_content


# Part 1
def Part1(data):
    score = 0
    for line in data.splitlines():
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(char)
        numbers = numbers[0] + numbers[-1]
        score += int(numbers)
    print(score)

# Part 2


def Part2(data):
    answer = 0
    for line in data.splitlines():
        numbers = []
        for i, char in enumerate(line):
            if char.isdigit():
                numbers.append(char)
            for pos, val in enumerate(letters):
                if line[i:i+len(val)] == val:
                    numbers.append(pos+1)
        score = str(numbers[0]) + str(numbers[-1])
        answer += int(score)
    print(answer)


if __name__ == '__main__':
    file_name = sys.argv[1]

    data = get_file_content(file_name)
    print("Which part do you want to run?")
    input = int(input("Enter 0 for both, 1 for part 1 and 2 for part 2: "))
    if input == 0:
        print("Part 1: ", Part1(data))
        print("Part 2: ", Part2(data))
    elif input == 1:
        print("Part 1: ", Part1(data))
    elif input == 2:
        print("Part 2: ")
        Part2(data)
    else:
        print("Invalid input")
