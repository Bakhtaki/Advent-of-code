import sys


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):
    possilities = 0
    for i, line in enumerate(data.splitlines()):
        game_id, game_result = line.split(':')
        game_id = game_id.split()[1]
        game_result = game_result.split(';')
        for hand in game_result:
            colors = {'red': 0, 'blue': 0, 'green': 0}
            for each in hand.split(', '):
                number, color = each.split()
                colors[color] = int(number)
            if colors['red'] > 12 or \
                    colors['blue'] > 14 or colors['green'] > 13:
                break
        else:
            possilities += i + 1
    print(f'Part 1 answer: {possilities}')


def part2(data):
    hand_point = []
    for i, line in enumerate(data.splitlines()):
        colors = {'red': 0, 'blue': 0, 'green': 0}
        game = line.split(':')[1]
        for each in game.split(';'):
            for card in each.split(', '):
                number, color = card.split()
                colors[color] = int(number) if int(
                    number) > colors[color] else colors[color]
        score = 1
        for value in colors.values():
            score *= value
        hand_point.append(score)
    print(f'Part 2 answer: {sum(hand_point)}')


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
