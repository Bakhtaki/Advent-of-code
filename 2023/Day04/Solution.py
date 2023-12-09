import sys


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):
    answer = 0
    for line in data.splitlines():
        win_cards, cards = [], []

        refrence, hand = line.split('|')
        refrence = refrence.split(': ')[1]
        for each in refrence.split():
            if each != ' ':
                win_cards.append(int(each))

        for each in hand.split():
            if each != ' ':
                cards.append(int(each))

        common = 0
        for number in win_cards:
            if number in cards:
                common += 1
        if common == 0:
            continue
        answer += 2 ** (common - 1)
    print(f"Part 1: {answer}")


def part2(data):
    answer = 0
    length = len(data.splitlines())
    copies = [[] for _ in range(length+1)]

    for ln, line in enumerate(data.splitlines()):
        win_cards, cards = [], []

        refrence, hand = line.split('|')
        refrence = refrence.split(': ')[1]
        for each in refrence.split():
            if each != ' ':
                win_cards.append(int(each))

        for each in hand.split():
            if each != ' ':
                cards.append(int(each))

        common = 0
        for number in win_cards:
            if number in cards:
                common += 1

        for j in range(ln+1, ln+common+1):
            copies[ln].append(j)

    score = [0] + [1 for _ in range(length)]
    for i in range(length-1, -1, -1):
        for j in copies[i]:
            score[i] += score[j]
    answer = sum(score)
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
