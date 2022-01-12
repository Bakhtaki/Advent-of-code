"""
This scripts for advent of code 2021.

Level8 part1.
"""


def get_data(filename):
    """Load data from file to scipts."""
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()
        outputs = [line.strip().split("|")[1] for line in lines]
    return outputs


def detect_digits(digits):
    """Determine 2,3,4,8 length digits."""
    count = 0
    for line in digits:
        line = line.split()
        for word in line:
            if len(word) in [2, 3, 4, 7]:
                count += 1
    print(f'Total simple digits : {count}')


def main():
    """Structure of script."""
    digits = get_data("advent_of_code_l8.txt")
    detect_digits(digits)


if __name__ == '__main__':
    main()
