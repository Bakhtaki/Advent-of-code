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
    line_counts = {}
    answer = 0
    for ln, line in enumerate(data.splitlines()):
        line = line.split(': ')[1]
        win_card, card = line.split('|')

        win_cards = []
        for each in win_card.split():
            if each != ' ':
                win_cards.append(int(each))

        cards = []
        for each in card.split():
            if each != ' ':
                cards.append(int(each))

        common = 0
        for number in win_cards:
            if number in cards:
                common += 1
        line_counts[ln+1] = common

    print(line_counts)


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
