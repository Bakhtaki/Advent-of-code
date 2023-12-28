import sys
from collections import defaultdict


letter_map = {'T': 'A',
              'J': 'B',
              'Q': 'C',
              'K': 'D',
              'A': 'E'
              }

letter_map2 = {'T': 'A',
               'J': '.',
               'Q': 'C',
               'K': 'D',
               'A': 'E',
               }


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content


def part1(data):
    def classify_hand(hand):
        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        amounts = sorted(count.values(), reverse=True)

        if amounts == [5]:
            return 6
        if amounts == [4, 1]:
            return 5
        if amounts == [3, 2]:
            return 4
        if amounts == [3, 1, 1]:
            return 3
        if amounts == [2, 2, 1]:
            return 2
        if amounts == [2, 1, 1, 1]:
            return 1
        if amounts == [1, 1, 1, 1, 1]:
            return 0

    def strength(hand):
        return (classify_hand(hand),
                [letter_map.get(card, card) for card in hand])

    plays = []
    for card in data.splitlines():
        hand, bid = card.split(' ')
        plays.append((strength(hand), int(bid)))

    plays.sort(key=lambda play: play[0])

    answer = 0

    for rank, (hand, bid) in enumerate(plays, 1):
        answer += rank * bid

    print(f"Part 1: {answer}")


def part2(data):

    def score(hand):
        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        amounts = sorted(count.values(), reverse=True)

        if amounts == [5]:
            return 6
        if amounts == [4, 1]:
            return 5
        if amounts == [3, 2]:
            return 4
        if amounts == [3, 1, 1]:
            return 3
        if amounts == [2, 2, 1]:
            return 2
        if amounts == [2, 1, 1, 1]:
            return 1
        if amounts == [1, 1, 1, 1, 1]:
            return 0

    def replacement(hand):
        if hand == '':
            return ['']

        return [
            x + y
            for x in ('23456789TQKA' if hand[0] == 'J' else hand[0])
            for y in replacement(hand[1:])
        ]

    def permutation(hand):
        return max(map(score, replacement(hand)))

    def strength(hand):
        return (permutation(hand),
                [letter_map2.get(card, card) for card in hand])

    plays = []
    for card in data.splitlines():
        hand, bid = card.split()
        plays.append((hand, int(bid)))

    plays.sort(key=lambda play: strength(play[0]))

    answer = 0

    for rank, (hand, bid) in enumerate(plays, 1):
        answer += rank * bid

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
