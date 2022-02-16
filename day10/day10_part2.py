"""
This is script for advent of code 2021.

day 10 part1.
"""


import statistics


def get_data(file_name):
    """Get data from file."""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        file.close()
    return lines


def complete_missing(data):
    """
    Fetch line and check whether is missing or not.

    complete missing file.

    input = data -> list
    output = score -> int
    """
    scores = []
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    forward = {'(': ')', '[': ']', '{': '}', '<': '>'}
    reverse = {_v: _c for _c, _v in forward.items()}

    for member in data:
        stack = []
        for letter in member:
            if letter in forward:
                stack.append(letter)
            elif letter in reverse:
                if reverse[letter] == stack[-1]:
                    stack.pop()
                else:
                    break
        else:
            score = 0
            for letter in reversed(stack):
                score *= 5
                score += points[forward[letter]]
            scores.append(score)
    return statistics.median(scores)


def main():
    """Logical flow of script."""
    data = get_data('level10.txt')
    score = complete_missing(data)
    print(f'score is equal to : {score}')


if __name__ == '__main__':
    main()
